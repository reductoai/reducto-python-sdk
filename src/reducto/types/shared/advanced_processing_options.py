# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union, Optional
from typing_extensions import Literal, TypeAlias

from . import page_range
from ..._models import BaseModel

__all__ = ["AdvancedProcessingOptions", "LargeTableChunking", "PageRange"]


class LargeTableChunking(BaseModel):
    enabled: Optional[bool] = None
    """
    If large tables should be chunked into smaller tables, currently only supported
    on spreadsheet and CSV files.
    """

    size: Optional[int] = None
    """The max row/column size for a table to be chunked.

    Defaults to 50. Header rows/columns are persisted based on heuristics.
    """


PageRange: TypeAlias = Union[page_range.PageRange, List[page_range.PageRange]]


class AdvancedProcessingOptions(BaseModel):
    add_page_markers: Optional[bool] = None
    """If True, add page markers to the output (e.g.

    [[PAGE 1 BEGINS HERE]] and [[PAGE 1 ENDS HERE]] added as blocks to the content).
    Defaults to False.
    """

    continue_hierarchy: Optional[bool] = None
    """
    A flag to indicate if the hierarchy of the document should be continued from
    chunk to chunk.
    """

    document_password: Optional[str] = None
    """Password to decrypt password-protected documents."""

    force_file_extension: Optional[str] = None
    """Force the URL to be downloaded as a specific file extension (e.g. .png)."""

    keep_line_breaks: Optional[bool] = None
    """If line breaks should be preserved in the text."""

    large_table_chunking: Optional[LargeTableChunking] = None
    """
    The configuration options for large table chunking (currently only supported on
    spreadsheet and CSV files).
    """

    merge_tables: Optional[bool] = None
    """
    A flag to indicate if consecutive tables with the same number of columns should
    be merged.
    """

    ocr_system: Optional[Literal["highres", "multilingual", "combined"]] = None
    """The OCR system to use.

    Highres is recommended for documents with English characters.
    """

    page_range: Optional[PageRange] = None
    """The page range to process. By default, the entire document is processed."""

    remove_text_formatting: Optional[bool] = None
    """If True, remove text formatting from the output (e.g.

    hyphens for list items). Defaults to False.
    """

    return_ocr_data: Optional[bool] = None
    """If True, return OCR data in the result. Defaults to False."""

    spreadsheet_table_clustering: Optional[Literal["default", "disabled"]] = None
    """
    On a spreadsheet, the algorithm that is used to split up sheets into multiple
    tables.
    """

    table_output_format: Optional[Literal["html", "json", "md", "jsonbbox", "dynamic", "ai_json", "csv"]] = None
    """The mode to use for table output.

    Dynamic returns md for simpler tables and html for more complex tables.
    """
