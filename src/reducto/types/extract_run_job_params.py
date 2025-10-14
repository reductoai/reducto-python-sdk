# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union, Iterable, Optional
from typing_extensions import Literal, Required, Annotated, TypeAlias, TypedDict

from .._types import SequenceNotStr
from .._utils import PropertyInfo
from .shared_params.upload import Upload
from .shared_params.page_range import PageRange

__all__ = [
    "ExtractRunJobParams",
    "Input",
    "Async",
    "AsyncWebhook",
    "AsyncWebhookSvixWebhookConfig",
    "AsyncWebhookDirectWebhookConfig",
    "Instructions",
    "Parsing",
    "ParsingEnhance",
    "ParsingEnhanceAgentic",
    "ParsingEnhanceAgenticTableAgentic",
    "ParsingEnhanceAgenticFigureAgentic",
    "ParsingEnhanceAgenticTextAgentic",
    "ParsingFormatting",
    "ParsingRetrieval",
    "ParsingRetrievalChunking",
    "ParsingSettings",
    "ParsingSettingsPageRange",
    "ParsingSpreadsheet",
    "ParsingSpreadsheetSplitLargeTables",
    "Settings",
    "SettingsCitations",
]


class ExtractRunJobParams(TypedDict, total=False):
    input: Required[Input]
    """The URL of the document to be processed.

    You can provide one of the following: 1. A publicly available URL 2. A presigned
    S3 URL 3. A reducto:// prefixed URL obtained from the /upload endpoint after
    directly uploading a document 4. A jobid:// prefixed URL obtained from a
    previous /parse invocation
    """

    async_: Annotated[Async, PropertyInfo(alias="async")]
    """The configuration options for asynchronous processing (default synchronous)."""

    instructions: Instructions
    """The instructions to use for the extraction."""

    parsing: Parsing
    """The configuration options for parsing the document.

    If you are passing in a jobid:// URL for the file, then this configuration will
    be ignored.
    """

    settings: Settings
    """The settings to use for the extraction."""


Input: TypeAlias = Union[str, Upload]


class AsyncWebhookSvixWebhookConfig(TypedDict, total=False):
    channels: SequenceNotStr[str]
    """
    A list of Svix channels the message will be delivered down, omit to send to all
    channels.
    """

    mode: Literal["svix"]


class AsyncWebhookDirectWebhookConfig(TypedDict, total=False):
    url: Required[str]

    mode: Literal["direct"]


AsyncWebhook: TypeAlias = Union[AsyncWebhookSvixWebhookConfig, AsyncWebhookDirectWebhookConfig]


class Async(TypedDict, total=False):
    metadata: object
    """JSON metadata included in webhook request body. Defaults to None."""

    priority: bool
    """
    If True, attempts to process the job with priority if the user has priority
    processing budget available; by default, sync jobs are prioritized above async
    jobs.
    """

    webhook: Optional[AsyncWebhook]
    """The webhook configuration for the asynchronous processing."""


class Instructions(TypedDict, total=False):
    schema: object
    """The JSON schema to use for the extraction."""

    system_prompt: str
    """The system prompt to use for the extraction."""


class ParsingEnhanceAgenticTableAgentic(TypedDict, total=False):
    scope: Required[Literal["table"]]

    prompt: Optional[str]
    """Custom prompt for table agentic."""


class ParsingEnhanceAgenticFigureAgentic(TypedDict, total=False):
    scope: Required[Literal["figure"]]

    prompt: Optional[str]
    """Custom prompt for figure agentic."""


class ParsingEnhanceAgenticTextAgentic(TypedDict, total=False):
    scope: Required[Literal["text"]]


ParsingEnhanceAgentic: TypeAlias = Union[
    ParsingEnhanceAgenticTableAgentic, ParsingEnhanceAgenticFigureAgentic, ParsingEnhanceAgenticTextAgentic
]


class ParsingEnhance(TypedDict, total=False):
    agentic: Iterable[ParsingEnhanceAgentic]
    """
    Agentic uses vision language models to enhance the accuracy of the output of
    different types of extraction. This will incur a cost and latency increase.
    """

    summarize_figures: bool
    """If True, summarize figures using a small vision language model.

    Defaults to True.
    """


class ParsingFormatting(TypedDict, total=False):
    add_page_markers: bool
    """If True, add page markers to the output.

    Defaults to False. Useful for extracting data with page specific information.
    """

    include: List[Literal["change_tracking", "highlight", "comments"]]
    """A list of formatting to include in the output.

    [insert description of each option here later]
    """

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


class ParsingRetrievalChunking(TypedDict, total=False):
    chunk_mode: Literal["variable", "section", "page", "disabled", "block", "page_sections"]
    """Choose how to partition chunks.

    Variable mode chunks by character length and visual context. Section mode chunks
    by section headers. Page mode chunks according to pages. Page sections mode
    chunks first by page, then by sections within each page. Disabled returns one
    single chunk.
    """

    chunk_size: Optional[int]
    """
    The approximate size of chunks (in characters) that the document will be split
    into. Defaults to null, in which case the chunk size is variable between 250 -
    1500 characters.
    """


class ParsingRetrieval(TypedDict, total=False):
    chunking: ParsingRetrievalChunking

    embedding_optimized: bool
    """If True, use embedding optimized mode. Defaults to False."""

    filter_blocks: List[
        Literal[
            "Header",
            "Footer",
            "Title",
            "Section Header",
            "Page Number",
            "List Item",
            "Figure",
            "Table",
            "Key Value",
            "Text",
            "Comment",
            "Signature",
        ]
    ]
    """A list of block types to filter out from 'content' and 'embed' fields.

    By default, no blocks are filtered.
    """


ParsingSettingsPageRange: TypeAlias = Union[PageRange, Iterable[PageRange], Iterable[int]]


class ParsingSettings(TypedDict, total=False):
    document_password: Optional[str]
    """Password to decrypt password-protected documents."""

    embed_pdf_metadata: bool
    """If True, embed OCR metadata into the returned PDF. Defaults to False."""

    force_file_extension: Optional[str]
    """Force the URL to be downloaded as a specific file extension (e.g. `.png`)."""

    force_url_result: bool
    """Force the result to be returned in URL form."""

    ocr_system: Literal["standard", "legacy"]
    """Standard is our best multilingual OCR system.

    Legacy only supports germanic languages and is available for backwards
    compatibility.
    """

    page_range: Optional[ParsingSettingsPageRange]
    """The page range to process (1-indexed).

    By default, the entire document is processed.
    """

    persist_results: bool
    """If True, persist the results indefinitely. Defaults to False."""

    return_images: List[Literal["figure", "table"]]
    """Whether to return images for the specified block types.

    By default, no images are returned.
    """

    return_ocr_data: bool
    """If True, return OCR data in the result. Defaults to False."""

    timeout: float
    """The timeout for the job in seconds. Defaults to 900."""


class ParsingSpreadsheetSplitLargeTables(TypedDict, total=False):
    enabled: bool
    """If True, split large tables into smaller tables. Defaults to True."""

    size: int
    """The size of the tables to split into. Defaults to 50."""


class ParsingSpreadsheet(TypedDict, total=False):
    clustering: Literal["accurate", "fast", "disabled"]
    """
    In a spreadsheet with different tables inside, we enable splitting up the tables
    by default. Accurate mode applies more powerful models for superior accuracy, at
    5× the default per-cell rate. Disabling will register as one large table.
    """

    exclude: List[Literal["hidden_sheets", "hidden_rows", "hidden_cols"]]
    """Whether to exclude hidden sheets, rows, or columns in the output."""

    include: List[Literal["cell_colors", "formula"]]
    """Whether to include cell color and formula information in the output."""

    split_large_tables: ParsingSpreadsheetSplitLargeTables


class Parsing(TypedDict, total=False):
    enhance: ParsingEnhance

    formatting: ParsingFormatting

    retrieval: ParsingRetrieval

    settings: ParsingSettings

    spreadsheet: ParsingSpreadsheet


class SettingsCitations(TypedDict, total=False):
    enabled: bool
    """If True, include citations in the extraction."""

    numerical_confidence: bool
    """If True, enable numeric citation confidence scores. Defaults to True."""


class Settings(TypedDict, total=False):
    array_extract: bool
    """If True, use array extraction."""

    citations: SettingsCitations
    """The citations to use for the extraction."""

    include_images: bool
    """If True, include images in the extraction."""

    optimize_for_latency: bool
    """
    If True, jobs will be processed with a higher throughput and priority at a
    higher cost. Defaults to False.
    """
