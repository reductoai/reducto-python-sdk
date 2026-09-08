from ..._models import BaseModel

__all__ = ["AsyncPipelineResponse"]


class AsyncPipelineResponse(BaseModel):
    job_id: str
