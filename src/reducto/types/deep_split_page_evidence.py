from typing import Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["DeepSplitPageEvidence"]


class DeepSplitPageEvidence(BaseModel):
    evidence: str

    page_number: int

    confidence: Optional[Literal["high", "medium", "low"]] = None
