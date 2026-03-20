# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union, Optional
from typing_extensions import Literal, TypeAlias, TypedDict

__all__ = ["SpreadsheetParam", "SplitLargeTables", "SplitLargeTablesSize", "SplitLargeTablesSizeSplitLargeTableSizes"]


class SplitLargeTablesSizeSplitLargeTableSizes(TypedDict, total=False):
    column: Optional[int]
    """The number of columns to include in each chunk when splitting large tables.

    Does not chunk columns if set to None.
    """

    row: Optional[int]
    """The number of rows to include in each chunk when splitting large tables.

    Does not chunk rows if set to None.
    """


SplitLargeTablesSize: TypeAlias = Union[int, SplitLargeTablesSizeSplitLargeTableSizes]


class SplitLargeTables(TypedDict, total=False):
    enabled: bool
    """If True, split large tables into smaller tables. Defaults to True."""

    size: SplitLargeTablesSize
    """The size of the tables to split into.

    Defaults to 50. Use 'row' and 'column' to independently specify the number of
    rows and columns to include when splitting. If you only want to split by rows or
    columns, set the other value to None.
    """


class SpreadsheetParam(TypedDict, total=False):
    clustering: Literal["accurate", "fast", "disabled"]
    """
    In a spreadsheet with different tables inside, we enable splitting up the tables
    by default. Accurate mode applies more powerful models for superior accuracy, at
    5× the default per-cell rate. Disabling will register as one large table.
    """

    exclude: List[Literal["hidden_sheets", "hidden_rows", "hidden_cols", "styling", "spreadsheet_images"]]
    """Whether to exclude hidden sheets, rows, or columns in the output."""

    include: List[Literal["cell_colors", "formula", "dropdowns"]]
    """Whether to include cell color, formula, and dropdown information in the output."""

    split_large_tables: SplitLargeTables
