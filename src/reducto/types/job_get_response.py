# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Union, Optional
from datetime import datetime
from typing_extensions import Literal, TypeAlias

from .._models import BaseModel
from .shared.edit_response import EditResponse
from .shared.parse_response import ParseResponse
from .shared.split_response import SplitResponse
from .shared.extract_response import ExtractResponse

__all__ = [
    "JobGetResponse",
    "AsyncJobResponse",
    "AsyncJobResponseResult",
    "EnhancedAsyncJobResponse",
    "EnhancedAsyncJobResponseResult",
]

AsyncJobResponseResult: TypeAlias = Union[ParseResponse, ExtractResponse, SplitResponse, EditResponse, None]


class AsyncJobResponse(BaseModel):
    status: Literal["Pending", "Completed", "Failed", "Idle"]

    progress: Optional[float] = None

    reason: Optional[str] = None

    result: Optional[AsyncJobResponseResult] = None


EnhancedAsyncJobResponseResult: TypeAlias = Union[ParseResponse, ExtractResponse, SplitResponse, EditResponse, None]


class EnhancedAsyncJobResponse(BaseModel):
    status: Literal["Pending", "Completed", "Failed", "Idle"]

    bucket: Optional[object] = None

    created_at: Optional[datetime] = None

    duration: Optional[float] = None

    num_pages: Optional[int] = None

    progress: Optional[float] = None

    raw_config: Optional[str] = None

    reason: Optional[str] = None

    result: Optional[EnhancedAsyncJobResponseResult] = None

    source: Optional[object] = None

    total_pages: Optional[int] = None

    type: Optional[Literal["Parse", "Extract", "Split", "Edit"]] = None


JobGetResponse: TypeAlias = Union[AsyncJobResponse, EnhancedAsyncJobResponse]
