# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Iterable
from typing_extensions import Required, TypeAlias, TypedDict

from .shared_params.upload import Upload
from .shared_params.split_category import SplitCategory
from .shared_params.base_processing_options import BaseProcessingOptions
from .shared_params.advanced_processing_options import AdvancedProcessingOptions
from .shared_params.experimental_processing_options import ExperimentalProcessingOptions

__all__ = ["SplitRunParams", "DocumentURL"]


class SplitRunParams(TypedDict, total=False):
    document_url: Required[DocumentURL]
    """The URL of the document to be processed. You can provide one of the following:

    1. A publicly available URL
    2. A presigned S3 URL
    3. A reducto:// prefixed URL obtained from the /upload endpoint after directly
       uploading a document
    """

    split_description: Required[Iterable[SplitCategory]]
    """The configuration options for processing the document."""

    advanced_options: AdvancedProcessingOptions

    experimental_options: ExperimentalProcessingOptions

    options: BaseProcessingOptions

    split_rules: str
    """The rules for splitting the document."""


DocumentURL: TypeAlias = Union[str, Upload]
