from typing import Optional

from ..._models import BaseModel

__all__ = ["DocumentProperties"]


class DocumentProperties(BaseModel):
    """Properties embedded in the customer's original document."""

    author: Optional[str] = None

    created_at: Optional[str] = None

    creator: Optional[str] = None

    keywords: Optional[str] = None

    last_modified_by: Optional[str] = None

    modified_at: Optional[str] = None

    producer: Optional[str] = None

    subject: Optional[str] = None

    title: Optional[str] = None
