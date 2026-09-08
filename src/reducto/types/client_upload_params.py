from __future__ import annotations

from typing import Union, Optional
from typing_extensions import TypeAlias, TypedDict

from .._types import FileTypes

__all__ = ["ClientUploadParams", "File"]


class ClientUploadParams(TypedDict, total=False):
    extension: Optional[str]

    file: Optional[File]


File: TypeAlias = Union[FileTypes, str]
