# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Any, cast
from typing_extensions import overload

import httpx

from ..types import extract_create_params
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
from ..types.instructions_param import InstructionsParam
from ..types.parse_options_param import ParseOptionsParam
from ..types.async_config_v3_param import AsyncConfigV3Param
from ..types.extract_settings_param import ExtractSettingsParam
from ..types.extract_create_response import ExtractCreateResponse

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
    def create(
        self,
        *,
        input: extract_create_params.SyncExtractConfigInput,
        instructions: InstructionsParam | Omit = omit,
        parsing: ParseOptionsParam | Omit = omit,
        settings: ExtractSettingsParam | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ExtractCreateResponse:
        """
        Extract

        Args:
          input: For parse/split/extract pipelines, the URL of the document to be processed. You
              can provide one of the following: 1. A publicly available URL 2. A presigned S3
              URL 3. A reducto:// prefixed URL obtained from the /upload endpoint after
              directly uploading a document 4. A jobid:// prefixed URL obtained from a
              previous /parse invocation 5. A list of URLs (for multi-document pipelines, V3
              API only)

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
    def create(
        self,
        *,
        input: extract_create_params.AsyncExtractConfigInput,
        async_: AsyncConfigV3Param | Omit = omit,
        instructions: InstructionsParam | Omit = omit,
        parsing: ParseOptionsParam | Omit = omit,
        settings: ExtractSettingsParam | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ExtractCreateResponse:
        """
        Extract

        Args:
          input: For parse/split/extract pipelines, the URL of the document to be processed. You
              can provide one of the following: 1. A publicly available URL 2. A presigned S3
              URL 3. A reducto:// prefixed URL obtained from the /upload endpoint after
              directly uploading a document 4. A jobid:// prefixed URL obtained from a
              previous /parse invocation 5. A list of URLs (for multi-document pipelines, V3
              API only)

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
    def create(
        self,
        *,
        input: extract_create_params.SyncExtractConfigInput | extract_create_params.AsyncExtractConfigInput,
        instructions: InstructionsParam | Omit = omit,
        parsing: ParseOptionsParam | Omit = omit,
        settings: ExtractSettingsParam | Omit = omit,
        async_: AsyncConfigV3Param | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ExtractCreateResponse:
        return cast(
            ExtractCreateResponse,
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
                    extract_create_params.ExtractCreateParams,
                ),
                options=make_request_options(
                    extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
                ),
                cast_to=cast(
                    Any, ExtractCreateResponse
                ),  # Union types cannot be passed in as arguments in the type system
            ),
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
    async def create(
        self,
        *,
        input: extract_create_params.SyncExtractConfigInput,
        instructions: InstructionsParam | Omit = omit,
        parsing: ParseOptionsParam | Omit = omit,
        settings: ExtractSettingsParam | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ExtractCreateResponse:
        """
        Extract

        Args:
          input: For parse/split/extract pipelines, the URL of the document to be processed. You
              can provide one of the following: 1. A publicly available URL 2. A presigned S3
              URL 3. A reducto:// prefixed URL obtained from the /upload endpoint after
              directly uploading a document 4. A jobid:// prefixed URL obtained from a
              previous /parse invocation 5. A list of URLs (for multi-document pipelines, V3
              API only)

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
    async def create(
        self,
        *,
        input: extract_create_params.AsyncExtractConfigInput,
        async_: AsyncConfigV3Param | Omit = omit,
        instructions: InstructionsParam | Omit = omit,
        parsing: ParseOptionsParam | Omit = omit,
        settings: ExtractSettingsParam | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ExtractCreateResponse:
        """
        Extract

        Args:
          input: For parse/split/extract pipelines, the URL of the document to be processed. You
              can provide one of the following: 1. A publicly available URL 2. A presigned S3
              URL 3. A reducto:// prefixed URL obtained from the /upload endpoint after
              directly uploading a document 4. A jobid:// prefixed URL obtained from a
              previous /parse invocation 5. A list of URLs (for multi-document pipelines, V3
              API only)

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
    async def create(
        self,
        *,
        input: extract_create_params.SyncExtractConfigInput | extract_create_params.AsyncExtractConfigInput,
        instructions: InstructionsParam | Omit = omit,
        parsing: ParseOptionsParam | Omit = omit,
        settings: ExtractSettingsParam | Omit = omit,
        async_: AsyncConfigV3Param | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ExtractCreateResponse:
        return cast(
            ExtractCreateResponse,
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
                    extract_create_params.ExtractCreateParams,
                ),
                options=make_request_options(
                    extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
                ),
                cast_to=cast(
                    Any, ExtractCreateResponse
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )


class ExtractResourceWithRawResponse:
    def __init__(self, extract: ExtractResource) -> None:
        self._extract = extract

        self.create = to_raw_response_wrapper(
            extract.create,
        )


class AsyncExtractResourceWithRawResponse:
    def __init__(self, extract: AsyncExtractResource) -> None:
        self._extract = extract

        self.create = async_to_raw_response_wrapper(
            extract.create,
        )


class ExtractResourceWithStreamingResponse:
    def __init__(self, extract: ExtractResource) -> None:
        self._extract = extract

        self.create = to_streamed_response_wrapper(
            extract.create,
        )


class AsyncExtractResourceWithStreamingResponse:
    def __init__(self, extract: AsyncExtractResource) -> None:
        self._extract = extract

        self.create = async_to_streamed_response_wrapper(
            extract.create,
        )
