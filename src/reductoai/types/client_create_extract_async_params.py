# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

from .shared_params.webhook_config_new import WebhookConfigNew
from .shared_params.array_extract_config import ArrayExtractConfig
from .shared_params.base_processing_options import BaseProcessingOptions
from .shared_params.advanced_processing_options import AdvancedProcessingOptions
from .shared_params.experimental_processing_options import ExperimentalProcessingOptions

__all__ = ["ClientCreateExtractAsyncParams"]


class ClientCreateExtractAsyncParams(TypedDict, total=False):
    document_url: Required[str]
    """The URL of the document to be processed. You can provide one of the following:

    1. A publicly available URL
    2. A presigned S3 URL
    3. A reducto:// prefixed URL obtained from the /upload endpoint after directly
       uploading a document
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

    webhook: WebhookConfigNew
