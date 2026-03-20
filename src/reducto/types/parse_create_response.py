# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Union
from typing_extensions import TypeAlias

from .parse_response import ParseResponse
from .async_parse_response import AsyncParseResponse

__all__ = ["ParseCreateResponse"]

ParseCreateResponse: TypeAlias = Union[ParseResponse, AsyncParseResponse]
