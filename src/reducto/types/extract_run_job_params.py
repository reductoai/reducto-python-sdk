# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union, Iterable, Optional
from typing_extensions import Literal, Required, Annotated, TypeAlias, TypedDict

from .._types import SequenceNotStr
from .._utils import PropertyInfo
from .shared_params.upload import Upload
from .shared_params.page_range import PageRange
from .shared_params.webhook_config_new import WebhookConfigNew
from .shared_params.array_extract_config import ArrayExtractConfig
from .shared_params.base_processing_options import BaseProcessingOptions
from .shared_params.advanced_citations_config import AdvancedCitationsConfig
from .shared_params.advanced_processing_options import AdvancedProcessingOptions
from .shared_params.experimental_processing_options import ExperimentalProcessingOptions

__all__ = [
    "ExtractRunJobParams",
    "AsyncExtractConfigNew",
    "AsyncExtractConfigNewDocumentURL",
    "AsyncExtractConfigNewAgentExtract",
    "AsyncExtractConfig",
    "AsyncExtractConfigInput",
    "AsyncExtractConfigAsync",
    "AsyncExtractConfigAsyncWebhook",
    "AsyncExtractConfigAsyncWebhookSvixWebhookConfig",
    "AsyncExtractConfigAsyncWebhookDirectWebhookConfig",
    "AsyncExtractConfigInstructions",
    "AsyncExtractConfigParsing",
    "AsyncExtractConfigParsingEnhance",
    "AsyncExtractConfigParsingEnhanceAgentic",
    "AsyncExtractConfigParsingEnhanceAgenticTableAgentic",
    "AsyncExtractConfigParsingEnhanceAgenticFigureAgentic",
    "AsyncExtractConfigParsingEnhanceAgenticTextAgentic",
    "AsyncExtractConfigParsingFormatting",
    "AsyncExtractConfigParsingRetrieval",
    "AsyncExtractConfigParsingRetrievalChunking",
    "AsyncExtractConfigParsingSettings",
    "AsyncExtractConfigParsingSettingsPageRange",
    "AsyncExtractConfigParsingSpreadsheet",
    "AsyncExtractConfigParsingSpreadsheetSplitLargeTables",
    "AsyncExtractConfigSettings",
    "AsyncExtractConfigSettingsCitations",
]


class AsyncExtractConfigNew(TypedDict, total=False):
    document_url: Required[AsyncExtractConfigNewDocumentURL]
    """The URL of the document to be processed. You can provide one of the following:

    1. A publicly available URL
    2. A presigned S3 URL
    3. A reducto:// prefixed URL obtained from the /upload endpoint after directly
       uploading a document
    4. A job_id (jobid://) or a list of job_ids (jobid://) obtained from a previous
       /parse endpoint
    """

    schema: Required[object]
    """The JSON schema to use for extraction."""

    advanced_options: AdvancedProcessingOptions

    agent_extract: AsyncExtractConfigNewAgentExtract
    """The configuration options for agent extract"""

    array_extract: ArrayExtractConfig
    """The configuration options for array extract"""

    citations_options: AdvancedCitationsConfig
    """The configuration options for citations."""

    experimental_options: ExperimentalProcessingOptions

    experimental_table_citations: bool
    """If table citations should be generated for the extracted content."""

    generate_citations: bool
    """If citations should be generated for the extracted content."""

    include_images: bool
    """If images should be passed directly for extractions.

    Can only be enabled for documents with less than 10 pages. Defaults to False.
    """

    latency_sensitive: bool
    """If True, the job will be processed with lower latency and higher priority.

    Uses 2x the cost of a regular job. Defaults to False.
    """

    options: BaseProcessingOptions

    priority: bool
    """
    If True, attempts to process the job with priority if the user has priority
    processing budget available; by default, sync jobs are prioritized above async
    jobs.
    """

    spreadsheet_agent: bool
    """If spreadsheet agent should be used for extraction."""

    system_prompt: str
    """A system prompt to use for the extraction.

    This is a general prompt that is applied to the entire document before any other
    prompts.
    """

    use_chunking: bool
    """If chunking should be used for the extraction. Defaults to False."""

    webhook: WebhookConfigNew


AsyncExtractConfigNewDocumentURL: TypeAlias = Union[str, SequenceNotStr[str], Upload]


class AsyncExtractConfigNewAgentExtract(TypedDict, total=False):
    enabled: bool
    """If agent extraction should be used for extraction."""


class AsyncExtractConfig(TypedDict, total=False):
    input: Required[AsyncExtractConfigInput]
    """The URL of the document to be processed.

    You can provide one of the following: 1. A publicly available URL 2. A presigned
    S3 URL 3. A reducto:// prefixed URL obtained from the /upload endpoint after
    directly uploading a document 4. A jobid:// prefixed URL obtained from a
    previous /parse invocation
    """

    async_: Annotated[AsyncExtractConfigAsync, PropertyInfo(alias="async")]
    """The configuration options for asynchronous processing (default synchronous)."""

    instructions: AsyncExtractConfigInstructions
    """The instructions to use for the extraction."""

    parsing: AsyncExtractConfigParsing
    """The configuration options for parsing the document.

    If you are passing in a jobid:// URL for the file, then this configuration will
    be ignored.
    """

    settings: AsyncExtractConfigSettings
    """The settings to use for the extraction."""


AsyncExtractConfigInput: TypeAlias = Union[str, Upload]


class AsyncExtractConfigAsyncWebhookSvixWebhookConfig(TypedDict, total=False):
    channels: SequenceNotStr[str]
    """
    A list of Svix channels the message will be delivered down, omit to send to all
    channels.
    """

    mode: Literal["svix"]


class AsyncExtractConfigAsyncWebhookDirectWebhookConfig(TypedDict, total=False):
    url: Required[str]

    mode: Literal["direct"]


AsyncExtractConfigAsyncWebhook: TypeAlias = Union[
    AsyncExtractConfigAsyncWebhookSvixWebhookConfig, AsyncExtractConfigAsyncWebhookDirectWebhookConfig
]


class AsyncExtractConfigAsync(TypedDict, total=False):
    metadata: object
    """JSON metadata included in webhook request body. Defaults to None."""

    priority: bool
    """
    If True, attempts to process the job with priority if the user has priority
    processing budget available; by default, sync jobs are prioritized above async
    jobs.
    """

    webhook: Optional[AsyncExtractConfigAsyncWebhook]
    """The webhook configuration for the asynchronous processing."""


class AsyncExtractConfigInstructions(TypedDict, total=False):
    schema: object
    """The JSON schema to use for the extraction."""

    system_prompt: str
    """The system prompt to use for the extraction."""


class AsyncExtractConfigParsingEnhanceAgenticTableAgentic(TypedDict, total=False):
    scope: Required[Literal["table"]]

    prompt: Optional[str]
    """Custom prompt for table agentic."""


class AsyncExtractConfigParsingEnhanceAgenticFigureAgentic(TypedDict, total=False):
    scope: Required[Literal["figure"]]

    prompt: Optional[str]
    """Custom prompt for figure agentic."""


class AsyncExtractConfigParsingEnhanceAgenticTextAgentic(TypedDict, total=False):
    scope: Required[Literal["text"]]


AsyncExtractConfigParsingEnhanceAgentic: TypeAlias = Union[
    AsyncExtractConfigParsingEnhanceAgenticTableAgentic,
    AsyncExtractConfigParsingEnhanceAgenticFigureAgentic,
    AsyncExtractConfigParsingEnhanceAgenticTextAgentic,
]


class AsyncExtractConfigParsingEnhance(TypedDict, total=False):
    agentic: Iterable[AsyncExtractConfigParsingEnhanceAgentic]
    """
    Agentic uses vision language models to enhance the accuracy of the output of
    different types of extraction. This will incur a cost and latency increase.
    """

    summarize_figures: bool
    """If True, summarize figures using a small vision language model.

    Defaults to True.
    """


class AsyncExtractConfigParsingFormatting(TypedDict, total=False):
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


class AsyncExtractConfigParsingRetrievalChunking(TypedDict, total=False):
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


class AsyncExtractConfigParsingRetrieval(TypedDict, total=False):
    chunking: AsyncExtractConfigParsingRetrievalChunking

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


AsyncExtractConfigParsingSettingsPageRange: TypeAlias = Union[PageRange, Iterable[PageRange], Iterable[int]]


class AsyncExtractConfigParsingSettings(TypedDict, total=False):
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

    page_range: Optional[AsyncExtractConfigParsingSettingsPageRange]
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


class AsyncExtractConfigParsingSpreadsheetSplitLargeTables(TypedDict, total=False):
    enabled: bool
    """If True, split large tables into smaller tables. Defaults to True."""

    size: int
    """The size of the tables to split into. Defaults to 50."""


class AsyncExtractConfigParsingSpreadsheet(TypedDict, total=False):
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

    split_large_tables: AsyncExtractConfigParsingSpreadsheetSplitLargeTables


class AsyncExtractConfigParsing(TypedDict, total=False):
    enhance: AsyncExtractConfigParsingEnhance

    formatting: AsyncExtractConfigParsingFormatting

    retrieval: AsyncExtractConfigParsingRetrieval

    settings: AsyncExtractConfigParsingSettings

    spreadsheet: AsyncExtractConfigParsingSpreadsheet


class AsyncExtractConfigSettingsCitations(TypedDict, total=False):
    enabled: bool
    """If True, include citations in the extraction."""

    numerical_confidence: bool
    """If True, enable numeric citation confidence scores. Defaults to True."""


class AsyncExtractConfigSettings(TypedDict, total=False):
    array_extract: bool
    """If True, use array extraction."""

    citations: AsyncExtractConfigSettingsCitations
    """The citations to use for the extraction."""

    include_images: bool
    """If True, include images in the extraction."""

    optimize_for_latency: bool
    """
    If True, jobs will be processed with a higher throughput and priority at a
    higher cost. Defaults to False.
    """


ExtractRunJobParams: TypeAlias = Union[AsyncExtractConfigNew, AsyncExtractConfig]
