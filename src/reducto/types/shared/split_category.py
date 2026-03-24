# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel

__all__ = ["SplitCategory"]


class SplitCategory(BaseModel):
    description: str

    name: str

    partition_key: Optional[str] = None
