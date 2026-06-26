# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union, Optional
from typing_extensions import Literal, TypeAlias

from ..._models import BaseModel

__all__ = [
    "ClassifyResponse",
    "Result",
    "ResultClassifyResponseCategory",
    "ResultURLResult",
    "ResponseConfidence",
    "ResponseConfidenceCategory",
    "ResponseConfidenceCategoryCriteriaConfidence",
    "Usage",
]


class ResultClassifyResponseCategory(BaseModel):
    category: str


class ResultURLResult(BaseModel):
    result_id: str

    type: Literal["url"]
    """type = 'url'"""

    url: str


Result: TypeAlias = Union[ResultClassifyResponseCategory, ResultURLResult]


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


class Usage(BaseModel):
    num_categories: int

    num_pages: int

    credits: Optional[float] = None


class ClassifyResponse(BaseModel):
    """Response from classify job - returned when polling /job/{job_id}"""

    job_id: str

    result: Result

    duration: Optional[float] = None
    """The duration of the classify request in seconds."""

    response_confidence: Optional[ResponseConfidence] = None
    """Overall confidence breakdown for classification response."""

    response_type: Optional[Literal["classify"]] = None

    usage: Optional[Usage] = None
