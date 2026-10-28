from __future__ import annotations

from typing import List, Optional
from typing_extensions import Literal, override

from .types import FailedPage, ProviderParseResponse
from ..._exceptions import ReductoError

__all__ = ["PageError", "PageParseError", "UnsupportedOnProviderError"]


class UnsupportedOnProviderError(ReductoError):
    """A file type, option, or resource that a client for your own r-1 endpoint cannot serve.
    `feature` names it, for example "DOCX files" or "The `formatting.add_page_markers` option"."""

    def __init__(self, feature: str, kind: Literal["feature", "file_type"] = "feature") -> None:
        super().__init__(feature, kind)
        self.feature = feature
        self.kind = kind

    @override
    def __str__(self) -> str:
        if self.kind == "file_type":
            return (
                f"{self.feature} are not supported when you call your own r-1 endpoint. "
                "The hosted Reducto API parses them."
            )
        return (
            f"{self.feature} cannot be used when you call your own r-1 endpoint. "
            "Use the hosted Reducto API, or contact Reducto for a VPC deployment."
        )


class PageParseError(ReductoError):
    """One or more pages of the document failed, so the parse failed. The client raises it after the other
    pages finish. `failed_pages` gives the page number and reason of each failed page. `partial_response`
    holds the pages that succeeded, or is None when no page succeeded."""

    def __init__(
        self, message: str, failed_pages: List[FailedPage], partial_response: Optional[ProviderParseResponse]
    ) -> None:
        super().__init__(message, failed_pages, partial_response)
        self.message = message
        self.failed_pages = failed_pages
        self.partial_response = partial_response

    @override
    def __str__(self) -> str:
        return self.message


class PageError(Exception):
    """One page cannot be rendered, decoded, or encoded. Only that page fails."""
