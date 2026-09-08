from typing import Dict, Optional
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["ChartResponse", "Result", "Usage"]


class Result(BaseModel):
    chart_data: Dict[str, object]

    reconstruction_url: str

    summary: str

    verified: bool


class Usage(BaseModel):
    credits: Optional[float] = None

    num_charts: Optional[Literal[1]] = None


class ChartResponse(BaseModel):
    job_id: str

    result: Result

    duration: Optional[float] = None

    response_type: Literal["chart"]

    usage: Optional[Usage] = None
