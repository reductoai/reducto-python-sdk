# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from ..._models import BaseModel
from .chunking_config import ChunkingConfig
from .table_summary_config import TableSummaryConfig
from .figure_summary_config import FigureSummaryConfig

__all__ = ["BaseProcessingOptions"]


class BaseProcessingOptions(BaseModel):
    chunking: Optional[ChunkingConfig] = None
    """The configuration options for chunking.

    Chunking is commonly used for RAG usecases.
    """

    extraction_mode: Optional[Literal["ocr", "metadata", "hybrid"]] = None
    """The mode to use for extraction.

    Metadata/hybrid are only recommended with high quality metadata embeddings.
    """

    figure_summary: Optional[FigureSummaryConfig] = None
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

    table_summary: Optional[TableSummaryConfig] = None
    """The configuration options for table summarization."""
