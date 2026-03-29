# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Union, Optional
from typing_extensions import Literal, TypeAlias

from ..._models import BaseModel
from ..parse_usage import ParseUsage
from ..deep_split_page_evidence import DeepSplitPageEvidence

__all__ = [
    "SplitResponse",
    "Result",
    "ResultSplitResult",
    "ResultSplitResultSplit",
    "ResultSplitResultSplitPartition",
    "ResultDeepSplitResult",
    "ResultDeepSplitResultSplit",
    "ResultDeepSplitResultSplitPartition",
]


class ResultSplitResultSplitPartition(BaseModel):
    name: str

    pages: List[int]

    conf: Optional[Literal["high", "low"]] = None


class ResultSplitResultSplit(BaseModel):
    name: str

    pages: List[int]

    conf: Optional[Literal["high", "low"]] = None

    partitions: Optional[List[ResultSplitResultSplitPartition]] = None


class ResultSplitResult(BaseModel):
    section_mapping: Optional[Dict[str, List[int]]] = None

    splits: List[ResultSplitResultSplit]


class ResultDeepSplitResultSplitPartition(BaseModel):
    name: str

    pages: List[DeepSplitPageEvidence]


class ResultDeepSplitResultSplit(BaseModel):
    name: str

    pages: List[DeepSplitPageEvidence]

    partitions: Optional[List[ResultDeepSplitResultSplitPartition]] = None


class ResultDeepSplitResult(BaseModel):
    splits: List[ResultDeepSplitResultSplit]


Result: TypeAlias = Union[ResultSplitResult, ResultDeepSplitResult]


class SplitResponse(BaseModel):
    result: Result
    """The split result."""

    usage: ParseUsage
