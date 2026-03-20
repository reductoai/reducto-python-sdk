# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

from .enhance_param import EnhanceParam
from .settings_param import SettingsParam
from .retrieval_param import RetrievalParam
from .formatting_param import FormattingParam
from .spreadsheet_param import SpreadsheetParam

__all__ = ["ParseOptionsParam"]


class ParseOptionsParam(TypedDict, total=False):
    enhance: EnhanceParam

    formatting: FormattingParam

    retrieval: RetrievalParam

    settings: SettingsParam

    spreadsheet: SpreadsheetParam
