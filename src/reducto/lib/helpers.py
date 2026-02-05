from typing import Iterator, Optional

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


def stream_url_response(response: ParseResponse) -> Iterator[ResultFullResultChunk]:
    """Stream parse results chunk by chunk from a ParseResponse.

    When the parse result is large, the API returns a presigned S3 URL instead of
    inline data. This function handles both cases and yields individual chunks,
    allowing you to process results incrementally without loading the entire
    response into memory at once.

    Args:
        response: The ParseResponse from a parse API call.

    Yields:
        Individual ResultFullResultChunk objects from the parse result.

    Example:
        ```python
        response = client.parse.run(input="https://example.com/large-doc.pdf")
        for chunk in stream_url_response(response):
            print(chunk.content)
        ```
    """
    if response.result.type == "url":
        with httpx.stream("GET", response.result.url) as r:
            content = r.read().decode()
            result = ResultFullResult.model_validate_json(content)
            yield from result.chunks
    else:
        yield from response.result.chunks
