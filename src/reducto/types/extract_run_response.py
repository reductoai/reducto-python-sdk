from typing import Union
from typing_extensions import TypeAlias

from .v3_extract import V3Extract
from .shared.async_extract_response import AsyncExtractResponse

__all__ = ["ExtractRunResponse"]

ExtractRunResponse: TypeAlias = Union[V3Extract, AsyncExtractResponse]
