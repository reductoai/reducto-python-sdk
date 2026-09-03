# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["TableAgentic"]


class TableAgentic(BaseModel):
    scope: Literal["table"]

    mode: Optional[Literal["default", "auto", "max"]] = None
    """
    Mode for table agentic: 'default' selectively applies enrichment only to tables
    likely to benefit, and 'max' runs enrichment on all tables.
    """

    prompt: Optional[str] = None
    """Custom prompt for table agentic."""
