# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union, Optional
from datetime import datetime
from typing_extensions import Literal, TypeAlias

from .._models import BaseModel
from .shared.bounding_box import BoundingBox
from .shared.parse_response import ParseResponse
from .shared.split_response import SplitResponse
from .shared.extract_response import ExtractResponse

__all__ = [
    "JobGetResponse",
    "AsyncJobResponse",
    "AsyncJobResponseResult",
    "AsyncJobResponseResultEditResponse",
    "AsyncJobResponseResultEditResponseFormSchema",
    "EnhancedAsyncJobResponse",
    "EnhancedAsyncJobResponseResult",
    "EnhancedAsyncJobResponseResultEditResponse",
    "EnhancedAsyncJobResponseResultEditResponseFormSchema",
]


class AsyncJobResponseResultEditResponseFormSchema(BaseModel):
    bbox: BoundingBox

    description: str

    type: Literal["text", "checkbox", "dropdown", "barcode"]


class AsyncJobResponseResultEditResponse(BaseModel):
    document_url: str

    form_schema: Optional[List[AsyncJobResponseResultEditResponseFormSchema]] = None


AsyncJobResponseResult: TypeAlias = Union[
    ParseResponse, ExtractResponse, SplitResponse, AsyncJobResponseResultEditResponse, None
]


class AsyncJobResponse(BaseModel):
    status: Literal["Pending", "Completed", "Failed", "Idle"]

    progress: Optional[float] = None

    reason: Optional[str] = None

    result: Optional[AsyncJobResponseResult] = None


class EnhancedAsyncJobResponseResultEditResponseFormSchema(BaseModel):
    bbox: BoundingBox

    description: str

    type: Literal["text", "checkbox", "dropdown", "barcode"]


class EnhancedAsyncJobResponseResultEditResponse(BaseModel):
    document_url: str

    form_schema: Optional[List[EnhancedAsyncJobResponseResultEditResponseFormSchema]] = None


EnhancedAsyncJobResponseResult: TypeAlias = Union[
    ParseResponse, ExtractResponse, SplitResponse, EnhancedAsyncJobResponseResultEditResponse, None
]


class EnhancedAsyncJobResponse(BaseModel):
    status: Literal["Pending", "Completed", "Failed", "Idle"]

    created_at: Optional[datetime] = None

    duration: Optional[float] = None

    num_pages: Optional[int] = None

    progress: Optional[float] = None

    raw_config: Optional[str] = None

    reason: Optional[str] = None

    result: Optional[EnhancedAsyncJobResponseResult] = None

    source: Optional[object] = None

    type: Optional[Literal["Parse", "Extract", "Split", "Edit"]] = None


JobGetResponse: TypeAlias = Union[AsyncJobResponse, EnhancedAsyncJobResponse]
