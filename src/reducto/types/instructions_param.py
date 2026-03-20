# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["InstructionsParam"]


class InstructionsParam(TypedDict, total=False):
    schema: object
    """The JSON schema to use for the extraction."""

    system_prompt: str
    """The system prompt to use for the extraction."""
