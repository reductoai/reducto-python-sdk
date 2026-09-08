from typing import Union
from typing_extensions import Annotated, TypeAlias

from .._utils import PropertyInfo
from .v3_extract import V3Extract
from .shared.extract_response import ExtractResponse
from .shared.async_extract_response import AsyncExtractResponse

__all__ = ["ExtractRunResponse"]

# The API returns ExtractResponse (response_type "extract") for accounts not on
# V3 extract, though the spec lists only V3ExtractResponse for this endpoint.
ExtractRunResponse: TypeAlias = Annotated[
    Union[ExtractResponse, V3Extract, AsyncExtractResponse], PropertyInfo(discriminator="response_type")
]
