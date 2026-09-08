from typing import Dict, List, Union, Optional
from typing_extensions import Literal, TypeAlias

from .._models import BaseModel

__all__ = [
    "ParseUsage",
    "PageBillingFeature",
    "UsageBreakdown",
    "UsageBreakdownParseUsageBreakdown",
    "UsageBreakdownSplitUsageBreakdown",
    "UsageBreakdownEditUsageBreakdown",
]

PageBillingFeature: TypeAlias = Literal[
    "page",
    "html_page",
    "docx_native_page",
    "agentic",
    "complex",
    "chart_agent",
    "spreadsheet_cells",
    "billable_spreadsheet_pages",
    "enrich_table",
    "figure_summary",
    "table_summary",
    "key_value",
    "agentic_text",
    "promptable_agentic_text",
    "reducto_lite_page",
]


class UsageBreakdownParseUsageBreakdown(BaseModel):
    parse_model: Literal["R-1", "Legacy"]

    tier: Literal["Default", "Batch"]

    charts: Optional[int] = None

    legacy_parse_credits: Optional[float] = None

    ocr_pages: Optional[int] = None

    parse_native_pages: Optional[int] = None

    parse_pages: Optional[int] = None

    prompted_blocks: Optional[int] = None


class UsageBreakdownSplitUsageBreakdown(BaseModel):
    split_model: Literal["Split", "Deep Split"]

    charts: Optional[int] = None

    ocr_pages: Optional[int] = None

    prompted_blocks: Optional[int] = None

    split_pages: Optional[int] = None


class UsageBreakdownEditUsageBreakdown(BaseModel):
    edit_model: Literal["Normal", "Prefill"]

    edit_pages: Optional[int] = None

    prefill_pages: Optional[int] = None


UsageBreakdown: TypeAlias = Union[
    UsageBreakdownParseUsageBreakdown, UsageBreakdownSplitUsageBreakdown, UsageBreakdownEditUsageBreakdown
]


class ParseUsage(BaseModel):
    num_pages: int

    credit_breakdown: Optional[Dict[str, float]] = None

    credits: Optional[float] = None

    non_empty_cell_count: Optional[int] = None
    """Total non-empty cells across all sheets. Only set for spreadsheet inputs."""

    page_billing_breakdown: Optional[Dict[str, List[PageBillingFeature]]] = None
    """Per-page breakdown of features used.

    Maps 1-indexed page numbers (as strings) to the list of billing features applied
    on that page (e.g. 'page', 'complex', 'chart_agent').
    """

    usage_breakdown: Optional[UsageBreakdown] = None
    """Raw usage quantities.

    Only set for accounts on the new pricing model; credit fields are omitted for
    those accounts.
    """
