# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import TypedDict

__all__ = ["PageRange"]


class PageRange(TypedDict, total=False):
    end: Optional[int]
    """The page number to stop processing at (1-indexed)."""

    start: Optional[int]
    """The page number to start processing from (1-indexed)."""
