from ..._models import BaseModel

__all__ = ["AsyncClassifyResponse"]


class AsyncClassifyResponse(BaseModel):
    job_id: str
