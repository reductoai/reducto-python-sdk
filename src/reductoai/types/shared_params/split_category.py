# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, TypedDict

__all__ = ["SplitCategory"]


class SplitCategory(TypedDict, total=False):
    description: Required[str]

    name: Required[str]

    partition_key: Optional[str]
