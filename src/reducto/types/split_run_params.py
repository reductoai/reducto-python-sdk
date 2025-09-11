# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Iterable
from typing_extensions import Literal, Required, TypeAlias, TypedDict

from .._types import SequenceNotStr
from .shared_params.upload import Upload
from .shared_params.split_category import SplitCategory
from .shared_params.base_processing_options import BaseProcessingOptions
from .shared_params.advanced_processing_options import AdvancedProcessingOptions
from .shared_params.experimental_processing_options import ExperimentalProcessingOptions

__all__ = ["SplitRunParams", "DocumentURL", "SplitOptions"]


class SplitRunParams(TypedDict, total=False):
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

    split_options: SplitOptions

    split_rules: str
    """The prompt that describes rules for splitting the document."""


DocumentURL: TypeAlias = Union[str, SequenceNotStr[str], Upload]


class SplitOptions(TypedDict, total=False):
    table_cutoff: Literal["truncate", "preserve"]
    """
    If tables should be truncated to the first few rows or if all content should be
    preserved. truncate improves latency, preserve is recommended for cases where
    partition_key is being used and the partition_key may be included within the
    table. Defaults to truncate
    """
