"""Workload identity federation: exchange a platform-issued JWT for a short-lived Reducto access token."""

from __future__ import annotations

import os
import time
import random
import importlib
import threading
from typing import Any, Dict, Tuple, Union, Callable, Optional, Generator, AsyncGenerator
from pathlib import Path
from typing_extensions import Literal, TypedDict, NotRequired, override

import anyio
import httpx

from .._utils import is_dict
from .._constants import MAX_RETRY_DELAY, DEFAULT_MAX_RETRIES, INITIAL_RETRY_DELAY
from .._exceptions import (
    OAuthError,
    ReductoError,
    APITimeoutError,
    APIConnectionError,
    SubjectTokenProviderError,
    APIResponseValidationError,
)
from .._utils._sync import to_thread

__all__ = [
    "SubjectTokenProvider",
    "WorkloadIdentity",
    "WorkloadIdentityAuth",
    "identity_token_file",
    "k8s_service_account_token_provider",
    "gcp_id_token_provider",
    "azure_managed_identity_token_provider",
    "github_actions_token_provider",
    "aws_web_identity_token_provider",
]

TOKEN_EXCHANGE_GRANT_TYPE = "urn:ietf:params:oauth:grant-type:token-exchange"
SUBJECT_TOKEN_TYPES = {
    "jwt": "urn:ietf:params:oauth:token-type:jwt",
    "id": "urn:ietf:params:oauth:token-type:id_token",
}
DEFAULT_AUDIENCE = "https://platform.reducto.ai"
DEFAULT_REFRESH_BUFFER_SECONDS = 1200.0
DEFAULT_K8S_TOKEN_PATH = "/var/run/secrets/kubernetes.io/serviceaccount/token"

# Sent in place of a real token until `WorkloadIdentityAuth` swaps in the access token.
WORKLOAD_IDENTITY_AUTHORIZATION = "Bearer workload-identity"


class SubjectTokenProvider(TypedDict):
    token_type: Literal["jwt", "id"]
    """`jwt` for `urn:ietf:params:oauth:token-type:jwt`, `id` for `urn:ietf:params:oauth:token-type:id_token`."""

    get_token: Callable[[], str]
    """Returns a fresh subject token. Called on every exchange."""


class WorkloadIdentity(TypedDict):
    identity_provider_id: str
    """The Reducto workload identity provider ID (`wip_...`)."""

    provider: SubjectTokenProvider
    """Where the subject token comes from."""

    refresh_buffer_seconds: NotRequired[float]
    """Refresh the access token this many seconds before it expires, capped at half its lifetime. Defaults to 1200."""


def identity_token_file(path: str | os.PathLike[str]) -> SubjectTokenProvider:
    """Read the subject token from a file. The file is re-read on every exchange, so rotated tokens are picked up."""

    def get_token() -> str:
        try:
            token = Path(path).read_text().strip()
        except OSError as e:
            raise SubjectTokenProviderError(f"Failed to read the identity token file at {path}: {e}") from e
        if not token:
            raise SubjectTokenProviderError(f"The identity token file at {path} is empty")
        return token

    return {"token_type": "jwt", "get_token": get_token}


def k8s_service_account_token_provider(path: str | os.PathLike[str] = DEFAULT_K8S_TOKEN_PATH) -> SubjectTokenProvider:
    """Read a Kubernetes service account token. Use a projected token volume with your Reducto audience."""
    return identity_token_file(path)


def gcp_id_token_provider(audience: str = DEFAULT_AUDIENCE, *, timeout: float = 10.0) -> SubjectTokenProvider:
    """Fetch an identity token for the attached service account from the Google Cloud metadata server."""

    def get_token() -> str:
        response = _fetch(
            "Google Cloud",
            "http://metadata.google.internal/computeMetadata/v1/instance/service-accounts/default/identity",
            params={"audience": audience},
            headers={"Metadata-Flavor": "Google"},
            timeout=timeout,
            trust_env=False,
        )
        token = response.text.strip()
        if not token:
            raise SubjectTokenProviderError("The Google Cloud metadata server returned an empty identity token")
        return token

    return {"token_type": "id", "get_token": get_token}


def azure_managed_identity_token_provider(
    resource: str = "https://management.azure.com/",
    *,
    client_id: Optional[str] = None,
    object_id: Optional[str] = None,
    msi_res_id: Optional[str] = None,
    api_version: str = "2018-02-01",
    timeout: float = 10.0,
) -> SubjectTokenProvider:
    """Fetch a managed identity token from Azure IMDS.

    Args:
        resource: the resource URI to request a token for. It becomes the token `aud`.
        client_id, object_id, msi_res_id: select one managed identity when several are assigned.
    """

    def get_token() -> str:
        params = {"api-version": api_version, "resource": resource}
        for key, value in (("client_id", client_id), ("object_id", object_id), ("msi_res_id", msi_res_id)):
            if value is not None:
                params[key] = value
        response = _fetch(
            "Azure managed identity",
            "http://169.254.169.254/metadata/identity/oauth2/token",
            params=params,
            headers={"Metadata": "true"},
            timeout=timeout,
            trust_env=False,
        )
        return _json_string(response, "access_token", "Azure managed identity")

    return {"token_type": "jwt", "get_token": get_token}


def github_actions_token_provider(audience: str = DEFAULT_AUDIENCE, *, timeout: float = 10.0) -> SubjectTokenProvider:
    """Fetch a GitHub Actions OIDC token. The job needs `permissions: id-token: write`."""

    def get_token() -> str:
        url = os.environ.get("ACTIONS_ID_TOKEN_REQUEST_URL")
        request_token = os.environ.get("ACTIONS_ID_TOKEN_REQUEST_TOKEN")
        if not url or not request_token:
            raise SubjectTokenProviderError(
                "ACTIONS_ID_TOKEN_REQUEST_URL and ACTIONS_ID_TOKEN_REQUEST_TOKEN are not set. "
                "Run inside GitHub Actions with `permissions: id-token: write`."
            )
        response = _fetch(
            "GitHub Actions",
            url,
            params={"audience": audience},
            headers={"Authorization": f"Bearer {request_token}"},
            timeout=timeout,
            trust_env=True,
        )
        return _json_string(response, "value", "GitHub Actions")

    return {"token_type": "jwt", "get_token": get_token}


def aws_web_identity_token_provider(
    audience: str = DEFAULT_AUDIENCE,
    *,
    signing_algorithm: Literal["RS256", "ES384"] = "RS256",
    duration_seconds: Optional[int] = None,
    sts_client: Any = None,
) -> SubjectTokenProvider:
    """Get a JWT for the current AWS identity with `sts:GetWebIdentityToken` (AWS outbound identity federation).

    Needs boto3. The Reducto access token cannot outlive this token, so set `duration_seconds`
    (60-3600, AWS default 300) to the lifetime you want.

    Args:
        sts_client: a boto3 STS client to use. Defaults to `boto3.client("sts")`.
    """
    sts: Any = sts_client
    if sts is None:
        try:
            boto3 = importlib.import_module("boto3")
        except ImportError as e:
            raise ReductoError(
                "aws_web_identity_token_provider requires boto3. Install it with `pip install boto3`."
            ) from e
        sts = boto3.client("sts")

    def get_token() -> str:
        kwargs: Dict[str, Any] = {"Audience": [audience], "SigningAlgorithm": signing_algorithm}
        if duration_seconds is not None:
            kwargs["DurationSeconds"] = duration_seconds
        try:
            token: object = sts.get_web_identity_token(**kwargs)["WebIdentityToken"]
        except Exception as e:
            raise SubjectTokenProviderError(f"Failed to get an AWS web identity token: {e}") from e
        if not isinstance(token, str) or not token:
            raise SubjectTokenProviderError("sts:GetWebIdentityToken returned an empty token")
        return token

    return {"token_type": "jwt", "get_token": get_token}


def _fetch(
    source: str, url: str, *, params: Dict[str, str], headers: Dict[str, str], timeout: float, trust_env: bool
) -> httpx.Response:
    try:
        with httpx.Client(timeout=timeout, trust_env=trust_env) as client:
            # Merge rather than replace: the GitHub Actions URL already has a query string.
            response = client.get(httpx.URL(url).copy_merge_params(params), headers=headers)
    except httpx.HTTPError as e:
        raise SubjectTokenProviderError(f"Failed to fetch a {source} token: {e}") from e
    if response.is_error:
        raise SubjectTokenProviderError(f"Failed to fetch a {source} token: HTTP {response.status_code}")
    return response


def _json_string(response: httpx.Response, field: str, source: str) -> str:
    try:
        body: object = response.json()
    except ValueError:
        body = None
    value = body.get(field) if is_dict(body) else None
    if not isinstance(value, str) or not value:
        raise SubjectTokenProviderError(f"The {source} token response did not include `{field}`")
    return value


def workload_identity_from_env() -> Optional[WorkloadIdentity]:
    provider_id = os.environ.get("REDUCTO_IDENTITY_PROVIDER_ID")
    if not provider_id:
        return None
    token_file = os.environ.get("REDUCTO_IDENTITY_TOKEN_FILE")
    token = os.environ.get("REDUCTO_IDENTITY_TOKEN")
    if token_file:
        provider = identity_token_file(token_file)
    elif token:
        provider = SubjectTokenProvider(token_type="jwt", get_token=lambda: token)
    else:
        raise ReductoError(
            "REDUCTO_IDENTITY_PROVIDER_ID is set, but neither REDUCTO_IDENTITY_TOKEN_FILE nor REDUCTO_IDENTITY_TOKEN is set"
        )
    return {"identity_provider_id": provider_id, "provider": provider}


def resolve_credentials(
    api_key: Optional[str], workload_identity: Optional[WorkloadIdentity]
) -> Tuple[Optional[str], Optional[WorkloadIdentity]]:
    """Precedence: `api_key=`, `workload_identity=`, `REDUCTO_API_KEY`, then the `REDUCTO_IDENTITY_*` variables."""
    if api_key is not None and workload_identity is not None:
        raise ReductoError("The api_key and workload_identity client options are mutually exclusive")
    if api_key is None and workload_identity is None:
        api_key = os.environ.get("REDUCTO_API_KEY")
        if api_key is None:
            workload_identity = workload_identity_from_env()
    if api_key is None and workload_identity is None:
        raise ReductoError(
            "The api_key client option must be set either by passing api_key to the client or by setting the "
            "REDUCTO_API_KEY environment variable. To use workload identity federation instead, pass "
            "workload_identity or set REDUCTO_IDENTITY_PROVIDER_ID with REDUCTO_IDENTITY_TOKEN_FILE or "
            "REDUCTO_IDENTITY_TOKEN."
        )
    return api_key, workload_identity


class WorkloadIdentityAuth(httpx.Auth):
    """Caches the Reducto access token and shares one in-flight exchange between threads and tasks.

    The exchange is sent through `http_client`, the client's own httpx client, so its proxy, TLS and transport
    settings apply to `/oauth/token` too. Pass an `httpx.Client` for `Reducto`, an `httpx.AsyncClient` for
    `AsyncReducto`.
    """

    def __init__(
        self,
        workload_identity: WorkloadIdentity,
        *,
        token_url: str,
        http_client: Union[httpx.Client, httpx.AsyncClient],
        max_retries: int = DEFAULT_MAX_RETRIES,
        timeout: float = 60.0,
    ) -> None:
        token_type = workload_identity["provider"]["token_type"]
        if token_type not in SUBJECT_TOKEN_TYPES:
            raise ReductoError(f"Unsupported subject token type {token_type!r}. Use one of: jwt, id")
        if not workload_identity["identity_provider_id"]:
            raise ReductoError("workload_identity.identity_provider_id must not be empty")
        self.workload_identity = workload_identity
        self.token_url = token_url
        self.http_client = http_client
        self.max_retries = max_retries
        self._timeout = timeout
        self._condition = threading.Condition()
        self._refreshing = False
        self._async_lock: Optional[anyio.Lock] = None
        self._token: Optional[str] = None
        self._expires_at = 0.0
        self._refresh_at = 0.0

    def get_token(self) -> str:
        with self._condition:
            while True:
                now = time.monotonic()
                if self._token is not None and now < self._refresh_at:
                    return self._token
                if not self._refreshing:
                    break
                # Another caller is refreshing. Keep using the current token until it expires.
                if self._token is not None and now < self._expires_at:
                    return self._token
                self._condition.wait()
            self._refreshing = True

        started = time.monotonic()
        token: Optional[str] = None
        expires_in = 0.0
        try:
            token, expires_in = self._exchange()
            return token
        finally:
            with self._condition:
                if token is not None:
                    self._store(token, started, expires_in)
                self._refreshing = False
                self._condition.notify_all()

    async def get_token_async(self) -> str:
        if self._async_lock is None:
            self._async_lock = anyio.Lock()
        with self._condition:
            now = time.monotonic()
            if self._token is not None and now < self._refresh_at:
                return self._token
            # Another task is refreshing. Keep using the current token until it expires.
            if self._async_lock.locked() and self._token is not None and now < self._expires_at:
                return self._token
        async with self._async_lock:
            with self._condition:
                if self._token is not None and time.monotonic() < self._refresh_at:
                    return self._token
            started = time.monotonic()
            token, expires_in = await self._exchange_async()
            with self._condition:
                self._store(token, started, expires_in)
            return token

    def invalidate(self, token: str) -> None:
        with self._condition:
            if self._token == token:
                self._token = None
                self._expires_at = self._refresh_at = 0.0

    @override
    def sync_auth_flow(self, request: httpx.Request) -> Generator[httpx.Request, httpx.Response, None]:
        if request.headers.get("Authorization") != WORKLOAD_IDENTITY_AUTHORIZATION:
            yield request
            return
        token = self.get_token()
        request.headers["Authorization"] = f"Bearer {token}"
        response = yield request
        if response.status_code == 401:
            # Release the connection before the exchange borrows one from the same pool.
            response.read()
            self.invalidate(token)
            request.headers["Authorization"] = f"Bearer {self.get_token()}"
            yield request

    @override
    async def async_auth_flow(self, request: httpx.Request) -> AsyncGenerator[httpx.Request, httpx.Response]:
        if request.headers.get("Authorization") != WORKLOAD_IDENTITY_AUTHORIZATION:
            yield request
            return
        token = await self.get_token_async()
        request.headers["Authorization"] = f"Bearer {token}"
        response = yield request
        if response.status_code == 401:
            await response.aread()
            self.invalidate(token)
            request.headers["Authorization"] = f"Bearer {await self.get_token_async()}"
            yield request

    def _store(self, token: str, started: float, expires_in: float) -> None:
        buffer = self.workload_identity.get("refresh_buffer_seconds", DEFAULT_REFRESH_BUFFER_SECONDS)
        self._token = token
        self._expires_at = started + expires_in
        self._refresh_at = self._expires_at - min(buffer, expires_in / 2)

    def _exchange(self) -> Tuple[str, float]:
        return _parse_exchange_response(self._post_with_retries(self._exchange_body()))

    async def _exchange_async(self) -> Tuple[str, float]:
        # Token providers are sync and may block (file reads, metadata servers), so call them off the event loop.
        body = await to_thread(self._exchange_body)
        return _parse_exchange_response(await self._post_with_retries_async(body))

    def _exchange_body(self) -> Dict[str, str]:
        provider = self.workload_identity["provider"]
        try:
            subject_token = provider["get_token"]()
        except SubjectTokenProviderError:
            raise
        except Exception as e:
            raise SubjectTokenProviderError(
                f"The workload identity provider failed to return a subject token: {e}"
            ) from e
        if not subject_token:
            raise SubjectTokenProviderError("The workload identity provider returned an empty subject token")
        return {
            "grant_type": TOKEN_EXCHANGE_GRANT_TYPE,
            "subject_token_type": SUBJECT_TOKEN_TYPES[provider["token_type"]],
            "subject_token": subject_token,
            "identity_provider_id": self.workload_identity["identity_provider_id"],
        }

    def _post_with_retries(self, body: Dict[str, str]) -> httpx.Response:
        """POST to the token endpoint, retrying like API requests: same status codes, backoff and `retry-after`."""
        client = self.http_client
        if not isinstance(client, httpx.Client):
            raise TypeError(f"Expected an httpx.Client for the token exchange, got {type(client)}")
        retries_taken = 0
        while True:
            retry_after: Optional[httpx.Headers] = None
            try:
                response = client.post(self.token_url, json=body, timeout=self._timeout, follow_redirects=False)
            except httpx.TimeoutException as e:
                if retries_taken >= self.max_retries:
                    raise APITimeoutError(request=e.request) from e
            except httpx.RequestError as e:
                if retries_taken >= self.max_retries:
                    raise APIConnectionError(request=e.request) from e
            else:
                if retries_taken >= self.max_retries or not _should_retry(response):
                    return response
                retry_after = response.headers
            time.sleep(_retry_delay(retries_taken, retry_after))
            retries_taken += 1

    async def _post_with_retries_async(self, body: Dict[str, str]) -> httpx.Response:
        client = self.http_client
        if not isinstance(client, httpx.AsyncClient):
            raise TypeError(f"Expected an httpx.AsyncClient for the token exchange, got {type(client)}")
        retries_taken = 0
        while True:
            retry_after: Optional[httpx.Headers] = None
            try:
                response = await client.post(self.token_url, json=body, timeout=self._timeout, follow_redirects=False)
            except httpx.TimeoutException as e:
                if retries_taken >= self.max_retries:
                    raise APITimeoutError(request=e.request) from e
            except httpx.RequestError as e:
                if retries_taken >= self.max_retries:
                    raise APIConnectionError(request=e.request) from e
            else:
                if retries_taken >= self.max_retries or not _should_retry(response):
                    return response
                retry_after = response.headers
            await anyio.sleep(_retry_delay(retries_taken, retry_after))
            retries_taken += 1


def _parse_exchange_response(response: httpx.Response) -> Tuple[str, float]:
    body: object
    try:
        body = response.json()
    except ValueError:
        body = response.text or None
    if not response.is_success:
        raise OAuthError(response=response, body=body)

    access_token = body.get("access_token") if is_dict(body) else None
    expires_in = body.get("expires_in") if is_dict(body) else None
    if (
        not isinstance(access_token, str)
        or not access_token
        or not isinstance(expires_in, (int, float))
        or isinstance(expires_in, bool)
        or expires_in <= 0
    ):
        raise APIResponseValidationError(
            response, body, message="Token exchange response did not include access_token and expires_in"
        )
    return access_token, float(expires_in)


def _should_retry(response: httpx.Response) -> bool:
    should_retry_header = response.headers.get("x-should-retry")
    if should_retry_header == "true":
        return True
    if should_retry_header == "false":
        return False
    return response.status_code in (408, 409, 429) or response.status_code >= 500


def _retry_delay(retries_taken: int, headers: Optional[httpx.Headers]) -> float:
    """Same schedule as `BaseClient._calculate_retry_timeout`."""
    if headers is not None:
        for name, scale in (("retry-after-ms", 1000.0), ("retry-after", 1.0)):
            try:
                retry_after = float(headers.get(name, "")) / scale
            except ValueError:
                continue
            if 0 < retry_after <= 60:
                return retry_after
    delay = min(INITIAL_RETRY_DELAY * pow(2.0, min(retries_taken, 1000)), MAX_RETRY_DELAY)
    return delay * (1 - 0.25 * random.random())
