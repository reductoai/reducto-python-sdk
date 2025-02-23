# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel

__all__ = ["PageRange"]


class PageRange(BaseModel):
    end: Optional[int] = None
    """The page number to stop processing at (1-indexed)."""

    start: Optional[int] = None
    """The page number to start processing from (1-indexed)."""
