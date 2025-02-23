# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import Literal, TypedDict

__all__ = ["BaseProcessingOptions", "Chunking", "FigureSummary", "TableSummary"]


class Chunking(TypedDict, total=False):
    chunk_mode: Literal["variable", "section", "page", "block", "disabled"]
    """The mode to use for chunking.

    Section chunks according to sections in the document. Page chunks according to
    pages. Disabled returns a single chunk.
    """

    chunk_size: int
    """
    The approximate size of chunks (in characters) that the document will be split
    into. Defaults to None, in which case the chunk size is variable between 250 -
    1500 characters.
    """


class FigureSummary(TypedDict, total=False):
    enabled: bool
    """If figure summarization should be performed."""

    override: bool
    """If the figure summary prompt should override our default prompt."""

    prompt: str
    """Add information to the prompt for figure summarization."""


class TableSummary(TypedDict, total=False):
    enabled: bool
    """If table summarization should be performed."""

    prompt: str
    """Add information to the prompt for table summarization."""


class BaseProcessingOptions(TypedDict, total=False):
    chunking: Chunking
    """The configuration options for chunking."""

    extraction_mode: Literal["ocr", "metadata", "hybrid"]
    """The mode to use for extraction."""

    figure_summary: FigureSummary
    """The configuration options for figure summarization."""

    filter_blocks: List[
        Literal[
            "Header",
            "Footer",
            "Title",
            "Section Header",
            "Page Number",
            "List Item",
            "Figure",
            "Table",
            "Key Value",
            "Text",
            "Comment",
            "Discard",
        ]
    ]
    """A list of block types to filter from chunk content."""

    force_url_result: bool
    """
    Force the result to be returned in URL form (by default only used for very large
    responses).
    """

    table_summary: TableSummary
    """The configuration options for table summarization."""
