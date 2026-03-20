# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from typing_extensions import Required, TypeAlias, TypedDict

from .._types import SequenceNotStr
from .enhance_param import EnhanceParam
from .settings_param import SettingsParam
from .retrieval_param import RetrievalParam
from .formatting_param import FormattingParam
from .spreadsheet_param import SpreadsheetParam
from .async_config_v3_param import AsyncConfigV3Param
from .upload_response_param import UploadResponseParam

__all__ = ["AsyncParseConfigParam", "Input"]

Input: TypeAlias = Union[str, SequenceNotStr[str], UploadResponseParam]

_AsyncParseConfigParamReservedKeywords = TypedDict(
    "_AsyncParseConfigParamReservedKeywords",
    {
        "async": AsyncConfigV3Param,
    },
    total=False,
)


class AsyncParseConfigParam(_AsyncParseConfigParamReservedKeywords, total=False):
    input: Required[Input]
    """For parse/split/extract pipelines, the URL of the document to be processed.

    You can provide one of the following: 1. A publicly available URL 2. A presigned
    S3 URL 3. A reducto:// prefixed URL obtained from the /upload endpoint after
    directly uploading a document 4. A jobid:// prefixed URL obtained from a
    previous /parse invocation 5. A list of URLs (for multi-document pipelines, V3
    API only)

                For edit pipelines, this should be a string containing the edit instructions
    """

    enhance: EnhanceParam

    formatting: FormattingParam

    retrieval: RetrievalParam

    settings: SettingsParam

    spreadsheet: SpreadsheetParam
