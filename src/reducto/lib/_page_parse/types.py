from typing import Optional
from typing_extensions import Literal, TypeAlias

from ..._models import BaseModel
from ...types.shared.parse_response import ParseResponse, ResultFullResult

__all__ = ["FailureReason", "FailedPage", "ProviderParseResponse"]

FailureReason: TypeAlias = Literal[
    "unprocessable",  # The endpoint answered 422 "input could not be processed". The client does not retry it.
    "error",  # Any other failure, after the retries. See `status` and `detail`.
]


class FailedPage(BaseModel):
    page: int
    """The page number in the original document (1-indexed)."""

    reason: FailureReason
    """Why the page has no result."""

    status: Optional[int] = None
    """The endpoint's HTTP status, when it answered with an error."""

    detail: Optional[str] = None
    """A short description of the failure."""


class ProviderParseResponse(ParseResponse):
    """A ParseResponse built on your machine, with the same fields as the hosted one. `result` is always the
    full result, so `result.chunks` needs no type check. `job_id` is a random local ID that the hosted API
    does not know."""

    result: ResultFullResult  # pyright: ignore[reportIncompatibleVariableOverride]
    """One chunk per page, in page order."""
