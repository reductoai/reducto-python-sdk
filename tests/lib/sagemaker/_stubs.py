# pyright: reportUnknownMemberType=false, reportUnknownVariableType=false, reportMissingTypeStubs=false
from __future__ import annotations

import io
import json
import threading
from typing import Any, Mapping, Callable, Iterator
from contextlib import contextmanager
from dataclasses import field, dataclass
from http.server import ThreadingHTTPServer, BaseHTTPRequestHandler
from typing_extensions import TypedDict, override

import pytest
from botocore.stub import ANY, Stubber
from botocore.response import StreamingBody

from reducto.lib.sagemaker._session import boto3_session
from reducto.lib.sagemaker._transport import RuntimeClient, SageMakerTransport, runtime_client
from reducto.lib._page_parse.transport import CANNOT_PROCESS_DETAIL

ENDPOINT = "my-endpoint"
CANNOT_PROCESS_BODY = json.dumps({"detail": CANNOT_PROCESS_DETAIL})


class Credentials(TypedDict):
    aws_access_key: str
    aws_secret_key: str


CREDENTIALS: Credentials = {"aws_access_key": "AKIDEXAMPLE", "aws_secret_key": "secret"}


def make_transport(timeout: float = 5.0) -> tuple[SageMakerTransport, RuntimeClient]:
    """A transport on a real botocore client, as the SageMaker client builds it."""
    session, _region = boto3_session(aws_region="us-east-2", aws_profile=None, aws_session_token=None, **CREDENTIALS)
    runtime = runtime_client(session, timeout=timeout, max_pool_connections=4)
    return SageMakerTransport(runtime, ENDPOINT), runtime


def runtime_meta(runtime: RuntimeClient) -> Any:
    """The botocore client metadata (region, config)."""
    return runtime.meta  # pyright: ignore[reportAttributeAccessIssue]


class Stub:
    """A typed wrapper of botocore's Stubber on a real `sagemaker-runtime` client."""

    def __init__(self, runtime: RuntimeClient) -> None:
        self._stubber = Stubber(runtime)
        self._stubber.activate()

    def reply(self, body: bytes, content_length: int | None = None) -> None:
        """A length over `len(body)` makes the read of the body fail."""
        stream = StreamingBody(io.BytesIO(body), content_length or len(body))
        response = {"Body": stream, "ContentType": "application/json"}
        expected = {"EndpointName": ENDPOINT, "ContentType": "application/json", "Body": ANY}
        self._stubber.add_response("invoke_endpoint", response, expected)

    def error(self, code: str, status: int, message: str = "", **fields: object) -> None:
        self._stubber.add_client_error(
            "invoke_endpoint",
            service_error_code=code,
            service_message=message,
            http_status_code=status,
            modeled_fields=fields or None,
        )

    def assert_all_used(self) -> None:
        self._stubber.assert_no_pending_responses()


class FakeRuntime:
    """A thread-safe fake `sagemaker-runtime` client. `handler` answers each call; it records the bodies
    and the peak number of calls in flight."""

    def __init__(self) -> None:
        self.handler: Callable[[int], Mapping[str, object]] = lambda _call: {"Body": io.BytesIO(b"{}")}
        self.bodies: list[bytes] = []
        self.closed = False
        self.in_flight = 0
        self.peak = 0
        self._lock = threading.Lock()

    def invoke_endpoint(self, *, EndpointName: str, ContentType: str, Body: bytes) -> Mapping[str, object]:  # noqa: N803
        assert EndpointName == ENDPOINT and ContentType == "application/json"
        with self._lock:
            call = len(self.bodies)
            self.bodies.append(Body)
            self.in_flight += 1
            self.peak = max(self.peak, self.in_flight)
        try:
            return self.handler(call)
        finally:
            with self._lock:
                self.in_flight -= 1

    def close(self) -> None:
        self.closed = True


@dataclass
class LocalEndpoint:
    """What a loopback endpoint answers, and the headers of each request that it gets."""

    status: int = 200
    body: bytes = b"{}"
    headers: dict[str, str] = field(default_factory=dict)
    delay: float = 0.0
    content_length: int | None = None
    """A length over `len(body)` sends a truncated body."""

    requests: list[Mapping[str, str]] = field(default_factory=list)
    """The headers of each request, with lowercase names."""


class _QuietServer(ThreadingHTTPServer):
    @override
    def handle_error(self, request: object, client_address: object) -> None:
        """A client that gives up first, as in the timeout tests, breaks the pipe. That is expected."""


@contextmanager
def serve(endpoint: LocalEndpoint, monkeypatch: pytest.MonkeyPatch) -> Iterator[None]:
    """Sends every SageMaker client made inside the block to a loopback server."""
    stop = threading.Event()

    class Handler(BaseHTTPRequestHandler):
        def do_POST(self) -> None:
            endpoint.requests.append({name.lower(): value for name, value in self.headers.items()})
            self.rfile.read(int(self.headers["Content-Length"]))
            stop.wait(endpoint.delay)
            self.send_response(endpoint.status)
            for name, value in {"Content-Type": "application/json", **endpoint.headers}.items():
                self.send_header(name, value)
            self.send_header("Content-Length", str(endpoint.content_length or len(endpoint.body)))
            self.end_headers()
            self.wfile.write(endpoint.body)

        @override
        def log_message(self, format: str, *args: object) -> None:  # noqa: A002, ARG002
            return None

    server = _QuietServer(("127.0.0.1", 0), Handler)
    thread = threading.Thread(target=server.serve_forever, args=(0.05,), daemon=True)
    thread.start()
    monkeypatch.setenv("AWS_ENDPOINT_URL_SAGEMAKER_RUNTIME", f"http://127.0.0.1:{server.server_address[1]}")
    try:
        yield
    finally:
        stop.set()
        server.shutdown()
        server.server_close()
