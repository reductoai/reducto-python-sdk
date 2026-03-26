# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Union, Optional
from typing_extensions import TypeAlias

from ..._models import BaseModel

__all__ = ["SplitLargeTables", "Size", "SizeSplitLargeTableSizes"]


class SizeSplitLargeTableSizes(BaseModel):
    column: Optional[int] = None
    """The number of columns to include in each chunk when splitting large tables.

    Does not chunk columns if set to None.
    """

    row: Optional[int] = None
    """The number of rows to include in each chunk when splitting large tables.

    Does not chunk rows if set to None.
    """


Size: TypeAlias = Union[int, SizeSplitLargeTableSizes]


class SplitLargeTables(BaseModel):
    enabled: Optional[bool] = None
    """If True, split large tables into smaller tables. Defaults to True."""

    size: Optional[Size] = None
    """The size of the tables to split into.

    Defaults to 50. Use 'row' and 'column' to independently specify the number of
    rows and columns to include when splitting. If you only want to split by rows or
    columns, set the other value to None.
    """
