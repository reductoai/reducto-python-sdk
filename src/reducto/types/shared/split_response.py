# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional

from ..._models import BaseModel
from .parse_usage import ParseUsage

__all__ = ["SplitResponse", "Result"]


class Result(BaseModel):
    section_mapping: Optional[Dict[str, List[int]]] = None

    splits: List[object]


class SplitResponse(BaseModel):
    result: Result
    """The extracted response in your provided schema.

    This is a list of dictionaries. If disbale_chunking is True (default), then it
    will be a list of length one.
    """

    usage: ParseUsage
