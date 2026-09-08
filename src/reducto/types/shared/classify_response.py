from typing import Dict, List, Union, Optional
from typing_extensions import Literal, TypeAlias

from ..._models import BaseModel
from .url_result import URLResult

__all__ = [
    "ClassifyResponse",
    "Result",
    "ResultCategory",
    "ResponseConfidence",
    "ResponseConfidenceCategory",
    "ResponseConfidenceCategoryCriteriaConfidence",
    "Usage",
    "UsageUsageBreakdown",
]


class ResultCategory(BaseModel):
    category: str


Result: TypeAlias = Union[ResultCategory, URLResult]


class ResponseConfidenceCategoryCriteriaConfidence(BaseModel):
    """Confidence result for a single criterion."""

    confidence: Literal["high", "low"]

    criterion: str


class ResponseConfidenceCategory(BaseModel):
    """Confidence result for a category."""

    category: str

    confidence: float

    criteria_confidence: List[ResponseConfidenceCategoryCriteriaConfidence]


class ResponseConfidence(BaseModel):
    """Overall confidence breakdown for classification response."""

    categories: List[ResponseConfidenceCategory]


class UsageUsageBreakdown(BaseModel):
    classify_model: Literal["Classify", "Deep Classify"]

    classify_pages: Optional[int] = None


class Usage(BaseModel):
    num_categories: int

    num_pages: int

    credits: Optional[float] = None

    usage_breakdown: Optional[UsageUsageBreakdown] = None
    """Raw usage quantities.

    Only set for accounts on the new pricing model; credit fields are omitted for
    those accounts.
    """


class ClassifyResponse(BaseModel):
    """Response from classify job - returned when polling /job/{job_id}"""

    job_id: str

    result: Result
    """The classify result.

    If force_url_result is True, this is returned as a URL result.
    """

    duration: Optional[float] = None
    """The duration of the classify request in seconds."""

    extra_metadata: Optional[Dict[str, str]] = None
    """Additional metadata for the classify response.

    Contains `grouping` when the request set `category_groups`. Omitted when empty.
    """

    response_confidence: Optional[ResponseConfidence] = None
    """Overall confidence breakdown for classification response."""

    response_type: Literal["classify"]

    usage: Optional[Usage] = None
