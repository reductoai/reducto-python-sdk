# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Iterable
from typing_extensions import Required, TypeAlias, TypedDict

from .._types import SequenceNotStr
from .parse_options_param import ParseOptionsParam
from .shared_params.upload import Upload
from .split_category_param import SplitCategoryParam
from .split_table_options_param import SplitTableOptionsParam

__all__ = ["SplitRunParams", "Input"]


class SplitRunParams(TypedDict, total=False):
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

    parsing: ParseOptionsParam
    """The configuration options for parsing the document.

    If you are passing in a jobid:// URL for the file, then this configuration will
    be ignored.
    """

    settings: SplitTableOptionsParam
    """The settings for split processing."""

    split_rules: str
    """The prompt that describes rules for splitting the document."""


Input: TypeAlias = Union[str, SequenceNotStr[str], Upload]
