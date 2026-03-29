# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = [
    "ClassifyResponse",
    "Result",
    "ResponseConfidence",
    "ResponseConfidenceCategory",
    "ResponseConfidenceCategoryCriteriaConfidence",
]


class Result(BaseModel):
    category: str


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


class ClassifyResponse(BaseModel):
    """Response from classify job - returned when polling /job/{job_id}"""

    job_id: str

    result: Result

    duration: Optional[float] = None
    """The duration of the classify request in seconds."""

    response_confidence: Optional[ResponseConfidence] = None
    """Overall confidence breakdown for classification response."""
