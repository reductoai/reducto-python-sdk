# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["FigureAgentic"]


class FigureAgentic(BaseModel):
    scope: Literal["figure"]

    prompt: Optional[str] = None
    """Custom prompt for figure agentic."""
