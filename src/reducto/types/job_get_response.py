# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Union, Optional
from typing_extensions import Literal, TypeAlias

from .._models import BaseModel
from .shared.parse_response import ParseResponse
from .shared.split_response import SplitResponse
from .shared.extract_response import ExtractResponse

__all__ = ["JobGetResponse", "Result", "ResultEditResponse"]


class ResultEditResponse(BaseModel):
    document_url: str


Result: TypeAlias = Union[ParseResponse, ExtractResponse, SplitResponse, ResultEditResponse, None]


class JobGetResponse(BaseModel):
    status: Literal["Pending", "Completed", "Failed", "Idle"]

    progress: Optional[float] = None

    reason: Optional[str] = None

    result: Optional[Result] = None
