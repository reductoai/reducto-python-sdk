# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["TableSummaryConfig"]


class TableSummaryConfig(TypedDict, total=False):
    enabled: bool
    """If table summarization should be performed."""

    prompt: str
    """Add information to the prompt for table summarization."""
