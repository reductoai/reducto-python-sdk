from typing import Optional

from ..._models import BaseModel

__all__ = ["AdvancedCitationsConfig"]


class AdvancedCitationsConfig(BaseModel):
    numerical_confidence: Optional[bool] = None
    """If True, enable numeric citation confidence scores. Defaults to False."""
