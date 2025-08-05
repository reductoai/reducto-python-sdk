# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Iterable, Optional
from typing_extensions import Literal, Required, TypeAlias, TypedDict

from .shared_params.upload import Upload
from .shared_params.bounding_box import BoundingBox

__all__ = ["EditRunParams", "DocumentURL", "EditOptions", "FormSchema"]


class EditRunParams(TypedDict, total=False):
    document_url: Required[DocumentURL]
    """The URL of the document to be processed. You can provide one of the following:

    1. A publicly available URL
    2. A presigned S3 URL
    3. A reducto:// prefixed URL obtained from the /upload endpoint after directly
       uploading a document
    """

    edit_instructions: Required[str]
    """The instructions for the edit."""

    edit_options: EditOptions

    form_schema: Optional[Iterable[FormSchema]]
    """Form schema for PDF forms.

    List of widgets with their types, descriptions, and bounding boxes. Only works
    for PDFs.
    """

    priority: bool
    """
    If True, attempts to process the job with priority if the user has priority
    processing budget available; by default, sync jobs are prioritized above async
    jobs.
    """


DocumentURL: TypeAlias = Union[str, Upload]


class EditOptions(TypedDict, total=False):
    color: str
    """The color to use for edits, in hex format."""


class FormSchema(TypedDict, total=False):
    bbox: Required[BoundingBox]
    """Bounding box coordinates of the widget"""

    description: Required[str]
    """Description of the widget extracted from the document"""

    type: Required[Literal["text", "checkbox", "dropdown", "barcode"]]
    """Type of the form widget"""
