# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union
from typing_extensions import Required, TypeAlias, TypedDict

from .shared_params.upload import Upload
from .shared_params.array_extract_config import ArrayExtractConfig
from .shared_params.base_processing_options import BaseProcessingOptions
from .shared_params.advanced_processing_options import AdvancedProcessingOptions
from .shared_params.experimental_processing_options import ExperimentalProcessingOptions

__all__ = ["ExtractRunParams", "DocumentURL"]


class ExtractRunParams(TypedDict, total=False):
    document_url: Required[DocumentURL]
    """The URL of the document to be processed. You can provide one of the following:

    1. A publicly available URL
    2. A presigned S3 URL
    3. A reducto:// prefixed URL obtained from the /upload endpoint after directly
       uploading a document
    4. A job_id (jobid://) or a list of job_ids (jobid://)
    """

    schema: Required[object]
    """The JSON schema to use for extraction."""

    advanced_options: AdvancedProcessingOptions

    array_extract: ArrayExtractConfig
    """The configuration options for array extract"""

    experimental_options: ExperimentalProcessingOptions

    generate_citations: bool
    """If citations should be generated for the extracted content."""

    options: BaseProcessingOptions

    system_prompt: str
    """A system prompt to use for the extraction.

    This is a general prompt that is applied to the entire document before any other
    prompts.
    """

    use_chunking: bool
    """If chunking should be used for the extraction. Defaults to False."""


DocumentURL: TypeAlias = Union[str, List[str], Upload]
