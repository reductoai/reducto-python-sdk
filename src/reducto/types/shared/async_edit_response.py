from ..._models import BaseModel

__all__ = ["AsyncEditResponse"]


class AsyncEditResponse(BaseModel):
    job_id: str
