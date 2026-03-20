# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable, Optional

import httpx

from ..types import classify_create_params
from .._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from .._utils import maybe_transform, async_maybe_transform
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._base_client import make_request_options
from ..types.classify_create_response import ClassifyCreateResponse

__all__ = ["ClassifyResource", "AsyncClassifyResource"]


class ClassifyResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ClassifyResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/reductoai/reducto-python-sdk#accessing-raw-response-data-eg-headers
        """
        return ClassifyResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ClassifyResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/reductoai/reducto-python-sdk#with_streaming_response
        """
        return ClassifyResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        input: classify_create_params.Input,
        classification_schema: Iterable[classify_create_params.ClassificationSchema] | Omit = omit,
        document_metadata: Optional[str] | Omit = omit,
        page_range: Optional[classify_create_params.PageRange] | Omit = omit,
        persist_results: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ClassifyCreateResponse:
        """
        Classify

        Args:
          input: For parse/split/extract pipelines, the URL of the document to be processed. You
              can provide one of the following: 1. A publicly available URL 2. A presigned S3
              URL 3. A reducto:// prefixed URL obtained from the /upload endpoint after
              directly uploading a document 4. A jobid:// prefixed URL obtained from a
              previous /parse invocation 5. A list of URLs (for multi-document pipelines, V3
              API only)

                          For edit pipelines, this should be a string containing the edit instructions

          classification_schema: A list of classification categories and their matching criteria.

          document_metadata: Optional document-level metadata to include in classification prompts.

          page_range: The page range to process (1-indexed). By default, the first 5 pages are used.
              If more than 25 pages are selected, only the first 25 (after sorting) are used.
              Only applies to PDFs; ignored for other document types.

          persist_results: If True, persist the results indefinitely. Defaults to False.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/classify",
            body=maybe_transform(
                {
                    "input": input,
                    "classification_schema": classification_schema,
                    "document_metadata": document_metadata,
                    "page_range": page_range,
                    "persist_results": persist_results,
                },
                classify_create_params.ClassifyCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ClassifyCreateResponse,
        )


class AsyncClassifyResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncClassifyResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/reductoai/reducto-python-sdk#accessing-raw-response-data-eg-headers
        """
        return AsyncClassifyResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncClassifyResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/reductoai/reducto-python-sdk#with_streaming_response
        """
        return AsyncClassifyResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        input: classify_create_params.Input,
        classification_schema: Iterable[classify_create_params.ClassificationSchema] | Omit = omit,
        document_metadata: Optional[str] | Omit = omit,
        page_range: Optional[classify_create_params.PageRange] | Omit = omit,
        persist_results: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ClassifyCreateResponse:
        """
        Classify

        Args:
          input: For parse/split/extract pipelines, the URL of the document to be processed. You
              can provide one of the following: 1. A publicly available URL 2. A presigned S3
              URL 3. A reducto:// prefixed URL obtained from the /upload endpoint after
              directly uploading a document 4. A jobid:// prefixed URL obtained from a
              previous /parse invocation 5. A list of URLs (for multi-document pipelines, V3
              API only)

                          For edit pipelines, this should be a string containing the edit instructions

          classification_schema: A list of classification categories and their matching criteria.

          document_metadata: Optional document-level metadata to include in classification prompts.

          page_range: The page range to process (1-indexed). By default, the first 5 pages are used.
              If more than 25 pages are selected, only the first 25 (after sorting) are used.
              Only applies to PDFs; ignored for other document types.

          persist_results: If True, persist the results indefinitely. Defaults to False.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/classify",
            body=await async_maybe_transform(
                {
                    "input": input,
                    "classification_schema": classification_schema,
                    "document_metadata": document_metadata,
                    "page_range": page_range,
                    "persist_results": persist_results,
                },
                classify_create_params.ClassifyCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ClassifyCreateResponse,
        )


class ClassifyResourceWithRawResponse:
    def __init__(self, classify: ClassifyResource) -> None:
        self._classify = classify

        self.create = to_raw_response_wrapper(
            classify.create,
        )


class AsyncClassifyResourceWithRawResponse:
    def __init__(self, classify: AsyncClassifyResource) -> None:
        self._classify = classify

        self.create = async_to_raw_response_wrapper(
            classify.create,
        )


class ClassifyResourceWithStreamingResponse:
    def __init__(self, classify: ClassifyResource) -> None:
        self._classify = classify

        self.create = to_streamed_response_wrapper(
            classify.create,
        )


class AsyncClassifyResourceWithStreamingResponse:
    def __init__(self, classify: AsyncClassifyResource) -> None:
        self._classify = classify

        self.create = async_to_streamed_response_wrapper(
            classify.create,
        )
