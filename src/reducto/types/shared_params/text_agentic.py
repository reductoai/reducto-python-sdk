# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal, Required, TypedDict

__all__ = ["TextAgentic"]


class TextAgentic(TypedDict, total=False):
    scope: Required[Literal["text"]]

    prompt: Optional[str]
    """Custom instructions for agentic text.

    Note: This only applies to form regions (key-value).
    """
