# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from ..._models import BaseModel
from .split_large_tables import SplitLargeTables

__all__ = ["Spreadsheet"]


class Spreadsheet(BaseModel):
    clustering: Optional[Literal["accurate", "fast", "disabled"]] = None
    """
    In a spreadsheet with different tables inside, we enable splitting up the tables
    by default. Accurate mode applies more powerful models for superior accuracy, at
    5× the default per-cell rate. Disabling will register as one large table.
    """

    exclude: Optional[List[Literal["hidden_sheets", "hidden_rows", "hidden_cols", "styling", "spreadsheet_images"]]] = (
        None
    )
    """Whether to exclude hidden sheets, rows, or columns in the output."""

    include: Optional[List[Literal["cell_colors", "formula"]]] = None
    """Whether to include cell color and formula information in the output."""

    split_large_tables: Optional[SplitLargeTables] = None
