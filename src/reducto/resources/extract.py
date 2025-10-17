# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Any, cast
from typing_extensions import overload

import httpx

from ..types import extract_run_params, extract_run_job_params
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
from ..types.extract_run_response import ExtractRunResponse
from ..types.extract_run_job_response import ExtractRunJobResponse
from ..types.shared_params.parse_options import ParseOptions
from ..types.shared_params.config_v3_async_config import ConfigV3AsyncConfig

__all__ = ["ExtractResource", "AsyncExtractResource"]


class ExtractResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ExtractResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/reductoai/reducto-python-sdk#accessing-raw-response-data-eg-headers
        """
        return ExtractResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ExtractResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/reductoai/reducto-python-sdk#with_streaming_response
        """
        return ExtractResourceWithStreamingResponse(self)

    @overload
    def run(
        self,
        *,
        input: extract_run_params.SyncExtractConfigInput,
        instructions: extract_run_params.SyncExtractConfigInstructions | Omit = omit,
        parsing: ParseOptions | Omit = omit,
        settings: extract_run_params.SyncExtractConfigSettings | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ExtractRunResponse:
        """
        Extract

        Args:
          input: For parse/split/extract pipelines, the URL of the document to be processed. You
              can provide one of the following: 1. A publicly available URL 2. A presigned S3
              URL 3. A reducto:// prefixed URL obtained from the /upload endpoint after
              directly uploading a document 4. A jobid:// prefixed URL obtained from a
              previous /parse invocation

                          For edit pipelines, this should be a string containing the edit instructions

          instructions: The instructions to use for the extraction.

          parsing: The configuration options for parsing the document. If you are passing in a
              jobid:// URL for the file, then this configuration will be ignored.

          settings: The settings to use for the extraction.

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
        input: extract_run_params.AsyncExtractConfigInput,
        async_: ConfigV3AsyncConfig | Omit = omit,
        instructions: extract_run_params.AsyncExtractConfigInstructions | Omit = omit,
        parsing: ParseOptions | Omit = omit,
        settings: extract_run_params.AsyncExtractConfigSettings | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ExtractRunResponse:
        """
        Extract

        Args:
          input: For parse/split/extract pipelines, the URL of the document to be processed. You
              can provide one of the following: 1. A publicly available URL 2. A presigned S3
              URL 3. A reducto:// prefixed URL obtained from the /upload endpoint after
              directly uploading a document 4. A jobid:// prefixed URL obtained from a
              previous /parse invocation

                          For edit pipelines, this should be a string containing the edit instructions

          async_: The configuration options for asynchronous processing (default synchronous).

          instructions: The instructions to use for the extraction.

          parsing: The configuration options for parsing the document. If you are passing in a
              jobid:// URL for the file, then this configuration will be ignored.

          settings: The settings to use for the extraction.

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
        input: extract_run_params.SyncExtractConfigInput | extract_run_params.AsyncExtractConfigInput,
        instructions: extract_run_params.SyncExtractConfigInstructions
        | extract_run_params.AsyncExtractConfigInstructions
        | Omit = omit,
        parsing: ParseOptions | Omit = omit,
        settings: extract_run_params.SyncExtractConfigSettings
        | extract_run_params.AsyncExtractConfigSettings
        | Omit = omit,
        async_: ConfigV3AsyncConfig | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ExtractRunResponse:
        return cast(
            ExtractRunResponse,
            self._post(
                "/extract",
                body=maybe_transform(
                    {
                        "input": input,
                        "instructions": instructions,
                        "parsing": parsing,
                        "settings": settings,
                        "async_": async_,
                    },
                    extract_run_params.ExtractRunParams,
                ),
                options=make_request_options(
                    extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
                ),
                cast_to=cast(
                    Any, ExtractRunResponse
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )

    def run_job(
        self,
        *,
        input: extract_run_job_params.Input,
        async_: ConfigV3AsyncConfig | Omit = omit,
        instructions: extract_run_job_params.Instructions | Omit = omit,
        parsing: ParseOptions | Omit = omit,
        settings: extract_run_job_params.Settings | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ExtractRunJobResponse:
        """
        Extract Async

        Args:
          input: For parse/split/extract pipelines, the URL of the document to be processed. You
              can provide one of the following: 1. A publicly available URL 2. A presigned S3
              URL 3. A reducto:// prefixed URL obtained from the /upload endpoint after
              directly uploading a document 4. A jobid:// prefixed URL obtained from a
              previous /parse invocation

                          For edit pipelines, this should be a string containing the edit instructions

          async_: The configuration options for asynchronous processing (default synchronous).

          instructions: The instructions to use for the extraction.

          parsing: The configuration options for parsing the document. If you are passing in a
              jobid:// URL for the file, then this configuration will be ignored.

          settings: The settings to use for the extraction.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/extract_async",
            body=maybe_transform(
                {
                    "input": input,
                    "async_": async_,
                    "instructions": instructions,
                    "parsing": parsing,
                    "settings": settings,
                },
                extract_run_job_params.ExtractRunJobParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ExtractRunJobResponse,
        )


class AsyncExtractResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncExtractResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/reductoai/reducto-python-sdk#accessing-raw-response-data-eg-headers
        """
        return AsyncExtractResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncExtractResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/reductoai/reducto-python-sdk#with_streaming_response
        """
        return AsyncExtractResourceWithStreamingResponse(self)

    @overload
    async def run(
        self,
        *,
        input: extract_run_params.SyncExtractConfigInput,
        instructions: extract_run_params.SyncExtractConfigInstructions | Omit = omit,
        parsing: ParseOptions | Omit = omit,
        settings: extract_run_params.SyncExtractConfigSettings | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ExtractRunResponse:
        """
        Extract

        Args:
          input: For parse/split/extract pipelines, the URL of the document to be processed. You
              can provide one of the following: 1. A publicly available URL 2. A presigned S3
              URL 3. A reducto:// prefixed URL obtained from the /upload endpoint after
              directly uploading a document 4. A jobid:// prefixed URL obtained from a
              previous /parse invocation

                          For edit pipelines, this should be a string containing the edit instructions

          instructions: The instructions to use for the extraction.

          parsing: The configuration options for parsing the document. If you are passing in a
              jobid:// URL for the file, then this configuration will be ignored.

          settings: The settings to use for the extraction.

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
        input: extract_run_params.AsyncExtractConfigInput,
        async_: ConfigV3AsyncConfig | Omit = omit,
        instructions: extract_run_params.AsyncExtractConfigInstructions | Omit = omit,
        parsing: ParseOptions | Omit = omit,
        settings: extract_run_params.AsyncExtractConfigSettings | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ExtractRunResponse:
        """
        Extract

        Args:
          input: For parse/split/extract pipelines, the URL of the document to be processed. You
              can provide one of the following: 1. A publicly available URL 2. A presigned S3
              URL 3. A reducto:// prefixed URL obtained from the /upload endpoint after
              directly uploading a document 4. A jobid:// prefixed URL obtained from a
              previous /parse invocation

                          For edit pipelines, this should be a string containing the edit instructions

          async_: The configuration options for asynchronous processing (default synchronous).

          instructions: The instructions to use for the extraction.

          parsing: The configuration options for parsing the document. If you are passing in a
              jobid:// URL for the file, then this configuration will be ignored.

          settings: The settings to use for the extraction.

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
        input: extract_run_params.SyncExtractConfigInput | extract_run_params.AsyncExtractConfigInput,
        instructions: extract_run_params.SyncExtractConfigInstructions
        | extract_run_params.AsyncExtractConfigInstructions
        | Omit = omit,
        parsing: ParseOptions | Omit = omit,
        settings: extract_run_params.SyncExtractConfigSettings
        | extract_run_params.AsyncExtractConfigSettings
        | Omit = omit,
        async_: ConfigV3AsyncConfig | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ExtractRunResponse:
        return cast(
            ExtractRunResponse,
            await self._post(
                "/extract",
                body=await async_maybe_transform(
                    {
                        "input": input,
                        "instructions": instructions,
                        "parsing": parsing,
                        "settings": settings,
                        "async_": async_,
                    },
                    extract_run_params.ExtractRunParams,
                ),
                options=make_request_options(
                    extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
                ),
                cast_to=cast(
                    Any, ExtractRunResponse
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )

    async def run_job(
        self,
        *,
        input: extract_run_job_params.Input,
        async_: ConfigV3AsyncConfig | Omit = omit,
        instructions: extract_run_job_params.Instructions | Omit = omit,
        parsing: ParseOptions | Omit = omit,
        settings: extract_run_job_params.Settings | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ExtractRunJobResponse:
        """
        Extract Async

        Args:
          input: For parse/split/extract pipelines, the URL of the document to be processed. You
              can provide one of the following: 1. A publicly available URL 2. A presigned S3
              URL 3. A reducto:// prefixed URL obtained from the /upload endpoint after
              directly uploading a document 4. A jobid:// prefixed URL obtained from a
              previous /parse invocation

                          For edit pipelines, this should be a string containing the edit instructions

          async_: The configuration options for asynchronous processing (default synchronous).

          instructions: The instructions to use for the extraction.

          parsing: The configuration options for parsing the document. If you are passing in a
              jobid:// URL for the file, then this configuration will be ignored.

          settings: The settings to use for the extraction.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/extract_async",
            body=await async_maybe_transform(
                {
                    "input": input,
                    "async_": async_,
                    "instructions": instructions,
                    "parsing": parsing,
                    "settings": settings,
                },
                extract_run_job_params.ExtractRunJobParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ExtractRunJobResponse,
        )


class ExtractResourceWithRawResponse:
    def __init__(self, extract: ExtractResource) -> None:
        self._extract = extract

        self.run = to_raw_response_wrapper(
            extract.run,
        )
        self.run_job = to_raw_response_wrapper(
            extract.run_job,
        )


class AsyncExtractResourceWithRawResponse:
    def __init__(self, extract: AsyncExtractResource) -> None:
        self._extract = extract

        self.run = async_to_raw_response_wrapper(
            extract.run,
        )
        self.run_job = async_to_raw_response_wrapper(
            extract.run_job,
        )


class ExtractResourceWithStreamingResponse:
    def __init__(self, extract: ExtractResource) -> None:
        self._extract = extract

        self.run = to_streamed_response_wrapper(
            extract.run,
        )
        self.run_job = to_streamed_response_wrapper(
            extract.run_job,
        )


class AsyncExtractResourceWithStreamingResponse:
    def __init__(self, extract: AsyncExtractResource) -> None:
        self._extract = extract

        self.run = async_to_streamed_response_wrapper(
            extract.run,
        )
        self.run_job = async_to_streamed_response_wrapper(
            extract.run_job,
        )
