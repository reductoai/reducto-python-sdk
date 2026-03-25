# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Optional
from typing_extensions import TypeAlias, TypedDict

from .svix_webhook_config import SvixWebhookConfig
from .direct_webhook_config import DirectWebhookConfig

__all__ = ["ConfigV3AsyncConfig", "Webhook"]

Webhook: TypeAlias = Union[SvixWebhookConfig, DirectWebhookConfig]


class ConfigV3AsyncConfig(TypedDict, total=False):
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
