# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["ClientUploadParams"]


class ClientUploadParams(TypedDict, total=False):
    query_extension: Annotated[Optional[str], PropertyInfo(alias="extension")]

    body_extension: Annotated[str, PropertyInfo(alias="extension")]
