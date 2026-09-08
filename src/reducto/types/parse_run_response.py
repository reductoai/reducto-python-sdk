from typing import Union
from typing_extensions import Annotated, TypeAlias

from .._utils import PropertyInfo
from .shared.parse_response import ParseResponse
from .shared.async_parse_response import AsyncParseResponse

__all__ = ["ParseRunResponse"]

ParseRunResponse: TypeAlias = Annotated[
    Union[ParseResponse, AsyncParseResponse], PropertyInfo(discriminator="response_type")
]
