from ..._models import BaseModel

__all__ = ["AsyncSplitResponse"]


class AsyncSplitResponse(BaseModel):
    job_id: str
