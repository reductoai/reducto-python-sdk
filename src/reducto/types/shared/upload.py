# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel

__all__ = ["Upload"]


class Upload(BaseModel):
    file_id: str

    presigned_url: Optional[str] = None
