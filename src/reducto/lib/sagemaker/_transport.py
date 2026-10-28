from __future__ import annotations

from typing import TYPE_CHECKING, Mapping, cast
from typing_extensions import Protocol, TypedDict

from ._session import Boto3Session
from .._page_parse._deps import LazyModule
from .._page_parse.transport import EndpointReply, EndpointOutcome, EndpointUnreachable

if TYPE_CHECKING:
    import botocore.config as botocore_config  # pyright: ignore[reportMissingTypeStubs]
    import botocore.exceptions as botocore_exceptions  # pyright: ignore[reportMissingTypeStubs]
else:
    botocore_config = LazyModule("botocore.config", "boto3", "sagemaker")
    botocore_exceptions = LazyModule("botocore.exceptions", "boto3", "sagemaker")

__all__ = ["BODY_LIMIT_BYTES", "RuntimeClient", "runtime_client", "SageMakerTransport"]

BODY_LIMIT_BYTES = 6 * 1024 * 1024
"""SageMaker InvokeEndpoint accepts a request body of at most 6 MB, with the base64 image."""

_MAX_CONNECT_TIMEOUT = 10.0
"""Seconds to wait for a connection. A reachable endpoint connects far faster, so a dead one fails early."""


class RuntimeClient(Protocol):
    """The part of the boto3 `sagemaker-runtime` client that the transport uses."""

    def invoke_endpoint(self, *, EndpointName: str, ContentType: str, Body: bytes) -> Mapping[str, object]: ...

    def close(self) -> None: ...


class _Body(Protocol):
    def read(self) -> bytes: ...


class _Error(TypedDict, total=False):
    Code: str
    Message: str


class _Metadata(TypedDict, total=False):
    HTTPStatusCode: int


class _ErrorResponse(TypedDict, total=False):
    """`ClientError.response`. A `ModelError` also carries the status and the body of the model container."""

    Error: _Error
    ResponseMetadata: _Metadata
    OriginalStatusCode: int
    OriginalMessage: str


def runtime_client(session: Boto3Session, *, timeout: float, max_pool_connections: int) -> RuntimeClient:
    """One client for every page. botocore retries are off, because the SDK retries each page."""
    config = botocore_config.Config(
        connect_timeout=min(timeout, _MAX_CONNECT_TIMEOUT),
        read_timeout=timeout,
        max_pool_connections=max_pool_connections,
        retries={"total_max_attempts": 1},
    )
    return cast(RuntimeClient, session.client("sagemaker-runtime", config=config))


class SageMakerTransport:
    """Sends each page to a SageMaker real-time endpoint. The botocore client is thread-safe."""

    body_limit = BODY_LIMIT_BYTES

    def __init__(self, client: RuntimeClient, endpoint_name: str) -> None:
        self._client = client
        self._endpoint_name = endpoint_name

    def send(self, body: bytes, /) -> EndpointOutcome:
        try:
            response = self._client.invoke_endpoint(
                EndpointName=self._endpoint_name, ContentType="application/json", Body=body
            )
            return EndpointReply(200, cast(_Body, response["Body"]).read())
        except botocore_exceptions.ClientError as error:
            reply = _page_error(cast(_ErrorResponse, error.response))
            if reply is None:
                raise
            return reply
        except (botocore_exceptions.ReadTimeoutError, botocore_exceptions.ConnectTimeoutError) as error:
            return EndpointUnreachable("timeout", str(error))
        except (
            botocore_exceptions.ConnectionError,
            botocore_exceptions.HTTPClientError,
            botocore_exceptions.IncompleteReadError,
        ) as error:
            return EndpointUnreachable("connection", str(error))


def _page_error(response: _ErrorResponse) -> EndpointReply | None:
    """The reply for an error of one page, or None for an error that fails every page, such as a missing endpoint."""
    code = response.get("Error", {}).get("Code", "")
    message = response.get("Error", {}).get("Message", "")
    status = response.get("ResponseMetadata", {}).get("HTTPStatusCode", 0)
    detail = f"{code}: {message}" if message else code
    if code == "ModelError":
        # The answer of the container. No error status means that the container did not answer in time: a 504.
        original_status = response.get("OriginalStatusCode", 0)
        original_body = response.get("OriginalMessage")
        status = original_status if original_status >= 400 else 504
        if original_body is not None:
            return EndpointReply(status, original_body.encode())
        return EndpointReply(status, detail=detail)
    if code == "ThrottlingException":
        return EndpointReply(429, detail=detail)
    if status in (413, 429) or status >= 500:
        return EndpointReply(status, detail=detail)
    return None
