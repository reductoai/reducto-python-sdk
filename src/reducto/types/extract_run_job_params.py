# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from typing_extensions import Required, Annotated, TypeAlias, TypedDict

from .._utils import PropertyInfo
from .shared_params.upload import Upload
from .shared_params.parse_options import ParseOptions
from .shared_params.config_v3_async_config import ConfigV3AsyncConfig

__all__ = ["ExtractRunJobParams", "Input", "Instructions", "Settings", "SettingsCitations"]


class ExtractRunJobParams(TypedDict, total=False):
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

    instructions: Instructions
    """The instructions to use for the extraction."""

    parsing: ParseOptions
    """The configuration options for parsing the document.

    If you are passing in a jobid:// URL for the file, then this configuration will
    be ignored.
    """

    settings: Settings
    """The settings to use for the extraction."""


Input: TypeAlias = Union[str, Upload]


class Instructions(TypedDict, total=False):
    schema: object
    """The JSON schema to use for the extraction."""

    system_prompt: str
    """The system prompt to use for the extraction."""


class SettingsCitations(TypedDict, total=False):
    enabled: bool
    """If True, include citations in the extraction."""

    numerical_confidence: bool
    """If True, enable numeric citation confidence scores. Defaults to True."""


class Settings(TypedDict, total=False):
    array_extract: bool
    """If True, use array extraction."""

    citations: SettingsCitations
    """The citations to use for the extraction."""

    include_images: bool
    """If True, include images in the extraction."""

    optimize_for_latency: bool
    """
    If True, jobs will be processed with a higher throughput and priority at a
    higher cost. Defaults to False.
    """
