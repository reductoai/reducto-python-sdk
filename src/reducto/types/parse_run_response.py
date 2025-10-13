# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Union
from typing_extensions import TypeAlias

from .._models import BaseModel
from .shared.parse_response import ParseResponse

__all__ = ["ParseRunResponse", "AsyncParseResponse"]


class AsyncParseResponse(BaseModel):
    job_id: str


ParseRunResponse: TypeAlias = Union[ParseResponse, AsyncParseResponse]
