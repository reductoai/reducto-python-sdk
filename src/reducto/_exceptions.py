from __future__ import annotations

from typing import Dict, Optional, cast
from typing_extensions import Literal

import httpx

__all__ = [
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
]


class ReductoError(Exception):
    pass


class SubjectTokenProviderError(ReductoError):
    """Raised when a workload identity provider fails to return a subject token."""


class APIError(ReductoError):
    message: str
    request: httpx.Request

    body: object | None
    """The API response body.

    If the API responded with a valid JSON structure then this property will be the
    decoded result.

    If it isn't a valid JSON structure then this will be the raw response.

    If there was no response associated with this error then it will be `None`.
    """

    def __init__(self, message: str, request: httpx.Request, *, body: object | None) -> None:  # noqa: ARG002
        super().__init__(message)
        self.request = request
        self.message = message
        self.body = body


class APIResponseValidationError(APIError):
    response: httpx.Response
    status_code: int

    def __init__(self, response: httpx.Response, body: object | None, *, message: str | None = None) -> None:
        super().__init__(message or "Data returned by API invalid for expected schema.", response.request, body=body)
        self.response = response
        self.status_code = response.status_code


class APIStatusError(APIError):
    """Raised when an API response has a status code of 4xx or 5xx."""

    response: httpx.Response
    status_code: int

    def __init__(self, message: str, *, response: httpx.Response, body: object | None) -> None:
        super().__init__(message, response.request, body=body)
        self.response = response
        self.status_code = response.status_code


class APIConnectionError(APIError):
    def __init__(self, *, message: str = "Connection error.", request: httpx.Request) -> None:
        super().__init__(message, request, body=None)


class APITimeoutError(APIConnectionError):
    def __init__(self, request: httpx.Request) -> None:
        super().__init__(message="Request timed out.", request=request)


class BadRequestError(APIStatusError):
    status_code: Literal[400] = 400  # pyright: ignore[reportIncompatibleVariableOverride]


class AuthenticationError(APIStatusError):
    status_code: Literal[401] = 401  # pyright: ignore[reportIncompatibleVariableOverride]


class PermissionDeniedError(APIStatusError):
    status_code: Literal[403] = 403  # pyright: ignore[reportIncompatibleVariableOverride]


class NotFoundError(APIStatusError):
    status_code: Literal[404] = 404  # pyright: ignore[reportIncompatibleVariableOverride]


class ConflictError(APIStatusError):
    status_code: Literal[409] = 409  # pyright: ignore[reportIncompatibleVariableOverride]


class UnprocessableEntityError(APIStatusError):
    status_code: Literal[422] = 422  # pyright: ignore[reportIncompatibleVariableOverride]


class RateLimitError(APIStatusError):
    status_code: Literal[429] = 429  # pyright: ignore[reportIncompatibleVariableOverride]


class InternalServerError(APIStatusError):
    pass


class OAuthError(APIStatusError):
    """Raised when the workload identity token exchange at `/oauth/token` fails."""

    error: Optional[str]
    """The RFC 6749 error code, e.g. `invalid_grant`."""

    error_description: Optional[str]

    def __init__(self, *, response: httpx.Response, body: object | None) -> None:
        fields = _as_fields(body)
        error, description = fields.get("error"), fields.get("error_description")
        self.error = error if isinstance(error, str) else None
        self.error_description = description if isinstance(description, str) else None
        message = f"Token exchange failed with status {response.status_code}"
        if self.error:
            message += f": {self.error}"
        if self.error_description:
            message += f": {self.error_description}"
        super().__init__(message, response=response, body=body)


def _as_fields(body: object) -> Dict[str, object]:
    return cast("Dict[str, object]", body) if isinstance(body, dict) else {}
