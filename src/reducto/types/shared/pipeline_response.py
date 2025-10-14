# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union, Optional
from typing_extensions import TypeAlias

from ..._models import BaseModel
from .parse_usage import ParseUsage
from .edit_response import EditResponse
from .parse_response import ParseResponse
from .split_response import SplitResponse
from .extract_response import ExtractResponse
from .v3_extract_response import V3ExtractResponse

__all__ = [
    "PipelineResponse",
    "Result",
    "ResultExtract",
    "ResultExtractUnionMember0",
    "ResultExtractUnionMember0Result",
]

ResultExtractUnionMember0Result: TypeAlias = Union[ExtractResponse, V3ExtractResponse]


class ResultExtractUnionMember0(BaseModel):
    page_range: List[int]

    result: ResultExtractUnionMember0Result

    split_name: str

    partition: Optional[str] = None


ResultExtract: TypeAlias = Union[List[ResultExtractUnionMember0], ExtractResponse, V3ExtractResponse, None]


class Result(BaseModel):
    extract: Optional[ResultExtract] = None

    parse: Optional[ParseResponse] = None

    split: Optional[SplitResponse] = None

    edit: Optional[EditResponse] = None


class PipelineResponse(BaseModel):
    job_id: str

    result: Result

    usage: ParseUsage
