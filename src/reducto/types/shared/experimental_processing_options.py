# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import TYPE_CHECKING, Dict, Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["ExperimentalProcessingOptions", "Enrich"]


class Enrich(BaseModel):
    enabled: Optional[bool] = None
    """
    If enabled, a large language/vision model will be used to postprocess the
    extracted content. Note: enabling enrich requires tables be outputted in
    markdown format. Defaults to False.
    """

    mode: Optional[Literal["standard", "page", "table"]] = None
    """The mode to use for enrichment. Defaults to standard"""

    prompt: Optional[str] = None
    """Add information to the prompt for enrichment."""


class ExperimentalProcessingOptions(BaseModel):
    danger_filter_wide_boxes: Optional[bool] = None
    """You probably shouldn't use this.

    If True, filter out boxes with width greater than 50% of the document width.
    Defaults to False. You probably don't want to use this.
    """

    embed_text_metadata_pdf: Optional[bool] = None
    """
    If extracted OCR text metadata should be embedded back into the returned PDF,
    overwriting any existing text. Defaults to False.
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

    enrich: Optional[Enrich] = None
    """The configuration options for enrichment."""

    layout_model: Optional[Literal["default", "beta"]] = None
    """The layout model to use for the document.

    This will be deprecated in the future.
    """

    native_office_conversion: Optional[bool] = None
    """
    Instead of using LibreOffice, when enabled, this flag uses a Windows VM to
    convert files. This is slower but more accurate.
    """

    numerical_parse_confidence: Optional[bool] = None
    """
    If True, enable numeric parse confidence scores in granular_confidence
    dictionary. Defaults to False.
    """

    return_figure_images: Optional[bool] = None
    """If figure images should be returned in the result. Defaults to False."""

    return_table_images: Optional[bool] = None
    """If table images should be returned in the result. Defaults to False."""

    rotate_figures: Optional[bool] = None
    """
    Use an orientation model to detect and rotate figures as needed, defaults to
    False
    """

    rotate_pages: Optional[bool] = None
    """Use an orientation model to detect and rotate pages as needed, defaults to True"""

    __pydantic_extra__: Dict[str, object] = FieldInfo(init=False)  # pyright: ignore[reportIncompatibleVariableOverride]
    if TYPE_CHECKING:
        # Stub to indicate that arbitrary properties are accepted.
        # To access properties that are not valid identifiers you can use `getattr`, e.g.
        # `getattr(obj, '$type')`
        def __getattr__(self, attr: str) -> object: ...
