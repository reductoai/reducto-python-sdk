# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Union, Optional
from typing_extensions import TypeAlias

from ..._models import BaseModel
from .svix_webhook_config import SvixWebhookConfig
from .direct_webhook_config import DirectWebhookConfig

__all__ = ["ConfigV3AsyncConfig", "Webhook"]

Webhook: TypeAlias = Union[SvixWebhookConfig, DirectWebhookConfig, None]


class ConfigV3AsyncConfig(BaseModel):
    metadata: Optional[object] = None
    """JSON metadata included in webhook request body. Defaults to None."""

    priority: Optional[bool] = None
    """
    If True, attempts to process the job with priority if the user has priority
    processing budget available; by default, sync jobs are prioritized above async
    jobs.
    """

    webhook: Optional[Webhook] = None
    """The webhook configuration for the asynchronous processing."""
