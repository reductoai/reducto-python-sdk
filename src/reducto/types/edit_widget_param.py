# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal, Required, TypedDict

from .bounding_box_param import BoundingBoxParam

__all__ = ["EditWidgetParam"]


class EditWidgetParam(TypedDict, total=False):
    bbox: Required[BoundingBoxParam]
    """Bounding box coordinates of the widget"""

    description: Required[str]
    """Description of the widget extracted from the document"""

    type: Required[Literal["text", "checkbox", "radio", "dropdown", "barcode"]]
    """Type of the form widget"""

    fill: bool
    """If True (default), the system will attempt to fill this widget.

    If False, the widget will be created but intentionally left unfilled.
    """

    font_size: Optional[float]
    """Font size in points for this specific field.

    Takes priority over the global font_size in EditOptions. If not set, falls back
    to the global font_size, then to auto-calculated sizing.
    """

    value: Optional[str]
    """
    If provided, this value will be used directly instead of attempting to
    intelligently determine the field value.
    """
