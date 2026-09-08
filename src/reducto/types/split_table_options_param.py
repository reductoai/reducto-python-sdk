from __future__ import annotations

from typing_extensions import Literal, TypedDict

__all__ = ["SplitTableOptionsParam"]


class SplitTableOptionsParam(TypedDict, total=False):
    allow_page_overlap: bool
    """If True, a page can belong to multiple categories/partitions.

    If False, each page must belong to exactly one category. Defaults to True.
    """

    auto_partition: bool
    """
    If True (default), deep split may split a category into partitions even when
    that category has no configured partition_key. If False, categories without a
    partition_key are never partitioned, so partitioning happens only where you
    explicitly configured a partition_key.
    """

    deep_split: bool
    """If True, uses the deep split agent for higher-quality document splitting.

    Off by default.
    """

    force_url_result: bool
    """Force the endpoint result to be returned in URL form."""

    table_cutoff: Literal["truncate", "preserve"]
    """
    If tables should be truncated to the first few rows or if all content should be
    preserved. truncate improves latency, preserve is recommended for cases where
    partition_key is being used and the partition_key may be included within the
    table. Defaults to truncate
    """
