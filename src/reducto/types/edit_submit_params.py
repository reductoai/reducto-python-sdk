# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Iterable, Optional
from typing_extensions import Required, TypeAlias, TypedDict

from .edit_widget_param import EditWidgetParam
from .edit_options_param import EditOptionsParam
from .upload_response_param import UploadResponseParam

__all__ = ["EditSubmitParams", "DocumentURL"]


class EditSubmitParams(TypedDict, total=False):
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


DocumentURL: TypeAlias = Union[str, UploadResponseParam]
