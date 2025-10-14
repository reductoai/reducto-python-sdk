# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["SplitLargeTables"]


class SplitLargeTables(TypedDict, total=False):
    enabled: bool
    """If True, split large tables into smaller tables. Defaults to True."""

    size: int
    """The size of the tables to split into. Defaults to 50."""
