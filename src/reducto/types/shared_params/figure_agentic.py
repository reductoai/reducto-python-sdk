# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal, Required, TypedDict

__all__ = ["FigureAgentic"]


class FigureAgentic(TypedDict, total=False):
    scope: Required[Literal["figure"]]

    advanced_chart_agent: bool
    """If True, use the advanced chart agent. Defaults to False."""

    prompt: Optional[str]
    """Custom prompt for figure agentic."""

    return_overlays: bool
    """If True, return overlays for the figure.

    This is so you can use the overlays to double check the quality of the
    extraction
    """
