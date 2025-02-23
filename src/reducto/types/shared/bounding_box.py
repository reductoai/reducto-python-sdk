# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel

__all__ = ["BoundingBox"]


class BoundingBox(BaseModel):
    height: float

    left: float

    page: int
    """The page number of the bounding box (1-indexed)."""

    top: float

    width: float

    original_page: Optional[int] = None
    """The page number in the original document of the bounding box (1-indexed)."""
