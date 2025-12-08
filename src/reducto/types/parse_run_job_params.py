# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from typing_extensions import Required, Annotated, TypeAlias, TypedDict

from .._utils import PropertyInfo
from .shared_params.upload import Upload
from .shared_params.enhance import Enhance
from .shared_params.settings import Settings
from .shared_params.retrieval import Retrieval
from .shared_params.formatting import Formatting
from .shared_params.spreadsheet import Spreadsheet
from .shared_params.config_v3_async_config import ConfigV3AsyncConfig

__all__ = ["ParseRunJobParams", "Input"]


class ParseRunJobParams(TypedDict, total=False):
    input: Required[Input]
    """For parse/split/extract pipelines, the URL of the document to be processed.

    You can provide one of the following: 1. A publicly available URL 2. A presigned
    S3 URL 3. A reducto:// prefixed URL obtained from the /upload endpoint after
    directly uploading a document 4. A jobid:// prefixed URL obtained from a
    previous /parse invocation

                For edit pipelines, this should be a string containing the edit instructions
    """

    async_: Annotated[ConfigV3AsyncConfig, PropertyInfo(alias="async")]
    """The configuration options for asynchronous processing (default synchronous)."""

    enhance: Enhance

    formatting: Formatting

    retrieval: Retrieval

    settings: Settings

    spreadsheet: Spreadsheet


Input: TypeAlias = Union[str, Upload]
