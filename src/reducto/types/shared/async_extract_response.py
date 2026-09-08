from ..._models import BaseModel

__all__ = ["AsyncExtractResponse"]


class AsyncExtractResponse(BaseModel):
    job_id: str
