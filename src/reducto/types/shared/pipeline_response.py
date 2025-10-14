# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union, Optional
from typing_extensions import TypeAlias

from ..._models import BaseModel
from .parse_usage import ParseUsage
from .edit_response import EditResponse
from .parse_response import ParseResponse
from .split_response import SplitResponse
from .extract_response import ExtractResponse

__all__ = [
    "PipelineResponse",
    "Result",
    "ResultExtract",
    "ResultExtractUnionMember0",
    "ResultExtractUnionMember0Result",
    "ResultExtractUnionMember0ResultV3ExtractResponse",
    "ResultExtractUnionMember0ResultV3ExtractResponseUsage",
    "ResultExtractV3ExtractResponse",
    "ResultExtractV3ExtractResponseUsage",
]


class ResultExtractUnionMember0ResultV3ExtractResponseUsage(BaseModel):
    num_fields: int

    num_pages: int

    credits: Optional[float] = None


class ResultExtractUnionMember0ResultV3ExtractResponse(BaseModel):
    result: Union[List[object], object]
    """The extracted response in your provided schema.

    This is a list of dictionaries. If disable_chunking is True (default), then it
    will be a list of length one.
    """

    usage: ResultExtractUnionMember0ResultV3ExtractResponseUsage

    job_id: Optional[str] = None

    studio_link: Optional[str] = None
    """The link to the studio pipeline for the document."""


ResultExtractUnionMember0Result: TypeAlias = Union[ExtractResponse, ResultExtractUnionMember0ResultV3ExtractResponse]


class ResultExtractUnionMember0(BaseModel):
    page_range: List[int]

    result: ResultExtractUnionMember0Result

    split_name: str

    partition: Optional[str] = None


class ResultExtractV3ExtractResponseUsage(BaseModel):
    num_fields: int

    num_pages: int

    credits: Optional[float] = None


class ResultExtractV3ExtractResponse(BaseModel):
    result: Union[List[object], object]
    """The extracted response in your provided schema.

    This is a list of dictionaries. If disable_chunking is True (default), then it
    will be a list of length one.
    """

    usage: ResultExtractV3ExtractResponseUsage

    job_id: Optional[str] = None

    studio_link: Optional[str] = None
    """The link to the studio pipeline for the document."""


ResultExtract: TypeAlias = Union[List[ResultExtractUnionMember0], ExtractResponse, ResultExtractV3ExtractResponse, None]


class Result(BaseModel):
    extract: Optional[ResultExtract] = None

    parse: Optional[ParseResponse] = None

    split: Optional[SplitResponse] = None

    edit: Optional[EditResponse] = None


class PipelineResponse(BaseModel):
    job_id: str

    result: Result

    usage: ParseUsage
