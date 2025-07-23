# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from typing_extensions import Required, TypeAlias, TypedDict

from .shared_params.upload import Upload
from .shared_params.webhook_config_new import WebhookConfigNew

__all__ = ["EditRunJobParams", "DocumentURL", "EditOptions"]


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

    edit_options: EditOptions

    priority: bool
    """
    If True, attempts to process the job with priority if the user has priority
    processing budget available; by default, sync jobs are prioritized above async
    jobs.
    """

    webhook: WebhookConfigNew


DocumentURL: TypeAlias = Union[str, Upload]


class EditOptions(TypedDict, total=False):
    color: str
    """The color to use for edits, in hex format."""
