from __future__ import annotations

import ssl
import json
import time
import shutil
import hashlib
import threading
import subprocess
from typing import Any, Dict, List, Tuple, Iterator, Optional
from pathlib import Path
from http.server import ThreadingHTTPServer, BaseHTTPRequestHandler
from typing_extensions import override

import httpx
import pytest
from respx import MockRouter

from reducto import Reducto, AsyncReducto, ReductoError, SubjectTokenProviderError
from reducto.auth import X509Provider, WorkloadIdentity, x509_workload_identity
from reducto._types import Omit

from .utils import update_env

mtls_url = "https://mtls.platform.reducto.ai"
no_env = {
    "REDUCTO_API_KEY": Omit(),
    "REDUCTO_BASE_URL": Omit(),
    "REDUCTO_IDENTITY_PROVIDER_ID": Omit(),
    "REDUCTO_IDENTITY_TOKEN_FILE": Omit(),
    "REDUCTO_IDENTITY_TOKEN": Omit(),
    "REDUCTO_MTLS_CERT_CHAIN": Omit(),
    "REDUCTO_MTLS_KEY": Omit(),
}

pytestmark = pytest.mark.skipif(shutil.which("openssl") is None, reason="needs the openssl CLI")


class Pki:
    """A CA, a `localhost` server certificate and client certificates, made with the openssl CLI."""

    def __init__(self, root: Path) -> None:
        self.root = root
        self.ca_cert, self.ca_key = self._issue("ca", "/CN=Test CA", ca=True)
        self.server_cert, self.server_key = self._issue("server", "/CN=localhost", san="DNS:localhost,IP:127.0.0.1")

    def client(self, name: str) -> Tuple[Path, Path]:
        """Returns (chain, key). The chain is the leaf then the CA."""
        cert, key = self._issue(name, f"/CN={name}")
        chain = self.root / f"{name}-chain.pem"
        chain.write_bytes(cert.read_bytes() + self.ca_cert.read_bytes())
        return chain, key

    def _issue(self, name: str, subject: str, *, ca: bool = False, san: Optional[str] = None) -> Tuple[Path, Path]:
        cert, key = self.root / f"{name}.pem", self.root / f"{name}-key.pem"
        args = ["openssl", "req", "-x509", "-newkey", "ec", "-pkeyopt", "ec_paramgen_curve:P-256", "-nodes"]
        args += ["-keyout", str(key), "-out", str(cert), "-subj", subject, "-days", "2"]
        if ca:
            args += ["-addext", "basicConstraints=critical,CA:TRUE", "-addext", "keyUsage=critical,keyCertSign"]
        else:
            args += ["-CA", str(self.ca_cert), "-CAkey", str(self.ca_key)]
            args += ["-addext", "basicConstraints=critical,CA:FALSE"]
        if san:
            args += ["-addext", f"subjectAltName={san}"]
        subprocess.run(args, check=True, capture_output=True)
        return cert, key


def fingerprint(chain: Path) -> str:
    leaf = chain.read_text().split("-----END CERTIFICATE-----")[0] + "-----END CERTIFICATE-----\n"
    return hashlib.sha256(ssl.PEM_cert_to_DER_cert(leaf)).hexdigest()


@pytest.fixture(scope="module")
def pki(tmp_path_factory: pytest.TempPathFactory) -> Pki:
    return Pki(tmp_path_factory.mktemp("pki"))


@pytest.fixture(autouse=True)
def clean_env() -> Iterator[None]:
    with update_env(**no_env):
        yield


def identity(chain: Path, key: Path) -> WorkloadIdentity:
    return {"identity_provider_id": "wip_x509", "provider": x509_workload_identity(cert_chain=chain, key=key)}


def token_response(n: int) -> httpx.Response:
    return httpx.Response(200, json={"access_token": f"rdat_{n}", "token_type": "Bearer", "expires_in": 3600})


class TestClient:
    def test_exchange_body_and_mtls_base_url(self, respx_mock: MockRouter, pki: Pki) -> None:
        token: Any = respx_mock.post(f"{mtls_url}/oauth/token").mock(return_value=token_response(1))
        api: Any = respx_mock.get(f"{mtls_url}/version").mock(return_value=httpx.Response(200, text="1"))

        client = Reducto(workload_identity=identity(*pki.client("a")))
        assert client.base_url == mtls_url
        assert client.api_version() == "1"

        assert json.loads(token.calls[0].request.content) == {
            "grant_type": "urn:ietf:params:oauth:grant-type:token-exchange",
            "subject_token_type": "urn:reducto:params:oauth:token-type:x509",
            "identity_provider_id": "wip_x509",
        }
        assert api.calls[0].request.headers["Authorization"] == "Bearer rdat_1"

    @pytest.mark.parametrize(
        "environment, expected",
        [
            ("production", "https://mtls.platform.reducto.ai"),
            ("eu", "https://mtls.eu.platform.reducto.ai"),
            ("au", "https://mtls.au.platform.reducto.ai"),
        ],
    )
    def test_regional_mtls_hosts(self, pki: Pki, environment: Any, expected: str) -> None:
        client = Reducto(workload_identity=identity(*pki.client("a")), environment=environment)
        assert client.base_url == expected
        auth = client._workload_identity_auth
        assert auth is not None and auth.token_url == f"{expected}/oauth/token"

    def test_explicit_base_url_is_kept(self, pki: Pki) -> None:
        assert Reducto(workload_identity=identity(*pki.client("a")), base_url="https://x.example").base_url == (
            "https://x.example"
        )
        with update_env(REDUCTO_BASE_URL="https://y.example"):
            assert Reducto(workload_identity=identity(*pki.client("a"))).base_url == "https://y.example"

    def test_custom_http_client_is_rejected(self, pki: Pki) -> None:
        with pytest.raises(ReductoError, match="custom http_client"):
            Reducto(workload_identity=identity(*pki.client("a")), http_client=httpx.Client())

    def test_copy_shares_http_client_and_token(self, pki: Pki) -> None:
        client = Reducto(workload_identity=identity(*pki.client("a")))
        copied = client.copy(timeout=5)
        assert copied._client is client._client
        assert copied._workload_identity_auth is client._workload_identity_auth
        other = client.copy(workload_identity=identity(*pki.client("b")))
        assert other._client is not client._client

    def test_copy_switches_default_host(self, pki: Pki) -> None:
        chain, key = pki.client("copy")
        client = Reducto(api_key="key", environment="eu")
        copied = client.copy(workload_identity=identity(chain, key))
        assert str(copied.base_url).rstrip("/") == "https://mtls.eu.platform.reducto.ai"
        assert str(copied.copy(api_key="key").base_url).rstrip("/") == "https://eu.platform.reducto.ai"
        explicit = Reducto(api_key="key", base_url="https://eu.platform.reducto.ai")
        explicit_copy = explicit.copy(workload_identity=identity(chain, key))
        assert str(explicit_copy.base_url).rstrip("/") == "https://eu.platform.reducto.ai"
        custom = Reducto(api_key="key", base_url="https://reducto.internal")
        assert (
            str(custom.copy(workload_identity=identity(chain, key)).base_url).rstrip("/") == "https://reducto.internal"
        )

    def test_unreadable_files(self, respx_mock: MockRouter, tmp_path: Path) -> None:
        respx_mock.get(f"{mtls_url}/version").mock(return_value=httpx.Response(200, text="1"))
        client = Reducto(workload_identity=identity(tmp_path / "missing.pem", tmp_path / "missing-key.pem"))
        with pytest.raises(SubjectTokenProviderError, match="Failed to read the client certificate"):
            client.api_version()

    def test_key_does_not_match(self, pki: Pki) -> None:
        chain, _ = pki.client("a")
        _, other_key = pki.client("b")
        client = Reducto(workload_identity=identity(chain, other_key))
        with pytest.raises(SubjectTokenProviderError, match="Failed to load the client certificate"):
            client.api_version()


class TestEnv:
    def test_mtls_env(self, pki: Pki) -> None:
        chain, key = pki.client("a")
        with update_env(
            REDUCTO_IDENTITY_PROVIDER_ID="wip_env", REDUCTO_MTLS_CERT_CHAIN=str(chain), REDUCTO_MTLS_KEY=str(key)
        ):
            client = Reducto()
        assert client.base_url == mtls_url
        assert client.workload_identity is not None
        provider = client.workload_identity["provider"]
        assert provider["token_type"] == "x509"
        assert provider["client_certificate"].cert_chain == str(chain)

    def test_cert_without_key(self) -> None:
        with update_env(REDUCTO_IDENTITY_PROVIDER_ID="wip_env", REDUCTO_MTLS_CERT_CHAIN="chain.pem"):
            with pytest.raises(ReductoError, match="must be set together"):
                Reducto()

    def test_mtls_and_token_env_conflict(self) -> None:
        with update_env(
            REDUCTO_IDENTITY_PROVIDER_ID="wip_env",
            REDUCTO_MTLS_CERT_CHAIN="chain.pem",
            REDUCTO_MTLS_KEY="key.pem",
            REDUCTO_IDENTITY_TOKEN="t",
        ):
            with pytest.raises(ReductoError, match="not both"):
                Reducto()


class MtlsServer:
    """An HTTPS server that requires a client certificate and records the leaf fingerprint of each request."""

    def __init__(self, pki: Pki) -> None:
        self.requests: List[Tuple[str, str, Optional[str]]] = []
        self.tokens: Dict[str, str] = {}
        self.expires_in = 3600
        server = self

        class Handler(BaseHTTPRequestHandler):
            protocol_version = "HTTP/1.1"  # keep-alive, so pooled connections are reused

            def do_POST(self) -> None:
                self._handle()

            def do_GET(self) -> None:
                self._handle()

            def _handle(self) -> None:
                self.rfile.read(int(self.headers.get("Content-Length") or 0))
                der = self.connection.getpeercert(binary_form=True)  # type: ignore[attr-defined]
                leaf = hashlib.sha256(der).hexdigest()
                server.requests.append((self.path, leaf, self.headers.get("Authorization")))
                if self.path == "/oauth/token":
                    token = f"rdat_{len(server.tokens) + 1}"
                    server.tokens[token] = leaf
                    body = json.dumps({"access_token": token, "token_type": "Bearer", "expires_in": server.expires_in})
                else:
                    bearer = (self.headers.get("Authorization") or "").removeprefix("Bearer ")
                    if server.tokens.get(bearer) != leaf:
                        self._send(
                            401, '{"detail": "certificate-bound token requires the matching client certificate"}'
                        )
                        return
                    body = "1"
                self._send(200, body)

            def _send(self, status: int, body: str) -> None:
                self.send_response(status)
                self.send_header("Content-Type", "application/json")
                self.send_header("Content-Length", str(len(body)))
                self.end_headers()
                self.wfile.write(body.encode())

            @override
            def log_message(self, format: str, *args: Any) -> None:
                pass

        context = ssl.create_default_context(ssl.Purpose.CLIENT_AUTH, cafile=str(pki.ca_cert))
        context.verify_mode = ssl.CERT_REQUIRED
        context.load_cert_chain(pki.server_cert, pki.server_key)
        self.httpd = ThreadingHTTPServer(("127.0.0.1", 0), Handler)
        self.httpd.socket = context.wrap_socket(self.httpd.socket, server_side=True)
        self.url = f"https://localhost:{self.httpd.server_address[1]}"
        threading.Thread(target=self.httpd.serve_forever, daemon=True).start()

    def close(self) -> None:
        self.httpd.shutdown()
        self.httpd.server_close()


@pytest.fixture
def server(pki: Pki) -> Iterator[MtlsServer]:
    server = MtlsServer(pki)
    with update_env(SSL_CERT_FILE=str(pki.ca_cert)):
        yield server
    server.close()


def rotate(provider: X509Provider, chain: Path, key: Path) -> None:
    Path(provider["client_certificate"].cert_chain).write_bytes(chain.read_bytes())
    Path(provider["client_certificate"].key).write_bytes(key.read_bytes())


class TestMutualTls:
    def test_certificate_on_exchange_and_api_and_rotation(self, server: MtlsServer, pki: Pki, tmp_path: Path) -> None:
        chain_a, key_a = pki.client("a")
        chain_b, key_b = pki.client("b")
        chain, key = tmp_path / "chain.pem", tmp_path / "key.pem"
        shutil.copy(chain_a, chain)
        shutil.copy(key_a, key)
        workload_identity = identity(chain, key)
        client = Reducto(workload_identity=workload_identity, base_url=server.url, max_retries=0)

        assert client.api_version() == "1"
        assert client.api_version() == "1"
        rotate(workload_identity["provider"], chain_b, key_b)  # type: ignore[arg-type]
        assert client.api_version() == "1"  # files are not re-read per request
        auth = client._workload_identity_auth
        assert auth is not None
        auth.invalidate("rdat_1")  # force the next re-exchange
        assert client.api_version() == "1"
        client.close()

        a, b = fingerprint(chain_a), fingerprint(chain_b)
        assert server.requests == [
            ("/oauth/token", a, None),
            ("/version", a, "Bearer rdat_1"),
            ("/version", a, "Bearer rdat_1"),
            ("/version", a, "Bearer rdat_1"),
            ("/oauth/token", b, None),
            ("/version", b, "Bearer rdat_2"),
        ]

    def test_rotation_on_scheduled_refresh(self, server: MtlsServer, pki: Pki, tmp_path: Path) -> None:
        # Tokens end at the leaf's not_after, so the scheduled refresh must pick up the rotated files.
        chain_a, key_a = pki.client("a")
        chain_b, key_b = pki.client("b")
        chain, key = tmp_path / "chain.pem", tmp_path / "key.pem"
        shutil.copy(chain_a, chain)
        shutil.copy(key_a, key)
        workload_identity = identity(chain, key)
        client = Reducto(workload_identity=workload_identity, base_url=server.url, max_retries=0)

        server.expires_in = 1
        assert client.api_version() == "1"
        rotate(workload_identity["provider"], chain_b, key_b)  # type: ignore[arg-type]
        time.sleep(0.6)  # past the refresh point at half the lifetime
        assert client.api_version() == "1"
        client.close()

        a, b = fingerprint(chain_a), fingerprint(chain_b)
        assert [(path, leaf) for path, leaf, _ in server.requests] == [
            ("/oauth/token", a),
            ("/version", a),
            ("/oauth/token", b),
            ("/version", b),
        ]

    async def test_async_client(self, server: MtlsServer, pki: Pki, tmp_path: Path) -> None:
        chain_a, key_a = pki.client("a")
        chain_b, key_b = pki.client("b")
        chain, key = tmp_path / "chain.pem", tmp_path / "key.pem"
        shutil.copy(chain_a, chain)
        shutil.copy(key_a, key)
        workload_identity = identity(chain, key)
        client = AsyncReducto(workload_identity=workload_identity, base_url=server.url, max_retries=0)

        assert await client.api_version() == "1"
        rotate(workload_identity["provider"], chain_b, key_b)  # type: ignore[arg-type]
        auth = client._workload_identity_auth
        assert auth is not None
        auth.invalidate("rdat_1")
        assert await client.api_version() == "1"
        await client.close()

        a, b = fingerprint(chain_a), fingerprint(chain_b)
        assert [(path, leaf) for path, leaf, _ in server.requests] == [
            ("/oauth/token", a),
            ("/version", a),
            ("/oauth/token", b),
            ("/version", b),
        ]
