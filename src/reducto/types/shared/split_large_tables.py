# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel

__all__ = ["SplitLargeTables"]


class SplitLargeTables(BaseModel):
    enabled: Optional[bool] = None
    """If True, split large tables into smaller tables. Defaults to True."""

    size: Optional[int] = None
    """The size of the tables to split into. Defaults to 50."""
