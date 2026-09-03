# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal, Required, TypedDict

__all__ = ["TableAgentic"]


class TableAgentic(TypedDict, total=False):
    scope: Required[Literal["table"]]

    mode: Literal["default", "auto", "max"]
    """
    Mode for table agentic: 'default' selectively applies enrichment only to tables
    likely to benefit, and 'max' runs enrichment on all tables.
    """

    prompt: Optional[str]
    """Custom prompt for table agentic."""
