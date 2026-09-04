# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["ExtractUsage", "UsageBreakdown"]


class UsageBreakdown(BaseModel):
    """Raw extract quantities for accounts on the new pricing model.

    ``extract_fields`` is reported but not billed at launch. The add-on
    quantities (``ocr_pages``, ``charts``, ``prompted_blocks``) come from the
    parse bundled into the extract job; its page cost is covered by
    ``extract_pages`` but its add-ons are billed separately. ``tier`` is
    "Batch" when the job ran on the batch queue, which takes the batch
    discount on the rate card.
    """

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
    """Raw extract quantities for accounts on the new pricing model.

    `extract_fields` is reported but not billed at launch. The add-on quantities
    (`ocr_pages`, `charts`, `prompted_blocks`) come from the parse bundled into the
    extract job; its page cost is covered by `extract_pages` but its add-ons are
    billed separately. `tier` is "Batch" when the job ran on the batch queue, which
    takes the batch discount on the rate card.
    """
