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

__all__ = ["PipelineResponse", "Result", "ResultExtractUnionMember0", "ResultParse"]


class ResultExtractUnionMember0(BaseModel):
    """This is the response format for Extract -> Split Pipelines"""

    page_range: List[int]

    result: Union[ExtractResponse, V3Extract]

    split_name: str

    partition: Optional[str] = None


ResultParse: TypeAlias = Union[ParseResponse, List[ParseResponse], None]


class Result(BaseModel):
    extract: Union[List[ResultExtractUnionMember0], ExtractResponse, V3Extract, None] = None

    parse: Optional[ResultParse] = None

    split: Optional[SplitResponse] = None

    edit: Optional[EditResponse] = None


class PipelineResponse(BaseModel):
    job_id: str

    result: Result

    usage: ParseUsage
