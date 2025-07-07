# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional
from typing_extensions import Literal

from ..._models import BaseModel
from .parse_usage import ParseUsage

__all__ = ["SplitResponse", "Result", "ResultSplit", "ResultSplitPartition"]


class ResultSplitPartition(BaseModel):
    name: str

    pages: List[int]

    conf: Optional[Literal["high", "low"]] = None


class ResultSplit(BaseModel):
    name: str

    pages: List[int]

    conf: Optional[Literal["high", "low"]] = None

    partitions: Optional[List[ResultSplitPartition]] = None


class Result(BaseModel):
    section_mapping: Optional[Dict[str, List[int]]] = None

    splits: List[ResultSplit]


class SplitResponse(BaseModel):
    result: Result
    """The split result."""

    usage: ParseUsage
