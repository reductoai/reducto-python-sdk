# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["TableAgentic"]


class TableAgentic(BaseModel):
    scope: Literal["table"]

    prompt: Optional[str] = None
    """Custom prompt for table agentic."""
