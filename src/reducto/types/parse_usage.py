# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, Optional

from .._models import BaseModel

__all__ = ["ParseUsage"]


class ParseUsage(BaseModel):
    num_pages: int

    credit_breakdown: Optional[Dict[str, float]] = None

    credits: Optional[float] = None
