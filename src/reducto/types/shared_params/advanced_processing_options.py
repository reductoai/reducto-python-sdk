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


PageRange: TypeAlias = Union[page_range.PageRange, Iterable[page_range.PageRange]]


class AdvancedProcessingOptions(TypedDict, total=False):
    add_page_markers: bool
    """If True, add page markers to the output (e.g.

    [[PAGE 1 BEGINS HERE]] and [[PAGE 1 ENDS HERE]] added as blocks to the content).
    Defaults to False.
    """

    bucket_name: str
    """The name of the bucket to use for the document."""

    continue_hierarchy: bool
    """
    A flag to indicate if the hierarchy of the document should be continued from
    chunk to chunk.
    """

    document_password: str
    """Password to decrypt password-protected documents."""

    force_file_extension: str
    """Force the URL to be downloaded as a specific file extension (e.g. .png)."""

    keep_line_breaks: bool
    """If line breaks should be preserved in the text."""

    kms_arn: str
    """The AWS KMS key to use for the document."""

    large_table_chunking: LargeTableChunking
    """
    The configuration options for large table chunking (currently only supported on
    spreadsheet and CSV files).
    """

    merge_tables: bool
    """
    A flag to indicate if consecutive tables with the same number of columns should
    be merged.
    """

    ocr_system: Literal["highres", "multilingual", "combined"]
    """The OCR system to use.

    Highres is recommended for documents with English characters.
    """

    page_range: PageRange
    """The page range to process. By default, the entire document is processed."""

    remove_text_formatting: bool
    """If True, remove text formatting from the output (e.g.

    hyphens for list items). Defaults to False.
    """

    return_ocr_data: bool
    """If True, return OCR data in the result. Defaults to False."""

    spreadsheet_table_clustering: Literal["default", "disabled"]
    """
    On a spreadsheet, the algorithm that is used to split up sheets into multiple
    tables.
    """

    table_output_format: Literal["html", "json", "md", "jsonbbox", "dynamic", "ai_json"]
    """The mode to use for table output.

    Dynamic returns md for simpler tables and html for more complex tables.
    """
