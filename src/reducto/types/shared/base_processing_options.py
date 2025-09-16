# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["BaseProcessingOptions", "Chunking", "FigureSummary", "TableSummary"]


class Chunking(BaseModel):
    chunk_mode: Optional[Literal["variable", "section", "page", "block", "disabled", "page_sections"]] = None
    """Choose how to partition chunks.

    Variable mode chunks by character length and visual context. Section mode chunks
    by section headers. Page mode chunks according to pages. Page sections mode
    chunks first by page, then by sections within each page. Disabled returns one
    single chunk.
    """

    chunk_size: Optional[int] = None
    """
    The approximate size of chunks (in characters) that the document will be split
    into. Defaults to None, in which case the chunk size is variable between 250 -
    1500 characters.
    """


class FigureSummary(BaseModel):
    enabled: Optional[bool] = None
    """If figure summarization should be performed."""

    override: Optional[bool] = None
    """If the figure summary prompt should override our default prompt."""

    prompt: Optional[str] = None
    """Add information to the prompt for figure summarization.

    Note any visual cues that should be incorporated. Example: 'When provided a
    diagram, extract all of the figure content verbatim.'
    """


class TableSummary(BaseModel):
    enabled: Optional[bool] = None
    """If table summarization should be performed."""

    prompt: Optional[str] = None
    """Add information to the prompt for table summarization."""


class BaseProcessingOptions(BaseModel):
    chunking: Optional[Chunking] = None
    """The configuration options for chunking.

    Chunking is commonly used for RAG usecases.
    """

    extraction_mode: Optional[Literal["ocr", "metadata", "hybrid"]] = None
    """The mode to use for extraction.

    Metadata/hybrid are only recommended with high quality metadata embeddings.
    """

    figure_summary: Optional[FigureSummary] = None
    """The configuration options for figure summarization."""

    filter_blocks: Optional[
        List[
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
    ] = None
    """A list of block types to filter from chunk content.

    Pass blocks to filter them from content. By default, no blocks are filtered.
    """

    force_url_result: Optional[bool] = None
    """
    Force the result to be returned in URL form (by default only used for very large
    responses).
    """

    ocr_mode: Optional[Literal["standard", "agentic"]] = None
    """The mode to use for OCR.

    Agentic mode adds an extra pass, correcting any table/text mistakes at a small
    cost.
    """

    table_summary: Optional[TableSummary] = None
    """The configuration options for table summarization."""
