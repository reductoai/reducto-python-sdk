# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable, Optional

import httpx

from ..types import classify_run_params
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
from ..types.shared.classify_response import ClassifyResponse

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

    def run(
        self,
        *,
        input: classify_run_params.Input,
        classification_schema: Iterable[classify_run_params.ClassificationSchema] | Omit = omit,
        document_metadata: Optional[str] | Omit = omit,
        page_range: Optional[classify_run_params.PageRange] | Omit = omit,
        persist_results: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ClassifyResponse:
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
                classify_run_params.ClassifyRunParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ClassifyResponse,
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

    async def run(
        self,
        *,
        input: classify_run_params.Input,
        classification_schema: Iterable[classify_run_params.ClassificationSchema] | Omit = omit,
        document_metadata: Optional[str] | Omit = omit,
        page_range: Optional[classify_run_params.PageRange] | Omit = omit,
        persist_results: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ClassifyResponse:
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
                classify_run_params.ClassifyRunParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ClassifyResponse,
        )


class ClassifyResourceWithRawResponse:
    def __init__(self, classify: ClassifyResource) -> None:
        self._classify = classify

        self.run = to_raw_response_wrapper(
            classify.run,
        )


class AsyncClassifyResourceWithRawResponse:
    def __init__(self, classify: AsyncClassifyResource) -> None:
        self._classify = classify

        self.run = async_to_raw_response_wrapper(
            classify.run,
        )


class ClassifyResourceWithStreamingResponse:
    def __init__(self, classify: ClassifyResource) -> None:
        self._classify = classify

        self.run = to_streamed_response_wrapper(
            classify.run,
        )


class AsyncClassifyResourceWithStreamingResponse:
    def __init__(self, classify: AsyncClassifyResource) -> None:
        self._classify = classify

        self.run = async_to_streamed_response_wrapper(
            classify.run,
        )
