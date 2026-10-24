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
