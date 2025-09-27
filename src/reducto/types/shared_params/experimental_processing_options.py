# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union, Optional
from typing_extensions import Literal, TypeAlias, TypedDict

__all__ = ["ExperimentalProcessingOptions", "Enrich"]


class Enrich(TypedDict, total=False):
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


class ExperimentalProcessingOptionsTyped(TypedDict, total=False):
    danger_filter_wide_boxes: bool
    """You probably shouldn't use this.

    If True, filter out boxes with width greater than 50% of the document width.
    Defaults to False. You probably don't want to use this.
    """

    detect_signatures: bool
    """If True, detect signatures in the document. Defaults to False."""

    embed_text_metadata_pdf: bool
    """
    If extracted OCR text metadata should be embedded back into the returned PDF,
    overwriting any existing text. Defaults to False.
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

    enrich: Enrich
    """The configuration options for enrichment."""

    layout_model: Literal["default", "beta"]
    """The layout model to use for the document.

    This will be deprecated in the future.
    """

    native_office_conversion: bool
    """
    Instead of using LibreOffice, when enabled, this flag uses a Windows VM to
    convert files. This is slower but more accurate.
    """

    return_figure_images: bool
    """If figure images should be returned in the result. Defaults to False."""

    return_table_images: bool
    """If table images should be returned in the result. Defaults to False."""

    rotate_figures: bool
    """
    Use an orientation model to detect and rotate figures as needed, defaults to
    False
    """

    rotate_pages: bool
    """Use an orientation model to detect and rotate pages as needed, defaults to True"""

    user_specified_timeout_seconds: Optional[float]
    """A user specified timeout, defaults to None"""


ExperimentalProcessingOptions: TypeAlias = Union[ExperimentalProcessingOptionsTyped, Dict[str, object]]
