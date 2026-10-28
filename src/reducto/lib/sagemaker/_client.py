from __future__ import annotations

from typing_extensions import override

from ._session import boto3_session
from ._transport import RuntimeClient, SageMakerTransport, runtime_client
from .._page_parse.client import (
    DEFAULT_MAX_RETRIES,
    DEFAULT_MAX_CONCURRENCY,
    PageParseClient,
    AsyncPageParseClient,
    _PageParseClientBase,
    check_client_settings,
)

__all__ = ["ReductoSageMaker", "AsyncReductoSageMaker"]

_DEFAULT_TIMEOUT = 65.0
"""Seconds to wait for one page. A SageMaker real-time endpoint must answer within 60 seconds."""

_POOL_HEADROOM = 2
"""Spare botocore connections beyond max_concurrency, so a page never waits for a connection that is closing."""


class _SageMakerClientBase(_PageParseClientBase):
    """The AWS parts of the SageMaker clients: credentials, region, and the `sagemaker-runtime` client."""

    _runtime: RuntimeClient
    _aws_region: str

    def __init__(
        self,
        *,
        endpoint_name: str,
        aws_region: str | None = None,
        aws_profile: str | None = None,
        aws_access_key: str | None = None,
        aws_secret_key: str | None = None,
        aws_session_token: str | None = None,
        max_concurrency: int = DEFAULT_MAX_CONCURRENCY,
        max_retries: int = DEFAULT_MAX_RETRIES,
        timeout: float = _DEFAULT_TIMEOUT,
    ) -> None:
        """`max_concurrency` is the number of pages in flight per client, across every `parse.run` call that
        shares the client. `timeout` is the read timeout of one call, in seconds. A bad limit raises ValueError.
        Incomplete AWS keys, an unknown profile, or no region raise ReductoError. Without AWS arguments, boto3
        finds the credentials."""
        check_client_settings(max_concurrency=max_concurrency, max_retries=max_retries, timeout=timeout)
        session, region = boto3_session(
            aws_region=aws_region,
            aws_profile=aws_profile,
            aws_access_key=aws_access_key,
            aws_secret_key=aws_secret_key,
            aws_session_token=aws_session_token,
        )
        self._runtime = runtime_client(session, timeout=timeout, max_pool_connections=max_concurrency + _POOL_HEADROOM)
        self._endpoint_name = endpoint_name
        self._aws_region = region
        super().__init__(
            transport=SageMakerTransport(self._runtime, endpoint_name),
            max_concurrency=max_concurrency,
            max_retries=max_retries,
        )

    @property
    def endpoint_name(self) -> str:
        return self._endpoint_name

    @property
    def aws_region(self) -> str:
        return self._aws_region

    @override
    def _close_transport(self) -> None:
        self._runtime.close()


class ReductoSageMaker(_SageMakerClientBase, PageParseClient):
    """A client for your r-1 endpoint on Amazon SageMaker. It supports `parse.run` only."""


class AsyncReductoSageMaker(_SageMakerClientBase, AsyncPageParseClient):
    """The async form of `ReductoSageMaker`. Each parse runs in a worker thread, because boto3 is not async."""
