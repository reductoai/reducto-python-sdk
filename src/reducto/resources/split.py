# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable

import httpx

from ..types import split_create_params
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
from ..types.split_response import SplitResponse
from ..types.parse_options_param import ParseOptionsParam
from ..types.split_category_param import SplitCategoryParam
from ..types.split_table_options_param import SplitTableOptionsParam

__all__ = ["SplitResource", "AsyncSplitResource"]


class SplitResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> SplitResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/reductoai/reducto-python-sdk#accessing-raw-response-data-eg-headers
        """
        return SplitResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> SplitResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/reductoai/reducto-python-sdk#with_streaming_response
        """
        return SplitResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        input: split_create_params.Input,
        split_description: Iterable[SplitCategoryParam],
        parsing: ParseOptionsParam | Omit = omit,
        settings: SplitTableOptionsParam | Omit = omit,
        split_rules: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SplitResponse:
        """
        Split

        Args:
          input: For parse/split/extract pipelines, the URL of the document to be processed. You
              can provide one of the following: 1. A publicly available URL 2. A presigned S3
              URL 3. A reducto:// prefixed URL obtained from the /upload endpoint after
              directly uploading a document 4. A jobid:// prefixed URL obtained from a
              previous /parse invocation 5. A list of URLs (for multi-document pipelines, V3
              API only)

                          For edit pipelines, this should be a string containing the edit instructions

          split_description: The configuration options for processing the document.

          parsing: The configuration options for parsing the document. If you are passing in a
              jobid:// URL for the file, then this configuration will be ignored.

          settings: The settings for split processing.

          split_rules: The prompt that describes rules for splitting the document.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/split",
            body=maybe_transform(
                {
                    "input": input,
                    "split_description": split_description,
                    "parsing": parsing,
                    "settings": settings,
                    "split_rules": split_rules,
                },
                split_create_params.SplitCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SplitResponse,
        )


class AsyncSplitResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncSplitResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/reductoai/reducto-python-sdk#accessing-raw-response-data-eg-headers
        """
        return AsyncSplitResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncSplitResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/reductoai/reducto-python-sdk#with_streaming_response
        """
        return AsyncSplitResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        input: split_create_params.Input,
        split_description: Iterable[SplitCategoryParam],
        parsing: ParseOptionsParam | Omit = omit,
        settings: SplitTableOptionsParam | Omit = omit,
        split_rules: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SplitResponse:
        """
        Split

        Args:
          input: For parse/split/extract pipelines, the URL of the document to be processed. You
              can provide one of the following: 1. A publicly available URL 2. A presigned S3
              URL 3. A reducto:// prefixed URL obtained from the /upload endpoint after
              directly uploading a document 4. A jobid:// prefixed URL obtained from a
              previous /parse invocation 5. A list of URLs (for multi-document pipelines, V3
              API only)

                          For edit pipelines, this should be a string containing the edit instructions

          split_description: The configuration options for processing the document.

          parsing: The configuration options for parsing the document. If you are passing in a
              jobid:// URL for the file, then this configuration will be ignored.

          settings: The settings for split processing.

          split_rules: The prompt that describes rules for splitting the document.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/split",
            body=await async_maybe_transform(
                {
                    "input": input,
                    "split_description": split_description,
                    "parsing": parsing,
                    "settings": settings,
                    "split_rules": split_rules,
                },
                split_create_params.SplitCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SplitResponse,
        )


class SplitResourceWithRawResponse:
    def __init__(self, split: SplitResource) -> None:
        self._split = split

        self.create = to_raw_response_wrapper(
            split.create,
        )


class AsyncSplitResourceWithRawResponse:
    def __init__(self, split: AsyncSplitResource) -> None:
        self._split = split

        self.create = async_to_raw_response_wrapper(
            split.create,
        )


class SplitResourceWithStreamingResponse:
    def __init__(self, split: SplitResource) -> None:
        self._split = split

        self.create = to_streamed_response_wrapper(
            split.create,
        )


class AsyncSplitResourceWithStreamingResponse:
    def __init__(self, split: AsyncSplitResource) -> None:
        self._split = split

        self.create = async_to_streamed_response_wrapper(
            split.create,
        )
