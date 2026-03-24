# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Iterable, Optional
from typing_extensions import Literal, Required, TypeAlias, TypedDict

from .._types import SequenceNotStr
from .edit_widget_param import EditWidgetParam
from .edit_options_param import EditOptionsParam
from .upload_response_param import UploadResponseParam

__all__ = ["EditRunJobParams", "DocumentURL", "Webhook"]


class EditRunJobParams(TypedDict, total=False):
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

    webhook: Webhook


DocumentURL: TypeAlias = Union[str, UploadResponseParam]


class Webhook(TypedDict, total=False):
    channels: SequenceNotStr[str]
    """
    A list of Svix channels the message will be delivered down, omit to send to all
    channels.
    """

    metadata: object
    """JSON metadata included in webhook request body"""

    mode: Literal["disabled", "svix", "direct"]
    """The mode to use for webhook delivery.

    Defaults to 'disabled'. We recommend using 'svix' for production environments.
    """

    url: str
    """The URL to send the webhook to (if using direct webhoook)."""
