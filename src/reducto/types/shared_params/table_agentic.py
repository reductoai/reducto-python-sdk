# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal, Required, TypedDict

__all__ = ["TableAgentic"]


class TableAgentic(TypedDict, total=False):
    scope: Required[Literal["table"]]

    mode: Literal["default", "auto"]
    """
    Routing mode for table agentic: 'default' runs enrichment on all tables, 'auto'
    uses the router to skip tables where enrichment is unlikely to help.
    """

    prompt: Optional[str]
    """Custom prompt for table agentic."""
