# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union, Optional
from datetime import datetime
from typing_extensions import Literal, TypeAlias

from .._models import BaseModel
from .shared.edit_response import EditResponse
from .shared.parse_response import ParseResponse
from .shared.split_response import SplitResponse
from .shared.extract_response import ExtractResponse
from .shared.pipeline_response import PipelineResponse
from .shared.v3_extract_response import V3ExtractResponse

__all__ = [
    "JobGetResponse",
    "AsyncJobResponse",
    "AsyncJobResponseResult",
    "AsyncJobResponseResultClassifyResponse",
    "AsyncJobResponseResultClassifyResponseResult",
    "AsyncJobResponseResultClassifyResponseResponseConfidence",
    "AsyncJobResponseResultClassifyResponseResponseConfidenceCategory",
    "AsyncJobResponseResultClassifyResponseResponseConfidenceCategoryCriteriaConfidence",
    "EnhancedAsyncJobResponse",
    "EnhancedAsyncJobResponseResult",
    "EnhancedAsyncJobResponseResultClassifyResponse",
    "EnhancedAsyncJobResponseResultClassifyResponseResult",
    "EnhancedAsyncJobResponseResultClassifyResponseResponseConfidence",
    "EnhancedAsyncJobResponseResultClassifyResponseResponseConfidenceCategory",
    "EnhancedAsyncJobResponseResultClassifyResponseResponseConfidenceCategoryCriteriaConfidence",
]


class AsyncJobResponseResultClassifyResponseResult(BaseModel):
    category: str


class AsyncJobResponseResultClassifyResponseResponseConfidenceCategoryCriteriaConfidence(BaseModel):
    """Confidence result for a single criterion."""

    confidence: Literal["high", "low"]

    criterion: str


class AsyncJobResponseResultClassifyResponseResponseConfidenceCategory(BaseModel):
    """Confidence result for a category."""

    category: str

    confidence: float

    criteria_confidence: List[AsyncJobResponseResultClassifyResponseResponseConfidenceCategoryCriteriaConfidence]


class AsyncJobResponseResultClassifyResponseResponseConfidence(BaseModel):
    """Overall confidence breakdown for classification response."""

    categories: List[AsyncJobResponseResultClassifyResponseResponseConfidenceCategory]


class AsyncJobResponseResultClassifyResponse(BaseModel):
    """Response from classify job - returned when polling /job/{job_id}"""

    job_id: str

    result: AsyncJobResponseResultClassifyResponseResult

    duration: Optional[float] = None
    """The duration of the classify request in seconds."""

    response_confidence: Optional[AsyncJobResponseResultClassifyResponseResponseConfidence] = None
    """Overall confidence breakdown for classification response."""


AsyncJobResponseResult: TypeAlias = Union[
    ParseResponse,
    ExtractResponse,
    SplitResponse,
    EditResponse,
    PipelineResponse,
    V3ExtractResponse,
    AsyncJobResponseResultClassifyResponse,
    None,
]


class AsyncJobResponse(BaseModel):
    status: Literal["Pending", "Completed", "Failed", "Idle"]

    progress: Optional[float] = None

    reason: Optional[str] = None

    result: Optional[AsyncJobResponseResult] = None
    """Response from classify job - returned when polling /job/{job_id}"""


class EnhancedAsyncJobResponseResultClassifyResponseResult(BaseModel):
    category: str


class EnhancedAsyncJobResponseResultClassifyResponseResponseConfidenceCategoryCriteriaConfidence(BaseModel):
    """Confidence result for a single criterion."""

    confidence: Literal["high", "low"]

    criterion: str


class EnhancedAsyncJobResponseResultClassifyResponseResponseConfidenceCategory(BaseModel):
    """Confidence result for a category."""

    category: str

    confidence: float

    criteria_confidence: List[
        EnhancedAsyncJobResponseResultClassifyResponseResponseConfidenceCategoryCriteriaConfidence
    ]


class EnhancedAsyncJobResponseResultClassifyResponseResponseConfidence(BaseModel):
    """Overall confidence breakdown for classification response."""

    categories: List[EnhancedAsyncJobResponseResultClassifyResponseResponseConfidenceCategory]


class EnhancedAsyncJobResponseResultClassifyResponse(BaseModel):
    """Response from classify job - returned when polling /job/{job_id}"""

    job_id: str

    result: EnhancedAsyncJobResponseResultClassifyResponseResult

    duration: Optional[float] = None
    """The duration of the classify request in seconds."""

    response_confidence: Optional[EnhancedAsyncJobResponseResultClassifyResponseResponseConfidence] = None
    """Overall confidence breakdown for classification response."""


EnhancedAsyncJobResponseResult: TypeAlias = Union[
    ParseResponse,
    ExtractResponse,
    SplitResponse,
    EditResponse,
    PipelineResponse,
    V3ExtractResponse,
    EnhancedAsyncJobResponseResultClassifyResponse,
    None,
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
