# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union, Optional
from datetime import datetime
from typing_extensions import Literal, TypeAlias

from .._models import BaseModel
from .shared.parse_usage import ParseUsage
from .shared.edit_response import EditResponse
from .shared.parse_response import ParseResponse
from .shared.split_response import SplitResponse
from .shared.extract_response import ExtractResponse

__all__ = [
    "JobGetResponse",
    "AsyncJobResponse",
    "AsyncJobResponseResult",
    "AsyncJobResponseResultPipelineResponse",
    "AsyncJobResponseResultPipelineResponseResult",
    "AsyncJobResponseResultPipelineResponseResultExtract",
    "AsyncJobResponseResultPipelineResponseResultExtractUnionMember0",
    "EnhancedAsyncJobResponse",
    "EnhancedAsyncJobResponseResult",
    "EnhancedAsyncJobResponseResultPipelineResponse",
    "EnhancedAsyncJobResponseResultPipelineResponseResult",
    "EnhancedAsyncJobResponseResultPipelineResponseResultExtract",
    "EnhancedAsyncJobResponseResultPipelineResponseResultExtractUnionMember0",
]


class AsyncJobResponseResultPipelineResponseResultExtractUnionMember0(BaseModel):
    page_range: List[int]

    result: ExtractResponse

    split_name: str

    partition: Optional[str] = None


AsyncJobResponseResultPipelineResponseResultExtract: TypeAlias = Union[
    List[AsyncJobResponseResultPipelineResponseResultExtractUnionMember0], ExtractResponse, None
]


class AsyncJobResponseResultPipelineResponseResult(BaseModel):
    extract: Optional[AsyncJobResponseResultPipelineResponseResultExtract] = None

    parse: Optional[ParseResponse] = None

    split: Optional[SplitResponse] = None


class AsyncJobResponseResultPipelineResponse(BaseModel):
    job_id: str

    result: AsyncJobResponseResultPipelineResponseResult

    usage: ParseUsage


AsyncJobResponseResult: TypeAlias = Union[
    ParseResponse, ExtractResponse, SplitResponse, EditResponse, AsyncJobResponseResultPipelineResponse, None
]


class AsyncJobResponse(BaseModel):
    status: Literal["Pending", "Completed", "Failed", "Idle"]

    progress: Optional[float] = None

    reason: Optional[str] = None

    result: Optional[AsyncJobResponseResult] = None


class EnhancedAsyncJobResponseResultPipelineResponseResultExtractUnionMember0(BaseModel):
    page_range: List[int]

    result: ExtractResponse

    split_name: str

    partition: Optional[str] = None


EnhancedAsyncJobResponseResultPipelineResponseResultExtract: TypeAlias = Union[
    List[EnhancedAsyncJobResponseResultPipelineResponseResultExtractUnionMember0], ExtractResponse, None
]


class EnhancedAsyncJobResponseResultPipelineResponseResult(BaseModel):
    extract: Optional[EnhancedAsyncJobResponseResultPipelineResponseResultExtract] = None

    parse: Optional[ParseResponse] = None

    split: Optional[SplitResponse] = None


class EnhancedAsyncJobResponseResultPipelineResponse(BaseModel):
    job_id: str

    result: EnhancedAsyncJobResponseResultPipelineResponseResult

    usage: ParseUsage


EnhancedAsyncJobResponseResult: TypeAlias = Union[
    ParseResponse, ExtractResponse, SplitResponse, EditResponse, EnhancedAsyncJobResponseResultPipelineResponse, None
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

    source: Optional[object] = None

    total_pages: Optional[int] = None

    type: Optional[Literal["Parse", "Extract", "Split", "Edit"]] = None


JobGetResponse: TypeAlias = Union[AsyncJobResponse, EnhancedAsyncJobResponse]
