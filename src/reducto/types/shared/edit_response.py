# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ..._models import BaseModel
from ..edit_widget import EditWidget
from ..parse_usage import ParseUsage

__all__ = ["EditResponse"]


class EditResponse(BaseModel):
    document_url: str
    """Presigned URL to download the edited document."""

    form_schema: Optional[List[EditWidget]] = None
    """Form schema for PDF forms.

    List of widgets with their types, descriptions, and bounding boxes.
    """

    usage: Optional[ParseUsage] = None
    """
    Usage information for the edit operation, including number of pages and credits
    charged.
    """
