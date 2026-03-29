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
    """For parse/split/extract pipelines, the URL of the document to be processed.

    You can provide one of the following: 1. A publicly available URL 2. A presigned
    S3 URL 3. A reducto:// prefixed URL obtained from the /upload endpoint after
    directly uploading a document 4. A jobid:// prefixed URL obtained from a
    previous /parse invocation 5. A list of URLs (for multi-document pipelines, V3
    API only)

                For edit pipelines, this should be a string containing the edit instructions
    """

    classification_schema: Iterable[ClassificationSchema]
    """A list of classification categories and their matching criteria."""

    document_metadata: Optional[str]
    """Optional document-level metadata to include in classification prompts."""

    page_range: Optional[PageRange]
    """The page range to process (1-indexed).

    By default, the first 5 pages are used. If more than 25 pages are selected, only
    the first 25 (after sorting) are used. Only applies to PDFs; ignored for other
    document types.
    """

    persist_results: bool
    """If True, persist the results indefinitely. Defaults to False."""


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
