# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from typing_extensions import Required, TypeAlias, TypedDict

from .._types import SequenceNotStr
from .upload_response_param import UploadResponseParam
from .pipeline_settings_param import PipelineSettingsParam

__all__ = ["PipelineRunParams", "Input"]


class PipelineRunParams(TypedDict, total=False):
    input: Required[Input]
    """For parse/split/extract pipelines, the URL of the document to be processed.

    You can provide one of the following: 1. A publicly available URL 2. A presigned
    S3 URL 3. A reducto:// prefixed URL obtained from the /upload endpoint after
    directly uploading a document 4. A jobid:// prefixed URL obtained from a
    previous /parse invocation 5. A list of URLs (for multi-document pipelines, V3
    API only)

                For edit pipelines, this should be a string containing the edit instructions
    """

    pipeline_id: Required[str]
    """The ID of the pipeline to use for the document."""

    settings: PipelineSettingsParam
    """Settings for pipeline execution that override pipeline defaults."""


Input: TypeAlias = Union[str, SequenceNotStr[str], UploadResponseParam]
