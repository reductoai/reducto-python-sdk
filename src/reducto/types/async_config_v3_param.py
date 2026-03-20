# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Optional
from typing_extensions import Literal, Required, TypeAlias, TypedDict

from .._types import SequenceNotStr

__all__ = ["AsyncConfigV3Param", "Webhook", "WebhookSvixWebhookConfig", "WebhookDirectWebhookConfig"]


class WebhookSvixWebhookConfig(TypedDict, total=False):
    channels: SequenceNotStr[str]
    """
    A list of Svix channels the message will be delivered down, omit to send to all
    channels.
    """

    mode: Literal["svix"]


class WebhookDirectWebhookConfig(TypedDict, total=False):
    url: Required[str]

    mode: Literal["direct"]


Webhook: TypeAlias = Union[WebhookSvixWebhookConfig, WebhookDirectWebhookConfig]


class AsyncConfigV3Param(TypedDict, total=False):
    metadata: object
    """JSON metadata included in webhook request body. Defaults to None."""

    priority: bool
    """
    If True, attempts to process the job with priority if the user has priority
    processing budget available; by default, sync jobs are prioritized above async
    jobs.
    """

    webhook: Optional[Webhook]
    """The webhook configuration for the asynchronous processing."""
