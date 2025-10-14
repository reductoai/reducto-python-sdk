# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Union
from typing_extensions import TypeAlias

from .._models import BaseModel
from .shared.v3_extract_response import V3ExtractResponse

__all__ = ["ExtractRunResponse", "AsyncExtractResponse"]


class AsyncExtractResponse(BaseModel):
    job_id: str


ExtractRunResponse: TypeAlias = Union[V3ExtractResponse, AsyncExtractResponse]
