# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["AdvancedCitationsConfig"]


class AdvancedCitationsConfig(TypedDict, total=False):
    numerical_confidence: bool
    """If True, enable numeric citation confidence scores. Defaults to False."""
