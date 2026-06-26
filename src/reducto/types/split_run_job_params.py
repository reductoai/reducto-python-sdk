# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Iterable
from typing_extensions import Literal, Required, Annotated, TypeAlias, TypedDict

from .._types import SequenceNotStr
from .._utils import PropertyInfo
from .parse_options_param import ParseOptionsParam
from .shared_params.upload import Upload
from .split_category_param import SplitCategoryParam
from .async_config_v3_param import AsyncConfigV3Param

__all__ = ["SplitRunJobParams", "Input", "Settings"]


class SplitRunJobParams(TypedDict, total=False):
    input: Required[Input]
    """For parse/split/extract pipelines, the URL of the document to be processed.

    You can provide one of the following: 1. A publicly available URL 2. A presigned
    S3 URL 3. A reducto:// prefixed URL obtained from the /upload endpoint after
    directly uploading a document 4. A jobid:// prefixed URL obtained from a
    previous /parse invocation 5. A list of URLs (for multi-document pipelines, V3
    API only)

                For edit pipelines, this should be a string containing the edit instructions
    """

    split_description: Required[Iterable[SplitCategoryParam]]
    """The configuration options for processing the document."""

    async_: Annotated[AsyncConfigV3Param, PropertyInfo(alias="async")]
    """The configuration options for asynchronous processing (default synchronous)."""

    parsing: ParseOptionsParam
    """The configuration options for parsing the document.

    If you are passing in a jobid:// URL for the file, then this configuration will
    be ignored.
    """

    settings: Settings
    """The settings for split processing."""

    split_rules: str
    """The prompt that describes rules for splitting the document."""


Input: TypeAlias = Union[str, SequenceNotStr[str], Upload]


class Settings(TypedDict, total=False):
    """The settings for split processing."""

    allow_page_overlap: bool
    """If True, a page can belong to multiple categories/partitions.

    If False, each page must belong to exactly one category. Defaults to True.
    """

    deep_split: bool
    """If True, uses the deep split agent for higher-quality document splitting.

    Off by default.
    """

    force_url_result: bool
    """Force the endpoint result to be returned in URL form."""

    table_cutoff: Literal["truncate", "preserve"]
    """
    If tables should be truncated to the first few rows or if all content should be
    preserved. truncate improves latency, preserve is recommended for cases where
    partition_key is being used and the partition_key may be included within the
    table. Defaults to truncate
    """
