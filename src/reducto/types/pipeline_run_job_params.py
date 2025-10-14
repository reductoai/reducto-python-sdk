# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Optional
from typing_extensions import Literal, Required, Annotated, TypeAlias, TypedDict

from .._types import SequenceNotStr
from .._utils import PropertyInfo
from .shared_params.upload import Upload

__all__ = [
    "PipelineRunJobParams",
    "Input",
    "Async",
    "AsyncWebhook",
    "AsyncWebhookSvixWebhookConfig",
    "AsyncWebhookDirectWebhookConfig",
]


class PipelineRunJobParams(TypedDict, total=False):
    input: Required[Input]
    """The URL of the document to be processed.

    You can provide one of the following: 1. A publicly available URL 2. A presigned
    S3 URL 3. A reducto:// prefixed URL obtained from the /upload endpoint after
    directly uploading a document 4. A jobid:// prefixed URL obtained from a
    previous /parse invocation
    """

    pipeline_id: Required[str]
    """The ID of the pipeline to use for the document."""

    async_: Annotated[Async, PropertyInfo(alias="async")]
    """The configuration options for asynchronous processing (default synchronous)."""


Input: TypeAlias = Union[str, Upload]


class AsyncWebhookSvixWebhookConfig(TypedDict, total=False):
    channels: SequenceNotStr[str]
    """
    A list of Svix channels the message will be delivered down, omit to send to all
    channels.
    """

    mode: Literal["svix"]


class AsyncWebhookDirectWebhookConfig(TypedDict, total=False):
    url: Required[str]

    mode: Literal["direct"]


AsyncWebhook: TypeAlias = Union[AsyncWebhookSvixWebhookConfig, AsyncWebhookDirectWebhookConfig]


class Async(TypedDict, total=False):
    metadata: object
    """JSON metadata included in webhook request body. Defaults to None."""

    priority: bool
    """
    If True, attempts to process the job with priority if the user has priority
    processing budget available; by default, sync jobs are prioritized above async
    jobs.
    """

    webhook: Optional[AsyncWebhook]
    """The webhook configuration for the asynchronous processing."""
