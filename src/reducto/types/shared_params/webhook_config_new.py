# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, TypedDict

from ..._types import SequenceNotStr

__all__ = ["WebhookConfigNew"]


class WebhookConfigNew(TypedDict, total=False):
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
