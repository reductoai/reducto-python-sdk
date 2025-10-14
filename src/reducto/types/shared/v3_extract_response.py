# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union, Optional

from ..._models import BaseModel
from .extract_usage import ExtractUsage

__all__ = ["V3ExtractResponse"]


class V3ExtractResponse(BaseModel):
    result: Union[List[object], object]
    """The extracted response in your provided schema.

    This is a list of dictionaries. If disable_chunking is True (default), then it
    will be a list of length one.
    """

    usage: ExtractUsage

    job_id: Optional[str] = None

    studio_link: Optional[str] = None
    """The link to the studio pipeline for the document."""
