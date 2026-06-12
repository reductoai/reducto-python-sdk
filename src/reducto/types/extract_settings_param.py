# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, TypedDict

__all__ = ["ExtractSettingsParam", "Citations"]


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

    include_images: bool
    """If True, include images in the extraction."""

    optimize_for_latency: bool
    """
    If True, jobs will be processed with a higher throughput and priority at a
    higher cost. Defaults to False.
    """
