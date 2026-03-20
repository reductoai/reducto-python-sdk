# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["ExtractUsage"]


class ExtractUsage(BaseModel):
    num_fields: int

    num_pages: int

    credits: Optional[float] = None

    extract_mode: Optional[Literal["super_agent", "extract", "spreadsheet_agent"]] = None
