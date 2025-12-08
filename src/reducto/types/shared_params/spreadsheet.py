# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import Literal, TypedDict

from .split_large_tables import SplitLargeTables

__all__ = ["Spreadsheet"]


class Spreadsheet(TypedDict, total=False):
    clustering: Literal["accurate", "fast", "disabled"]
    """
    In a spreadsheet with different tables inside, we enable splitting up the tables
    by default. Accurate mode applies more powerful models for superior accuracy, at
    5× the default per-cell rate. Disabling will register as one large table.
    """

    exclude: List[Literal["hidden_sheets", "hidden_rows", "hidden_cols", "styling", "spreadsheet_images"]]
    """Whether to exclude hidden sheets, rows, or columns in the output."""

    include: List[Literal["cell_colors", "formula"]]
    """Whether to include cell color and formula information in the output."""

    split_large_tables: SplitLargeTables
