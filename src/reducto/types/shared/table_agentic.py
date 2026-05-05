# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["TableAgentic"]


class TableAgentic(BaseModel):
    scope: Literal["table"]

    mode: Optional[Literal["default", "auto"]] = None
    """
    Routing mode for table agentic: 'default' runs enrichment on all tables, 'auto'
    uses the router to skip tables where enrichment is unlikely to help.
    """

    prompt: Optional[str] = None
    """Custom prompt for table agentic."""
