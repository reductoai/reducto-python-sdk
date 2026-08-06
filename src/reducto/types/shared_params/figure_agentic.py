# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal, Required, TypedDict

__all__ = ["FigureAgentic"]


class FigureAgentic(TypedDict, total=False):
    scope: Required[Literal["figure"]]

    advanced_chart_agent: bool
    """
    If True, run advanced chart extraction on figures classified as charts: an
    agentic extractor that returns full structured series data (chart_data) plus a
    reconstruction image re-drawn from that data (extra.chart_reconstruction).
    Higher latency. Defaults to False.
    """

    prompt: Optional[str]
    """Custom prompt for figure agentic."""

    return_overlays: bool
    """If True, return overlays for the figure.

    This is so you can use the overlays to double check the quality of the
    extraction
    """
