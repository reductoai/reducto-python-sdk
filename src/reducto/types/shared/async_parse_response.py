from ..._models import BaseModel

__all__ = ["AsyncParseResponse"]


class AsyncParseResponse(BaseModel):
    job_id: str
