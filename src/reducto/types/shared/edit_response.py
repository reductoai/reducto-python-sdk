# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from ..._models import BaseModel
from .bounding_box import BoundingBox

__all__ = ["EditResponse", "FormSchema"]


class FormSchema(BaseModel):
    bbox: BoundingBox
    """Bounding box coordinates of the widget"""

    description: str
    """Description of the widget extracted from the document"""

    type: Literal["text", "checkbox", "dropdown", "barcode"]
    """Type of the form widget"""

    fill: Optional[bool] = None
    """If True (default), the system will attempt to fill this widget.

    If False, the widget will be created but intentionally left unfilled.
    """

    value: Optional[str] = None
    """
    If provided, this value will be used directly instead of attempting to
    intelligently determine the field value.
    """


class EditResponse(BaseModel):
    document_url: str
    """Presigned URL to download the edited document."""

    form_schema: Optional[List[FormSchema]] = None
    """Form schema for PDF forms.

    List of widgets with their types, descriptions, and bounding boxes.
    """
