from typing import Union, Optional
from datetime import datetime
from typing_extensions import Literal, Annotated, TypeAlias

from .._utils import PropertyInfo
from .._models import BaseModel
from .v3_extract import V3Extract
from .shared.error_detail import ErrorDetail
from .shared.edit_response import EditResponse
from .shared.chart_response import ChartResponse
from .shared.parse_response import ParseResponse
from .shared.split_response import SplitResponse
from .shared.extract_response import ExtractResponse
from .shared.classify_response import ClassifyResponse
from .shared.pipeline_response import PipelineResponse

__all__ = [
    "JobGetResponse",
    "AsyncJobResponse",
    "AsyncJobResponseResult",
    "EnhancedAsyncJobResponse",
    "EnhancedAsyncJobResponseResult",
]

AsyncJobResponseResult: TypeAlias = Annotated[
    Union[
        ParseResponse,
        ExtractResponse,
        SplitResponse,
        EditResponse,
        PipelineResponse,
        V3Extract,
        ClassifyResponse,
        ChartResponse,
        None,
    ],
    PropertyInfo(discriminator="response_type"),
]


class AsyncJobResponse(BaseModel):
    status: Literal["Pending", "Completed", "Failed", "Idle"]

    error: Optional[ErrorDetail] = None

    progress: Optional[float] = None

    reason: Optional[str] = None

    result: Optional[AsyncJobResponseResult] = None


EnhancedAsyncJobResponseResult: TypeAlias = Annotated[
    Union[
        ParseResponse,
        ExtractResponse,
        SplitResponse,
        EditResponse,
        PipelineResponse,
        V3Extract,
        ClassifyResponse,
        ChartResponse,
        None,
    ],
    PropertyInfo(discriminator="response_type"),
]


class EnhancedAsyncJobResponse(BaseModel):
    status: Literal["Pending", "Completed", "Failed", "Idle"]

    bucket: Optional[object] = None

    created_at: Optional[datetime] = None

    duration: Optional[float] = None

    error: Optional[ErrorDetail] = None

    num_pages: Optional[int] = None

    progress: Optional[float] = None

    raw_config: Optional[str] = None

    reason: Optional[str] = None

    result: Optional[EnhancedAsyncJobResponseResult] = None

    source: Optional[object] = None

    total_pages: Optional[int] = None

    type: Optional[Literal["Parse", "Extract", "Split", "Edit", "Pipeline", "Classify", "Chart"]] = None


JobGetResponse: TypeAlias = Union[AsyncJobResponse, EnhancedAsyncJobResponse]
