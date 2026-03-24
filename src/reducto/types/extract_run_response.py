# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Union
from typing_extensions import TypeAlias

from .v3_extract import V3Extract
from .async_extract_response import AsyncExtractResponse

__all__ = ["ExtractRunResponse"]

ExtractRunResponse: TypeAlias = Union[V3Extract, AsyncExtractResponse]
