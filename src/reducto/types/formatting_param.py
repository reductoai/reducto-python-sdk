# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import Literal, TypedDict

__all__ = ["FormattingParam"]


class FormattingParam(TypedDict, total=False):
    add_page_markers: bool
    """If True, add page markers to the output.

    Defaults to False. Useful for extracting data with page specific information.
    """

    include: List[Literal["change_tracking", "highlight", "comments", "hyperlinks", "signatures", "ignore_watermarks"]]
    """For legacy Parse, the formatting details to include in the output.

    r-1 handles highlights, signatures, and watermarks natively and ignores those
    values. r-1 does not support hyperlinks.
    """

    merge_tables: bool
    """
    A flag to indicate if consecutive tables with the same number of columns should
    be merged. Defaults to False.
    """

    table_output_format: Literal["html", "json", "md", "jsonbbox", "dynamic", "csv"]
    """The table output format.

    Defaults to dynamic, which returns md for simpler tables and html for more
    complex tables. r-1 does not support jsonbbox.
    """
