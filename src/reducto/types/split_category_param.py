from __future__ import annotations

from typing import Optional
from typing_extensions import Required, TypedDict

__all__ = ["SplitCategoryParam"]


class SplitCategoryParam(TypedDict, total=False):
    description: Required[str]

    name: Required[str]

    partition_key: Optional[str]
