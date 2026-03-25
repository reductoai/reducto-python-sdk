# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from typing_extensions import Literal, Required, Annotated, TypeAlias, TypedDict

from .._types import SequenceNotStr
from .._utils import PropertyInfo
from .enhance_param import EnhanceParam
from .settings_param import SettingsParam
from .retrieval_param import RetrievalParam
from .formatting_param import FormattingParam
from .spreadsheet_param import SpreadsheetParam
from .shared_params.upload import Upload
from .async_config_v3_param import AsyncConfigV3Param

__all__ = ["ParseRunJobParams", "Input"]


class ParseRunJobParams(TypedDict, total=False):
    input: Required[Input]
    """For parse/split/extract pipelines, the URL of the document to be processed.

    You can provide one of the following: 1. A publicly available URL 2. A presigned
    S3 URL 3. A reducto:// prefixed URL obtained from the /upload endpoint after
    directly uploading a document 4. A jobid:// prefixed URL obtained from a
    previous /parse invocation 5. A list of URLs (for multi-document pipelines, V3
    API only)

                For edit pipelines, this should be a string containing the edit instructions
    """

    async_: Annotated[AsyncConfigV3Param, PropertyInfo(alias="async")]
    """The configuration options for asynchronous processing (default synchronous)."""

    enhance: EnhanceParam

    formatting: FormattingParam

    queue_priority: Literal["auto", "batch"]
    """Queue priority.

    'batch' for non-urgent work that processes when spare GPU capacity is available.
    """

    retrieval: RetrievalParam

    settings: SettingsParam

    spreadsheet: SpreadsheetParam


Input: TypeAlias = Union[str, SequenceNotStr[str], Upload]
