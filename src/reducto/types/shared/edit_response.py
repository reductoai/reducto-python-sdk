# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from ..._models import BaseModel
from .bounding_box import BoundingBox

__all__ = ["EditResponse", "FormSchema"]


class FormSchema(BaseModel):
    bbox: BoundingBox

    description: str

    type: Literal["text", "checkbox", "dropdown", "barcode"]

    fill: Optional[bool] = None
    """If True (default), the system will attempt to fill this widget.

    If False, the widget will be created but intentionally left unfilled.
    """


class EditResponse(BaseModel):
    document_url: str

    form_schema: Optional[List[FormSchema]] = None
