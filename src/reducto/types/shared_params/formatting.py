# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import Literal, TypedDict

__all__ = ["Formatting"]


class Formatting(TypedDict, total=False):
    add_page_markers: bool
    """If True, add page markers to the output.

    Defaults to False. Useful for extracting data with page specific information.
    """

    include: List[Literal["change_tracking", "highlight", "comments", "hyperlinks", "signatures"]]
    """A list of formatting to include in the output."""

    merge_tables: bool
    """
    A flag to indicate if consecutive tables with the same number of columns should
    be merged. Defaults to False.
    """

    table_output_format: Literal["html", "json", "md", "jsonbbox", "dynamic", "csv"]
    """The mode to use for table output.

    Defaults to dynamic, which returns md for simpler tables and html for more
    complex tables.
    """
