# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Iterable, Optional
from typing_extensions import Literal, TypeAlias, TypedDict

from .._types import SequenceNotStr
from .shared_params import page_range

__all__ = ["ExtractSettingsParam", "Citations", "PageRange"]


class Citations(TypedDict, total=False):
    """The citations to use for the extraction."""

    enabled: bool
    """If True, include citations in the extraction."""

    numerical_confidence: bool
    """If True, enable numeric citation confidence scores. Defaults to True."""

    parent_block: Literal["full", "bbox_only"]
    """How much of the source parse block to embed on each citation's parentBlock.

    'full' (default) embeds the verbatim source-block HTML in parentBlock.content.
    'bbox_only' suppresses parentBlock.content (returned as an empty string) while
    keeping parentBlock.bbox and all citation-level fields — this can drastically
    shrink responses on table-heavy schemas where the same source block is cited
    many times.
    """


PageRange: TypeAlias = Union[page_range.PageRange, Iterable[page_range.PageRange], Iterable[int], SequenceNotStr[str]]


class ExtractSettingsParam(TypedDict, total=False):
    array_extract: bool
    """If True, use array extraction."""

    citations: Citations
    """The citations to use for the extraction."""

    deep_extract: bool
    """
    If True, use Deep Extract, an agentic extraction mode that iteratively refines
    its output to achieve near-perfect accuracy. Best for complex documents where
    accuracy is critical.
    """

    force_url_result: bool
    """Force the endpoint result to be returned in URL form."""

    include_images: bool
    """If True, include images in the extraction."""

    optimize_for_latency: bool
    """
    If True, jobs will be processed with a higher throughput and priority at a
    higher cost. Defaults to False.
    """

    page_range: Optional[PageRange]
    """The page range to extract from (1-indexed).

    By default, the entire document is used. For spreadsheets, you can also provide
    a list of sheet names.
    """
