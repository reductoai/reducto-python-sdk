# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Any, cast
from typing_extensions import overload

import httpx

from ..types import parse_run_params, parse_run_job_params
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
from ..types.parse_run_response import ParseRunResponse
from ..types.shared_params.enhance import Enhance
from ..types.parse_run_job_response import ParseRunJobResponse
from ..types.shared_params.settings import Settings
from ..types.shared_params.retrieval import Retrieval
from ..types.shared_params.formatting import Formatting
from ..types.shared_params.spreadsheet import Spreadsheet
from ..types.shared_params.config_v3_async_config import ConfigV3AsyncConfig

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
    def run(
        self,
        *,
        input: parse_run_params.SyncParseConfigInput,
        enhance: Enhance | Omit = omit,
        formatting: Formatting | Omit = omit,
        retrieval: Retrieval | Omit = omit,
        settings: Settings | Omit = omit,
        spreadsheet: Spreadsheet | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ParseRunResponse:
        """
        Parse

        Args:
          input: For parse/split/extract pipelines, the URL of the document to be processed. You
              can provide one of the following: 1. A publicly available URL 2. A presigned S3
              URL 3. A reducto:// prefixed URL obtained from the /upload endpoint after
              directly uploading a document 4. A jobid:// prefixed URL obtained from a
              previous /parse invocation

                          For edit pipelines, this should be a string containing the edit instructions

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def run(
        self,
        *,
        input: parse_run_params.AsyncParseConfigInput,
        async_: ConfigV3AsyncConfig | Omit = omit,
        enhance: Enhance | Omit = omit,
        formatting: Formatting | Omit = omit,
        retrieval: Retrieval | Omit = omit,
        settings: Settings | Omit = omit,
        spreadsheet: Spreadsheet | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ParseRunResponse:
        """
        Parse

        Args:
          input: For parse/split/extract pipelines, the URL of the document to be processed. You
              can provide one of the following: 1. A publicly available URL 2. A presigned S3
              URL 3. A reducto:// prefixed URL obtained from the /upload endpoint after
              directly uploading a document 4. A jobid:// prefixed URL obtained from a
              previous /parse invocation

                          For edit pipelines, this should be a string containing the edit instructions

          async_: The configuration options for asynchronous processing (default synchronous).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @required_args(["input"])
    def run(
        self,
        *,
        input: parse_run_params.SyncParseConfigInput | parse_run_params.AsyncParseConfigInput,
        enhance: Enhance | Omit = omit,
        formatting: Formatting | Omit = omit,
        retrieval: Retrieval | Omit = omit,
        settings: Settings | Omit = omit,
        spreadsheet: Spreadsheet | Omit = omit,
        async_: ConfigV3AsyncConfig | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ParseRunResponse:
        return cast(
            ParseRunResponse,
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
                    parse_run_params.ParseRunParams,
                ),
                options=make_request_options(
                    extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
                ),
                cast_to=cast(Any, ParseRunResponse),  # Union types cannot be passed in as arguments in the type system
            ),
        )

    def run_job(
        self,
        *,
        input: parse_run_job_params.Input,
        async_: ConfigV3AsyncConfig | Omit = omit,
        enhance: Enhance | Omit = omit,
        formatting: Formatting | Omit = omit,
        retrieval: Retrieval | Omit = omit,
        settings: Settings | Omit = omit,
        spreadsheet: Spreadsheet | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ParseRunJobResponse:
        """
        Async Parse

        Args:
          input: For parse/split/extract pipelines, the URL of the document to be processed. You
              can provide one of the following: 1. A publicly available URL 2. A presigned S3
              URL 3. A reducto:// prefixed URL obtained from the /upload endpoint after
              directly uploading a document 4. A jobid:// prefixed URL obtained from a
              previous /parse invocation

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
                parse_run_job_params.ParseRunJobParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ParseRunJobResponse,
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
    async def run(
        self,
        *,
        input: parse_run_params.SyncParseConfigInput,
        enhance: Enhance | Omit = omit,
        formatting: Formatting | Omit = omit,
        retrieval: Retrieval | Omit = omit,
        settings: Settings | Omit = omit,
        spreadsheet: Spreadsheet | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ParseRunResponse:
        """
        Parse

        Args:
          input: For parse/split/extract pipelines, the URL of the document to be processed. You
              can provide one of the following: 1. A publicly available URL 2. A presigned S3
              URL 3. A reducto:// prefixed URL obtained from the /upload endpoint after
              directly uploading a document 4. A jobid:// prefixed URL obtained from a
              previous /parse invocation

                          For edit pipelines, this should be a string containing the edit instructions

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def run(
        self,
        *,
        input: parse_run_params.AsyncParseConfigInput,
        async_: ConfigV3AsyncConfig | Omit = omit,
        enhance: Enhance | Omit = omit,
        formatting: Formatting | Omit = omit,
        retrieval: Retrieval | Omit = omit,
        settings: Settings | Omit = omit,
        spreadsheet: Spreadsheet | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ParseRunResponse:
        """
        Parse

        Args:
          input: For parse/split/extract pipelines, the URL of the document to be processed. You
              can provide one of the following: 1. A publicly available URL 2. A presigned S3
              URL 3. A reducto:// prefixed URL obtained from the /upload endpoint after
              directly uploading a document 4. A jobid:// prefixed URL obtained from a
              previous /parse invocation

                          For edit pipelines, this should be a string containing the edit instructions

          async_: The configuration options for asynchronous processing (default synchronous).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @required_args(["input"])
    async def run(
        self,
        *,
        input: parse_run_params.SyncParseConfigInput | parse_run_params.AsyncParseConfigInput,
        enhance: Enhance | Omit = omit,
        formatting: Formatting | Omit = omit,
        retrieval: Retrieval | Omit = omit,
        settings: Settings | Omit = omit,
        spreadsheet: Spreadsheet | Omit = omit,
        async_: ConfigV3AsyncConfig | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ParseRunResponse:
        return cast(
            ParseRunResponse,
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
                    parse_run_params.ParseRunParams,
                ),
                options=make_request_options(
                    extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
                ),
                cast_to=cast(Any, ParseRunResponse),  # Union types cannot be passed in as arguments in the type system
            ),
        )

    async def run_job(
        self,
        *,
        input: parse_run_job_params.Input,
        async_: ConfigV3AsyncConfig | Omit = omit,
        enhance: Enhance | Omit = omit,
        formatting: Formatting | Omit = omit,
        retrieval: Retrieval | Omit = omit,
        settings: Settings | Omit = omit,
        spreadsheet: Spreadsheet | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ParseRunJobResponse:
        """
        Async Parse

        Args:
          input: For parse/split/extract pipelines, the URL of the document to be processed. You
              can provide one of the following: 1. A publicly available URL 2. A presigned S3
              URL 3. A reducto:// prefixed URL obtained from the /upload endpoint after
              directly uploading a document 4. A jobid:// prefixed URL obtained from a
              previous /parse invocation

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
                parse_run_job_params.ParseRunJobParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ParseRunJobResponse,
        )


class ParseResourceWithRawResponse:
    def __init__(self, parse: ParseResource) -> None:
        self._parse = parse

        self.run = to_raw_response_wrapper(
            parse.run,
        )
        self.run_job = to_raw_response_wrapper(
            parse.run_job,
        )


class AsyncParseResourceWithRawResponse:
    def __init__(self, parse: AsyncParseResource) -> None:
        self._parse = parse

        self.run = async_to_raw_response_wrapper(
            parse.run,
        )
        self.run_job = async_to_raw_response_wrapper(
            parse.run_job,
        )


class ParseResourceWithStreamingResponse:
    def __init__(self, parse: ParseResource) -> None:
        self._parse = parse

        self.run = to_streamed_response_wrapper(
            parse.run,
        )
        self.run_job = to_streamed_response_wrapper(
            parse.run_job,
        )


class AsyncParseResourceWithStreamingResponse:
    def __init__(self, parse: AsyncParseResource) -> None:
        self._parse = parse

        self.run = async_to_streamed_response_wrapper(
            parse.run,
        )
        self.run_job = async_to_streamed_response_wrapper(
            parse.run_job,
        )
