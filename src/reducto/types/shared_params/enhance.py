# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Iterable
from typing_extensions import TypeAlias, TypedDict

from .text_agentic import TextAgentic
from .table_agentic import TableAgentic
from .figure_agentic import FigureAgentic

__all__ = ["Enhance", "Agentic"]

Agentic: TypeAlias = Union[TableAgentic, FigureAgentic, TextAgentic]


class Enhance(TypedDict, total=False):
    agentic: Iterable[Agentic]
    """
    Agentic uses vision language models to enhance the accuracy of the output of
    different types of extraction. This will incur a cost and latency increase.
    """

    summarize_figures: bool
    """If True, summarize figures using a small vision language model.

    Defaults to True.
    """
