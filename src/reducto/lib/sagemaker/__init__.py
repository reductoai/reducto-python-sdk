from ._client import ReductoSageMaker as ReductoSageMaker, AsyncReductoSageMaker as AsyncReductoSageMaker
from .._page_parse.types import FailedPage as FailedPage, ProviderParseResponse as ProviderParseResponse
from .._page_parse.errors import (
    PageParseError as PageParseError,
    UnsupportedOnProviderError as UnsupportedOnProviderError,
)

__all__ = [
    "ReductoSageMaker",
    "AsyncReductoSageMaker",
    "PageParseError",
    "FailedPage",
    "UnsupportedOnProviderError",
    "ProviderParseResponse",
]

# The clients are public as `reducto.ReductoSageMaker`, so they show that module in reprs and errors.
ReductoSageMaker.__module__ = "reducto"
AsyncReductoSageMaker.__module__ = "reducto"
