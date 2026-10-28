from __future__ import annotations

import io
import json
import time
import threading
import traceback
from typing import Any, Mapping
from pathlib import Path

import anyio
import pytest
import anyio.to_thread

import reducto
from reducto import (
    PageParseError,
    ReductoSageMaker,
    AsyncReductoSageMaker,
    UnsupportedOnProviderError,
)
from reducto._types import omit, not_given
from reducto.lib.sagemaker import ProviderParseResponse
from reducto.resources.parse import ParseResource
from reducto.lib.sagemaker._transport import RuntimeClient

from ._stubs import ENDPOINT, CREDENTIALS, CANNOT_PROCESS_BODY, Stub, FakeRuntime
from .._page_parse._helpers import make_pdf, blocks_answer, encrypted_pdf

_HTTP_PLUMBING = {
    "auth_headers",
    "base_url",
    "custom_auth",
    "default_headers",
    "default_query",
    "delete",
    "get",
    "get_api_list",
    "is_closed",
    "patch",
    "platform_headers",
    "post",
    "put",
    "qs",
    "request",
    "user_agent",
}


def _public(cls: type) -> set[str]:
    return {name for name in dir(cls) if not name.startswith("_")}


_HOSTED_ONLY = sorted(_public(reducto.Reducto) - _HTTP_PLUMBING - {"parse", "close"})
_HOSTED_ONLY_PARSE = sorted(_public(ParseResource) - {"run"})


def _page(number: int) -> bytes:
    return blocks_answer((("Title", f"Page {number}"),))


def _numbered(call: int) -> Mapping[str, object]:
    """Answers call N with a page titled "Page N+1"."""
    return {"Body": io.BytesIO(_page(call + 1))}


def _client(max_concurrency: int = 1) -> ReductoSageMaker:
    return ReductoSageMaker(
        endpoint_name=ENDPOINT,
        aws_region="us-east-2",
        max_concurrency=max_concurrency,
        **CREDENTIALS,
    )


def _async_client(max_concurrency: int = 1) -> AsyncReductoSageMaker:
    return AsyncReductoSageMaker(
        endpoint_name=ENDPOINT, aws_region="us-east-2", max_concurrency=max_concurrency, **CREDENTIALS
    )


def _pages(response: ProviderParseResponse) -> list[tuple[int | None, str]]:
    return [(chunk.blocks[0].bbox.original_page, chunk.blocks[0].content) for chunk in response.result.chunks]


def test_parse_run_returns_one_chunk_per_page_in_order(fake_runtime: FakeRuntime) -> None:
    """Catches a broken path from the client to the endpoint, or pages assembled out of order."""
    fake_runtime.handler = _numbered
    response = _client().parse.run(input=make_pdf(3))
    assert _pages(response) == [(1, "Page 1"), (2, "Page 2"), (3, "Page 3")]


def test_client_sends_only_the_page_image(fake_runtime: FakeRuntime) -> None:
    """Catches the client adding a field to the page-parse body on the way to SageMaker."""
    fake_runtime.handler = _numbered
    _client().parse.run(input=make_pdf(1))
    assert list(json.loads(fake_runtime.bodies[0])) == ["image_b64"]


def test_unprocessable_page_raises_page_parse_error(runtimes: list[RuntimeClient]) -> None:
    """Catches a wrapped 422 page returned as a short success, retried, or raised before the other pages finish."""
    client = _client()
    stub = Stub(runtimes[0])
    stub.reply(_page(1))
    stub.error("ModelError", 424, "client error", OriginalStatusCode=422, OriginalMessage=CANNOT_PROCESS_BODY)
    with pytest.raises(PageParseError) as raised:
        client.parse.run(input=make_pdf(2))
    assert raised.value.partial_response is not None
    assert _pages(raised.value.partial_response) == [(1, "Page 1")]
    assert [(page.page, page.reason, page.status) for page in raised.value.failed_pages] == [(2, "unprocessable", 422)]
    stub.assert_all_used()


async def test_async_unprocessable_page_raises_page_parse_error(runtimes: list[RuntimeClient]) -> None:
    """Catches an async client that returns a failed page as a short success."""
    async with _async_client() as client:
        stub = Stub(runtimes[0])
        stub.reply(_page(1))
        stub.error("ModelError", 424, "client error", OriginalStatusCode=422, OriginalMessage=CANNOT_PROCESS_BODY)
        with pytest.raises(PageParseError) as raised:
            await client.parse.run(input=make_pdf(2))
    assert raised.value.partial_response is not None
    assert _pages(raised.value.partial_response) == [(1, "Page 1")]
    assert [page.page for page in raised.value.failed_pages] == [2]


def test_page_range_sends_only_those_pages(fake_runtime: FakeRuntime) -> None:
    """Catches `settings.page_range` dropped by the client, which bills every page of the document."""
    fake_runtime.handler = _numbered
    response = _client().parse.run(input=make_pdf(3), settings={"page_range": {"start": 2, "end": 2}})
    assert len(fake_runtime.bodies) == 1
    assert [chunk.blocks[0].bbox.original_page for chunk in response.result.chunks] == [2]


async def test_async_parse_reads_a_path_and_returns_every_page(tmp_path: Path, fake_runtime: FakeRuntime) -> None:
    """Catches an async client that reads a path input wrong, or loses a page."""
    fake_runtime.handler = _numbered
    path = tmp_path / "report.pdf"
    path.write_bytes(make_pdf(2))
    async with _async_client() as client:
        response = await client.parse.run(input=path)
    assert _pages(response) == [(1, "Page 1"), (2, "Page 2")]
    assert fake_runtime.closed


def test_document_password_opens_the_pdf(fake_runtime: FakeRuntime) -> None:
    """Catches `settings.document_password` dropped by the client, so a locked PDF cannot be read."""
    fake_runtime.handler = _numbered
    response = _client().parse.run(input=encrypted_pdf("secret"), settings={"document_password": "secret"})
    assert _pages(response) == [(1, "Page 1")]


def test_bad_page_range_raises_before_the_file_is_read(tmp_path: Path, fake_runtime: FakeRuntime) -> None:
    """Catches a page_range of the wrong shape found only after a large file is read and rendered."""
    with pytest.raises(ValueError, match="Wrap one page in a list"):
        _client().parse.run(input=tmp_path / "missing.pdf", settings={"page_range": 3})  # type: ignore[typeddict-item]
    assert fake_runtime.bodies == []


def test_unsupported_option_raises_before_any_call(fake_runtime: FakeRuntime) -> None:
    """Catches an option the endpoint cannot honor that is ignored, or found only after pages are billed."""
    with pytest.raises(UnsupportedOnProviderError, match="formatting.table_output_format"):
        _client().parse.run(input=make_pdf(1), formatting={"table_output_format": "md"})
    assert fake_runtime.bodies == []


async def test_async_unsupported_option_raises_before_any_call(fake_runtime: FakeRuntime) -> None:
    """Catches an async client that skips the option check, so an ignored option changes the output silently."""
    with pytest.raises(UnsupportedOnProviderError, match="enhance.agentic"):
        await _async_client().parse.run(input=make_pdf(1), enhance={"agentic": [{"scope": "text"}]})
    assert fake_runtime.bodies == []


async def test_cancelled_async_parse_returns_at_once_and_sends_no_more_pages(fake_runtime: FakeRuntime) -> None:
    """Catches a cancel that waits for the endpoint call to finish, or that keeps sending the other pages."""
    entered = threading.Event()
    release = threading.Event()

    def handler(call: int) -> Mapping[str, object]:
        entered.set()
        release.wait(5)
        return _numbered(call)

    fake_runtime.handler = handler
    cancelled_after = 0.0
    cancelled_at = time.monotonic()
    try:
        async with anyio.create_task_group() as tasks:
            tasks.start_soon(_parse_five_pages)
            assert await anyio.to_thread.run_sync(entered.wait, 5)
            cancelled_at = time.monotonic()
            tasks.cancel_scope.cancel()
        cancelled_after = time.monotonic() - cancelled_at
    finally:
        release.set()
    deadline = time.monotonic() + 5
    while any(thread.name.startswith("reducto-page") for thread in threading.enumerate()):
        assert time.monotonic() < deadline
        time.sleep(0.01)
    assert cancelled_after < 1
    assert len(fake_runtime.bodies) == 1


async def _parse_five_pages() -> None:
    await _async_client().parse.run(input=make_pdf(5))


async def test_async_parse_takes_no_token_of_the_shared_thread_limiter(fake_runtime: FakeRuntime) -> None:
    """Catches a parse that waits for anyio's shared thread limiter, which the app may have used up."""
    fake_runtime.handler = _numbered
    shared = anyio.to_thread.current_default_thread_limiter()
    tokens = shared.total_tokens
    shared.total_tokens = 1
    held = threading.Event()
    chunks: list[int] = []
    try:
        async with anyio.create_task_group() as tasks:
            tasks.start_soon(anyio.to_thread.run_sync, held.wait)
            await anyio.sleep(0.05)
            with anyio.fail_after(5):
                response = await _async_client().parse.run(input=make_pdf(2))
            chunks.append(len(response.result.chunks))
            held.set()
    finally:
        held.set()
        shared.total_tokens = tokens
    assert chunks == [2]


def test_concurrent_parses_share_the_client_page_limit(fake_runtime: FakeRuntime) -> None:
    """Catches a page limit per call instead of per client, which lets threads that share a client
    throttle the endpoint."""

    def handler(call: int) -> Mapping[str, object]:
        time.sleep(0.02)
        return _numbered(call)

    fake_runtime.handler = handler
    client = _client(max_concurrency=2)
    errors: list[BaseException] = []

    def parse() -> None:
        try:
            client.parse.run(input=make_pdf(6))
        except BaseException as error:  # noqa: BLE001
            errors.append(error)

    threads = [threading.Thread(target=parse) for _ in range(3)]
    for thread in threads:
        thread.start()
    for thread in threads:
        thread.join(timeout=30)
    assert errors == []
    assert len(fake_runtime.bodies) == 18
    assert fake_runtime.peak == 2


_HOSTED_REQUEST_OPTIONS: list[tuple[str, object]] = [
    ("async_", {"enabled": True}),
    ("queue_priority", "batch"),
    ("extra_headers", {"X-Test": "1"}),
    ("extra_query", {"q": "1"}),
    ("extra_body", {"b": 1}),
    ("timeout", 5.0),
]


@pytest.mark.parametrize(("name", "value"), _HOSTED_REQUEST_OPTIONS, ids=[name for name, _ in _HOSTED_REQUEST_OPTIONS])
async def test_hosted_request_options_raise_before_any_call(
    fake_runtime: FakeRuntime, name: str, value: object
) -> None:
    """Catches a hosted `parse.run` option that the client accepts and silently ignores."""
    options: dict[str, Any] = {name: value}
    with pytest.raises(UnsupportedOnProviderError, match=f"The `{name}` option cannot be used"):
        _client().parse.run(input=make_pdf(1), **options)
    with pytest.raises(UnsupportedOnProviderError, match=f"The `{name}` option cannot be used"):
        await _async_client().parse.run(input=make_pdf(1), **options)
    assert fake_runtime.bodies == []


def test_hosted_request_options_at_their_defaults_are_accepted(fake_runtime: FakeRuntime) -> None:
    """Catches code that passes the hosted defaults explicitly and gets an error."""
    fake_runtime.handler = _numbered
    response = _client().parse.run(
        input=make_pdf(1),
        async_=omit,
        queue_priority=omit,
        extra_headers=None,
        extra_query=None,
        extra_body=None,
        timeout=not_given,
    )
    assert len(response.result.chunks) == 1


def test_hosted_only_error_shows_the_public_class_in_tracebacks() -> None:
    """Catches a traceback that names a private class, which callers cannot import or look up."""
    with pytest.raises(UnsupportedOnProviderError) as raised:
        getattr(_client(), "extract")  # noqa: B009
    assert traceback.format_exception_only(type(raised.value), raised.value)[0].startswith(
        "reducto.UnsupportedOnProviderError: `client.extract` cannot be used"
    )


@pytest.mark.parametrize("name", _HOSTED_ONLY)
def test_hosted_only_names_raise(name: str) -> None:
    """Catches a hosted resource, new or old, that fails with a bare AttributeError and no pointer to the hosted API."""
    with pytest.raises(UnsupportedOnProviderError, match=f"`client.{name}` cannot be used .* hosted Reducto API"):
        getattr(_client(), name)
    with pytest.raises(UnsupportedOnProviderError):
        getattr(_async_client(), name)


@pytest.mark.parametrize("name", _HOSTED_ONLY_PARSE)
def test_hosted_only_parse_names_raise(name: str) -> None:
    """Catches `parse.run_job` or a raw-response wrapper that fails with a bare AttributeError."""
    with pytest.raises(UnsupportedOnProviderError, match=f"`client.parse.{name}` cannot be used"):
        getattr(_client().parse, name)
    with pytest.raises(UnsupportedOnProviderError):
        getattr(_async_client().parse, name)


def test_hasattr_is_false_for_every_missing_name() -> None:
    """Catches a `__getattr__` error that is not an AttributeError, which makes `hasattr` and `copy` raise."""
    client = _client()
    assert not hasattr(client, "copy")
    assert not hasattr(client, "not_a_resource")
    assert not hasattr(client.parse, "run_job")


@pytest.mark.parametrize(
    ("options", "named"),
    [
        ({"max_concurrency": 0}, "max_concurrency"),
        ({"max_concurrency": 2.5}, "max_concurrency"),
        ({"max_retries": -1}, "max_retries"),
        ({"timeout": 0}, "timeout"),
    ],
)
def test_invalid_limits_raise_at_construction(options: dict[str, object], named: str) -> None:
    """Catches a bad limit found only on the first parse, or passed to botocore as a pool of no connections."""
    with pytest.raises(ValueError, match=named):
        ReductoSageMaker(endpoint_name=ENDPOINT, aws_region="us-east-2", **CREDENTIALS, **options)  # type: ignore[arg-type]
