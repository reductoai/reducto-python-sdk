# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Iterable, Optional
from typing_extensions import Required, TypeAlias, TypedDict

from .._types import SequenceNotStr
from .shared_params import page_range
from .shared_params.upload import Upload

__all__ = ["ClassifyRunParams", "Input", "ClassificationSchema", "PageRange"]


class ClassifyRunParams(TypedDict, total=False):
    input: Required[Input]
    """The URL of the document to be classified. You can provide one of the following:

    1. A publicly available URL
    2. A presigned S3 URL
    3. A reducto:// prefixed URL obtained from the /upload endpoint after directly
       uploading a document
    """

    classification_schema: Iterable[ClassificationSchema]
    """A list of classification categories and their matching criteria."""

    document_metadata: Optional[str]
    """Optional document-level metadata to include in classification prompts."""

    force_url_result: bool
    """Force the endpoint result to be returned in URL form."""

    page_range: Optional[PageRange]
    """The page range to process (1-indexed).

    By default, the first 5 pages are used. At most 10 pages can be selected. Only
    applies to PDFs; ignored for other document types.
    """

    priority: bool
    """
    Workers poll the priority queue ahead of the standard queue, so priority jobs
    start sooner when there is queued work; sync jobs are prioritized above async
    jobs by default.
    """


Input: TypeAlias = Union[str, SequenceNotStr[str], Upload]


class ClassificationSchema(TypedDict, total=False):
    """A single classification category with its matching criteria."""

    category: Required[str]
    """
    The category name/label that documents will be classified into (e.g., 'invoice',
    'contract', 'receipt').
    """

    criteria: Required[SequenceNotStr[str]]
    """
    A list of criteria, keywords, or descriptions that define what characteristics a
    document must have to be classified into this category (e.g., ['contains billing
    information', 'has itemized charges']).
    """


PageRange: TypeAlias = Union[page_range.PageRange, Iterable[page_range.PageRange], Iterable[int]]
