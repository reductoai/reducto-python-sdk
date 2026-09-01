# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Iterable
from typing_extensions import TypeAlias, TypedDict

from .shared_params.text_agentic import TextAgentic
from .shared_params.table_agentic import TableAgentic
from .shared_params.figure_agentic import FigureAgentic

__all__ = ["EnhanceParam", "Agentic"]

Agentic: TypeAlias = Union[TableAgentic, FigureAgentic, TextAgentic]


class EnhanceParam(TypedDict, total=False):
    advanced_chart_agent: bool
    """
    If True, run advanced chart extraction on figures classified as charts, without
    requiring a figure-scoped agentic entry. Returns full structured series data
    (chart_data) plus a reconstruction image re-drawn from that data. Higher
    latency. Defaults to False.
    """

    agentic: Iterable[Agentic]
    """
    For legacy Parse, agentic processing uses vision language models to improve
    text, table, or figure extraction. With r-1, use agentic processing for custom
    prompts or advanced chart extraction. Agentic processing adds latency.
    """

    intelligent_ordering: bool
    """
    For legacy Parse, if True, use an advanced vision language model to improve
    reading order accuracy, with a small increase in latency. r-1 handles reading
    order natively and ignores this setting. Defaults to False.
    """

    summarize_figures: bool
    """
    For legacy Parse, if True, summarize figures using a separate vision language
    model. r-1 generates figure descriptions natively and ignores this setting.
    Defaults to True.
    """
