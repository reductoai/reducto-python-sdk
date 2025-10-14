# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["SvixWebhookConfig"]


class SvixWebhookConfig(BaseModel):
    channels: Optional[List[str]] = None
    """
    A list of Svix channels the message will be delivered down, omit to send to all
    channels.
    """

    mode: Optional[Literal["svix"]] = None
