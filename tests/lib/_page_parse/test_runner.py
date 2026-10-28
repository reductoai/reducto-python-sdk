from __future__ import annotations

import json
import time
import threading
from typing import Any

import pytest
from PIL import Image

from reducto import ReductoError, PageParseError
from reducto._constants import MAX_RETRY_DELAY
from reducto.lib.sagemaker import ProviderParseResponse
from reducto.lib._page_parse.errors import PageError
from reducto.lib._page_parse.runner import Stopped, PageSlots, parse_pages, check_limits
from reducto.lib._page_parse.options import ParseOptions
from reducto.lib._page_parse.response import VERSION_ERROR
from reducto.lib._page_parse.documents import PdfPages
from reducto.lib._page_parse.transport import (
    EndpointReply,
    PageTransport,
    EndpointOutcome,
    EndpointUnreachable,
    backoff_seconds,
)

from ._helpers import CANNOT_PROCESS, FakeTransport, reply, always, replay, titled, make_pdf, error_reply


def _long_delay(_retry: int) -> float:
    return 30.0


def _options(page_range: object) -> ParseOptions:
    return ParseOptions.from_run_kwargs({"settings": {"page_range": page_range}})


def _titles(response: ProviderParseResponse) -> list[str]:
    return [chunk.content for chunk in response.result.chunks]


def _page_error(
    source: bytes, transport: PageTransport, *, max_concurrency: int = 4, max_retries: int = 2
) -> PageParseError:
    with pytest.raises(PageParseError) as raised:
        parse_pages(source, transport, slots=PageSlots(max_concurrency), max_retries=max_retries)
    return raised.value


def _failures(error: PageParseError) -> list[tuple[int, str, int | None]]:
    return [(failed.page, failed.reason, failed.status) for failed in error.failed_pages]


def _partial(error: PageParseError) -> ProviderParseResponse:
    assert error.partial_response is not None
    return error.partial_response


def _assert_fatal_first_call_stops_the_sends(fatal: EndpointOutcome) -> None:
    """Parses 20 pages, 2 at a time. The first call answers `fatal`; every other call waits until the parse
    has raised. Re-raises the parse error after it checks that no page was sent after the error."""
    raised = threading.Event()

    def outcomes(call: int) -> EndpointOutcome:
        if call == 0:
            return fatal
        assert raised.wait(timeout=5)
        return reply()

    transport = FakeTransport(outcomes)
    try:
        parse_pages(make_pdf(20), transport, slots=PageSlots(2))
    except ReductoError:
        sent = len(transport.bodies)
        raised.set()
        _wait_for_page_workers()
        assert sent <= 2
        assert len(transport.bodies) == sent
        raise
    finally:
        raised.set()


def _wait_for_page_workers() -> None:
    deadline = time.monotonic() + 5
    while any(thread.name.startswith("reducto-page") for thread in threading.enumerate()):
        assert time.monotonic() < deadline, "a page worker is still running"
        time.sleep(0.01)


def _unreadable_pages(monkeypatch: pytest.MonkeyPatch, unreadable: set[int]) -> None:
    original_render = PdfPages.render

    def render(self: PdfPages, page: int) -> Image.Image:
        if page in unreadable:
            raise PageError(f"Page {page} of the PDF cannot be rendered")
        return original_render(self, page)

    monkeypatch.setattr(PdfPages, "render", render)


def _count_renders(monkeypatch: pytest.MonkeyPatch) -> list[int]:
    """Records each page as its render starts."""
    renders: list[int] = []
    original_render = PdfPages.render

    def render(self: PdfPages, page: int) -> Image.Image:
        renders.append(page)
        return original_render(self, page)

    monkeypatch.setattr(PdfPages, "render", render)
    return renders


def test_each_page_gets_one_page_parse_body() -> None:
    """Catches a page sent twice, or a body with any field other than the page image."""
    transport = always(reply())
    parse_pages(make_pdf(3), transport)
    assert len(transport.bodies) == 3
    for body in transport.bodies:
        assert list(json.loads(body)) == ["image_b64"]


@pytest.mark.parametrize("status", [429, 500, 502, 503])
def test_transient_status_is_retried(status: int) -> None:
    """Catches a throttled or briefly failing endpoint that loses the page."""
    transport = FakeTransport(replay([error_reply(status), reply()]))
    response = parse_pages(make_pdf(1), transport)
    assert len(transport.bodies) == 2
    assert len(response.result.chunks) == 1


def test_broken_connection_is_retried_up_to_max_retries() -> None:
    """Catches a retry loop that gives up early or never stops."""
    transport = always(EndpointUnreachable("connection", "connection refused"))
    error = _page_error(make_pdf(1), transport, max_retries=2)
    assert len(transport.bodies) == 3
    assert _failures(error) == [(1, "error", None)]


@pytest.mark.parametrize(
    ("outcome", "reason", "status"),
    [
        (error_reply(504, "timed out"), "error", 504),
        (CANNOT_PROCESS, "unprocessable", 422),
        (error_reply(415, "unsupported image"), "error", 415),
        (EndpointUnreachable("timeout", "read timed out"), "error", None),
    ],
    ids=["504", "422-cannot-process", "415", "client-timeout"],
)
def test_final_failures_are_not_retried(outcome: EndpointOutcome, reason: str, status: int | None) -> None:
    """Catches a retry of a final failure (504, 422, 415, or a client timeout), which the client must not retry."""
    transport = FakeTransport(lambda call: reply() if call else outcome)
    error = _page_error(make_pdf(2), transport, max_concurrency=1)
    assert len(transport.bodies) == 2
    assert _failures(error) == [(1, reason, status)]


@pytest.mark.parametrize("outcome", [error_reply(422, "request is not valid"), error_reply(400, "bad request")])
def test_rejected_request_stops_the_document(outcome: EndpointReply) -> None:
    """Catches a request that the endpoint rejects for every page, returned as a document of failed pages,
    or a fatal error that lets the other pages keep sending."""
    with pytest.raises(ReductoError, match="The endpoint rejected the request"):
        _assert_fatal_first_call_stops_the_sends(outcome)


def test_stop_interrupts_a_retry_backoff(monkeypatch: pytest.MonkeyPatch) -> None:
    """Catches a worker that sleeps through its backoff after the parse stopped, which holds its thread."""
    monkeypatch.setattr("reducto.lib._page_parse.runner.backoff_seconds", _long_delay)
    first_call_done = threading.Event()

    def outcomes(call: int) -> EndpointOutcome:
        if call == 0:
            first_call_done.set()
            return error_reply(503)
        assert first_call_done.wait(timeout=5)
        raise PermissionError("no credentials")

    with pytest.raises(PermissionError):
        parse_pages(make_pdf(2), FakeTransport(outcomes), slots=PageSlots(2))
    _wait_for_page_workers()


def test_unprocessable_page_names_the_status_and_detail() -> None:
    """Catches a failed page with no hint of why it failed."""
    error = _page_error(make_pdf(1), always(CANNOT_PROCESS))
    assert error.failed_pages[0].detail == "status 422: input could not be processed"


def test_one_unprocessable_page_in_ten_raises_with_the_other_nine() -> None:
    """Catches a 422 page returned as a short document with no error, or a failure that loses the other pages."""
    transport = FakeTransport(lambda call: CANNOT_PROCESS if call == 6 else titled(call + 1))
    error = _page_error(make_pdf(10), transport, max_concurrency=1)
    assert len(transport.bodies) == 10
    assert str(error) == '1 of 10 pages failed: page 7 (unprocessable). Retry them with settings={"page_range": [7]}.'
    assert _failures(error) == [(7, "unprocessable", 422)]
    partial = _partial(error)
    assert _titles(partial) == [f"Page {page}" for page in range(1, 11) if page != 7]
    assert partial.usage.num_pages == 9


def test_failed_page_numbers_retry_exactly_those_pages() -> None:
    """Catches failed page numbers given as positions in the plan, so a retry with them parses the wrong pages."""
    transport = FakeTransport(lambda call: CANNOT_PROCESS if call in (1, 3) else reply())
    with pytest.raises(PageParseError) as raised:
        parse_pages(make_pdf(10), transport, options=_options([2, 4, 6, 8]), slots=PageSlots(1))
    pages = [failed.page for failed in raised.value.failed_pages]
    assert pages == [4, 8]
    assert str(raised.value).endswith('Retry them with settings={"page_range": [4, 8]}.')
    retry = always(reply())
    response = parse_pages(make_pdf(10), retry, options=_options(pages))
    assert len(retry.bodies) == 2
    assert [chunk.blocks[0].bbox.original_page for chunk in response.result.chunks] == [4, 8]


def test_success_returns_every_page() -> None:
    """Catches a success response that drops or reorders a page."""
    response = parse_pages(make_pdf(3), FakeTransport(lambda call: titled(call + 1)), slots=PageSlots(1))
    assert _titles(response) == ["Page 1", "Page 2", "Page 3"]
    assert response.usage.num_pages == 3


def test_invalid_answer_fails_only_that_page() -> None:
    """Catches a garbled answer that fails the document, or that comes back as a real page."""
    garbled = EndpointReply(200, b'{"blocks": [{"type": "Text"}]}')
    transport = FakeTransport(lambda call: garbled if call == 0 else reply())
    error = _page_error(make_pdf(2), transport, max_concurrency=1)
    assert len(_partial(error).result.chunks) == 1
    assert [(failed.page, failed.reason) for failed in error.failed_pages] == [(1, "error")]
    assert "no string content" in (error.failed_pages[0].detail or "")


def test_answer_without_blocks_stops_the_document_with_the_version_error() -> None:
    """Catches an endpoint whose answer has no blocks read as a page, reported once per page, or left sending."""
    with pytest.raises(ReductoError) as raised:
        _assert_fatal_first_call_stops_the_sends(EndpointReply(200, b'{"other": "anything"}'))
    assert str(raised.value) == VERSION_ERROR


def test_every_page_failing_raises_with_no_partial_response() -> None:
    """Catches a document where every page fails returned as an empty success, or with the reasons lost."""
    error = _page_error(make_pdf(3), always(error_reply(500)))
    assert error.partial_response is None
    assert [failed.page for failed in error.failed_pages] == [1, 2, 3]
    assert str(error) == (
        "3 of 3 pages failed: page 1 (error), page 2 (error), page 3 (error). "
        'Retry them with settings={"page_range": [1, 2, 3]}.'
    )


def test_pages_finishing_out_of_order_keep_page_order() -> None:
    """Catches results assembled in completion order when later pages answer first."""
    first_page_waits = threading.Event()

    def outcomes(call: int) -> EndpointOutcome:
        if call == 0:
            assert first_page_waits.wait(timeout=5)
        elif call == 3:
            first_page_waits.set()
        return titled(call + 1)

    response = parse_pages(make_pdf(4), FakeTransport(outcomes), slots=PageSlots(4))
    assert [chunk.blocks[0].bbox.original_page for chunk in response.result.chunks] == [1, 2, 3, 4]


def test_concurrency_reaches_but_never_exceeds_the_limit(monkeypatch: pytest.MonkeyPatch) -> None:
    """Catches a burst of calls that throttles the endpoint, or more pages rendered than the limit."""
    renders = _count_renders(monkeypatch)
    renders_at_full: list[int] = []
    barrier = threading.Barrier(3, action=lambda: renders_at_full.append(len(renders)), timeout=5)
    transport = FakeTransport(lambda _call: reply(), barrier=barrier)
    response = parse_pages(make_pdf(12), transport, slots=PageSlots(3))
    assert len(response.result.chunks) == 12
    assert transport.peak == 3
    assert renders_at_full[0] == 3


def test_transport_exception_propagates() -> None:
    """Catches a credentials error swallowed into a response where every page failed."""

    def outcomes(_call: int) -> EndpointOutcome:
        raise PermissionError("no credentials")

    with pytest.raises(PermissionError):
        parse_pages(make_pdf(3), FakeTransport(outcomes))


def test_sync_error_stops_the_other_pages_at_once() -> None:
    """Catches an error raised only after every page is sent, which keeps billing the endpoint."""
    release = threading.Event()

    def outcomes(call: int) -> EndpointOutcome:
        if call == 2:
            raise PermissionError("no credentials")
        if call != 1:
            assert release.wait(timeout=5)
        return reply()

    transport = FakeTransport(outcomes)
    try:
        with pytest.raises(PermissionError):
            parse_pages(make_pdf(40), transport, slots=PageSlots(4))
        assert not release.is_set()
        sent = len(transport.bodies)
    finally:
        release.set()
    _wait_for_page_workers()
    assert len(transport.bodies) == sent < 12


def test_page_range_limits_the_calls() -> None:
    """Catches settings.page_range ignored, which bills the buyer for every page."""
    transport = always(reply())
    response = parse_pages(make_pdf(5), transport, options=_options([2, 4]))
    assert len(transport.bodies) == 2
    assert [chunk.blocks[0].bbox.original_page for chunk in response.result.chunks] == [2, 4]
    assert [chunk.blocks[0].bbox.page for chunk in response.result.chunks] == [1, 2]
    assert response.usage.num_pages == 2


def test_unreadable_page_fails_only_that_page(monkeypatch: pytest.MonkeyPatch) -> None:
    """Catches one corrupt page that aborts the whole document."""
    _unreadable_pages(monkeypatch, {2})
    transport = always(reply())
    error = _page_error(make_pdf(3), transport)
    assert len(transport.bodies) == 2
    assert [(failed.page, failed.reason) for failed in error.failed_pages] == [(2, "error")]


@pytest.mark.parametrize(("max_concurrency", "max_retries"), [(0, 2), (1, -1), (2.5, 2), (True, 2), (1, 1.5)])
def test_invalid_limits_raise(max_concurrency: int, max_retries: int) -> None:
    """Catches max_concurrency=0, which would leave no slot for any page and hang the parse."""
    with pytest.raises(ValueError):
        check_limits(max_concurrency, max_retries)


async def test_sync_runner_works_inside_a_running_event_loop() -> None:
    """Catches asyncio.run in the sync path, which fails in a Jupyter notebook."""
    response = parse_pages(make_pdf(2), always(reply()))
    assert len(response.result.chunks) == 2


def test_encode_error_fails_only_that_page(monkeypatch: pytest.MonkeyPatch) -> None:
    """Catches a Pillow save error, such as a JPEG side over 65,500 px, that stops the whole document."""
    original_save = Image.Image.save
    saves = 0

    def save(self: Image.Image, *args: Any, **kwargs: Any) -> None:
        nonlocal saves
        saves += 1
        if saves == 1:
            raise OSError("encoder error")
        original_save(self, *args, **kwargs)

    monkeypatch.setattr(Image.Image, "save", save)
    transport = always(reply())
    error = _page_error(make_pdf(2), transport, max_concurrency=1)
    assert len(transport.bodies) == 1
    assert [(failed.page, failed.reason) for failed in error.failed_pages] == [(1, "error")]
    assert "cannot be encoded" in (error.failed_pages[0].detail or "")


def test_backoff_is_capped_for_any_retry_count() -> None:
    """Catches a large max_retries that sleeps for hours or overflows the exponent."""
    assert all(0 < backoff_seconds(retry) <= MAX_RETRY_DELAY for retry in (1, 5, 10_000))


def test_stop_from_another_thread_stops_new_sends_and_closes_the_document(monkeypatch: pytest.MonkeyPatch) -> None:
    """Catches a cancelled parse that keeps sending pages, or that leaves pdfium memory open."""
    closed: list[bool] = []
    original_close = PdfPages.close

    def close(self: PdfPages) -> None:
        closed.append(True)
        original_close(self)

    monkeypatch.setattr(PdfPages, "close", close)
    release = threading.Event()
    stop = threading.Event()

    def outcomes(_call: int) -> EndpointOutcome:
        assert release.wait(timeout=5)
        return reply()

    transport = FakeTransport(outcomes)
    errors: list[BaseException] = []

    def parse() -> None:
        try:
            parse_pages(make_pdf(5), transport, slots=PageSlots(1), stop=stop)
        except BaseException as error:  # noqa: BLE001
            errors.append(error)

    thread = threading.Thread(target=parse)
    thread.start()
    deadline = time.monotonic() + 5
    while not transport.bodies:
        assert time.monotonic() < deadline
        time.sleep(0.01)
    stop.set()
    release.set()
    thread.join(timeout=5)
    _wait_for_page_workers()
    assert len(transport.bodies) == 1
    assert [type(error) for error in errors] == [Stopped]
    assert closed == [True]
