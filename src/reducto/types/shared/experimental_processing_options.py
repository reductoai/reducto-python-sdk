# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import TYPE_CHECKING, Dict, Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel
from .enrich_config import EnrichConfig

__all__ = ["ExperimentalProcessingOptions"]


class ExperimentalProcessingOptions(BaseModel):
    chunk_table_blocks: Optional[bool] = None
    """
    If True, split table blocks into smaller chunks based on the specified chunk
    size in the chunking option. Defaults to False.
    """

    danger_filter_wide_boxes: Optional[bool] = None
    """You probably shouldn't use this.

    If True, filter out boxes with width greater than 50% of the document width.
    Defaults to False. You probably don't want to use this.
    """

    detect_signatures: Optional[bool] = None
    """If True, detect signatures in the document. Defaults to False."""

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

    enrich: Optional[EnrichConfig] = None
    """The configuration options for enrichment."""

    layout_enrichment: Optional[bool] = None
    """
    Layout enrichment is a beta feature that improves our layout and reading order
    performance at the cost of increased latency. Defaults to False.
    """

    layout_model: Optional[Literal["default", "beta"]] = None
    """The layout model to use for the document.

    This will be deprecated in the future.
    """

    native_office_conversion: Optional[bool] = None
    """
    Instead of using LibreOffice, when enabled, this flag uses a Windows VM to
    convert files. This is slower but more accurate.
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

    user_specified_timeout_seconds: Optional[float] = None
    """A user specified timeout, defaults to None"""

    if TYPE_CHECKING:
        # Some versions of Pydantic <2.8.0 have a bug and don’t allow assigning a
        # value to this field, so for compatibility we avoid doing it at runtime.
        __pydantic_extra__: Dict[str, object] = FieldInfo(init=False)  # pyright: ignore[reportIncompatibleVariableOverride]

        # Stub to indicate that arbitrary properties are accepted.
        # To access properties that are not valid identifiers you can use `getattr`, e.g.
        # `getattr(obj, '$type')`
        def __getattr__(self, attr: str) -> object: ...
    else:
        __pydantic_extra__: Dict[str, object]
