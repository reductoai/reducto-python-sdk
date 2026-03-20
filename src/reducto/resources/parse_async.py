# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..types import parse_async_create_params
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
from ..types.enhance_param import EnhanceParam
from ..types.settings_param import SettingsParam
from ..types.retrieval_param import RetrievalParam
from ..types.formatting_param import FormattingParam
from ..types.spreadsheet_param import SpreadsheetParam
from ..types.async_parse_response import AsyncParseResponse
from ..types.async_config_v3_param import AsyncConfigV3Param

__all__ = ["ParseAsyncResource", "AsyncParseAsyncResource"]


class ParseAsyncResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ParseAsyncResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/reductoai/reducto-python-sdk#accessing-raw-response-data-eg-headers
        """
        return ParseAsyncResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ParseAsyncResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/reductoai/reducto-python-sdk#with_streaming_response
        """
        return ParseAsyncResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        input: parse_async_create_params.Input,
        async_: AsyncConfigV3Param | Omit = omit,
        enhance: EnhanceParam | Omit = omit,
        formatting: FormattingParam | Omit = omit,
        retrieval: RetrievalParam | Omit = omit,
        settings: SettingsParam | Omit = omit,
        spreadsheet: SpreadsheetParam | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncParseResponse:
        """
        Async Parse

        Args:
          input: For parse/split/extract pipelines, the URL of the document to be processed. You
              can provide one of the following: 1. A publicly available URL 2. A presigned S3
              URL 3. A reducto:// prefixed URL obtained from the /upload endpoint after
              directly uploading a document 4. A jobid:// prefixed URL obtained from a
              previous /parse invocation 5. A list of URLs (for multi-document pipelines, V3
              API only)

                          For edit pipelines, this should be a string containing the edit instructions

          async_: The configuration options for asynchronous processing (default synchronous).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/parse_async",
            body=maybe_transform(
                {
                    "input": input,
                    "async_": async_,
                    "enhance": enhance,
                    "formatting": formatting,
                    "retrieval": retrieval,
                    "settings": settings,
                    "spreadsheet": spreadsheet,
                },
                parse_async_create_params.ParseAsyncCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AsyncParseResponse,
        )


class AsyncParseAsyncResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncParseAsyncResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/reductoai/reducto-python-sdk#accessing-raw-response-data-eg-headers
        """
        return AsyncParseAsyncResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncParseAsyncResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/reductoai/reducto-python-sdk#with_streaming_response
        """
        return AsyncParseAsyncResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        input: parse_async_create_params.Input,
        async_: AsyncConfigV3Param | Omit = omit,
        enhance: EnhanceParam | Omit = omit,
        formatting: FormattingParam | Omit = omit,
        retrieval: RetrievalParam | Omit = omit,
        settings: SettingsParam | Omit = omit,
        spreadsheet: SpreadsheetParam | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncParseResponse:
        """
        Async Parse

        Args:
          input: For parse/split/extract pipelines, the URL of the document to be processed. You
              can provide one of the following: 1. A publicly available URL 2. A presigned S3
              URL 3. A reducto:// prefixed URL obtained from the /upload endpoint after
              directly uploading a document 4. A jobid:// prefixed URL obtained from a
              previous /parse invocation 5. A list of URLs (for multi-document pipelines, V3
              API only)

                          For edit pipelines, this should be a string containing the edit instructions

          async_: The configuration options for asynchronous processing (default synchronous).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/parse_async",
            body=await async_maybe_transform(
                {
                    "input": input,
                    "async_": async_,
                    "enhance": enhance,
                    "formatting": formatting,
                    "retrieval": retrieval,
                    "settings": settings,
                    "spreadsheet": spreadsheet,
                },
                parse_async_create_params.ParseAsyncCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AsyncParseResponse,
        )


class ParseAsyncResourceWithRawResponse:
    def __init__(self, parse_async: ParseAsyncResource) -> None:
        self._parse_async = parse_async

        self.create = to_raw_response_wrapper(
            parse_async.create,
        )


class AsyncParseAsyncResourceWithRawResponse:
    def __init__(self, parse_async: AsyncParseAsyncResource) -> None:
        self._parse_async = parse_async

        self.create = async_to_raw_response_wrapper(
            parse_async.create,
        )


class ParseAsyncResourceWithStreamingResponse:
    def __init__(self, parse_async: ParseAsyncResource) -> None:
        self._parse_async = parse_async

        self.create = to_streamed_response_wrapper(
            parse_async.create,
        )


class AsyncParseAsyncResourceWithStreamingResponse:
    def __init__(self, parse_async: AsyncParseAsyncResource) -> None:
        self._parse_async = parse_async

        self.create = async_to_streamed_response_wrapper(
            parse_async.create,
        )
