from typing import Optional
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["TextAgentic"]


class TextAgentic(BaseModel):
    scope: Literal["text"]

    prompt: Optional[str] = None
    """Custom instructions for agentic text.

    Note: This only applies to form regions (key-value).
    """
