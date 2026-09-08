from .._models import BaseModel

__all__ = ["JobDeleteResponse"]


class JobDeleteResponse(BaseModel):
    job_id: str
