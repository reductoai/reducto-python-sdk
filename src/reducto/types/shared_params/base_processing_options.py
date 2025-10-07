# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import Literal, TypedDict

from .chunking_config import ChunkingConfig
from .table_summary_config import TableSummaryConfig
from .figure_summary_config import FigureSummaryConfig

__all__ = ["BaseProcessingOptions"]


class BaseProcessingOptions(TypedDict, total=False):
    chunking: ChunkingConfig
    """The configuration options for chunking.

    Chunking is commonly used for RAG usecases.
    """

    extraction_mode: Literal["ocr", "metadata", "hybrid"]
    """The mode to use for extraction.

    Metadata/hybrid are only recommended with high quality metadata embeddings.
    """

    figure_summary: FigureSummaryConfig
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

    table_summary: TableSummaryConfig
    """The configuration options for table summarization."""
