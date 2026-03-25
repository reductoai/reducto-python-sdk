# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["WebhookConfigNew"]


class WebhookConfigNew(BaseModel):
    channels: Optional[List[str]] = None
    """
    A list of Svix channels the message will be delivered down, omit to send to all
    channels.
    """

    metadata: Optional[object] = None
    """JSON metadata included in webhook request body"""

    mode: Optional[Literal["disabled", "svix", "direct"]] = None
    """The mode to use for webhook delivery.

    Defaults to 'disabled'. We recommend using 'svix' for production environments.
    """

    url: Optional[str] = None
    """The URL to send the webhook to (if using direct webhoook)."""
