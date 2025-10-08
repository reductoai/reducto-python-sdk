# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["LargeTableChunkingConfig"]


class LargeTableChunkingConfig(TypedDict, total=False):
    enabled: bool
    """
    If large tables should be chunked into smaller tables, currently only supported
    on spreadsheet and CSV files.
    """

    size: int
    """The max row/column size for a table to be chunked.

    Defaults to 50. Header rows/columns are persisted based on heuristics.
    """
