# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["ParseUsage"]


class ParseUsage(BaseModel):
    num_pages: int

    credit_breakdown: Optional[Dict[str, float]] = None

    credits: Optional[float] = None

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
                ]
            ],
        ]
    ] = None
    """Per-page breakdown of features used.

    Maps 1-indexed page numbers (as strings) to the list of billing features applied
    on that page (e.g. 'page', 'complex', 'chart_agent').
    """
