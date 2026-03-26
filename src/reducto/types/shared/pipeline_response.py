# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union, Optional
from typing_extensions import TypeAlias

from ..._models import BaseModel
from ..v3_extract import V3Extract
from ..parse_usage import ParseUsage
from .edit_response import EditResponse
from .parse_response import ParseResponse
from .split_response import SplitResponse
from .extract_response import ExtractResponse

__all__ = [
    "PipelineResponse",
    "Result",
    "ResultExtract",
    "ResultExtractExtractVariant0",
    "ResultExtractExtractVariant0Result",
    "ResultParse",
]

ResultExtractExtractVariant0Result: TypeAlias = Union[ExtractResponse, V3Extract]


class ResultExtractExtractVariant0(BaseModel):
    """This is the response format for Extract -> Split Pipelines"""

    page_range: List[int]

    result: ResultExtractExtractVariant0Result

    split_name: str

    partition: Optional[str] = None


ResultExtract: TypeAlias = Union[List[ResultExtractExtractVariant0], ExtractResponse, V3Extract, None]

ResultParse: TypeAlias = Union[ParseResponse, List[ParseResponse], None]


class Result(BaseModel):
    extract: Optional[ResultExtract] = None

    parse: Optional[ResultParse] = None

    split: Optional[SplitResponse] = None

    edit: Optional[EditResponse] = None


class PipelineResponse(BaseModel):
    job_id: str

    result: Result

    usage: ParseUsage
