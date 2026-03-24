# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, TypedDict

__all__ = ["Upload"]


class Upload(TypedDict, total=False):
    file_id: Required[str]

    presigned_url: Optional[str]
