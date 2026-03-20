# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal, TypedDict

__all__ = ["EditOptionsParam"]


class EditOptionsParam(TypedDict, total=False):
    color: str
    """The color to use for edits, in hex format."""

    enable_overflow_pages: bool
    """If True, creates overflow pages for text that doesn't fit in form fields.

    Defaults to False.
    """

    flatten: bool
    """If True, flattens form fields after filling, converting them to static content.

    Defaults to False.
    """

    font_size: Optional[float]
    """The font size (in points) to use for filled text fields.

    If not specified, font size is automatically calculated based on field
    dimensions.
    """

    llm_provider_preference: Optional[Literal["openai", "anthropic", "google"]]
    """The LLM provider to use for edit processing.

    If not specified, defaults to 'google'
    """
