# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import TypedDict

__all__ = ["JobGetAllParams"]


class JobGetAllParams(TypedDict, total=False):
    cursor: Optional[str]
    """Cursor for pagination.

    Use the next_cursor from the previous response to fetch the next page.
    """

    exclude_configs: bool
    """Exclude raw_config from response to reduce size"""

    limit: int
    """Maximum number of jobs to return per page. Defaults to 100, max 500."""
