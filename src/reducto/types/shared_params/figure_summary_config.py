# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["FigureSummaryConfig"]


class FigureSummaryConfig(TypedDict, total=False):
    enabled: bool
    """If figure summarization should be performed."""

    override: bool
    """If the figure summary prompt should override our default prompt."""

    prompt: str
    """Add information to the prompt for figure summarization.

    Note any visual cues that should be incorporated. Example: 'When provided a
    diagram, extract all of the figure content verbatim.'
    """
