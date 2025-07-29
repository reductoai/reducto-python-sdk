# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from .._models import BaseModel
from .shared.bounding_box import BoundingBox

__all__ = ["EditRunResponse", "FormSchema"]


class FormSchema(BaseModel):
    bbox: BoundingBox

    description: str

    type: Literal["text", "checkbox", "dropdown", "barcode"]


class EditRunResponse(BaseModel):
    document_url: str

    form_schema: Optional[List[FormSchema]] = None
