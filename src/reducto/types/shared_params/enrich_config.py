# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, TypedDict

__all__ = ["EnrichConfig"]


class EnrichConfig(TypedDict, total=False):
    enabled: bool
    """
    If enabled, a large language/vision model will be used to postprocess the
    extracted content. Note: enabling enrich requires tables be outputted in
    markdown format. Defaults to False.
    """

    mode: Literal["standard", "page", "table"]
    """The mode to use for enrichment. Defaults to standard"""

    prompt: str
    """Add information to the prompt for enrichment."""
