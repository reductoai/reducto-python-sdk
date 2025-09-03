# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from typing_extensions import Required, TypeAlias, TypedDict

from .._types import SequenceNotStr
from .shared_params.upload import Upload
from .shared_params.array_extract_config import ArrayExtractConfig
from .shared_params.base_processing_options import BaseProcessingOptions
from .shared_params.advanced_processing_options import AdvancedProcessingOptions
from .shared_params.experimental_processing_options import ExperimentalProcessingOptions

__all__ = ["ExtractRunParams", "DocumentURL", "CitationsOptions"]


class ExtractRunParams(TypedDict, total=False):
    document_url: Required[DocumentURL]
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

    array_extract: ArrayExtractConfig
    """The configuration options for array extract"""

    citations_options: CitationsOptions
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


DocumentURL: TypeAlias = Union[str, SequenceNotStr[str], Upload]


class CitationsOptions(TypedDict, total=False):
    numerical_confidence: bool
    """If True, enable numeric citation confidence scores. Defaults to False."""
