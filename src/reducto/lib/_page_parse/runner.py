from __future__ import annotations

import time
import threading
from typing import List, Optional
from dataclasses import dataclass
from concurrent.futures import FIRST_EXCEPTION, Future, ThreadPoolExecutor, wait

from .types import FailedPage, ProviderParseResponse
from .errors import PageError
from .render import encode_page
from .options import ParseOptions, is_int
from .response import PageResult, ParsedPage, InvalidAnswerError, read_answer, build_response
from .documents import Document, DocumentInput, plan_pages, open_document
from .transport import Failure, PageOutcome, PageTransport, backoff_seconds, classify_outcome
from ..._exceptions import ReductoError

__all__ = ["DEFAULT_MAX_CONCURRENCY", "DEFAULT_MAX_RETRIES", "PageSlots", "Stopped", "check_limits", "parse_pages"]

DEFAULT_MAX_CONCURRENCY = 4
DEFAULT_MAX_RETRIES = 2

_STOP_POLL_SECONDS = 0.05
"""How often a page that waits for a slot checks whether the parse stopped."""


class Stopped(Exception):
    """The parse stopped (another page raised, or the caller cancelled), so this page does no more work."""


class PageSlots:
    """The limit on pages in flight, shared by every parse of one client."""

    def __init__(self, size: int) -> None:
        self.size = size
        self._semaphore = threading.BoundedSemaphore(size)

    def acquire(self, stop: threading.Event) -> None:
        """Waits for a free slot. Raises Stopped when the parse stops first."""
        while not self._semaphore.acquire(timeout=_STOP_POLL_SECONDS):
            if stop.is_set():
                raise Stopped
        if stop.is_set():
            self._semaphore.release()
            raise Stopped

    def release(self) -> None:
        self._semaphore.release()


@dataclass(frozen=True)
class _EncodedPage:
    index: int
    """The position of the page in the page plan (1-indexed)."""

    page: int
    """The page number in the original document (1-indexed)."""

    body: bytes


def check_limits(max_concurrency: int, max_retries: int) -> None:
    """Raises ValueError for a limit that the runner cannot use. Provider clients call it at construction."""
    if not is_int(max_concurrency) or max_concurrency < 1:
        raise ValueError("max_concurrency must be an integer of at least 1.")
    if not is_int(max_retries) or max_retries < 0:
        raise ValueError("max_retries must be an integer of at least 0.")


def parse_pages(
    source: DocumentInput,
    transport: PageTransport,
    *,
    options: Optional[ParseOptions] = None,
    slots: Optional[PageSlots] = None,
    max_retries: int = DEFAULT_MAX_RETRIES,
    stop: Optional[threading.Event] = None,
) -> ProviderParseResponse:
    """Parses a document on a thread pool. It blocks, but it starts no event loop, so it works in a notebook.

    Raises PageParseError when any page fails. Setting `stop` from another thread stops new renders and sends;
    the parse then raises Stopped.
    """
    options = options or ParseOptions()
    slots = slots or PageSlots(DEFAULT_MAX_CONCURRENCY)
    stop = stop or threading.Event()
    started = time.monotonic()
    document = open_document(source, options.document_password)
    try:
        if document.page_count == 0:
            raise ReductoError("The document has no pages.")
        pages = plan_pages(options.page_spans, document.page_count)
        results = _run(document, pages, transport, slots, max_retries, stop)
    finally:
        document.close()
    return build_response(results, duration=time.monotonic() - started)


def _run(
    document: Document,
    pages: List[int],
    transport: PageTransport,
    slots: PageSlots,
    max_retries: int,
    stop: threading.Event,
) -> List[PageResult]:
    """Each worker renders, sends, and reads one page. The first error stops every page and is raised at once."""
    pool = ThreadPoolExecutor(max_workers=slots.size, thread_name_prefix="reducto-page")
    futures = [
        pool.submit(_parse_page, document, index, page, transport, slots, max_retries, stop)
        for index, page in enumerate(pages, start=1)
    ]
    try:
        wait(futures, return_when=FIRST_EXCEPTION)
        error = _first_error(futures)
        if error is not None:
            raise error
    except BaseException:
        stop.set()
        pool.shutdown(wait=False, cancel_futures=True)
        raise
    pool.shutdown()
    return [future.result() for future in futures]


def _first_error(futures: List[Future[PageResult]]) -> Optional[BaseException]:
    """The error that stopped the parse. A page that only saw the stop raised Stopped, so any other error wins."""
    errors = [
        error
        for future in futures
        if future.done() and not future.cancelled() and (error := future.exception()) is not None
    ]
    return next((error for error in errors if not isinstance(error, Stopped)), errors[0] if errors else None)


def _parse_page(
    document: Document,
    index: int,
    page: int,
    transport: PageTransport,
    slots: PageSlots,
    max_retries: int,
    stop: threading.Event,
) -> PageResult:
    slots.acquire(stop)
    try:
        return _parse_held_page(document, index, page, transport, max_retries, stop)
    except Stopped:
        raise
    except BaseException:
        # A fatal error (a rejected request, an endpoint that does not support this SDK) stops the other pages.
        stop.set()
        raise
    finally:
        slots.release()


def _parse_held_page(
    document: Document, index: int, page: int, transport: PageTransport, max_retries: int, stop: threading.Event
) -> PageResult:
    encoded = _prepare(document, index, page, transport.body_limit)
    if isinstance(encoded, FailedPage):
        return encoded
    outcome = _send(transport, encoded.body, stop)
    for retry in range(1, max_retries + 1):
        if not _retryable(outcome):
            break
        if stop.wait(backoff_seconds(retry)):
            raise Stopped
        outcome = _send(transport, encoded.body, stop)
    return _page_result(encoded, outcome)


def _send(transport: PageTransport, body: bytes, stop: threading.Event) -> PageOutcome:
    if stop.is_set():
        raise Stopped
    return classify_outcome(transport.send(body))


def _prepare(document: Document, index: int, page: int, body_limit: int) -> _EncodedPage | FailedPage:
    """Renders and encodes one page. Only the body is kept, so the image is freed before the network wait."""
    try:
        return _EncodedPage(index, page, encode_page(document.render(page), body_limit))
    except PageError as error:
        return FailedPage(page=page, reason="error", detail=str(error))


def _page_result(encoded: _EncodedPage, outcome: PageOutcome) -> PageResult:
    if isinstance(outcome, Failure):
        return FailedPage(page=encoded.page, reason=outcome.reason, status=outcome.status, detail=outcome.detail)
    try:
        blocks = read_answer(outcome.body, index=encoded.index, page=encoded.page)
    except InvalidAnswerError as error:
        return FailedPage(page=encoded.page, reason="error", detail=f"The endpoint answer is not valid: {error}.")
    return ParsedPage(encoded.page, tuple(blocks))


def _retryable(outcome: PageOutcome) -> bool:
    return isinstance(outcome, Failure) and outcome.retryable
