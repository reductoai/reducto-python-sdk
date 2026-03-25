# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Union, Optional
from datetime import datetime
from typing_extensions import Literal, TypeAlias

from .._models import BaseModel
from .v3_extract import V3Extract
from .edit_response import EditResponse
from .parse_response import ParseResponse
from .split_response import SplitResponse
from .extract_response import ExtractResponse
from .classify_response import ClassifyResponse
from .pipeline_response import PipelineResponse

__all__ = [
    "JobGetResponse",
    "AsyncJobResponse",
    "AsyncJobResponseResult",
    "EnhancedAsyncJobResponse",
    "EnhancedAsyncJobResponseResult",
]

AsyncJobResponseResult: TypeAlias = Union[
    ParseResponse, ExtractResponse, SplitResponse, EditResponse, PipelineResponse, V3Extract, ClassifyResponse, None
]


class AsyncJobResponse(BaseModel):
    status: Literal["Pending", "Completed", "Failed", "Idle"]

    progress: Optional[float] = None

    reason: Optional[str] = None

    result: Optional[AsyncJobResponseResult] = None
    """Response from classify job - returned when polling /job/{job_id}"""


EnhancedAsyncJobResponseResult: TypeAlias = Union[
    ParseResponse, ExtractResponse, SplitResponse, EditResponse, PipelineResponse, V3Extract, ClassifyResponse, None
]


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
    """Response from classify job - returned when polling /job/{job_id}"""

    source: Optional[object] = None

    total_pages: Optional[int] = None

    type: Optional[Literal["Parse", "Extract", "Split", "Edit", "Pipeline", "Classify"]] = None


JobGetResponse: TypeAlias = Union[AsyncJobResponse, EnhancedAsyncJobResponse]
