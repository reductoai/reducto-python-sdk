from __future__ import annotations

import json

import pytest
from botocore.exceptions import (  # pyright: ignore[reportMissingTypeStubs]
    ClientError,
    NoCredentialsError,
    ConnectTimeoutError,
    EndpointConnectionError,
)

from reducto import PageParseError, ReductoSageMaker
from reducto.lib.sagemaker._transport import RuntimeClient
from reducto.lib._page_parse.transport import Failure, EndpointReply, EndpointUnreachable, classify_outcome

from ._stubs import (
    ENDPOINT,
    CREDENTIALS,
    CANNOT_PROCESS_BODY,
    Stub,
    FakeRuntime,
    LocalEndpoint,
    serve,
    runtime_meta,
    make_transport,
)
from .._page_parse._helpers import make_pdf


def test_success_returns_the_body() -> None:
    """Catches a reply that drops or re-encodes the endpoint's JSON body."""
    transport, runtime = make_transport()
    stub = Stub(runtime)
    stub.reply(b'{"blocks": []}')
    assert transport.send(b"{}") == EndpointReply(200, b'{"blocks": []}')
    stub.assert_all_used()


@pytest.mark.parametrize(
    ("original_status", "original_body"),
    [(422, CANNOT_PROCESS_BODY), (500, '{"detail": "server error"}'), (415, '{"detail": "unsupported"}')],
)
def test_model_error_returns_the_container_status_and_body(original_status: int, original_body: str) -> None:
    """Catches a 424 taken at face value: the 422 would not count as unprocessable and a 500 would not be retried."""
    transport, runtime = make_transport()
    Stub(runtime).error(
        "ModelError", 424, "client error", OriginalStatusCode=original_status, OriginalMessage=original_body
    )
    assert transport.send(b"{}") == EndpointReply(original_status, original_body.encode())


def test_wrapped_422_is_an_unprocessable_page() -> None:
    """Catches the SageMaker 424 for a page the endpoint cannot process, read as a retryable or generic error."""
    transport, runtime = make_transport()
    Stub(runtime).error("ModelError", 424, "client error", OriginalStatusCode=422, OriginalMessage=CANNOT_PROCESS_BODY)
    outcome = classify_outcome(transport.send(b"{}"))
    assert outcome == Failure("unprocessable", "status 422: input could not be processed", 422, retryable=False)


@pytest.mark.parametrize("original_status", [None, 0, 1, 399])
def test_container_timeout_is_a_final_504(original_status: int | None) -> None:
    """Catches a container that did not answer in time reported as a success, or retried."""
    transport, runtime = make_transport()
    fields = {} if original_status is None else {"OriginalStatusCode": original_status}
    Stub(runtime).error("ModelError", 424, "The container did not answer.", **fields)
    outcome = classify_outcome(transport.send(b"{}"))
    assert isinstance(outcome, Failure)
    assert (outcome.reason, outcome.status, outcome.retryable) == ("error", 504, False)
    assert outcome.detail == "status 504: ModelError: The container did not answer."


@pytest.mark.parametrize(
    ("code", "status", "expected"),
    [
        ("ThrottlingException", 400, 429),
        ("ModelNotReadyException", 429, 429),
        ("PayloadTooLarge", 413, 413),
        ("InternalFailure", 500, 500),
        ("ServiceUnavailable", 503, 503),
        ("InternalDependencyException", 530, 530),
    ],
)
def test_page_errors_fail_only_the_page(code: str, status: int, expected: int) -> None:
    """Catches a throttle, an oversize page, or an outage that stops every page of the document."""
    transport, runtime = make_transport()
    Stub(runtime).error(code, status, "Try again later.")
    assert transport.send(b"{}") == EndpointReply(expected, detail=f"{code}: Try again later.")


@pytest.mark.parametrize(
    ("code", "status"),
    [("ValidationError", 400), ("AccessDeniedException", 403), ("UnrecognizedClientException", 403)],
)
def test_configuration_errors_raise_unchanged(code: str, status: int) -> None:
    """Catches a wrong endpoint name or a missing permission hidden as a failed page on every page."""
    transport, runtime = make_transport()
    Stub(runtime).error(code, status, "Endpoint my-endpoint not found.")
    with pytest.raises(ClientError) as raised:
        transport.send(b"{}")
    assert raised.value.response["Error"]["Code"] == code  # pyright: ignore[reportUnknownMemberType]


def test_botocore_does_not_retry(monkeypatch: pytest.MonkeyPatch) -> None:
    """Catches botocore retries on top of the SDK's, which multiply the calls and the wait for a bad page."""
    endpoint = LocalEndpoint(503, b'{"message": "busy"}', {"x-amzn-ErrorType": "ServiceUnavailable"})
    with serve(endpoint, monkeypatch):
        reply = make_transport()[0].send(b"{}")
    assert isinstance(reply, EndpointReply) and reply.status == 503
    assert len(endpoint.requests) == 1


def test_model_error_on_the_wire_is_unwrapped(monkeypatch: pytest.MonkeyPatch) -> None:
    """Catches a parse of the 424 that misses OriginalStatusCode in a real SageMaker answer."""
    wire = json.dumps({"OriginalStatusCode": 422, "OriginalMessage": CANNOT_PROCESS_BODY, "Message": "client error"})
    with serve(LocalEndpoint(424, wire.encode(), {"x-amzn-ErrorType": "ModelError"}), monkeypatch):
        assert make_transport()[0].send(b"{}") == EndpointReply(422, CANNOT_PROCESS_BODY.encode())


def test_timeout_fails_the_page_without_a_retry(monkeypatch: pytest.MonkeyPatch, runtimes: list[RuntimeClient]) -> None:
    """Catches a `timeout` that is not applied, which waits on a stuck endpoint for a minute or more."""
    endpoint = LocalEndpoint(delay=5)
    with serve(endpoint, monkeypatch), pytest.raises(PageParseError) as raised:
        client = ReductoSageMaker(endpoint_name=ENDPOINT, aws_region="us-east-2", timeout=0.2, **CREDENTIALS)
        client.parse.run(input=make_pdf(1))
    assert [(page.reason, page.status) for page in raised.value.failed_pages] == [("error", None)]
    assert (raised.value.failed_pages[0].detail or "").startswith("timeout:")
    assert len(endpoint.requests) == 1
    assert len(runtimes) == 1


def test_truncated_body_is_a_connection_failure(monkeypatch: pytest.MonkeyPatch) -> None:
    """Catches a connection that breaks in the body, raised out of the parse instead of a retry of the page."""
    with serve(LocalEndpoint(body=b'{"blocks"', content_length=100), monkeypatch):
        outcome = make_transport()[0].send(b"{}")
    assert isinstance(outcome, EndpointUnreachable) and outcome.kind == "connection"


@pytest.mark.parametrize(
    ("error", "calls", "kind"),
    [
        (EndpointConnectionError(endpoint_url="http://127.0.0.1:9"), 3, "connection:"),
        (ConnectTimeoutError(endpoint_url="http://127.0.0.1:9"), 1, "timeout:"),
    ],
    ids=["refused-is-retried", "connect-timeout-is-not"],
)
def test_connect_failures(fake_runtime: FakeRuntime, error: Exception, calls: int, kind: str) -> None:
    """Catches a refused connect raised out of the parse instead of a retry, or a connect timeout retried,
    which triples the wait on a dead endpoint."""

    def handler(_call: int) -> dict[str, object]:
        raise error

    fake_runtime.handler = handler
    client = ReductoSageMaker(endpoint_name=ENDPOINT, aws_region="us-east-2", **CREDENTIALS)
    with pytest.raises(PageParseError) as raised:
        client.parse.run(input=make_pdf(1))
    assert len(fake_runtime.bodies) == calls
    assert (raised.value.failed_pages[0].detail or "").startswith(kind)


def test_client_config_bounds_the_connect_wait_and_sizes_the_pool(runtimes: list[RuntimeClient]) -> None:
    """Catches a 60-second connect wait on a dead endpoint, or a pool smaller than the pages in flight."""
    ReductoSageMaker(endpoint_name=ENDPOINT, aws_region="us-east-2", max_concurrency=7, **CREDENTIALS)
    config = runtime_meta(runtimes[0]).config
    assert config.connect_timeout == 10
    assert config.max_pool_connections >= 7


def test_missing_credentials_raise(monkeypatch: pytest.MonkeyPatch) -> None:
    """Catches missing credentials hidden as a failed page on every page of the document."""
    endpoint = LocalEndpoint()
    with serve(endpoint, monkeypatch):
        client = ReductoSageMaker(endpoint_name=ENDPOINT, aws_region="us-east-2")
        with pytest.raises(NoCredentialsError):
            client.parse.run(input=make_pdf(1))
    assert endpoint.requests == []
