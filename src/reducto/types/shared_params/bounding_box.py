# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["BoundingBox"]


class BoundingBox(TypedDict, total=False):
    height: Required[float]

    left: Required[float]

    page: Required[int]
    """The page number of the bounding box (1-indexed)."""

    top: Required[float]

    width: Required[float]

    original_page: int
    """The page number in the original document of the bounding box (1-indexed)."""
