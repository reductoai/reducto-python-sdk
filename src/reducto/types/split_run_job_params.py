# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union, Iterable
from typing_extensions import Required, TypeAlias, TypedDict

from .shared_params.upload import Upload
from .shared_params.split_category import SplitCategory
from .shared_params.webhook_config_new import WebhookConfigNew
from .shared_params.base_processing_options import BaseProcessingOptions
from .shared_params.advanced_processing_options import AdvancedProcessingOptions
from .shared_params.experimental_processing_options import ExperimentalProcessingOptions

__all__ = ["SplitRunJobParams", "DocumentURL"]


class SplitRunJobParams(TypedDict, total=False):
    document_url: Required[DocumentURL]
    """The URL of the document to be processed. You can provide one of the following:

    1. A publicly available URL
    2. A presigned S3 URL
    3. A reducto:// prefixed URL obtained from the /upload endpoint after directly
       uploading a document
    4. A job_id (jobid://) or a list of job_ids (jobid://) obtained from a previous
       /parse endpoint
    """

    split_description: Required[Iterable[SplitCategory]]
    """The configuration options for processing the document."""

    advanced_options: AdvancedProcessingOptions

    experimental_options: ExperimentalProcessingOptions

    options: BaseProcessingOptions

    priority: bool
    """
    If True, attempts to process the job with priority if the user has priority
    processing budget available; by default, sync jobs are prioritized above async
    jobs.
    """

    split_rules: str
    """The prompt that describes rules for splitting the document."""

    webhook: WebhookConfigNew


DocumentURL: TypeAlias = Union[str, List[str], Upload]
