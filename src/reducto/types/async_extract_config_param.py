# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from typing_extensions import Required, TypeAlias, TypedDict

from .._types import SequenceNotStr
from .instructions_param import InstructionsParam
from .parse_options_param import ParseOptionsParam
from .shared_params.upload import Upload
from .async_config_v3_param import AsyncConfigV3Param
from .extract_settings_param import ExtractSettingsParam

__all__ = ["AsyncExtractConfigParam", "Input"]

Input: TypeAlias = Union[str, SequenceNotStr[str], Upload]

_AsyncExtractConfigParamReservedKeywords = TypedDict(
    "_AsyncExtractConfigParamReservedKeywords",
    {
        "async": AsyncConfigV3Param,
    },
    total=False,
)


class AsyncExtractConfigParam(_AsyncExtractConfigParamReservedKeywords, total=False):
    input: Required[Input]
    """For parse/split/extract pipelines, the URL of the document to be processed.

    You can provide one of the following: 1. A publicly available URL 2. A presigned
    S3 URL 3. A reducto:// prefixed URL obtained from the /upload endpoint after
    directly uploading a document 4. A jobid:// prefixed URL obtained from a
    previous /parse invocation 5. A list of URLs (for multi-document pipelines, V3
    API only)

                For edit pipelines, this should be a string containing the edit instructions
    """

    instructions: InstructionsParam
    """The instructions to use for the extraction."""

    parsing: ParseOptionsParam
    """The configuration options for parsing the document.

    If you are passing in a jobid:// URL for the file, then this configuration will
    be ignored.
    """

    settings: ExtractSettingsParam
    """The settings to use for the extraction."""
