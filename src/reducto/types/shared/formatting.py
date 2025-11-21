# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["Formatting"]


class Formatting(BaseModel):
    add_page_markers: Optional[bool] = None
    """If True, add page markers to the output.

    Defaults to False. Useful for extracting data with page specific information.
    """

    include: Optional[List[Literal["change_tracking", "highlight", "comments", "hyperlinks", "signatures"]]] = None
    """A list of formatting to include in the output."""

    merge_tables: Optional[bool] = None
    """
    A flag to indicate if consecutive tables with the same number of columns should
    be merged. Defaults to False.
    """

    table_output_format: Optional[Literal["html", "json", "md", "jsonbbox", "dynamic", "csv"]] = None
    """The mode to use for table output.

    Defaults to dynamic, which returns md for simpler tables and html for more
    complex tables.
    """
