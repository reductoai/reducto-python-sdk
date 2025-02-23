# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, TypedDict

__all__ = ["ArrayExtractConfig"]


class ArrayExtractConfig(TypedDict, total=False):
    enabled: bool
    """
    Array extraction allows you to extract long lists of information from lengthy
    documents. It makes parallel calls on overlapping sections of the document.
    """

    mode: Literal["auto", "legacy", "streaming", "no_overlap"]
    """The array extraction version to use."""

    pages_per_segment: int
    """Length of each segment, in pages, for parallel calls with array extraction."""

    streaming_extract_item_density: int
    """Number of items to extract in each stream call.

    Lower numbers will increase quality but be much slower. 50 works well for most
    documents with tables.
    """
