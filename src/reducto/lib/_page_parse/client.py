"""The parts of a client for your own r-1 endpoint that every provider shares. A provider client calls
`check_client_settings`, builds its `PageTransport`, and passes it to `PageParseClient` or
`AsyncPageParseClient`."""

from __future__ import annotations

import inspect
import functools
import threading
from types import TracebackType
from typing import TYPE_CHECKING, Dict, Mapping, Optional, AbstractSet
from typing_extensions import Self, Literal

import anyio
import httpx
import anyio.to_thread

from ._deps import check_installed
from .types import ProviderParseResponse
from .errors import UnsupportedOnProviderError
from .runner import DEFAULT_MAX_RETRIES, DEFAULT_MAX_CONCURRENCY, PageSlots, parse_pages, check_limits
from .options import ParseOptions
from ..._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ..._utils import is_given
from ..._compat import cached_property
from .documents import DocumentInput
from .transport import PageTransport
from ...types.enhance_param import EnhanceParam
from ...types.settings_param import SettingsParam
from ...types.retrieval_param import RetrievalParam
from ...types.formatting_param import FormattingParam
from ...types.spreadsheet_param import SpreadsheetParam
from ...types.async_config_v3_param import AsyncConfigV3Param

__all__ = [
    "DEFAULT_MAX_CONCURRENCY",
    "DEFAULT_MAX_RETRIES",
    "AsyncPageParseClient",
    "AsyncPageParseResource",
    "PageParseClient",
    "PageParseResource",
    "check_client_settings",
]

_ABANDON_ON_CANCEL = "abandon_on_cancel" in inspect.signature(anyio.to_thread.run_sync).parameters

_HOSTED_ONLY_CLIENT = frozenset(
    {
        "extract",
        "split",
        "edit",
        "pipeline",
        "classify",
        "job",
        "webhook",
        "upload",
        "delete_upload",
        "api_version",
        "copy",
        "with_options",
        "with_raw_response",
        "with_streaming_response",
    }
)
_HOSTED_ONLY_PARSE = frozenset({"run_job", "with_raw_response", "with_streaming_response"})


class _UnsupportedAttribute(UnsupportedOnProviderError, AttributeError):
    """Also an AttributeError, so `hasattr` returns False for a hosted-only name."""


# Tracebacks show the public class that callers catch.
_UnsupportedAttribute.__module__ = "reducto"
_UnsupportedAttribute.__qualname__ = _UnsupportedAttribute.__name__ = "UnsupportedOnProviderError"


def check_client_settings(*, max_concurrency: int, max_retries: int, timeout: float) -> None:
    """Checks the shared client settings and the installed packages. A provider calls it before it builds its
    transport. A bad limit raises ValueError; a missing package raises ImportError with the install hint."""
    check_limits(max_concurrency, max_retries)
    if timeout <= 0:
        raise ValueError("timeout must be positive.")
    check_installed()


def _missing_attribute(owner: object, path: str, name: str, hosted_only: AbstractSet[str]) -> AttributeError:
    """The error for a name that the object does not have. A hosted-only name points to the hosted API."""
    if name in hosted_only:
        return _UnsupportedAttribute(f"`{path}.{name}`")
    return AttributeError(f"{type(owner).__name__!r} object has no attribute {name!r}")


class _PageParseClientBase:
    def __init__(
        self,
        *,
        transport: PageTransport,
        max_concurrency: int = DEFAULT_MAX_CONCURRENCY,
        max_retries: int = DEFAULT_MAX_RETRIES,
    ) -> None:
        """`transport` sends each page. Call `check_client_settings` before you build it."""
        self._transport = transport
        self._slots = PageSlots(max_concurrency)
        self._max_retries = max_retries

    def _close_transport(self) -> None:
        """Releases the transport's connections. A provider overrides it when its transport holds any."""

    if not TYPE_CHECKING:

        def __getattr__(self, name: str) -> object:
            raise _missing_attribute(self, "client", name, _HOSTED_ONLY_CLIENT)


class PageParseClient(_PageParseClientBase):
    """A client for your own r-1 endpoint. It supports `parse.run` only."""

    @cached_property
    def parse(self) -> PageParseResource:
        return PageParseResource(self)

    def close(self) -> None:
        """Closes the connections to the endpoint."""
        self._close_transport()

    def __enter__(self) -> Self:
        return self

    def __exit__(
        self, exc_type: type[BaseException] | None, exc: BaseException | None, exc_tb: TracebackType | None
    ) -> None:
        self.close()


class AsyncPageParseClient(_PageParseClientBase):
    """The async form of `PageParseClient`. Each parse runs in a worker thread."""

    @cached_property
    def parse(self) -> AsyncPageParseResource:
        return AsyncPageParseResource(self)

    async def close(self) -> None:
        """Closes the connections to the endpoint."""
        self._close_transport()

    async def __aenter__(self) -> Self:
        return self

    async def __aexit__(
        self, exc_type: type[BaseException] | None, exc: BaseException | None, exc_tb: TracebackType | None
    ) -> None:
        await self.close()


def _run_options(
    *,
    enhance: EnhanceParam | Omit,
    formatting: FormattingParam | Omit,
    retrieval: RetrievalParam | Omit,
    settings: SettingsParam | Omit,
    spreadsheet: SpreadsheetParam | Omit,
    async_: AsyncConfigV3Param | Omit,
    queue_priority: Literal["auto", "standard", "batch"] | Omit,
    extra_headers: Headers | None,
    extra_query: Query | None,
    extra_body: Body | None,
    timeout: float | httpx.Timeout | None | NotGiven,
) -> Dict[str, object]:
    """The `parse.run` option groups. Raises UnsupportedOnProviderError for a hosted request option that is
    given: the client sends each page itself, so it cannot apply them."""
    request_options: Dict[str, object] = {
        "async_": async_,
        "queue_priority": queue_priority,
        "extra_headers": extra_headers,
        "extra_query": extra_query,
        "extra_body": extra_body,
        "timeout": timeout,
    }
    for name, value in request_options.items():
        if value is not None and is_given(value):
            raise UnsupportedOnProviderError(f"The `{name}` option")
    return {
        "enhance": enhance,
        "formatting": formatting,
        "retrieval": retrieval,
        "settings": settings,
        "spreadsheet": spreadsheet,
    }


class _ParseResource:
    def __init__(self, client: _PageParseClientBase) -> None:
        self._client = client

    def _parse(
        self, input: DocumentInput, groups: Mapping[str, object], stop: Optional[threading.Event]
    ) -> ProviderParseResponse:
        return parse_pages(
            input,
            self._client._transport,
            options=ParseOptions.from_run_kwargs(groups),
            slots=self._client._slots,
            max_retries=self._client._max_retries,
            stop=stop,
        )

    if not TYPE_CHECKING:

        def __getattr__(self, name: str) -> object:
            raise _missing_attribute(self, "client.parse", name, _HOSTED_ONLY_PARSE)


class PageParseResource(_ParseResource):
    def run(
        self,
        *,
        input: DocumentInput,
        enhance: EnhanceParam | Omit = omit,
        formatting: FormattingParam | Omit = omit,
        retrieval: RetrievalParam | Omit = omit,
        settings: SettingsParam | Omit = omit,
        spreadsheet: SpreadsheetParam | Omit = omit,
        async_: AsyncConfigV3Param | Omit = omit,
        queue_priority: Literal["auto", "standard", "batch"] | Omit = omit,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ProviderParseResponse:
        """Parses a PDF or an image page by page. `input` is a path, bytes, or a binary file.
        Only `settings.page_range` and `settings.document_password` are supported; the hosted request options
        (`async_`, `queue_priority`, `extra_*`, `timeout`) raise UnsupportedOnProviderError when given.
        Raises PageParseError when any page fails."""
        groups = _run_options(
            enhance=enhance,
            formatting=formatting,
            retrieval=retrieval,
            settings=settings,
            spreadsheet=spreadsheet,
            async_=async_,
            queue_priority=queue_priority,
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
        )
        return self._parse(input, groups, None)


class AsyncPageParseResource(_ParseResource):
    async def run(
        self,
        *,
        input: DocumentInput,
        enhance: EnhanceParam | Omit = omit,
        formatting: FormattingParam | Omit = omit,
        retrieval: RetrievalParam | Omit = omit,
        settings: SettingsParam | Omit = omit,
        spreadsheet: SpreadsheetParam | Omit = omit,
        async_: AsyncConfigV3Param | Omit = omit,
        queue_priority: Literal["auto", "standard", "batch"] | Omit = omit,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ProviderParseResponse:
        """Parses a PDF or an image page by page in a worker thread.
        Only `settings.page_range` and `settings.document_password` are supported; the hosted request options
        (`async_`, `queue_priority`, `extra_*`, `timeout`) raise UnsupportedOnProviderError when given.
        Raises PageParseError when any page fails. A cancel returns at once and stops new renders and sends;
        a page call that is in progress finishes in the background."""
        groups = _run_options(
            enhance=enhance,
            formatting=formatting,
            retrieval=retrieval,
            settings=settings,
            spreadsheet=spreadsheet,
            async_=async_,
            queue_priority=queue_priority,
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
        )
        ParseOptions.from_run_kwargs(groups)
        stop = threading.Event()
        call = functools.partial(self._parse, input, groups, stop)
        limiter = anyio.CapacityLimiter(1)
        try:
            if _ABANDON_ON_CANCEL:
                return await anyio.to_thread.run_sync(call, abandon_on_cancel=True, limiter=limiter)
            return await anyio.to_thread.run_sync(call, cancellable=True, limiter=limiter)
        finally:
            stop.set()
