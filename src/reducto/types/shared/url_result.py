from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["URLResult"]


class URLResult(BaseModel):
    result_id: str

    type: Literal["url"]
    """type = 'url'"""

    url: str
