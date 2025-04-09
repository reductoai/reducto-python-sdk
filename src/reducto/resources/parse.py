# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..types import parse_run_params, parse_run_job_params
from .._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from .._utils import (
    maybe_transform,
    async_maybe_transform,
)
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._base_client import make_request_options
from ..types.shared.parse_response import ParseResponse
from ..types.parse_run_job_response import ParseRunJobResponse
from ..types.shared_params.webhook_config_new import WebhookConfigNew
from ..types.shared_params.base_processing_options import BaseProcessingOptions
from ..types.shared_params.advanced_processing_options import AdvancedProcessingOptions
from ..types.shared_params.experimental_processing_options import ExperimentalProcessingOptions

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

    def run(
        self,
        *,
        document_url: parse_run_params.DocumentURL,
        advanced_options: AdvancedProcessingOptions | NotGiven = NOT_GIVEN,
        experimental_options: ExperimentalProcessingOptions | NotGiven = NOT_GIVEN,
        options: BaseProcessingOptions | NotGiven = NOT_GIVEN,
        priority: bool | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ParseResponse:
        """Parse

        Args:
          document_url:
              The URL of the document to be processed.

        You can provide one of the following:

              1. A publicly available URL
              2. A presigned S3 URL
              3. A reducto:// prefixed URL obtained from the /upload endpoint after directly
                 uploading a document

          priority: If True, attempts to process the job with priority if the user has priority
              processing budget available; by default, sync jobs are prioritized above async
              jobs.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/parse",
            body=maybe_transform(
                {
                    "document_url": document_url,
                    "advanced_options": advanced_options,
                    "experimental_options": experimental_options,
                    "options": options,
                    "priority": priority,
                },
                parse_run_params.ParseRunParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ParseResponse,
        )

    def run_job(
        self,
        *,
        document_url: parse_run_job_params.DocumentURL,
        advanced_options: AdvancedProcessingOptions | NotGiven = NOT_GIVEN,
        experimental_options: ExperimentalProcessingOptions | NotGiven = NOT_GIVEN,
        options: BaseProcessingOptions | NotGiven = NOT_GIVEN,
        priority: bool | NotGiven = NOT_GIVEN,
        webhook: WebhookConfigNew | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ParseRunJobResponse:
        """
        Async Parse

        Args:
          document_url:
              The URL of the document to be processed. You can provide one of the following:

              1. A publicly available URL
              2. A presigned S3 URL
              3. A reducto:// prefixed URL obtained from the /upload endpoint after directly
                 uploading a document

          priority: If True, attempts to process the job with priority if the user has priority
              processing budget available; by default, sync jobs are prioritized above async
              jobs.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/parse_async",
            body=maybe_transform(
                {
                    "document_url": document_url,
                    "advanced_options": advanced_options,
                    "experimental_options": experimental_options,
                    "options": options,
                    "priority": priority,
                    "webhook": webhook,
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

    async def run(
        self,
        *,
        document_url: parse_run_params.DocumentURL,
        advanced_options: AdvancedProcessingOptions | NotGiven = NOT_GIVEN,
        experimental_options: ExperimentalProcessingOptions | NotGiven = NOT_GIVEN,
        options: BaseProcessingOptions | NotGiven = NOT_GIVEN,
        priority: bool | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ParseResponse:
        """Parse

        Args:
          document_url:
              The URL of the document to be processed.

        You can provide one of the following:

              1. A publicly available URL
              2. A presigned S3 URL
              3. A reducto:// prefixed URL obtained from the /upload endpoint after directly
                 uploading a document

          priority: If True, attempts to process the job with priority if the user has priority
              processing budget available; by default, sync jobs are prioritized above async
              jobs.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/parse",
            body=await async_maybe_transform(
                {
                    "document_url": document_url,
                    "advanced_options": advanced_options,
                    "experimental_options": experimental_options,
                    "options": options,
                    "priority": priority,
                },
                parse_run_params.ParseRunParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ParseResponse,
        )

    async def run_job(
        self,
        *,
        document_url: parse_run_job_params.DocumentURL,
        advanced_options: AdvancedProcessingOptions | NotGiven = NOT_GIVEN,
        experimental_options: ExperimentalProcessingOptions | NotGiven = NOT_GIVEN,
        options: BaseProcessingOptions | NotGiven = NOT_GIVEN,
        priority: bool | NotGiven = NOT_GIVEN,
        webhook: WebhookConfigNew | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ParseRunJobResponse:
        """
        Async Parse

        Args:
          document_url:
              The URL of the document to be processed. You can provide one of the following:

              1. A publicly available URL
              2. A presigned S3 URL
              3. A reducto:// prefixed URL obtained from the /upload endpoint after directly
                 uploading a document

          priority: If True, attempts to process the job with priority if the user has priority
              processing budget available; by default, sync jobs are prioritized above async
              jobs.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/parse_async",
            body=await async_maybe_transform(
                {
                    "document_url": document_url,
                    "advanced_options": advanced_options,
                    "experimental_options": experimental_options,
                    "options": options,
                    "priority": priority,
                    "webhook": webhook,
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
