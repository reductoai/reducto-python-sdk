# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .enhance import Enhance
from .settings import Settings
from ..._models import BaseModel
from .retrieval import Retrieval
from .formatting import Formatting
from .spreadsheet import Spreadsheet

__all__ = ["ParseOptions"]


class ParseOptions(BaseModel):
    enhance: Optional[Enhance] = None

    formatting: Optional[Formatting] = None

    retrieval: Optional[Retrieval] = None

    settings: Optional[Settings] = None

    spreadsheet: Optional[Spreadsheet] = None
