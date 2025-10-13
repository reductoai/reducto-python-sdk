# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, List, Union, Iterable, Optional
from typing_extensions import Literal, Required, Annotated, TypeAlias, TypedDict

from .._types import SequenceNotStr
from .._utils import PropertyInfo
from .shared_params.upload import Upload
from .shared_params.page_range import PageRange
from .shared_params.array_extract_config import ArrayExtractConfig
from .shared_params.base_processing_options import BaseProcessingOptions
from .shared_params.advanced_citations_config import AdvancedCitationsConfig
from .shared_params.advanced_processing_options import AdvancedProcessingOptions
from .shared_params.experimental_processing_options import ExperimentalProcessingOptions

__all__ = [
    "ExtractRunParams",
    "ExtractConfig",
    "ExtractConfigDocumentURL",
    "ExtractConfigAgentExtract",
    "ExtractConfigAsync",
    "ExtractConfigAsyncWebhook",
    "ExtractConfigOptions",
    "ExtractConfigParseConfig",
    "ExtractConfigParseConfigPageRange",
    "SyncExtractConfig",
    "SyncExtractConfigInput",
    "SyncExtractConfigInstructions",
    "SyncExtractConfigParsing",
    "SyncExtractConfigParsingEnhance",
    "SyncExtractConfigParsingEnhanceAgentic",
    "SyncExtractConfigParsingEnhanceAgenticTableAgentic",
    "SyncExtractConfigParsingEnhanceAgenticFigureAgentic",
    "SyncExtractConfigParsingEnhanceAgenticTextAgentic",
    "SyncExtractConfigParsingFormatting",
    "SyncExtractConfigParsingRetrieval",
    "SyncExtractConfigParsingRetrievalChunking",
    "SyncExtractConfigParsingSettings",
    "SyncExtractConfigParsingSettingsPageRange",
    "SyncExtractConfigParsingSpreadsheet",
    "SyncExtractConfigParsingSpreadsheetSplitLargeTables",
    "SyncExtractConfigSettings",
    "SyncExtractConfigSettingsCitations",
]


class ExtractConfig(TypedDict, total=False):
    document_url: Required[ExtractConfigDocumentURL]
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

    agent_extract: ExtractConfigAgentExtract
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


ExtractConfigDocumentURL: TypeAlias = Union[str, SequenceNotStr[str], Upload]


class ExtractConfigAgentExtract(TypedDict, total=False):
    enabled: bool
    """If agent extraction should be used for extraction."""


class ExtractConfig(TypedDict, total=False):
    document_url: Required[Union[str, SequenceNotStr[str]]]

    schema: Required[object]
    """The JSON schema to use for extraction."""

    agent_extract: bool
    """If agent extraction should be used for extraction."""

    alpha_big_extraction_model: bool

    alpha_deep_extract: bool

    alpha_table_citations: bool

    async_: Annotated[ExtractConfigAsync, PropertyInfo(alias="async")]
    """The configuration options for asynchronous processing (default synchronous)."""

    include_images: bool

    latency_sensitive: bool
    """If True, the job will be processed with lower latency and higher priority.

    Uses 2x the cost of a regular job. Defaults to False.
    """

    normalized_schema: object
    """The normalized JSON schema to use for extraction."""

    options: ExtractConfigOptions
    """The configuration options for extraction."""

    parse_config: ExtractConfigParseConfig
    """The configuration options for extraction."""

    priority: bool
    """
    If True, attempts to process the job with priority if the user has priority
    processing budget available; by default, sync jobs are prioritized above async
    jobs.
    """

    system_prompt: str
    """A system prompt to use for the extraction.

    This is a general prompt that is applied to the entire document before any other
    prompts.
    """

    user_config: Dict[str, object]
    """User-specific configuration options."""


class ExtractConfigAsyncWebhook(TypedDict, total=False):
    channels: SequenceNotStr[str]
    """
    A list of Svix channels the message will be delivered down, omit to send to all
    channels.
    """

    metadata: object

    mode: Literal["direct", "svix"]

    url: Optional[str]


class ExtractConfigAsync(TypedDict, total=False):
    enabled: bool

    priority: bool

    webhook: ExtractConfigAsyncWebhook


class ExtractConfigOptions(TypedDict, total=False):
    array_extract: bool
    """
    Array extraction allows you to extract long lists of information from lengthy
    documents. It makes parallel calls on overlapping sections of the document.
    """

    array_extract_pages: int
    """Length of each segment, in pages, for parallel calls with array extraction."""

    experimental_table_citations: bool
    """If table citations should be generated for the extracted content."""

    extract_algorithm: Literal["auto", "legacy", "streaming", "no_overlap"]
    """The array extraction version to use."""

    generate_citations: bool
    """If citations should be generated for the extracted content."""

    numerical_confidence: bool
    """If True, enable numeric citation confidence scores. Defaults to False."""

    spreadsheet_agent: bool
    """If spreadsheet agent should be used for extraction."""

    streaming_extract_item_density: int
    """Number of items to extract in each stream call."""


ExtractConfigParseConfigPageRange: TypeAlias = Union[PageRange, Iterable[PageRange], Iterable[int]]


class ExtractConfigParseConfig(TypedDict, total=False):
    add_page_markers: bool
    """If True, add page markers to the output. Defaults to False."""

    beta_layout_enrichment: bool
    """
    If enabled, a large language/vision model will be used to postprocess the layout
    predictions. Defaults to False.
    """

    bucket_name: str
    """The name of the bucket to use for the document."""

    chart_extract: bool
    """
    A flag to indicate if bar chart extraction should be performed (requires
    figure_summary=True). Defaults to False.
    """

    chunk_mode: Literal["variable", "section", "page", "disabled", "block", "page_sections"]
    """The mode to use for chunking.

    Defaults to 'variable'. Section chunks according to sections in the document.
    Page chunks according to pages. Page sections chunks according to both pages and
    sections. Disabled returns a single chunk.
    """

    chunk_size: int
    """
    The approximate size of chunks (in characters) that the document will be split
    into. Defaults to None, in which case the chunk size is variable between 250 -
    1500 characters.
    """

    continue_hierarchy: bool
    """
    A flag to indicate if the hierarchy of the document should be continued from
    chunk to chunk. E.g. ## Prev Section (cont.)
    """

    custom_format: Literal["aml", "ai_usage"]

    customer_id: str
    """Override the customer ID for the request. Defaults to None."""

    danger_filter_wide_boxes: bool
    """If True, filter out boxes with width greater than 50% of the document width.

    Defaults to False. You probably don't want to use this.
    """

    detect_signatures: bool
    """If True, detect signatures in the document. Defaults to False."""

    disable_chunking: bool
    """DEPRECATED, use chunk_mode=disabled instead"""

    document_password: str
    """Password to decrypt password-protected documents."""

    dpi: int
    """The dots per inch (DPI) setting for image processing.

    Higher values increase resolution but increase latency. The maximum recommended
    value is 300.
    """

    embed_text_metadata_pdf: bool
    """If True, embed text metadata into the returned PDF. Defaults to False."""

    enable_change_tracking: bool
    """
    Add <u> tag around text that's underlined and surround strikethroughs and
    underlines with <change> tags, defaults to False
    """

    enable_comments: bool
    """Pull PDF comments from the document, defaults to False"""

    enable_highlight_detection: bool
    """
    Add <mark> tags around highlighted text detected using the segmentation model,
    defaults to False
    """

    enable_scripts: bool
    """
    Add <sub> tag around subscripts and <sup> tag around superscripts, defaults to
    False
    """

    enhanced_docx_conversion: bool
    """
    Instead of using LibreOffice, when enabled, this flag uses a Windows VM to
    convert docx files. This is slower but more accurate.
    """

    enhanced_figure_summary: bool
    """If True, use enhanced figure summarization pipeline for complex charts.

    Defaults to False.
    """

    enrich: bool
    """
    If enabled, a large language/vision model will be used to postprocess the
    extracted content. Defaults to False.
    """

    enrich_mode: Literal["standard", "page", "table"]
    """The mode to use for enrichment. Defaults to standard"""

    enrich_prompt: str
    """Add information to the prompt for enrichment."""

    exclude_hidden_rows_cols: bool
    """Skip hidden rows and cols in Excel files. Defaults to False."""

    exclude_hidden_sheets: bool
    """Skip hidden sheets in Excel files. Defaults to False."""

    experimental_large_spreadsheet_table_chunking: bool
    """Note, this is an alpha feature subject to change at any time.

    If enabled, large tables will be chunked into multiple tables. Defaults to
    False.
    """

    extra_metadata: Dict[str, object]
    """Extra metadata to be added to logs."""

    figure_summary: bool
    """A flag to indicate if figure summarization should be performed.

    Defaults to False.
    """

    figure_summary_override: bool
    """If the figure summary prompt should override our default prompt."""

    figure_summary_prompt: str
    """Add information to the prompt for figure summarization."""

    filter_line_numbers: bool
    """If True, filter out line numbers from the output. Defaults to False."""

    force_file_extension: Optional[str]
    """Force the URL to be downloaded as a specific file extension (e.g. `.png`)."""

    force_url_result: bool
    """Force the result to be returned in URL form."""

    ignore_blocks: List[
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
    """A list of block types to ignore.

    Defaults to ['Page Number', 'Header', 'Footer', 'Comment'].
    """

    include_color_information: bool
    """
    If True, preserve color information in spreadsheet cells by wrapping text with
    LaTeX color commands during parsing.
    """

    include_formula_information: bool
    """
    If True, preserve formula information in spreadsheet cells by wrapping text with
    LaTeX formula commands during parsing.
    """

    infer_table_color: bool
    """If table cell colors should be used to determine table structure.

    Defaults to False.
    """

    json_bbox: bool
    """If True, include bounding box information in JSON table output.

    Defaults to False.
    """

    keep_line_breaks: bool
    """If line breaks should be preserved in the text. Defaults to False."""

    kms_arn: str
    """The AWS KMS key to use for the document."""

    large_table_chunking: bool
    """
    If large tables should be chunked into smaller tables, currently only supported
    on spreadsheet and CSV files.
    """

    large_table_chunking_size: int
    """The max row/column size for a table to be chunked. Defaults to 50."""

    layout_model: Literal["default", "beta"]
    """The layout model to use for the document.

    This will be deprecated in the future.
    """

    max_batch_size: int
    """The maximum number of pages to process in a single batch. Defaults to 10."""

    merge_tables: bool
    """
    A flag to indicate if consecutive tables with the same number of columns should
    be merged. Defaults to False.
    """

    mode: Literal["document", "deck", "auto"]
    """The type of document to be processed.

    Defaults to document. If auto is specified, the orientation of the first page
    will be used to determine the document type.
    """

    num_ocr_crops: int
    """The dimension of the OCR crops along each axis.

    num_ocr_crops^2 is the total number of crops. Defaults to 2.
    """

    numerical_parse_confidence: bool
    """If True, enable numeric parse confidence scores in granular_confidence field.

    Defaults to False.
    """

    ocr_mode: Literal["standard", "agentic"]
    """The mode to use for OCR.

    If agentic is enabled, table OCR will be automatically edited.
    """

    ocr_system: Literal["gcloud", "textract", "tesseract", "combined"]
    """The OCR system to use. Defaults to cloud (AWS Textract/Azure DocAI/etc)."""

    overlap_threshold: float
    """The threshold for box overlap. Defaults to 0.5."""

    page_end: int
    """The page number to stop processing at."""

    page_range: ExtractConfigParseConfigPageRange
    """The page range to process."""

    page_start: int
    """The page number to start processing from."""

    pdf_ocr: Literal["hybrid", "pdf", "ocr"]
    """The method to use for OCR.

    hybrid uses the PDF text first, then OCR. pdf only uses the PDF text. ocr only
    uses OCR.
    """

    persist_results: bool
    """If True, persist the results indefinitely. Defaults to False."""

    region_preference: Optional[Literal["us"]]
    """Forces all external API calls to be routed to specified country/region."""

    remove_text_formatting: bool
    """If True, remove text formatting from the output (e.g.

    hyphens for list items). Defaults to False.
    """

    return_figure_images: bool
    """If figure images should be returned in the result. Defaults to False."""

    return_ocr_data: bool
    """If True, return OCR data in the result. Defaults to False."""

    return_table_images: bool
    """If table images should be returned in the result. Defaults to False."""

    rotate_figures: bool
    """
    Use an orientation model to detect and rotate figures as needed, defaults to
    False
    """

    rotate_pages: bool
    """
    Use an orientation model to detect and rotate pages as needed, defaults to False
    """

    spreadsheet_table_clustering: Literal["default", "disabled", "intelligent"]
    """
    On a spreadsheet, the algorithm that is used to split up sheets into multiple
    tables.
    """

    summarize_all_figures: bool
    """
    If True, enable figure summaries for all figures regardless of size (onprem
    only). Defaults to False.
    """

    table_output_format: Literal["html", "json", "md", "dynamic", "ai_json", "csv"]
    """The mode to use for table output. Defaults to html."""

    table_summary: bool
    """If tables should be summarized for embedding. Defaults to True."""

    table_summary_prompt: str
    """Add information to the prompt for table summarization."""

    timeout: float
    """LEGACY: For sync/on-prem only.

    The timeout for the job in seconds. Defaults to 1800.
    """

    use_checkboxes: bool
    """Add checkboxes to the output, defaults to False"""

    use_equations: bool
    """Add equations to the output, defaults to False"""

    use_fast_inference: bool
    """Use a faster inference model for parsing. Defaults to False."""

    use_gpu_ocr: bool
    """Use GPU acceleration for OCR processing. Defaults to False."""

    user_specified_timeout_seconds: Optional[float]
    """A user specified timeout, defaults to None"""

    version: Literal["v1", "v2", "v3"]
    """The version of the processing options."""


class SyncExtractConfig(TypedDict, total=False):
    input: Required[SyncExtractConfigInput]
    """The URL of the document to be processed.

    You can provide one of the following: 1. A publicly available URL 2. A presigned
    S3 URL 3. A reducto:// prefixed URL obtained from the /upload endpoint after
    directly uploading a document 4. A jobid:// prefixed URL obtained from a
    previous /parse invocation
    """

    instructions: SyncExtractConfigInstructions
    """The instructions to use for the extraction."""

    parsing: SyncExtractConfigParsing
    """The configuration options for parsing the document.

    If you are passing in a jobid:// URL for the file, then this configuration will
    be ignored.
    """

    settings: SyncExtractConfigSettings
    """The settings to use for the extraction."""


SyncExtractConfigInput: TypeAlias = Union[str, Upload]


class SyncExtractConfigInstructions(TypedDict, total=False):
    schema: object
    """The JSON schema to use for the extraction."""

    system_prompt: str
    """The system prompt to use for the extraction."""


class SyncExtractConfigParsingEnhanceAgenticTableAgentic(TypedDict, total=False):
    scope: Required[Literal["table"]]

    prompt: Optional[str]
    """Custom prompt for table agentic."""


class SyncExtractConfigParsingEnhanceAgenticFigureAgentic(TypedDict, total=False):
    scope: Required[Literal["figure"]]

    prompt: Optional[str]
    """Custom prompt for figure agentic."""


class SyncExtractConfigParsingEnhanceAgenticTextAgentic(TypedDict, total=False):
    scope: Required[Literal["text"]]


SyncExtractConfigParsingEnhanceAgentic: TypeAlias = Union[
    SyncExtractConfigParsingEnhanceAgenticTableAgentic,
    SyncExtractConfigParsingEnhanceAgenticFigureAgentic,
    SyncExtractConfigParsingEnhanceAgenticTextAgentic,
]


class SyncExtractConfigParsingEnhance(TypedDict, total=False):
    agentic: Iterable[SyncExtractConfigParsingEnhanceAgentic]
    """
    Agentic uses vision language models to enhance the accuracy of the output of
    different types of extraction. This will incur a cost and latency increase.
    """

    summarize_figures: bool
    """If True, summarize figures using a small vision language model.

    Defaults to True.
    """


class SyncExtractConfigParsingFormatting(TypedDict, total=False):
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


class SyncExtractConfigParsingRetrievalChunking(TypedDict, total=False):
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


class SyncExtractConfigParsingRetrieval(TypedDict, total=False):
    chunking: SyncExtractConfigParsingRetrievalChunking

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


SyncExtractConfigParsingSettingsPageRange: TypeAlias = Union[PageRange, Iterable[PageRange], Iterable[int]]


class SyncExtractConfigParsingSettings(TypedDict, total=False):
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

    page_range: Optional[SyncExtractConfigParsingSettingsPageRange]
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


class SyncExtractConfigParsingSpreadsheetSplitLargeTables(TypedDict, total=False):
    enabled: bool
    """If True, split large tables into smaller tables. Defaults to True."""

    size: int
    """The size of the tables to split into. Defaults to 50."""


class SyncExtractConfigParsingSpreadsheet(TypedDict, total=False):
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

    split_large_tables: SyncExtractConfigParsingSpreadsheetSplitLargeTables


class SyncExtractConfigParsing(TypedDict, total=False):
    enhance: SyncExtractConfigParsingEnhance

    formatting: SyncExtractConfigParsingFormatting

    retrieval: SyncExtractConfigParsingRetrieval

    settings: SyncExtractConfigParsingSettings

    spreadsheet: SyncExtractConfigParsingSpreadsheet


class SyncExtractConfigSettingsCitations(TypedDict, total=False):
    enabled: bool
    """If True, include citations in the extraction."""

    numerical_confidence: bool
    """If True, enable numeric citation confidence scores. Defaults to True."""


class SyncExtractConfigSettings(TypedDict, total=False):
    array_extract: bool
    """If True, use array extraction."""

    citations: SyncExtractConfigSettingsCitations
    """The citations to use for the extraction."""

    include_images: bool
    """If True, include images in the extraction."""

    optimize_for_latency: bool
    """
    If True, jobs will be processed with a higher throughput and priority at a
    higher cost. Defaults to False.
    """


ExtractRunParams: TypeAlias = Union[ExtractConfig, ExtractConfig, SyncExtractConfig]
