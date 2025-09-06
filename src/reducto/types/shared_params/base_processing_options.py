# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import Literal, TypedDict

__all__ = ["BaseProcessingOptions", "Chunking", "FigureSummary", "TableSummary"]


class Chunking(TypedDict, total=False):
    chunk_mode: Literal["variable", "section", "page", "block", "disabled", "page_sections"]
    """Choose how to partition chunks.

    Variable mode chunks by character length and visual context. Section mode chunks
    by section headers. Page mode chunks according to pages. Page sections mode
    chunks first by page, then by sections within each page. Disabled returns one
    single chunk.
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
    """Add information to the prompt for figure summarization.

    Note any visual cues that should be incorporated. Example: 'When provided a
    diagram, extract all of the figure content verbatim.'
    """


class TableSummary(TypedDict, total=False):
    enabled: bool
    """If table summarization should be performed."""

    prompt: str
    """Add information to the prompt for table summarization."""


class BaseProcessingOptions(TypedDict, total=False):
    chunking: Chunking
    """The configuration options for chunking.

    Chunking is commonly used for RAG usecases.
    """

    extraction_mode: Literal["ocr", "metadata", "hybrid"]
    """The mode to use for extraction.

    Metadata/hybrid are only recommended with high quality metadata embeddings.
    """

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
            "Signature",
        ]
    ]
    """A list of block types to filter from chunk content.

    Pass blocks to filter them from content. By default, no blocks are filtered.
    """

    force_url_result: bool
    """
    Force the result to be returned in URL form (by default only used for very large
    responses).
    """

    ocr_mode: Literal["standard", "agentic"]
    """The mode to use for OCR.

    Agentic mode adds an extra pass, correcting any table/text mistakes at a small
    cost.
    """

    table_summary: TableSummary
    """The configuration options for table summarization."""
