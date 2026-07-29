# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Union, Optional
from typing_extensions import Literal, TypeAlias

from ..._models import BaseModel
from ..extract_usage import ExtractUsage

__all__ = ["ExtractResponse", "Citations", "CitationsURLResult", "Result", "ResultURLResult"]


class CitationsURLResult(BaseModel):
    result_id: str

    type: Literal["url"]
    """type = 'url'"""

    url: str


Citations: TypeAlias = Union[List[object], CitationsURLResult, None]


class ResultURLResult(BaseModel):
    result_id: str

    type: Literal["url"]
    """type = 'url'"""

    url: str


Result: TypeAlias = Union[List[object], ResultURLResult]


class ExtractResponse(BaseModel):
    citations: Optional[Citations] = None
    """The citations corresponding to the extracted response.

    If force_url_result is True and citations are present, this is returned as a URL
    result.
    """

    result: Result
    """The extracted response in your provided schema.

    This is a list of dictionaries. If disable_chunking is True (default), then it
    will be a list of length one. If force_url_result is True, this is returned as a
    URL result.
    """

    usage: ExtractUsage

    job_id: Optional[str] = None

    response_confidence: Optional[Dict[str, object]] = None
    """
    Optional deep extract confidence metadata containing document-level confidence
    plus a mirrored leaf-level confidence tree.
    """

    response_type: Optional[Literal["extract"]] = None

    studio_link: Optional[str] = None
    """The link to the studio pipeline for the document."""
