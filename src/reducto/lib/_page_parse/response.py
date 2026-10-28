from __future__ import annotations

import json
import uuid
from typing import List, Tuple, Union, Mapping, Sequence, cast
from dataclasses import dataclass
from typing_extensions import TypeAlias

from .types import FailedPage, ProviderParseResponse
from .errors import PageParseError
from ..._utils import is_list, is_mapping
from ..._exceptions import ReductoError
from ...types.parse_usage import ParseUsage
from ...types.bounding_box import BoundingBox
from ...types.shared.parse_response import ResultFullResult, ResultFullResultChunk, ResultFullResultChunkBlock

__all__ = ["VERSION_ERROR", "InvalidAnswerError", "PageResult", "ParsedPage", "build_response", "read_answer"]

VERSION_ERROR = (
    "This endpoint does not return the answer this SDK reads. Update the endpoint to a version that supports this SDK."
)

_BOX_FIELDS = ("left", "top", "width", "height")
_EDGE_TOLERANCE = 1e-9
"""Float slack for a box that ends on the far edge of the page."""

_NAMED_FAILURES = 10
"""The error message names at most this many failed pages. `failed_pages` holds all of them."""


class InvalidAnswerError(Exception):
    """A 2xx answer that does not follow the blocks contract. Only that page fails."""


@dataclass(frozen=True)
class ParsedPage:
    page: int
    """The page number in the original document (1-indexed)."""

    blocks: Tuple[ResultFullResultChunkBlock, ...]


PageResult: TypeAlias = Union[ParsedPage, FailedPage]


def read_answer(body: bytes, *, index: int, page: int) -> List[ResultFullResultChunkBlock]:
    """The blocks of one page answer, in reading order. `index` is the position of the page in the page plan
    and `page` its number in the document, both 1-indexed. A block `type` that this SDK version does not
    list passes through, as in the hosted client.

    Raises ReductoError when the answer has no `blocks` key: the endpoint does not support this SDK, so the
    client stops the document. Raises InvalidAnswerError for any other contract break.
    """
    try:
        answer = cast(object, json.loads(body))
    except ValueError as error:
        raise InvalidAnswerError("the answer is not JSON") from error
    if not is_mapping(answer):
        raise InvalidAnswerError("the answer is not a JSON object")
    if "blocks" not in answer:
        raise ReductoError(VERSION_ERROR)
    blocks = answer["blocks"]
    if not is_list(blocks):
        raise InvalidAnswerError("`blocks` is not a list")
    return [_block(block, f"block {position}", index, page) for position, block in enumerate(blocks)]


def build_response(results: Sequence[PageResult], *, duration: float) -> ProviderParseResponse:
    """One chunk per page, in page order. Raises PageParseError when any page failed."""
    ordered = sorted(results, key=lambda result: result.page)
    parsed = [result for result in ordered if isinstance(result, ParsedPage)]
    failed = [result for result in ordered if isinstance(result, FailedPage)]
    if not failed:
        return _response(parsed, duration)
    partial = _response(parsed, duration) if parsed else None
    raise PageParseError(_failure_message(failed, len(ordered)), failed, partial)


def _block(block: object, where: str, index: int, page: int) -> ResultFullResultChunkBlock:
    if not is_mapping(block):
        raise InvalidAnswerError(f"{where} is not an object")
    block_type = block.get("type")
    if not isinstance(block_type, str) or not block_type:
        raise InvalidAnswerError(f"{where} has no type")
    content = block.get("content")
    if not isinstance(content, str):
        raise InvalidAnswerError(f"{where} has no string content")
    left, top, width, height = _box(block.get("bbox"), where)
    bbox = BoundingBox.construct(left=left, top=top, width=width, height=height, page=index, original_page=page)
    return ResultFullResultChunkBlock.construct(type=block_type, content=content, bbox=bbox)


def _box(bbox: object, where: str) -> tuple[float, float, float, float]:
    if not is_mapping(bbox):
        raise InvalidAnswerError(f"{where} has no bbox object")
    left, top, width, height = (_unit(bbox, name, where) for name in _BOX_FIELDS)
    if left + width > 1.0 + _EDGE_TOLERANCE or top + height > 1.0 + _EDGE_TOLERANCE:
        raise InvalidAnswerError(f"{where} has a bbox that ends off the page")
    return left, top, width, height


def _unit(bbox: Mapping[str, object], name: str, where: str) -> float:
    value = bbox.get(name)
    if isinstance(value, bool) or not isinstance(value, (int, float)) or not 0.0 <= value <= 1.0:
        raise InvalidAnswerError(f"{where} has a bbox {name} that is not a number from 0 to 1")
    return float(value)


def _response(pages: Sequence[ParsedPage], duration: float) -> ProviderParseResponse:
    return ProviderParseResponse.construct(
        duration=duration,
        job_id=f"local-{uuid.uuid4()}",
        result=ResultFullResult.construct(type="full", chunks=[_chunk(page) for page in pages]),
        usage=ParseUsage.construct(num_pages=len(pages)),
        response_type="parse",
    )


def _chunk(page: ParsedPage) -> ResultFullResultChunk:
    text = "\n\n".join(block.content for block in page.blocks)
    return ResultFullResultChunk.construct(blocks=list(page.blocks), content=text, embed=text)


def _failure_message(failed: Sequence[FailedPage], page_count: int) -> str:
    """Names the first failed pages and ends with the page_range that retries them. The page numbers are
    the 1-based document page (or image frame) numbers that page_range takes."""
    named = ", ".join(f"page {page.page} ({page.reason})" for page in failed[:_NAMED_FAILURES])
    more = len(failed) - _NAMED_FAILURES
    if more > 0:
        named += f", and {more} more (see error.failed_pages)"
    if len(failed) <= _NAMED_FAILURES:
        retry = f"settings={json.dumps({'page_range': [page.page for page in failed]})}"
    else:
        retry = 'settings={"page_range": [p.page for p in error.failed_pages]}'
    noun = "page" if page_count == 1 else "pages"
    return f"{len(failed)} of {page_count} {noun} failed: {named}. Retry them with {retry}."
