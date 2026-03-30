# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, TypedDict

__all__ = ["SplitTableOptionsParam"]


class SplitTableOptionsParam(TypedDict, total=False):
    allow_page_overlap: bool
    """If True, a page can belong to multiple categories/partitions.

    If False, each page must belong to exactly one category. Defaults to True.
    """

    table_cutoff: Literal["truncate", "preserve"]
    """
    If tables should be truncated to the first few rows or if all content should be
    preserved. truncate improves latency, preserve is recommended for cases where
    partition_key is being used and the partition_key may be included within the
    table. Defaults to truncate
    """
