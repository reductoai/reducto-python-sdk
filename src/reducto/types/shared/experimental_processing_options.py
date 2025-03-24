# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["ExperimentalProcessingOptions", "Enrich"]


class Enrich(BaseModel):
    enabled: Optional[bool] = None
    """
    If enabled, a large language/vision model will be used to postprocess the
    extracted content. Note: enabling enrich requires tables be outputted in
    markdown format. Defaults to False.
    """

    mode: Optional[Literal["standard", "page"]] = None
    """The mode to use for enrichment. Defaults to standard"""

    prompt: Optional[str] = None
    """Add information to the prompt for enrichment."""


class ExperimentalProcessingOptions(BaseModel):
    custom_format: Optional[Literal["aml", "ai_usage"]] = None

    danger_filter_wide_boxes: Optional[bool] = None
    """You probably shouldn't use this.

    If True, filter out boxes with width greater than 50% of the document width.
    Defaults to False. You probably don't want to use this.
    """

    enable_checkboxes: Optional[bool] = None
    """
    Use an experimental checkbox detection model to add checkboxes to the output,
    defaults to False
    """

    enable_equations: Optional[bool] = None
    """
    Use an experimental equation detection model to add equations to the output,
    defaults to False
    """

    enable_scripts: Optional[bool] = None
    """
    Add <sub> tag around subscripts and <sup> tag around superscripts, defaults to
    False
    """

    enable_underlines: Optional[bool] = None
    """
    Add <u> tag around text that's underlined and surround strikethroughs and
    underlines with <change> tags, defaults to False
    """

    enrich: Optional[Enrich] = None
    """The configuration options for enrichment."""

    native_office_conversion: Optional[bool] = None
    """
    Instead of using LibreOffice, when enabled, this flag uses a Windows VM to
    convert files. This is slower but more accurate.
    """

    return_figure_images: Optional[bool] = None
    """If figure images should be returned in the result. Defaults to False."""

    return_table_images: Optional[bool] = None
    """If table images should be returned in the result. Defaults to False."""

    rotate_pages: Optional[bool] = None
    """
    Use an orientation model to detect and rotate pages as needed, defaults to False
    """
