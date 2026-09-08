from typing import Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["ExtractUsage", "UsageBreakdown"]


class UsageBreakdown(BaseModel):
    extract_model: Literal["Extract", "Deep Extract"]

    charts: Optional[int] = None

    extract_fields: Optional[int] = None

    extract_pages: Optional[int] = None

    ocr_pages: Optional[int] = None

    prompted_blocks: Optional[int] = None

    tier: Optional[Literal["Default", "Batch"]] = None


class ExtractUsage(BaseModel):
    num_fields: int

    num_pages: int

    credits: Optional[float] = None

    extract_mode: Optional[Literal["super_agent", "extract", "spreadsheet_agent"]] = None

    usage_breakdown: Optional[UsageBreakdown] = None
    """Raw usage quantities.

    Only set for accounts on the new pricing model; credit fields are omitted for
    those accounts.
    """
