# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Union, Optional
from datetime import datetime
from typing_extensions import Literal, Annotated, TypeAlias

from .._utils import PropertyInfo
from .._models import BaseModel
from .v3_extract import V3Extract
from .shared.edit_response import EditResponse
from .shared.parse_response import ParseResponse
from .shared.split_response import SplitResponse
from .shared.extract_response import ExtractResponse
from .shared.classify_response import ClassifyResponse
from .shared.pipeline_response import PipelineResponse

__all__ = [
    "JobGetResponse",
    "AsyncJobResponse",
    "AsyncJobResponseError",
    "AsyncJobResponseResult",
    "EnhancedAsyncJobResponse",
    "EnhancedAsyncJobResponseError",
    "EnhancedAsyncJobResponseResult",
]


class AsyncJobResponseError(BaseModel):
    """Structured error body returned to customers.

    Matches the format specified in ``ERROR_POLICY.md``.
    """

    code: int

    message: str

    name: Literal[
        "TIMEOUT",
        "CUSTOMER_TIMEOUT",
        "INTERNAL_ERROR",
        "SERVICE_UNAVAILABLE",
        "GPU_ALLOCATION_ERROR",
        "GPU_POOL_SATURATED",
        "BATCH_QUEUE_FULL",
        "JOB_STATE_ERROR",
        "DOCUMENT_CORRUPT",
        "DOCUMENT_UNSUPPORTED",
        "DOCUMENT_TOO_LARGE",
        "IMAGE_TOO_LARGE",
        "IMAGE_TOO_SMALL",
        "IMAGE_INVALID_ASPECT_RATIO",
        "DOCUMENT_PASSWORD_PROTECTED",
        "FORM_FILL_FAILED",
        "INTERNAL_INVARIANT_VIOLATION",
        "CONTEXT_WINDOW_EXCEEDED",
        "PROCESSING_FAILED",
        "INFERENCE_METHOD_UNSUPPORTED",
        "SUBPROCESS_CRASHED",
        "BATCH_ORPHANED",
        "OVERSIZED_RESULT",
        "LLM_OUTPUT_PARSE_FAILED",
        "LLM_PROVIDER_ERROR",
        "INVALID_CONFIG",
        "INVALID_SCHEMA",
        "AUTH_ERROR",
        "NOT_APPLICABLE",
        "REGION_UNAVAILABLE",
        "NOT_FOUND",
        "JOB_DELETION_IN_PROGRESS",
        "JOB_DELETED",
        "JOB_NOT_COMPLETE",
        "JOB_CANCELLED",
        "RATE_LIMIT",
        "CELL_COUNT_EXCEEDED",
    ]
    """Machine-readable error names returned in API error responses.

    Each member maps to a category (Transient / Processing / Input) and a default
    HTTP status code defined in `ERROR_CODE_DEFAULTS`. The enum value is the string
    customers see in the `error.name` field.
    """

    job_id: Optional[str] = None


AsyncJobResponseResult: TypeAlias = Annotated[
    Union[
        ParseResponse, ExtractResponse, SplitResponse, EditResponse, PipelineResponse, V3Extract, ClassifyResponse, None
    ],
    PropertyInfo(discriminator="response_type"),
]


class AsyncJobResponse(BaseModel):
    status: Literal["Pending", "Completed", "Failed", "Idle"]

    error: Optional[AsyncJobResponseError] = None
    """Structured error body returned to customers.

    Matches the format specified in `ERROR_POLICY.md`.
    """

    progress: Optional[float] = None

    reason: Optional[str] = None

    result: Optional[AsyncJobResponseResult] = None
    """Response from classify job - returned when polling /job/{job_id}"""


class EnhancedAsyncJobResponseError(BaseModel):
    """Structured error body returned to customers.

    Matches the format specified in ``ERROR_POLICY.md``.
    """

    code: int

    message: str

    name: Literal[
        "TIMEOUT",
        "CUSTOMER_TIMEOUT",
        "INTERNAL_ERROR",
        "SERVICE_UNAVAILABLE",
        "GPU_ALLOCATION_ERROR",
        "GPU_POOL_SATURATED",
        "BATCH_QUEUE_FULL",
        "JOB_STATE_ERROR",
        "DOCUMENT_CORRUPT",
        "DOCUMENT_UNSUPPORTED",
        "DOCUMENT_TOO_LARGE",
        "IMAGE_TOO_LARGE",
        "IMAGE_TOO_SMALL",
        "IMAGE_INVALID_ASPECT_RATIO",
        "DOCUMENT_PASSWORD_PROTECTED",
        "FORM_FILL_FAILED",
        "INTERNAL_INVARIANT_VIOLATION",
        "CONTEXT_WINDOW_EXCEEDED",
        "PROCESSING_FAILED",
        "INFERENCE_METHOD_UNSUPPORTED",
        "SUBPROCESS_CRASHED",
        "BATCH_ORPHANED",
        "OVERSIZED_RESULT",
        "LLM_OUTPUT_PARSE_FAILED",
        "LLM_PROVIDER_ERROR",
        "INVALID_CONFIG",
        "INVALID_SCHEMA",
        "AUTH_ERROR",
        "NOT_APPLICABLE",
        "REGION_UNAVAILABLE",
        "NOT_FOUND",
        "JOB_DELETION_IN_PROGRESS",
        "JOB_DELETED",
        "JOB_NOT_COMPLETE",
        "JOB_CANCELLED",
        "RATE_LIMIT",
        "CELL_COUNT_EXCEEDED",
    ]
    """Machine-readable error names returned in API error responses.

    Each member maps to a category (Transient / Processing / Input) and a default
    HTTP status code defined in `ERROR_CODE_DEFAULTS`. The enum value is the string
    customers see in the `error.name` field.
    """

    job_id: Optional[str] = None


EnhancedAsyncJobResponseResult: TypeAlias = Annotated[
    Union[
        ParseResponse, ExtractResponse, SplitResponse, EditResponse, PipelineResponse, V3Extract, ClassifyResponse, None
    ],
    PropertyInfo(discriminator="response_type"),
]


class EnhancedAsyncJobResponse(BaseModel):
    status: Literal["Pending", "Completed", "Failed", "Idle"]

    bucket: Optional[object] = None

    created_at: Optional[datetime] = None

    duration: Optional[float] = None

    error: Optional[EnhancedAsyncJobResponseError] = None
    """Structured error body returned to customers.

    Matches the format specified in `ERROR_POLICY.md`.
    """

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
