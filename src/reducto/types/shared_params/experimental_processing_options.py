# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, TypedDict

__all__ = ["ExperimentalProcessingOptions", "Enrich"]


class Enrich(TypedDict, total=False):
    enabled: bool
    """
    If enabled, a large language/vision model will be used to postprocess the
    extracted content. Note: enabling enrich requires tables be outputted in
    markdown format. Defaults to False.
    """

    mode: Literal["standard", "page"]
    """The mode to use for enrichment. Defaults to standard"""

    prompt: str
    """Add information to the prompt for enrichment."""


class ExperimentalProcessingOptions(TypedDict, total=False):
    custom_format: Literal["ai_usage", "aml"]

    danger_filter_wide_boxes: bool
    """You probably shouldn't use this.

    If True, filter out boxes with width greater than 50% of the document width.
    Defaults to False. You probably don't want to use this.
    """

    enable_checkboxes: bool
    """
    Use an experimental checkbox detection model to add checkboxes to the output,
    defaults to False
    """

    enable_equations: bool
    """
    Use an experimental equation detection model to add equations to the output,
    defaults to False
    """

    enable_scripts: bool
    """
    Add <sub> tag around subscripts and <sup> tag around superscripts, defaults to
    False
    """

    enable_underlines: bool
    """
    Add <u> tag around text that's underlined and surround strikethroughs and
    underlines with <change> tags, defaults to False
    """

    enrich: Enrich
    """The configuration options for enrichment."""

    native_office_conversion: bool
    """
    Instead of using LibreOffice, when enabled, this flag uses a Windows VM to
    convert files. This is slower but more accurate.
    """

    return_figure_images: bool
    """If figure images should be returned in the result. Defaults to False."""

    return_table_images: bool
    """If table images should be returned in the result. Defaults to False."""

    rotate_pages: bool
    """Use an orientation model to detect and rotate pages as needed, defaults to True"""
