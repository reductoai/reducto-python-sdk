# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Iterable
from typing_extensions import Literal, Required, Annotated, TypeAlias, TypedDict

from .._utils import PropertyInfo
from .shared_params.upload import Upload
from .shared_params.parse_options import ParseOptions
from .shared_params.split_category import SplitCategory
from .shared_params.config_v3_async_config import ConfigV3AsyncConfig

__all__ = ["SplitRunJobParams", "Input", "Settings"]


class SplitRunJobParams(TypedDict, total=False):
    input: Required[Input]
    """For parse/split/extract pipelines, the URL of the document to be processed.

    You can provide one of the following: 1. A publicly available URL 2. A presigned
    S3 URL 3. A reducto:// prefixed URL obtained from the /upload endpoint after
    directly uploading a document 4. A jobid:// prefixed URL obtained from a
    previous /parse invocation

                For edit pipelines, this should be a string containing the edit instructions
    """

    split_description: Required[Iterable[SplitCategory]]
    """The configuration options for processing the document."""

    async_: Annotated[ConfigV3AsyncConfig, PropertyInfo(alias="async")]
    """The configuration options for asynchronous processing (default synchronous)."""

    parsing: ParseOptions
    """The configuration options for parsing the document.

    If you are passing in a jobid:// URL for the file, then this configuration will
    be ignored.
    """

    settings: Settings
    """The settings for split processing."""

    split_rules: str
    """The prompt that describes rules for splitting the document."""


Input: TypeAlias = Union[str, Upload]


class Settings(TypedDict, total=False):
    table_cutoff: Literal["truncate", "preserve"]
    """
    If tables should be truncated to the first few rows or if all content should be
    preserved. truncate improves latency, preserve is recommended for cases where
    partition_key is being used and the partition_key may be included within the
    table. Defaults to truncate
    """
