import typing as _t

from . import types
from ._types import NOT_GIVEN, Omit, NoneType, NotGiven, Transport, ProxiesTypes, omit, not_given
from ._utils import file_from_path
from ._client import (
    ENVIRONMENTS,
    Client,
    Stream,
    Reducto,
    Timeout,
    Transport,
    AsyncClient,
    AsyncStream,
    AsyncReducto,
    RequestOptions,
)
from ._models import BaseModel
from ._version import __title__, __version__
from ._response import APIResponse as APIResponse, AsyncAPIResponse as AsyncAPIResponse
from ._constants import DEFAULT_TIMEOUT, DEFAULT_MAX_RETRIES, DEFAULT_CONNECTION_LIMITS
from ._exceptions import (
    APIError,
    OAuthError,
    ReductoError,
    ConflictError,
    NotFoundError,
    APIStatusError,
    RateLimitError,
    APITimeoutError,
    BadRequestError,
    APIConnectionError,
    AuthenticationError,
    InternalServerError,
    PermissionDeniedError,
    UnprocessableEntityError,
    SubjectTokenProviderError,
    APIResponseValidationError,
)
from ._base_client import DefaultHttpxClient, DefaultAioHttpClient, DefaultAsyncHttpxClient
from ._utils._logs import setup_logging as _setup_logging

__all__ = [
    "types",
    "__version__",
    "__title__",
    "NoneType",
    "Transport",
    "ProxiesTypes",
    "NotGiven",
    "NOT_GIVEN",
    "not_given",
    "Omit",
    "omit",
    "ReductoError",
    "APIError",
    "APIStatusError",
    "APITimeoutError",
    "APIConnectionError",
    "APIResponseValidationError",
    "BadRequestError",
    "AuthenticationError",
    "PermissionDeniedError",
    "NotFoundError",
    "ConflictError",
    "UnprocessableEntityError",
    "RateLimitError",
    "InternalServerError",
    "OAuthError",
    "SubjectTokenProviderError",
    "UnsupportedOnProviderError",
    "PageParseError",
    "Timeout",
    "RequestOptions",
    "Client",
    "AsyncClient",
    "Stream",
    "AsyncStream",
    "Reducto",
    "AsyncReducto",
    "ReductoSageMaker",
    "AsyncReductoSageMaker",
    "ENVIRONMENTS",
    "file_from_path",
    "BaseModel",
    "DEFAULT_TIMEOUT",
    "DEFAULT_MAX_RETRIES",
    "DEFAULT_CONNECTION_LIMITS",
    "DefaultHttpxClient",
    "DefaultAsyncHttpxClient",
    "DefaultAioHttpClient",
]

if _t.TYPE_CHECKING:
    from .lib.sagemaker import (
        PageParseError,
        ReductoSageMaker,
        AsyncReductoSageMaker,
        UnsupportedOnProviderError,
    )
else:
    import importlib as _importlib

    from ._utils._resources_proxy import resources as resources

    # The provider names load the local page parse code, so only their first use imports it.
    _LAZY = {
        "ReductoSageMaker": "reducto.lib.sagemaker",
        "AsyncReductoSageMaker": "reducto.lib.sagemaker",
        "PageParseError": "reducto.lib._page_parse.errors",
        "UnsupportedOnProviderError": "reducto.lib._page_parse.errors",
    }

    def __getattr__(name: str) -> object:
        module = _LAZY.get(name)
        if module is None:
            raise AttributeError(f"module {__name__!r} has no attribute {name!r}")
        value = getattr(_importlib.import_module(module), name)
        globals()[name] = value
        return value

    def __dir__() -> _t.List[str]:
        return sorted({*globals(), *_LAZY})


_setup_logging()

# Update the __module__ attribute for exported symbols so that
# error messages point to this module instead of the module
# it was originally defined in, e.g.
# reducto._exceptions.NotFoundError -> reducto.NotFoundError
__locals = locals()
for __name in __all__:
    if not __name.startswith("__") and __name in __locals:
        try:
            __locals[__name].__module__ = "reducto"
        except (TypeError, AttributeError):
            # Some of our exported symbols are builtins which we can't set attributes for.
            pass
