from __future__ import annotations

import json
import time
import asyncio
import threading
from types import SimpleNamespace
from typing import Any, Dict, List, Iterator, Optional
from pathlib import Path

import anyio
import httpx
import pytest
from respx import MockRouter

from reducto import (
    Reducto,
    OAuthError,
    AsyncReducto,
    ReductoError,
    APIConnectionError,
    AuthenticationError,
    SubjectTokenProviderError,
)
from reducto.auth import (
    WorkloadIdentity,
    SubjectTokenProvider,
    WorkloadIdentityAuth,
    _workload,
    identity_token_file,
    gcp_id_token_provider,
    github_actions_token_provider,
    aws_web_identity_token_provider,
    k8s_service_account_token_provider,
    azure_managed_identity_token_provider,
)
from reducto._types import Omit

from .utils import update_env

base_url = "https://platform.reducto.ai"
token_url = f"{base_url}/oauth/token"
no_env = {
    "REDUCTO_API_KEY": Omit(),
    "REDUCTO_BASE_URL": Omit(),
    "REDUCTO_IDENTITY_PROVIDER_ID": Omit(),
    "REDUCTO_IDENTITY_TOKEN_FILE": Omit(),
    "REDUCTO_IDENTITY_TOKEN": Omit(),
}


def static_provider(token: str = "subject.jwt") -> SubjectTokenProvider:
    return {"token_type": "jwt", "get_token": lambda: token}


def identity(
    provider: Optional[SubjectTokenProvider] = None, refresh_buffer_seconds: Optional[float] = None
) -> WorkloadIdentity:
    result: WorkloadIdentity = {"identity_provider_id": "wip_test", "provider": provider or static_provider()}
    if refresh_buffer_seconds is not None:
        result["refresh_buffer_seconds"] = refresh_buffer_seconds
    return result


class TokenServer:
    """Mints `rdat_1`, `rdat_2`, ... and records each exchange body."""

    def __init__(self, expires_in: float = 3600, delay: float = 0) -> None:
        self.expires_in = expires_in
        self.delay = delay
        self.bodies: List[Dict[str, Any]] = []
        self._lock = threading.Lock()

    def __call__(self, request: httpx.Request) -> httpx.Response:
        if self.delay:
            time.sleep(self.delay)
        with self._lock:
            self.bodies.append(json.loads(request.content))
            n = len(self.bodies)
        return httpx.Response(
            200,
            json={
                "access_token": f"rdat_{n}",
                "issued_token_type": "urn:ietf:params:oauth:token-type:access_token",
                "token_type": "Bearer",
                "expires_in": self.expires_in,
                "expires_at": 1793329845,
            },
        )


class FakeClock:
    def __init__(self) -> None:
        self.now = 1000.0

        self.sleeps: List[float] = []

    def monotonic(self) -> float:
        return self.now

    def sleep(self, seconds: float) -> None:
        self.sleeps.append(seconds)
        self.now += seconds

    async def async_sleep(self, seconds: float) -> None:
        self.sleep(seconds)


@pytest.fixture
def clock(monkeypatch: pytest.MonkeyPatch) -> FakeClock:
    fake = FakeClock()
    monkeypatch.setattr(_workload, "time", fake)
    monkeypatch.setattr(_workload, "anyio", SimpleNamespace(sleep=fake.async_sleep, Lock=anyio.Lock))
    return fake


@pytest.fixture(autouse=True)
def clean_env() -> Iterator[None]:
    with update_env(**no_env):
        yield


def auth_headers(route: Any) -> List[str]:
    return [call.request.headers["Authorization"] for call in route.calls]


class TestExchange:
    def test_exchange_body_and_bearer(self, respx_mock: MockRouter) -> None:
        server = TokenServer()
        respx_mock.post(token_url).mock(side_effect=server)
        api = respx_mock.get(f"{base_url}/version").mock(return_value=httpx.Response(200, text="1"))

        client = Reducto(workload_identity=identity())
        assert client.api_version() == "1"

        assert server.bodies == [
            {
                "grant_type": "urn:ietf:params:oauth:grant-type:token-exchange",
                "subject_token_type": "urn:ietf:params:oauth:token-type:jwt",
                "subject_token": "subject.jwt",
                "identity_provider_id": "wip_test",
            }
        ]
        assert auth_headers(api) == ["Bearer rdat_1"]

    def test_id_token_type(self, respx_mock: MockRouter) -> None:
        server = TokenServer()
        respx_mock.post(token_url).mock(side_effect=server)
        provider: SubjectTokenProvider = {"token_type": "id", "get_token": lambda: "id.jwt"}
        WorkloadIdentityAuth(identity(provider=provider), token_url=token_url, http_client=httpx.Client()).get_token()
        assert server.bodies[0]["subject_token_type"] == "urn:ietf:params:oauth:token-type:id_token"

    def test_exchange_uses_base_url(self, respx_mock: MockRouter) -> None:
        server = TokenServer()
        route = respx_mock.post("https://eu.platform.reducto.ai/oauth/token").mock(side_effect=server)
        respx_mock.get("https://eu.platform.reducto.ai/version").mock(return_value=httpx.Response(200, text="1"))
        Reducto(workload_identity=identity(), environment="eu").api_version()
        assert route.call_count == 1

    def test_caches_token(self, respx_mock: MockRouter) -> None:
        server = TokenServer()
        respx_mock.post(token_url).mock(side_effect=server)
        api = respx_mock.get(f"{base_url}/version").mock(return_value=httpx.Response(200, text="1"))

        client = Reducto(workload_identity=identity())
        client.api_version()
        client.api_version()
        client.with_options(timeout=5).api_version()

        assert len(server.bodies) == 1
        assert auth_headers(api) == ["Bearer rdat_1"] * 3

    def test_refreshes_before_expiry(self, respx_mock: MockRouter, clock: FakeClock) -> None:
        server = TokenServer(expires_in=100)
        respx_mock.post(token_url).mock(side_effect=server)
        auth = WorkloadIdentityAuth(identity(), token_url=token_url, http_client=httpx.Client())

        assert auth.get_token() == "rdat_1"
        clock.now += 49  # buffer is min(1200, 100 / 2) = 50
        assert auth.get_token() == "rdat_1"
        clock.now += 2
        assert auth.get_token() == "rdat_2"

    def test_refresh_buffer_option(self, respx_mock: MockRouter, clock: FakeClock) -> None:
        server = TokenServer(expires_in=3600)
        respx_mock.post(token_url).mock(side_effect=server)
        auth = WorkloadIdentityAuth(
            identity(refresh_buffer_seconds=60), token_url=token_url, http_client=httpx.Client()
        )

        assert auth.get_token() == "rdat_1"
        clock.now += 3539
        assert auth.get_token() == "rdat_1"
        clock.now += 2
        assert auth.get_token() == "rdat_2"

    def test_concurrent_threads_share_one_exchange(self, respx_mock: MockRouter) -> None:
        server = TokenServer(delay=0.2)
        respx_mock.post(token_url).mock(side_effect=server)
        auth = WorkloadIdentityAuth(identity(), token_url=token_url, http_client=httpx.Client())

        results: List[str] = []
        threads = [threading.Thread(target=lambda: results.append(auth.get_token())) for _ in range(10)]
        for t in threads:
            t.start()
        for t in threads:
            t.join()

        assert results == ["rdat_1"] * 10
        assert len(server.bodies) == 1

    async def test_concurrent_tasks_share_one_exchange(self, respx_mock: MockRouter) -> None:
        server = TokenServer(delay=0.2)
        respx_mock.post(token_url).mock(side_effect=server)
        auth = WorkloadIdentityAuth(identity(), token_url=token_url, http_client=httpx.AsyncClient())

        results = await asyncio.gather(*(auth.get_token_async() for _ in range(10)))

        assert results == ["rdat_1"] * 10
        assert len(server.bodies) == 1

    def test_oauth_error(self, respx_mock: MockRouter) -> None:
        route = respx_mock.post(token_url).mock(
            return_value=httpx.Response(
                400, json={"error": "invalid_grant", "error_description": "mapping: no mapping matched"}
            )
        )
        api = respx_mock.get(f"{base_url}/version").mock(return_value=httpx.Response(200, text="1"))
        client = Reducto(workload_identity=identity(), max_retries=2)

        with pytest.raises(OAuthError) as exc_info:
            client.api_version()

        assert exc_info.value.status_code == 400
        assert exc_info.value.error == "invalid_grant"
        assert exc_info.value.error_description == "mapping: no mapping matched"
        assert route.call_count == 1
        assert api.call_count == 0

    def test_unavailable_is_retried_with_backoff_then_raised(self, respx_mock: MockRouter, clock: FakeClock) -> None:
        route = respx_mock.post(token_url).mock(
            return_value=httpx.Response(
                503, json={"error": "temporarily_unavailable", "error_description": "Token exchange is not available."}
            )
        )
        api = respx_mock.get(f"{base_url}/version").mock(return_value=httpx.Response(200, text="1"))
        client = Reducto(workload_identity=identity(), max_retries=2)

        with pytest.raises(OAuthError) as exc_info:
            client.api_version()

        assert str(exc_info.value) == (
            "Token exchange failed with status 503: temporarily_unavailable: Token exchange is not available."
        )
        assert exc_info.value.error == "temporarily_unavailable"
        assert route.call_count == 3
        assert api.call_count == 0
        assert len(clock.sleeps) == 2
        assert 0.375 <= clock.sleeps[0] <= 0.5
        assert 0.75 <= clock.sleeps[1] <= 1.0

    def test_slow_down_honors_retry_after(self, respx_mock: MockRouter, clock: FakeClock) -> None:
        slow_down = httpx.Response(429, headers={"retry-after": "3"}, json={"error": "slow_down"})
        route = respx_mock.post(token_url).mock(
            side_effect=[slow_down, slow_down, TokenServer()(httpx.Request("POST", token_url, json={}))]
        )
        api = respx_mock.get(f"{base_url}/version").mock(return_value=httpx.Response(200, text="1"))
        client = Reducto(workload_identity=identity(), max_retries=2)

        assert client.api_version() == "1"
        assert route.call_count == 3
        assert clock.sleeps == [3.0, 3.0]
        assert auth_headers(api) == ["Bearer rdat_1"]

    def test_slow_down_raises_after_max_retries(self, respx_mock: MockRouter, clock: FakeClock) -> None:
        route = respx_mock.post(token_url).mock(
            return_value=httpx.Response(429, json={"error": "slow_down", "error_description": "Too many requests"})
        )
        client = Reducto(workload_identity=identity(), max_retries=1)

        with pytest.raises(OAuthError) as exc_info:
            client.api_version()

        assert exc_info.value.status_code == 429
        assert exc_info.value.error == "slow_down"
        assert route.call_count == 2
        assert len(clock.sleeps) == 1

    def test_max_retries_zero_does_not_retry(self, respx_mock: MockRouter, clock: FakeClock) -> None:
        route = respx_mock.post(token_url).mock(return_value=httpx.Response(429, json={"error": "slow_down"}))
        client = Reducto(workload_identity=identity(), max_retries=0)

        with pytest.raises(OAuthError):
            client.api_version()

        assert route.call_count == 1
        assert clock.sleeps == []

    def test_connection_error_is_retried(self, respx_mock: MockRouter, clock: FakeClock) -> None:
        route = respx_mock.post(token_url).mock(side_effect=httpx.ConnectError("refused"))
        client = Reducto(workload_identity=identity(), max_retries=2)

        with pytest.raises(APIConnectionError):
            client.api_version()

        assert route.call_count == 3
        assert len(clock.sleeps) == 2

    async def test_async_slow_down_is_retried_with_backoff(self, respx_mock: MockRouter, clock: FakeClock) -> None:
        slow_down = httpx.Response(429, json={"error": "slow_down"})
        route = respx_mock.post(token_url).mock(
            side_effect=[slow_down, TokenServer()(httpx.Request("POST", token_url, json={}))]
        )
        api = respx_mock.get(f"{base_url}/version").mock(return_value=httpx.Response(200, text="1"))
        client = AsyncReducto(workload_identity=identity(), max_retries=2)

        assert await client.api_version() == "1"
        assert route.call_count == 2
        assert len(clock.sleeps) == 1
        assert 0.375 <= clock.sleeps[0] <= 0.5
        assert auth_headers(api) == ["Bearer rdat_1"]

    def test_reassigned_base_url_exchanges_in_new_region(self, respx_mock: MockRouter) -> None:
        eu_url = "https://eu.platform.reducto.ai"
        us_token = respx_mock.post(token_url).mock(side_effect=TokenServer())
        eu_token = respx_mock.post(f"{eu_url}/oauth/token").mock(side_effect=TokenServer())
        respx_mock.get(f"{base_url}/version").mock(return_value=httpx.Response(200, text="1"))
        eu_api = respx_mock.get(f"{eu_url}/version").mock(return_value=httpx.Response(200, text="1"))
        client = Reducto(workload_identity=identity())

        client.api_version()
        client.base_url = eu_url
        client.api_version()

        assert us_token.call_count == 1
        assert eu_token.call_count == 1
        assert auth_headers(eu_api) == ["Bearer rdat_1"]

    def test_custom_http_client_sends_the_exchange(self) -> None:
        server = TokenServer()
        requests: List[httpx.Request] = []

        def handler(request: httpx.Request) -> httpx.Response:
            requests.append(request)
            return server(request) if request.url.path == "/oauth/token" else httpx.Response(200, text="1")

        client = Reducto(workload_identity=identity(), http_client=httpx.Client(transport=httpx.MockTransport(handler)))

        assert client.api_version() == "1"
        assert [str(r.url) for r in requests] == [token_url, f"{base_url}/version"]
        assert requests[1].headers["Authorization"] == "Bearer rdat_1"

    async def test_custom_async_http_client_sends_the_exchange(self) -> None:
        server = TokenServer()
        requests: List[httpx.Request] = []

        def handler(request: httpx.Request) -> httpx.Response:
            requests.append(request)
            return server(request) if request.url.path == "/oauth/token" else httpx.Response(200, text="1")

        client = AsyncReducto(
            workload_identity=identity(), http_client=httpx.AsyncClient(transport=httpx.MockTransport(handler))
        )

        assert await client.api_version() == "1"
        assert [str(r.url) for r in requests] == [token_url, f"{base_url}/version"]
        assert requests[1].headers["Authorization"] == "Bearer rdat_1"

    def test_exchange_does_not_follow_redirects(self) -> None:
        requests: List[httpx.Request] = []

        def handler(request: httpx.Request) -> httpx.Response:
            requests.append(request)
            return httpx.Response(307, headers={"Location": "https://attacker.example/oauth/token"})

        client = Reducto(
            workload_identity=identity(),
            http_client=httpx.Client(transport=httpx.MockTransport(handler), follow_redirects=True),
        )

        with pytest.raises(OAuthError) as exc:
            client.api_version()
        assert exc.value.status_code == 307
        assert [str(r.url) for r in requests] == [token_url]

    def test_provider_error(self) -> None:
        def get_token() -> str:
            raise RuntimeError("boom")

        client = Reducto(workload_identity=identity(provider={"token_type": "jwt", "get_token": get_token}))
        with pytest.raises(SubjectTokenProviderError, match="boom"):
            client.api_version()

    def test_explicit_authorization_header_is_kept(self, respx_mock: MockRouter) -> None:
        token = respx_mock.post(token_url).mock(side_effect=TokenServer())
        api = respx_mock.get(f"{base_url}/version").mock(return_value=httpx.Response(200, text="1"))
        client = Reducto(workload_identity=identity())
        client.api_version(extra_headers={"Authorization": "Bearer mine"})
        assert auth_headers(api) == ["Bearer mine"]
        assert token.call_count == 0


class TestRetryOn401:
    def test_reexchanges_and_retries_once(self, respx_mock: MockRouter) -> None:
        server = TokenServer()
        respx_mock.post(token_url).mock(side_effect=server)
        api = respx_mock.get(f"{base_url}/version").mock(
            side_effect=[httpx.Response(401, json={"detail": "revoked"}), httpx.Response(200, text="1")]
        )

        client = Reducto(workload_identity=identity(), max_retries=0)
        assert client.api_version() == "1"

        assert len(server.bodies) == 2
        assert auth_headers(api) == ["Bearer rdat_1", "Bearer rdat_2"]

    def test_gives_up_after_one_retry(self, respx_mock: MockRouter) -> None:
        server = TokenServer()
        respx_mock.post(token_url).mock(side_effect=server)
        api = respx_mock.get(f"{base_url}/version").mock(return_value=httpx.Response(401, json={"detail": "no"}))

        client = Reducto(workload_identity=identity())
        with pytest.raises(AuthenticationError):
            client.api_version()

        assert len(server.bodies) == 2
        assert api.call_count == 2

    async def test_async_client(self, respx_mock: MockRouter) -> None:
        server = TokenServer()
        respx_mock.post(token_url).mock(side_effect=server)
        api = respx_mock.get(f"{base_url}/version").mock(
            side_effect=[
                httpx.Response(200, text="1"),
                httpx.Response(401, json={"detail": "revoked"}),
                httpx.Response(200, text="1"),
            ]
        )

        client = AsyncReducto(workload_identity=identity(), max_retries=0)
        await client.api_version()
        await client.api_version()

        assert len(server.bodies) == 2
        assert auth_headers(api) == ["Bearer rdat_1", "Bearer rdat_1", "Bearer rdat_2"]


class TestCredentials:
    def test_token_file_env_is_reread(self, respx_mock: MockRouter, tmp_path: Path) -> None:
        server = TokenServer()
        respx_mock.post(token_url).mock(side_effect=server)
        token_file = tmp_path / "token"
        token_file.write_text("first.jwt\n")

        with update_env(REDUCTO_IDENTITY_PROVIDER_ID="wip_env", REDUCTO_IDENTITY_TOKEN_FILE=str(token_file)):
            client = Reducto()
        auth = client._workload_identity_auth
        assert auth is not None
        auth.get_token()
        token_file.write_text("second.jwt")
        auth.invalidate("rdat_1")
        auth.get_token()

        assert [b["subject_token"] for b in server.bodies] == ["first.jwt", "second.jwt"]
        assert server.bodies[0]["identity_provider_id"] == "wip_env"

    def test_static_token_env(self) -> None:
        with update_env(REDUCTO_IDENTITY_PROVIDER_ID="wip_env", REDUCTO_IDENTITY_TOKEN="static.jwt"):
            client = Reducto()
        assert client.workload_identity is not None
        provider = client.workload_identity["provider"]
        assert provider["token_type"] == "jwt"
        assert provider["get_token"]() == "static.jwt"

    def test_provider_id_without_token(self) -> None:
        with update_env(REDUCTO_IDENTITY_PROVIDER_ID="wip_env"):
            with pytest.raises(ReductoError, match="REDUCTO_IDENTITY_TOKEN"):
                Reducto()

    def test_api_key_and_workload_identity_conflict(self) -> None:
        with pytest.raises(ReductoError, match="mutually exclusive"):
            Reducto(api_key="key", workload_identity=identity())
        with pytest.raises(ReductoError, match="mutually exclusive"):
            AsyncReducto(api_key="key", workload_identity=identity())

    def test_missing_credentials(self) -> None:
        with pytest.raises(ReductoError, match="REDUCTO_IDENTITY_PROVIDER_ID"):
            Reducto()

    def test_precedence(self) -> None:
        wif_env = {"REDUCTO_IDENTITY_PROVIDER_ID": "wip_env", "REDUCTO_IDENTITY_TOKEN": "env.jwt"}
        explicit = identity()

        with update_env(REDUCTO_API_KEY="env-key", **wif_env):
            client = Reducto(api_key="arg-key")
            assert client.api_key == "arg-key" and client.workload_identity is None

            client = Reducto(workload_identity=explicit)
            assert client.workload_identity is explicit

            client = Reducto()
            assert client.api_key == "env-key" and client.workload_identity is None

        with update_env(**wif_env):
            client = Reducto()
            assert client.workload_identity is not None
            assert client.workload_identity["identity_provider_id"] == "wip_env"

    def test_copy(self) -> None:
        client = Reducto(workload_identity=identity())
        assert client.copy()._workload_identity_auth is client._workload_identity_auth
        assert client.copy(api_key="key")._workload_identity_auth is None
        other = client.copy(base_url="https://au.platform.reducto.ai")._workload_identity_auth
        assert other is not None and other.token_url == "https://au.platform.reducto.ai/oauth/token"


class TestProviders:
    def test_identity_token_file(self, tmp_path: Path) -> None:
        path = tmp_path / "token"
        provider = identity_token_file(path)
        with pytest.raises(SubjectTokenProviderError):
            provider["get_token"]()
        path.write_text("")
        with pytest.raises(SubjectTokenProviderError, match="empty"):
            provider["get_token"]()
        path.write_text(" a.jwt \n")
        assert provider["get_token"]() == "a.jwt"
        assert provider["token_type"] == "jwt"

    def test_k8s_default_path(self) -> None:
        with pytest.raises(SubjectTokenProviderError, match="/var/run/secrets/kubernetes.io/serviceaccount/token"):
            k8s_service_account_token_provider()["get_token"]()

    def test_gcp(self, respx_mock: MockRouter) -> None:
        route = respx_mock.get(
            "http://metadata.google.internal/computeMetadata/v1/instance/service-accounts/default/identity"
        ).mock(return_value=httpx.Response(200, text="gcp.jwt"))
        provider = gcp_id_token_provider()
        assert provider["token_type"] == "id"
        assert provider["get_token"]() == "gcp.jwt"
        request = route.calls.last.request
        assert request.headers["Metadata-Flavor"] == "Google"
        assert request.url.params["audience"] == "https://platform.reducto.ai"

    def test_azure(self, respx_mock: MockRouter) -> None:
        route = respx_mock.get("http://169.254.169.254/metadata/identity/oauth2/token").mock(
            return_value=httpx.Response(200, json={"access_token": "azure.jwt"})
        )
        provider = azure_managed_identity_token_provider("api://reducto", client_id="cid")
        assert provider["get_token"]() == "azure.jwt"
        request = route.calls.last.request
        assert request.headers["Metadata"] == "true"
        assert dict(request.url.params) == {
            "api-version": "2018-02-01",
            "resource": "api://reducto",
            "client_id": "cid",
        }

    def test_azure_http_error(self, respx_mock: MockRouter) -> None:
        respx_mock.get("http://169.254.169.254/metadata/identity/oauth2/token").mock(return_value=httpx.Response(400))
        with pytest.raises(SubjectTokenProviderError, match="HTTP 400"):
            azure_managed_identity_token_provider()["get_token"]()

    def test_github_actions(self, respx_mock: MockRouter) -> None:
        route = respx_mock.get("https://gha.example/token").mock(
            return_value=httpx.Response(200, json={"value": "gha.jwt"})
        )
        provider = github_actions_token_provider()
        with pytest.raises(SubjectTokenProviderError, match="id-token: write"):
            provider["get_token"]()
        with update_env(
            ACTIONS_ID_TOKEN_REQUEST_URL="https://gha.example/token?api-version=2.0",
            ACTIONS_ID_TOKEN_REQUEST_TOKEN="req",
        ):
            assert provider["get_token"]() == "gha.jwt"
        request = route.calls.last.request
        assert request.headers["Authorization"] == "Bearer req"
        assert dict(request.url.params) == {"api-version": "2.0", "audience": "https://platform.reducto.ai"}

    def test_aws(self) -> None:
        calls: List[Dict[str, Any]] = []

        class FakeSTS:
            def get_web_identity_token(self, **kwargs: Any) -> Dict[str, Any]:
                calls.append(kwargs)
                return {"WebIdentityToken": "aws.jwt"}

        provider = aws_web_identity_token_provider(duration_seconds=900, sts_client=FakeSTS())
        assert provider["get_token"]() == "aws.jwt"
        assert calls == [
            {"Audience": ["https://platform.reducto.ai"], "SigningAlgorithm": "RS256", "DurationSeconds": 900}
        ]

    def test_aws_without_boto3(self, monkeypatch: pytest.MonkeyPatch) -> None:
        def missing(_name: str) -> Any:
            raise ImportError("No module named 'boto3'")

        monkeypatch.setattr(_workload.importlib, "import_module", missing)
        with pytest.raises(ReductoError, match="pip install boto3"):
            aws_web_identity_token_provider()
