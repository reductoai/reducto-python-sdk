# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from .._models import BaseModel
from .bounding_box import BoundingBox

__all__ = ["EditWidget"]


class EditWidget(BaseModel):
    bbox: BoundingBox
    """Bounding box coordinates of the widget"""

    description: str
    """Description of the widget extracted from the document"""

    type: Literal["text", "checkbox", "radio", "dropdown", "barcode"]
    """Type of the form widget"""

    fill: Optional[bool] = None
    """If True (default), the system will attempt to fill this widget.

    If False, the widget will be created but intentionally left unfilled.
    """

    font_size: Optional[float] = None
    """Font size in points for this specific field.

    Takes priority over the global font_size in EditOptions. If not set, falls back
    to the global font_size, then to auto-calculated sizing.
    """

    value: Optional[str] = None
    """
    If provided, this value will be used directly instead of attempting to
    intelligently determine the field value.
    """
