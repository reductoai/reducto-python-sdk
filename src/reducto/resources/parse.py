# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Any, cast
from typing_extensions import overload

import httpx

from ..types import parse_create_params
from .._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from .._utils import required_args, maybe_transform, async_maybe_transform
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
from ..types.async_config_v3_param import AsyncConfigV3Param
from ..types.parse_create_response import ParseCreateResponse

__all__ = ["ParseResource", "AsyncParseResource"]


class ParseResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ParseResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/reductoai/reducto-python-sdk#accessing-raw-response-data-eg-headers
        """
        return ParseResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ParseResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/reductoai/reducto-python-sdk#with_streaming_response
        """
        return ParseResourceWithStreamingResponse(self)

    @overload
    def create(
        self,
        *,
        input: parse_create_params.SyncParseConfigInput,
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
    ) -> ParseCreateResponse:
        """
        Parse

        Args:
          input: For parse/split/extract pipelines, the URL of the document to be processed. You
              can provide one of the following: 1. A publicly available URL 2. A presigned S3
              URL 3. A reducto:// prefixed URL obtained from the /upload endpoint after
              directly uploading a document 4. A jobid:// prefixed URL obtained from a
              previous /parse invocation 5. A list of URLs (for multi-document pipelines, V3
              API only)

                          For edit pipelines, this should be a string containing the edit instructions

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def create(
        self,
        *,
        input: parse_create_params.AsyncParseConfigInput,
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
    ) -> ParseCreateResponse:
        """
        Parse

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
        ...

    @required_args(["input"])
    def create(
        self,
        *,
        input: parse_create_params.SyncParseConfigInput | parse_create_params.AsyncParseConfigInput,
        enhance: EnhanceParam | Omit = omit,
        formatting: FormattingParam | Omit = omit,
        retrieval: RetrievalParam | Omit = omit,
        settings: SettingsParam | Omit = omit,
        spreadsheet: SpreadsheetParam | Omit = omit,
        async_: AsyncConfigV3Param | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ParseCreateResponse:
        return cast(
            ParseCreateResponse,
            self._post(
                "/parse",
                body=maybe_transform(
                    {
                        "input": input,
                        "enhance": enhance,
                        "formatting": formatting,
                        "retrieval": retrieval,
                        "settings": settings,
                        "spreadsheet": spreadsheet,
                        "async_": async_,
                    },
                    parse_create_params.ParseCreateParams,
                ),
                options=make_request_options(
                    extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
                ),
                cast_to=cast(
                    Any, ParseCreateResponse
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )


class AsyncParseResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncParseResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/reductoai/reducto-python-sdk#accessing-raw-response-data-eg-headers
        """
        return AsyncParseResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncParseResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/reductoai/reducto-python-sdk#with_streaming_response
        """
        return AsyncParseResourceWithStreamingResponse(self)

    @overload
    async def create(
        self,
        *,
        input: parse_create_params.SyncParseConfigInput,
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
    ) -> ParseCreateResponse:
        """
        Parse

        Args:
          input: For parse/split/extract pipelines, the URL of the document to be processed. You
              can provide one of the following: 1. A publicly available URL 2. A presigned S3
              URL 3. A reducto:// prefixed URL obtained from the /upload endpoint after
              directly uploading a document 4. A jobid:// prefixed URL obtained from a
              previous /parse invocation 5. A list of URLs (for multi-document pipelines, V3
              API only)

                          For edit pipelines, this should be a string containing the edit instructions

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def create(
        self,
        *,
        input: parse_create_params.AsyncParseConfigInput,
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
    ) -> ParseCreateResponse:
        """
        Parse

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
        ...

    @required_args(["input"])
    async def create(
        self,
        *,
        input: parse_create_params.SyncParseConfigInput | parse_create_params.AsyncParseConfigInput,
        enhance: EnhanceParam | Omit = omit,
        formatting: FormattingParam | Omit = omit,
        retrieval: RetrievalParam | Omit = omit,
        settings: SettingsParam | Omit = omit,
        spreadsheet: SpreadsheetParam | Omit = omit,
        async_: AsyncConfigV3Param | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ParseCreateResponse:
        return cast(
            ParseCreateResponse,
            await self._post(
                "/parse",
                body=await async_maybe_transform(
                    {
                        "input": input,
                        "enhance": enhance,
                        "formatting": formatting,
                        "retrieval": retrieval,
                        "settings": settings,
                        "spreadsheet": spreadsheet,
                        "async_": async_,
                    },
                    parse_create_params.ParseCreateParams,
                ),
                options=make_request_options(
                    extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
                ),
                cast_to=cast(
                    Any, ParseCreateResponse
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )


class ParseResourceWithRawResponse:
    def __init__(self, parse: ParseResource) -> None:
        self._parse = parse

        self.create = to_raw_response_wrapper(
            parse.create,
        )


class AsyncParseResourceWithRawResponse:
    def __init__(self, parse: AsyncParseResource) -> None:
        self._parse = parse

        self.create = async_to_raw_response_wrapper(
            parse.create,
        )


class ParseResourceWithStreamingResponse:
    def __init__(self, parse: ParseResource) -> None:
        self._parse = parse

        self.create = to_streamed_response_wrapper(
            parse.create,
        )


class AsyncParseResourceWithStreamingResponse:
    def __init__(self, parse: AsyncParseResource) -> None:
        self._parse = parse

        self.create = async_to_streamed_response_wrapper(
            parse.create,
        )
