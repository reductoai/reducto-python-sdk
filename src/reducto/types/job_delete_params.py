from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["JobDeleteParams"]


class JobDeleteParams(TypedDict, total=False):
    include_persisted: bool
    """Also delete long-retention persisted artifacts for this job."""
