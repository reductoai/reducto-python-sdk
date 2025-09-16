# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from typing_extensions import Required, TypeAlias, TypedDict

from .shared_params.upload import Upload

__all__ = ["PipelineRunParams", "DocumentURL"]


class PipelineRunParams(TypedDict, total=False):
    document_url: Required[DocumentURL]
    """The URL of the document to be processed.

    You can provide one of the following: 1. A publicly available URL 2. A presigned
    S3 URL 3. A reducto:// prefixed URL obtained from the /upload endpoint after
    directly uploading a document
    """

    pipeline_id: Required[str]
    """The ID of the pipeline to use for the document."""


DocumentURL: TypeAlias = Union[str, Upload]
