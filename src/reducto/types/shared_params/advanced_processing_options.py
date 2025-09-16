# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Iterable
from typing_extensions import Literal, TypeAlias, TypedDict

from . import page_range

__all__ = ["AdvancedProcessingOptions", "LargeTableChunking", "PageRange"]


class LargeTableChunking(TypedDict, total=False):
    enabled: bool
    """
    If large tables should be chunked into smaller tables, currently only supported
    on spreadsheet and CSV files.
    """

    size: int
    """The max row/column size for a table to be chunked.

    Defaults to 50. Header rows/columns are persisted based on heuristics.
    """


PageRange: TypeAlias = Union[page_range.PageRange, Iterable[page_range.PageRange], Iterable[int]]


class AdvancedProcessingOptions(TypedDict, total=False):
    add_page_markers: bool
    """If True, add page markers to the output (e.g.

    [[PAGE 1 BEGINS HERE]] and [[PAGE 1 ENDS HERE]] added as blocks to the content).
    Defaults to False.
    """

    continue_hierarchy: bool
    """
    A flag to indicate if the hierarchy of the document should be continued from
    chunk to chunk.
    """

    document_password: str
    """Password to decrypt password-protected documents."""

    enable_change_tracking: bool
    """
    Enables model-based detection of underlines and strikethroughs, adding <u>/<s>
    tags to OCR text. Works with any extraction mode. Defaults to False.
    """

    enable_highlight_detection: bool
    """If True, enable highlight detection.

    Highlighted text will be surrounded by <mark> tags in the output. Defaults to
    False.
    """

    exclude_hidden_rows_cols: bool
    """Skip hidden rows and cols in Excel files. Defaults to False."""

    exclude_hidden_sheets: bool
    """Skip hidden sheets in Excel files. Defaults to False."""

    filter_line_numbers: bool
    """If True, filter out line numbers from the output. Defaults to False."""

    force_file_extension: str
    """Force the URL to be downloaded as a specific file extension (e.g. .png)."""

    include_color_information: bool
    """
    If True, preserve Excel cell colours in the extracted spreadsheet text using
    LaTeX colour commands.
    """

    include_formula_information: bool
    """
    If True, preserve formula information in spreadsheet cells by wrapping text with
    LaTeX formula commands during parsing.
    """

    keep_line_breaks: bool
    """If line breaks should be preserved in the text."""

    large_table_chunking: LargeTableChunking
    """
    The configuration options for large table chunking (currently only supported on
    spreadsheet and CSV files).
    """

    merge_tables: bool
    """
    A flag to indicate if consecutive tables with the same number of columns should
    be merged across breaks and spaces.
    """

    ocr_system: Literal["highres", "multilingual", "combined", "legacy"]
    """The OCR system to use.

    Highres is recommended for documents with English characters. Legacy uses an
    alternative OCR backend.
    """

    page_range: PageRange
    """The page range to process (1-indexed).

    By default, the entire document is processed.
    """

    persist_results: bool
    """If True, persist the results indefinitely. Defaults to False."""

    read_comments: bool
    """If True, pull in PDF comments from the document. Defaults to False."""

    remove_text_formatting: bool
    """If True, remove text formatting from the output (e.g.

    hyphens for list items). Defaults to False.
    """

    return_ocr_data: bool
    """If True, return OCR data in the result. Defaults to False."""

    spreadsheet_table_clustering: Literal["default", "disabled", "intelligent"]
    """
    In a spreadsheet with different tables inside, we enable splitting up the tables
    by default. Intelligent mode applies more powerful models for superior accuracy,
    at 5× the default per-cell rate. Disabling will register as one large table.
    """

    table_output_format: Literal["html", "json", "md", "jsonbbox", "dynamic", "ai_json", "csv"]
    """The mode to use for table output.

    Dynamic returns md for simpler tables and html for more complex tables.
    """
