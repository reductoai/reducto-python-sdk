from __future__ import annotations

import json

import pytest

from reducto import ReductoError, PageParseError
from reducto.lib.sagemaker import FailedPage
from reducto.lib._page_parse.response import (
    VERSION_ERROR,
    ParsedPage,
    InvalidAnswerError,
    read_answer,
    build_response,
)
from reducto.types.shared.parse_response import ResultFullResultChunkBlock

from ._helpers import blocks_answer


def _block(**fields: object) -> bytes:
    block: dict[str, object] = {
        "type": "Text",
        "bbox": {"left": 0.1, "top": 0.1, "width": 0.5, "height": 0.2},
        "content": "Hello",
    }
    block.update(fields)
    return json.dumps({"blocks": [block]}).encode()


def _read(body: bytes) -> list[ResultFullResultChunkBlock]:
    return read_answer(body, index=1, page=1)


def _parsed(page: int, *contents: str) -> ParsedPage:
    blocks = _read(blocks_answer(tuple(("Text", content) for content in contents)))
    return ParsedPage(page, tuple(blocks))


def test_answer_blocks_keep_type_box_content_and_order() -> None:
    """Catches blocks reordered, or a box, content, or page number lost on the way to the response."""
    blocks = read_answer(
        blocks_answer((("Title", "Q3"), ("Table", "<table><tr><td>1</td></tr></table>"))), index=2, page=7
    )
    assert [(block.type, block.content) for block in blocks] == [
        ("Title", "Q3"),
        ("Table", "<table><tr><td>1</td></tr></table>"),
    ]
    box = blocks[1].bbox
    assert (box.left, box.top, box.width, box.height, box.page, box.original_page) == (0.1, 0.5, 0.8, 0.25, 2, 7)


def test_new_block_type_passes_through() -> None:
    """Catches a block type added to the endpoint after this SDK version, which would fail every page with it."""
    blocks = _read(_block(type="FutureType"))
    assert [(block.type, block.content) for block in blocks] == [("FutureType", "Hello")]


def test_usage_is_optional() -> None:
    """Catches an answer rejected because it has, or lacks, usage."""
    assert len(_read(blocks_answer(usage={}))) == 2
    assert len(_read(blocks_answer())) == 2


@pytest.mark.parametrize(
    "body",
    [b'{"other": "anything"}', b'{"usage": {}}', b"{}"],
    ids=["no-blocks", "usage-only", "empty-object"],
)
def test_answer_without_blocks_raises_the_version_error(body: bytes) -> None:
    """Catches an answer without a `blocks` key read as a page."""
    with pytest.raises(ReductoError) as raised:
        _read(body)
    assert str(raised.value) == VERSION_ERROR


@pytest.mark.parametrize(
    "body",
    [
        b"<html>gateway</html>",
        b"[]",
        b'{"blocks": {}}',
        b'{"blocks": ["Text"]}',
        _block(type=None),
        _block(type=""),
        _block(content=None),
        _block(bbox=None),
        _block(bbox={"left": 0.1, "top": 0.1, "width": 0.5}),
        _block(bbox={"left": -0.1, "top": 0.1, "width": 0.5, "height": 0.2}),
        _block(bbox={"left": 0.1, "top": 0.1, "width": 1.5, "height": 0.2}),
        _block(bbox={"left": 0.1, "top": 0.1, "width": True, "height": 0.2}),
        _block(bbox={"left": 0.6, "top": 0.1, "width": 0.5, "height": 0.2}),
        _block(bbox={"left": 0.1, "top": 0.9, "width": 0.5, "height": 0.2}),
    ],
    ids=[
        "not-json",
        "not-object",
        "blocks-not-list",
        "block-not-object",
        "no-type",
        "empty-type",
        "no-content",
        "no-bbox",
        "missing-height",
        "negative-left",
        "width-over-1",
        "bool-width",
        "right-edge-off-page",
        "bottom-edge-off-page",
    ],
)
def test_answer_off_the_contract_is_invalid(body: bytes) -> None:
    """Catches a block with no type or content, or a box off the page, passed on to the caller."""
    with pytest.raises(InvalidAnswerError):
        _read(body)


def test_box_on_the_far_edge_is_accepted() -> None:
    """Catches float rounding on a box that ends on the page edge, read as a box off the page."""
    blocks = _read(_block(bbox={"left": 0.7, "top": 0.0, "width": 0.3000000001, "height": 1.0}))
    assert blocks[0].bbox.left + blocks[0].bbox.width > 1.0


def test_blank_page_gives_an_empty_chunk() -> None:
    """Catches a blank page dropped from the chunks, which shifts every later page."""
    assert _read(b'{"blocks": []}') == []
    response = build_response([ParsedPage(1, ())], duration=0.0)
    assert [(chunk.content, chunk.blocks) for chunk in response.result.chunks] == [("", [])]


def test_response_has_one_chunk_per_page_in_page_order() -> None:
    """Catches pages out of order, or chunk text that does not join the blocks."""
    response = build_response([_parsed(7, "End."), _parsed(2, "Q3", "Up.")], duration=1.5)
    assert [chunk.content for chunk in response.result.chunks] == ["Q3\n\nUp.", "End."]
    assert [chunk.embed for chunk in response.result.chunks] == ["Q3\n\nUp.", "End."]
    assert response.usage.num_pages == 2
    assert response.duration == 1.5
    assert response.job_id.startswith("local-")


def test_a_failed_page_raises_with_the_other_pages_in_order() -> None:
    """Catches a failed page dropped without an error, or a partial response that loses or reorders pages."""
    failed = FailedPage(page=4, reason="unprocessable", status=422)
    with pytest.raises(PageParseError) as raised:
        build_response([_parsed(9, "C."), failed, _parsed(2, "A.")], duration=0.0)
    assert raised.value.failed_pages == [failed]
    assert raised.value.partial_response is not None
    assert [chunk.content for chunk in raised.value.partial_response.result.chunks] == ["A.", "C."]
    assert str(raised.value) == (
        '1 of 3 pages failed: page 4 (unprocessable). Retry them with settings={"page_range": [4]}.'
    )


def test_message_names_at_most_ten_failed_pages() -> None:
    """Catches an error message that lists hundreds of pages, or a retry hint that drops some of them."""
    failed = [FailedPage(page=page, reason="error") for page in range(1, 16)]
    with pytest.raises(PageParseError) as raised:
        build_response(failed, duration=0.0)
    message = str(raised.value)
    assert message.startswith("15 of 15 pages failed: page 1 (error), ")
    assert "page 10 (error), and 5 more (see error.failed_pages)." in message
    assert "page 11" not in message
    assert message.endswith('Retry them with settings={"page_range": [p.page for p in error.failed_pages]}.')
    assert len(raised.value.failed_pages) == 15
