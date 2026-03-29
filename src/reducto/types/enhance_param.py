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
