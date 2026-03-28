# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import TypedDict

from .._types import FileTypes

__all__ = ["ClientUploadParams"]


class ClientUploadParams(TypedDict, total=False):
    extension: Optional[str]

    file: Optional[FileTypes]
