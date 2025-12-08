# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["FigureAgentic"]


class FigureAgentic(BaseModel):
    scope: Literal["figure"]

    advanced_chart_agent: Optional[bool] = None
    """If True, use the advanced chart agent. Defaults to False."""

    prompt: Optional[str] = None
    """Custom prompt for figure agentic."""

    return_overlays: Optional[bool] = None
    """If True, return overlays for the figure.

    This is so you can use the overlays to double check the quality of the
    extraction
    """
