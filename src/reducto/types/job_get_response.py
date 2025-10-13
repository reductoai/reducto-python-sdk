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

__all__ = [
    "JobGetResponse",
    "AsyncJobResponse",
    "AsyncJobResponseResult",
    "AsyncJobResponseResultV3ExtractResponse",
    "AsyncJobResponseResultV3ExtractResponseUsage",
    "EnhancedAsyncJobResponse",
    "EnhancedAsyncJobResponseResult",
    "EnhancedAsyncJobResponseResultV3ExtractResponse",
    "EnhancedAsyncJobResponseResultV3ExtractResponseUsage",
]


class AsyncJobResponseResultV3ExtractResponseUsage(BaseModel):
    num_fields: int

    num_pages: int

    credits: Optional[float] = None


class AsyncJobResponseResultV3ExtractResponse(BaseModel):
    result: Union[List[object], object]
    """The extracted response in your provided schema.

    This is a list of dictionaries. If disable_chunking is True (default), then it
    will be a list of length one.
    """

    usage: AsyncJobResponseResultV3ExtractResponseUsage

    job_id: Optional[str] = None

    studio_link: Optional[str] = None
    """The link to the studio pipeline for the document."""


AsyncJobResponseResult: TypeAlias = Union[
    ParseResponse,
    ExtractResponse,
    SplitResponse,
    EditResponse,
    PipelineResponse,
    AsyncJobResponseResultV3ExtractResponse,
    None,
]


class AsyncJobResponse(BaseModel):
    status: Literal["Pending", "Completed", "Failed", "Idle"]

    progress: Optional[float] = None

    reason: Optional[str] = None

    result: Optional[AsyncJobResponseResult] = None


class EnhancedAsyncJobResponseResultV3ExtractResponseUsage(BaseModel):
    num_fields: int

    num_pages: int

    credits: Optional[float] = None


class EnhancedAsyncJobResponseResultV3ExtractResponse(BaseModel):
    result: Union[List[object], object]
    """The extracted response in your provided schema.

    This is a list of dictionaries. If disable_chunking is True (default), then it
    will be a list of length one.
    """

    usage: EnhancedAsyncJobResponseResultV3ExtractResponseUsage

    job_id: Optional[str] = None

    studio_link: Optional[str] = None
    """The link to the studio pipeline for the document."""


EnhancedAsyncJobResponseResult: TypeAlias = Union[
    ParseResponse,
    ExtractResponse,
    SplitResponse,
    EditResponse,
    PipelineResponse,
    EnhancedAsyncJobResponseResultV3ExtractResponse,
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

    source: Optional[object] = None

    total_pages: Optional[int] = None

    type: Optional[Literal["Parse", "Extract", "Split", "Edit", "Pipeline"]] = None


JobGetResponse: TypeAlias = Union[AsyncJobResponse, EnhancedAsyncJobResponse]
