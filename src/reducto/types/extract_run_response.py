# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union, Optional
from typing_extensions import TypeAlias

from .._models import BaseModel
from .shared.extract_response import ExtractResponse

__all__ = ["ExtractRunResponse", "V3ExtractResponse", "V3ExtractResponseUsage"]


class V3ExtractResponseUsage(BaseModel):
    num_fields: int

    num_pages: int

    credits: Optional[float] = None


class V3ExtractResponse(BaseModel):
    result: Union[List[object], object]
    """The extracted response in your provided schema.

    This is a list of dictionaries. If disable_chunking is True (default), then it
    will be a list of length one.
    """

    usage: V3ExtractResponseUsage

    job_id: Optional[str] = None

    studio_link: Optional[str] = None
    """The link to the studio pipeline for the document."""


ExtractRunResponse: TypeAlias = Union[ExtractResponse, V3ExtractResponse]
