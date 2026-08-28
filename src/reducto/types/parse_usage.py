# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Union, Optional
from typing_extensions import Literal, TypeAlias

from .._models import BaseModel

__all__ = [
    "ParseUsage",
    "UsageBreakdown",
    "UsageBreakdownParseUsageBreakdown",
    "UsageBreakdownSplitUsageBreakdown",
    "UsageBreakdownEditUsageBreakdown",
]


class UsageBreakdownParseUsageBreakdown(BaseModel):
    """Raw parse quantities for accounts on the new (Q3 2026) pricing model.

    ``parse_model`` is "R-1" for the new parse model and "Legacy" for the
    legacy parse pipeline. A legacy-pipeline parse carries its cost in
    ``legacy_parse_credits``; add-on quantities (``ocr_pages``, ``charts``,
    ``prompted_blocks``) apply to the new parse model only.
    """

    parse_model: Literal["R-1", "Legacy"]

    tier: Literal["Default", "Batch"]

    charts: Optional[int] = None

    legacy_parse_credits: Optional[float] = None

    ocr_pages: Optional[int] = None

    parse_native_pages: Optional[int] = None

    parse_pages: Optional[int] = None

    prompted_blocks: Optional[int] = None


class UsageBreakdownSplitUsageBreakdown(BaseModel):
    """Raw split quantities for accounts on the new pricing model.

    The add-on quantities (``ocr_pages``, ``charts``, ``prompted_blocks``)
    come from the parse bundled into the split job; its page cost is covered
    by ``split_pages`` but its add-ons are billed separately.
    """

    split_model: Literal["Split", "Deep Split"]

    charts: Optional[int] = None

    ocr_pages: Optional[int] = None

    prompted_blocks: Optional[int] = None

    split_pages: Optional[int] = None


class UsageBreakdownEditUsageBreakdown(BaseModel):
    """Raw edit quantities for accounts on the new pricing model.

    ``edit_pages`` is the page count billed at the ``edit_model`` rate. A job
    with both normal and prefilled pages reports ``edit_model="Normal"`` with
    the prefilled pages in ``prefill_pages``, billed at the "Prefill" rate.
    """

    edit_model: Literal["Normal", "Prefill"]

    edit_pages: Optional[int] = None

    prefill_pages: Optional[int] = None


UsageBreakdown: TypeAlias = Union[
    UsageBreakdownParseUsageBreakdown, UsageBreakdownSplitUsageBreakdown, UsageBreakdownEditUsageBreakdown, None
]


class ParseUsage(BaseModel):
    num_pages: int

    credit_breakdown: Optional[Dict[str, float]] = None

    credits: Optional[float] = None

    non_empty_cell_count: Optional[int] = None
    """Total non-empty cells across all sheets. Only set for spreadsheet inputs."""

    page_billing_breakdown: Optional[
        Dict[
            str,
            List[
                Literal[
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
            ],
        ]
    ] = None
    """Per-page breakdown of features used.

    Maps 1-indexed page numbers (as strings) to the list of billing features applied
    on that page (e.g. 'page', 'complex', 'chart_agent').
    """

    usage_breakdown: Optional[UsageBreakdown] = None
    """Raw usage quantities.

    Only set for accounts on the new pricing model; credit fields are omitted for
    those accounts.
    """
