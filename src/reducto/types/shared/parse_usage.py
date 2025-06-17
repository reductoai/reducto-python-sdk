# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel

__all__ = ["ParseUsage"]


class ParseUsage(BaseModel):
    num_pages: int

    credits: Optional[float] = None
