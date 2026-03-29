# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Union
from typing_extensions import TypeAlias

from .shared.parse_response import ParseResponse
from .shared.async_parse_response import AsyncParseResponse

__all__ = ["ParseRunResponse"]

ParseRunResponse: TypeAlias = Union[ParseResponse, AsyncParseResponse]
