# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Iterable, Optional
from typing_extensions import Literal, Required, TypeAlias, TypedDict

__all__ = ["EnhanceParam", "Agentic", "AgenticTableAgentic", "AgenticFigureAgentic", "AgenticTextAgentic"]


class AgenticTableAgentic(TypedDict, total=False):
    scope: Required[Literal["table"]]

    prompt: Optional[str]
    """Custom prompt for table agentic."""


class AgenticFigureAgentic(TypedDict, total=False):
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


class AgenticTextAgentic(TypedDict, total=False):
    scope: Required[Literal["text"]]

    prompt: Optional[str]
    """Custom instructions for agentic text.

    Note: This only applies to form regions (key-value).
    """


Agentic: TypeAlias = Union[AgenticTableAgentic, AgenticFigureAgentic, AgenticTextAgentic]


class EnhanceParam(TypedDict, total=False):
    agentic: Iterable[Agentic]
    """
    Agentic uses vision language models to enhance the accuracy of the output of
    different types of extraction. This will incur a cost and latency increase.
    """

    intelligent_ordering: bool
    """
    If True, use an advanced vision language model to improve reading order
    accuracy, with a small increase in latency. Defaults to False.
    """

    summarize_figures: bool
    """If True, summarize figures using a small vision language model.

    Defaults to True.
    """
