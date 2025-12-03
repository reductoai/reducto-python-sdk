# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel

__all__ = ["FigureSummaryConfig"]


class FigureSummaryConfig(BaseModel):
    advanced_chart_agent: Optional[bool] = None
    """If True, use the advanced chart agent. Defaults to False."""

    enabled: Optional[bool] = None
    """If figure summarization should be performed."""

    override: Optional[bool] = None
    """If the figure summary prompt should override our default prompt."""

    prompt: Optional[str] = None
    """Add information to the prompt for figure summarization.

    Note any visual cues that should be incorporated. Example: 'When provided a
    diagram, extract all of the figure content verbatim.'
    """
