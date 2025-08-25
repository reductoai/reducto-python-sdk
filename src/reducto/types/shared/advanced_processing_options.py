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


PageRange: TypeAlias = Union[page_range.PageRange, List[page_range.PageRange], List[int]]


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

    enable_change_tracking: Optional[bool] = None
    """
    Enables model-based detection of underlines and strikethroughs, adding <u>/<s>
    tags to OCR text. Works with any extraction mode. Defaults to False.
    """

    exclude_hidden_rows_cols: Optional[bool] = None
    """Skip hidden rows and cols in Excel files. Defaults to False."""

    exclude_hidden_sheets: Optional[bool] = None
    """Skip hidden sheets in Excel files. Defaults to False."""

    filter_line_numbers: Optional[bool] = None
    """If True, filter out line numbers from the output. Defaults to False."""

    force_file_extension: Optional[str] = None
    """Force the URL to be downloaded as a specific file extension (e.g. .png)."""

    include_color_information: Optional[bool] = None
    """
    If True, preserve Excel cell colours in the extracted spreadsheet text using
    LaTeX colour commands.
    """

    include_formula_information: Optional[bool] = None
    """
    If True, preserve formula information in spreadsheet cells by wrapping text with
    LaTeX formula commands during parsing.
    """

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
    be merged across breaks and spaces.
    """

    ocr_system: Optional[Literal["highres", "multilingual", "combined", "legacy"]] = None
    """The OCR system to use.

    Highres is recommended for documents with English characters. Legacy uses an
    alternative OCR backend.
    """

    page_range: Optional[PageRange] = None
    """The page range to process (1-indexed).

    By default, the entire document is processed.
    """

    persist_results: Optional[bool] = None
    """If True, persist the results indefinitely. Defaults to False."""

    read_comments: Optional[bool] = None
    """If True, pull in PDF comments from the document. Defaults to False."""

    remove_text_formatting: Optional[bool] = None
    """If True, remove text formatting from the output (e.g.

    hyphens for list items). Defaults to False.
    """

    return_ocr_data: Optional[bool] = None
    """If True, return OCR data in the result. Defaults to False."""

    spreadsheet_table_clustering: Optional[Literal["default", "disabled", "intelligent"]] = None
    """
    In a spreadsheet with different tables inside, we enable splitting up the tables
    by default. Intelligent mode applies more powerful models for superior accuracy,
    at 5× the default per-cell rate. Disabling will register as one large table.
    """

    table_output_format: Optional[Literal["html", "json", "md", "jsonbbox", "dynamic", "ai_json", "csv"]] = None
    """The mode to use for table output.

    Dynamic returns md for simpler tables and html for more complex tables.
    """
