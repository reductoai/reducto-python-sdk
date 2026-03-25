# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel

__all__ = ["TableSummaryConfig"]


class TableSummaryConfig(BaseModel):
    enabled: Optional[bool] = None
    """If table summarization should be performed."""

    prompt: Optional[str] = None
    """Add information to the prompt for table summarization."""
