# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["ArrayExtractConfig"]


class ArrayExtractConfig(BaseModel):
    enabled: Optional[bool] = None
    """
    Array extraction allows you to extract long lists of information from lengthy
    documents. It makes parallel calls on overlapping sections of the document.
    """

    mode: Optional[Literal["auto", "legacy", "no_overlap"]] = None
    """The array extraction version to use."""

    pages_per_segment: Optional[int] = None
    """Length of each segment, in pages, for parallel calls with array extraction."""
