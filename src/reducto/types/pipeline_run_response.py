# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union, Optional
from typing_extensions import TypeAlias

from .._models import BaseModel
from .shared.parse_usage import ParseUsage
from .shared.parse_response import ParseResponse
from .shared.split_response import SplitResponse
from .shared.extract_response import ExtractResponse

__all__ = ["PipelineRunResponse", "Result", "ResultExtract", "ResultExtractUnionMember0"]


class ResultExtractUnionMember0(BaseModel):
    page_range: List[int]

    result: ExtractResponse

    split_name: str

    partition: Optional[str] = None


ResultExtract: TypeAlias = Union[List[ResultExtractUnionMember0], ExtractResponse, None]


class Result(BaseModel):
    extract: Optional[ResultExtract] = None

    parse: Optional[ParseResponse] = None

    split: Optional[SplitResponse] = None


class PipelineRunResponse(BaseModel):
    job_id: str

    result: Result

    usage: ParseUsage
