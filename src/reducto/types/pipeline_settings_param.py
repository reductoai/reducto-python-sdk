# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import TypedDict

__all__ = ["PipelineSettingsParam"]


class PipelineSettingsParam(TypedDict, total=False):
    """Settings for pipeline execution that override pipeline defaults."""

    document_password: Optional[str]
    """Password to decrypt password-protected documents."""
