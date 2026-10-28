from __future__ import annotations

import json
import random
from typing import Union, Optional, cast
from dataclasses import dataclass
from typing_extensions import Literal, Protocol, TypeAlias

from .types import FailureReason
from ..._utils import is_mapping
from ..._constants import MAX_RETRY_DELAY, INITIAL_RETRY_DELAY
from ..._exceptions import ReductoError

__all__ = [
    "CANNOT_PROCESS_DETAIL",
    "Answer",
    "EndpointOutcome",
    "EndpointReply",
    "EndpointUnreachable",
    "Failure",
    "PageOutcome",
    "PageTransport",
    "backoff_seconds",
    "classify_outcome",
]

CANNOT_PROCESS_DETAIL = "input could not be processed"
"""The endpoint's 422 detail for a page that it cannot process."""


@dataclass(frozen=True)
class EndpointReply:
    """The endpoint answered. `status` is the HTTP status of the model container, unwrapped from provider errors.
    `detail` is set when the transport, not the container, describes the error; else it is read from `body`."""

    status: int
    body: bytes = b""
    detail: Optional[str] = None


@dataclass(frozen=True)
class EndpointUnreachable:
    """No answer came back: the connection failed or broke, or the call timed out."""

    kind: Literal["connection", "timeout"]
    detail: str


EndpointOutcome: TypeAlias = Union[EndpointReply, EndpointUnreachable]


class PageTransport(Protocol):
    """Sends one page-parse body. Must be thread-safe.
    Raise only for errors that fail every page, such as bad credentials."""

    @property
    def body_limit(self) -> int:
        """The largest request body, in bytes, that the endpoint accepts."""
        ...

    def send(self, body: bytes, /) -> EndpointOutcome: ...


@dataclass(frozen=True)
class Answer:
    """A 2xx answer. The response module reads its body."""

    body: bytes


@dataclass(frozen=True)
class Failure:
    reason: FailureReason
    detail: str
    status: Optional[int] = None
    retryable: bool = False


PageOutcome: TypeAlias = Union[Answer, Failure]


def classify_outcome(outcome: EndpointOutcome) -> PageOutcome:
    """Retry 429, a 5xx other than 504, and a broken connection. Every other failure is final.

    Raises ReductoError for a 400, or for a 422 with any other detail: the request is not valid,
    so the client stops the document.
    """
    if isinstance(outcome, EndpointUnreachable):
        return Failure("error", f"{outcome.kind}: {outcome.detail}", retryable=outcome.kind == "connection")
    if 200 <= outcome.status < 300:
        return Answer(outcome.body)
    detail = outcome.detail if outcome.detail is not None else _body_detail(outcome.body)
    described = f"status {outcome.status}: {detail}" if detail else f"status {outcome.status}"
    if outcome.status == 422 and detail == CANNOT_PROCESS_DETAIL:
        return Failure("unprocessable", described, outcome.status)
    if outcome.status in (400, 422):
        raise ReductoError(f"The endpoint rejected the request ({described}).")
    retryable = outcome.status == 429 or (outcome.status >= 500 and outcome.status != 504)
    return Failure("error", described, outcome.status, retryable=retryable)


def backoff_seconds(retry: int) -> float:
    """Exponential backoff from the SDK's retry delays, capped, with up to 25% jitter."""
    delay = min(INITIAL_RETRY_DELAY * pow(2.0, min(retry - 1, 1000)), MAX_RETRY_DELAY)
    return delay * (1 - 0.25 * random.random())


def _body_detail(body: bytes) -> str | None:
    """The `detail` of a JSON error body from the container."""
    try:
        data = cast(object, json.loads(body))
    except ValueError:
        return None
    detail = data.get("detail") if is_mapping(data) else None
    return detail if isinstance(detail, str) else None
