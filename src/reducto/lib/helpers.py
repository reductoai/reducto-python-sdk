from typing import Optional

import httpx
from pydantic import BaseModel

from reducto.types import ParseResponse
from reducto.types.shared.parse_response import ParseUsage, ResultFullResult


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
            result = ResultFullResult.model_validate_json(r.text)
            return FullParseResponse(
                duration=response.duration,
                job_id=response.job_id,
                result=result,
                usage=response.usage,
            )
    else:
        return FullParseResponse.model_validate(response.model_dump())
