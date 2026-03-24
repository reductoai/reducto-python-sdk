# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

from .enhance import Enhance
from .settings import Settings
from .retrieval import Retrieval
from .formatting import Formatting
from .spreadsheet import Spreadsheet

__all__ = ["ParseOptions"]


class ParseOptions(TypedDict, total=False):
    enhance: Enhance

    formatting: Formatting

    retrieval: Retrieval

    settings: Settings

    spreadsheet: Spreadsheet
