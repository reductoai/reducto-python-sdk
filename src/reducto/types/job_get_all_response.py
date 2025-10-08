# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["JobGetAllResponse", "Job"]


class Job(BaseModel):
    created_at: datetime

    duration: Optional[float] = None

    job_id: str

    num_pages: Optional[int] = None

    raw_config: str

    status: Literal["Pending", "Completed", "Failed", "Idle", "InProgress", "Completing", "Cancelled"]

    total_pages: Optional[int] = None

    type: Literal["Parse", "Extract", "Split", "Edit", "Pipeline"]

    bucket: Optional[object] = None

    source: Optional[object] = None


class JobGetAllResponse(BaseModel):
    jobs: List[Job]
    """
    List of jobs with their job_id, status, type, raw_config, created_at, num_pages
    and duration
    """

    next_cursor: Optional[str] = None
    """Cursor to fetch the next page of results. If null, there are no more results."""
