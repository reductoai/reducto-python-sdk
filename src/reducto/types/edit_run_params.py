# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Iterable, Optional
from typing_extensions import Required, TypeAlias, TypedDict

from .edit_widget_param import EditWidgetParam
from .edit_options_param import EditOptionsParam
from .shared_params.upload import Upload

__all__ = ["EditRunParams", "DocumentURL"]


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

    edit_options: EditOptionsParam

    form_schema: Optional[Iterable[EditWidgetParam]]
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

    enable_overflow_pages: bool
    """If True, creates overflow pages for text that doesn't fit in form fields.

    Defaults to False.
    """

    flatten: bool
    """If True, flattens form fields after filling, converting them to static content.

    Defaults to False.
    """

    font_size: Optional[float]
    """The font size (in points) to use for filled text fields.

    If not specified, font size is automatically calculated based on field
    dimensions.
    """

    llm_provider_preference: Optional[Literal["openai", "anthropic", "google"]]
    """The LLM provider to use for edit processing.

    If not specified, defaults to 'google'
    """


class FormSchema(TypedDict, total=False):
    bbox: Required[BoundingBox]
    """Bounding box coordinates of the widget"""

    description: Required[str]
    """Description of the widget extracted from the document"""

    type: Required[Literal["text", "checkbox", "radio", "dropdown", "barcode"]]
    """Type of the form widget"""

    fill: bool
    """If True (default), the system will attempt to fill this widget.

    If False, the widget will be created but intentionally left unfilled.
    """

    value: Optional[str]
    """
    If provided, this value will be used directly instead of attempting to
    intelligently determine the field value.
    """
