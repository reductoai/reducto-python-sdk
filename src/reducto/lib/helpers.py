import json
from typing import Any, Dict, Iterator, Optional

import httpx
from pydantic import BaseModel

from reducto.types import ParseResponse
from reducto.types.shared.parse_response import ParseUsage, ResultFullResult, ResultFullResultChunk

__all__ = ["FullParseResponse", "handle_url_response", "stream_url_response", "ParseResponse"]


class FullParseResponse(BaseModel):
    duration: float
    """The duration of the parse request in seconds."""

    job_id: str

    result: ResultFullResult
    """The full response from the document processing service."""

    usage: ParseUsage

    pdf_url: Optional[str] = None
    """The storage URL of the converted PDF file."""


def handle_url_response(response: ParseResponse) -> FullParseResponse:
    if response.result.type == "url":
        with httpx.stream("GET", response.result.url) as r:
            content = r.read().decode()
            result = ResultFullResult.model_validate_json(content)
            return FullParseResponse(
                duration=response.duration,
                job_id=response.job_id,
                result=result,
                usage=response.usage,
            )
    else:
        return FullParseResponse.model_validate(response.model_dump())


def _iter_json_array_objects(byte_iter: Iterator[bytes], key: str) -> Iterator[Dict[str, Any]]:
    """Incrementally extract objects from a JSON array field without loading the full response.

    Streams bytes from ``byte_iter``, locates the array stored under ``key`` in the
    top-level JSON object, and yields each element (expected to be a JSON object)
    one at a time.  Only the current element and a small read-ahead buffer are held
    in memory at any point.

    Args:
        byte_iter: An iterator of raw bytes (e.g. ``httpx.Response.iter_bytes()``).
        key: The JSON key whose value is the target array (e.g. ``"chunks"``).

    Yields:
        Parsed ``dict`` objects, one per array element.
    """
    buf = ""
    exhausted = False
    iter_ref = iter(byte_iter)

    def _fill() -> bool:
        nonlocal buf, exhausted
        if exhausted:
            return False
        try:
            raw = next(iter_ref)
        except StopIteration:
            exhausted = True
            return False
        buf += raw.decode("utf-8")
        return True

    needle = f'"{key}"'

    while needle not in buf:
        if not _fill():
            return

    idx = buf.index(needle)
    buf = buf[idx + len(needle) :]

    while True:
        stripped = buf.lstrip()
        if stripped and stripped[0] == ":":
            buf = stripped[1:]
            break
        if not _fill():
            return

    while True:
        stripped = buf.lstrip()
        if stripped and stripped[0] == "[":
            buf = stripped[1:]
            break
        if not _fill():
            return

    while True:
        while True:
            stripped = buf.lstrip(" \t\n\r,")
            if stripped:
                buf = stripped
                break
            if not _fill():
                return

        if buf[0] == "]":
            return

        if buf[0] != "{":
            buf = buf[1:]
            continue

        depth = 0
        in_str = False
        esc = False
        pos = 0

        while True:
            while pos < len(buf):
                ch = buf[pos]

                if esc:
                    esc = False
                    pos += 1
                    continue

                if ch == "\\" and in_str:
                    esc = True
                    pos += 1
                    continue

                if ch == '"':
                    in_str = not in_str
                elif not in_str:
                    if ch == "{":
                        depth += 1
                    elif ch == "}":
                        depth -= 1
                        if depth == 0:
                            obj_text = buf[: pos + 1]
                            buf = buf[pos + 1 :]
                            yield json.loads(obj_text)
                            break
                pos += 1
            else:
                if not _fill():
                    return
                continue
            break


def stream_url_response(response: ParseResponse) -> Iterator[ResultFullResultChunk]:
    """Stream parse result chunks one at a time from a ``ParseResponse``.

    When the parse result is too large to return inline, the API stores it at a
    presigned S3 URL.  This function streams the bytes from that URL and
    incrementally parses individual chunk objects so that **only one chunk is
    held in memory at a time**.

    If the response already contains inline results (``type="full"``), the
    chunks are yielded directly.

    Args:
        response: A ``ParseResponse`` returned by the parse API.

    Yields:
        ``ResultFullResultChunk`` objects, one per chunk.

    Example::

        response = client.parse.run(
            input="https://example.com/large-doc.pdf",
            settings={"force_url_result": True},
        )
        for chunk in stream_url_response(response):
            print(chunk.content)
    """
    if response.result.type == "url":
        with httpx.stream("GET", response.result.url) as r:
            for raw_chunk in _iter_json_array_objects(r.iter_bytes(), "chunks"):
                yield ResultFullResultChunk.model_validate(raw_chunk)
    else:
        yield from response.result.chunks
