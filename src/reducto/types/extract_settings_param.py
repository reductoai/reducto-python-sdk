# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["ExtractSettingsParam", "Citations"]


class Citations(TypedDict, total=False):
    """The citations to use for the extraction."""

    enabled: bool
    """If True, include citations in the extraction."""

    numerical_confidence: bool
    """If True, enable numeric citation confidence scores. Defaults to True."""


class ExtractSettingsParam(TypedDict, total=False):
    array_extract: bool
    """If True, use array extraction."""

    citations: Citations
    """The citations to use for the extraction."""

    include_images: bool
    """If True, include images in the extraction."""

    optimize_for_latency: bool
    """
    If True, jobs will be processed with a higher throughput and priority at a
    higher cost. Defaults to False.
    """
