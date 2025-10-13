# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Any, Dict, Union, cast
from typing_extensions import overload

import httpx

from ..types import parse_run_params, parse_run_job_params
from .._types import Body, Omit, Query, Headers, NotGiven, SequenceNotStr, omit, not_given
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

    @overload
    def run(
        self,
        *,
        document_url: parse_run_params.ParseConfigDocumentURL,
        advanced_options: AdvancedProcessingOptions | Omit = omit,
        experimental_options: ExperimentalProcessingOptions | Omit = omit,
        options: BaseProcessingOptions | Omit = omit,
        priority: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ParseRunResponse:
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
        ...

    @overload
    def run(
        self,
        *,
        document_url: Union[str, SequenceNotStr[str]],
        async_: parse_run_params.ParseConfigAsync | Omit = omit,
        config: parse_run_params.ParseConfigConfig | Omit = omit,
        priority: bool | Omit = omit,
        user_config: Dict[str, object] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ParseRunResponse:
        """Parse

        Args:
          document_url: The URL of the document to process.

        Either a public URL or a presigned URL with
              a valid expiration time.

          async_: The configuration options for asynchronous processing (default synchronous).

          config: The configuration options for processing the document.

          priority: If True, attempts to process the job with priority if the user has priority
              processing budget available; by default, sync jobs are prioritized above async
              jobs.

          user_config: User-specific configuration options.

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
        input: parse_run_params.SyncParseConfigInput,
        enhance: parse_run_params.SyncParseConfigEnhance | Omit = omit,
        formatting: parse_run_params.SyncParseConfigFormatting | Omit = omit,
        retrieval: parse_run_params.SyncParseConfigRetrieval | Omit = omit,
        settings: parse_run_params.SyncParseConfigSettings | Omit = omit,
        spreadsheet: parse_run_params.SyncParseConfigSpreadsheet | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ParseRunResponse:
        """Parse

        Args:
          input: The URL of the document to be processed.

        You can provide one of the
              following: 1. A publicly available URL 2. A presigned S3 URL 3. A reducto://
              prefixed URL obtained from the /upload endpoint after directly uploading a
              document 4. A jobid:// prefixed URL obtained from a previous /parse invocation

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @required_args(["document_url"], ["input"])
    def run(
        self,
        *,
        document_url: parse_run_params.ParseConfigDocumentURL | Union[str, SequenceNotStr[str]] | Omit = omit,
        advanced_options: AdvancedProcessingOptions | Omit = omit,
        experimental_options: ExperimentalProcessingOptions | Omit = omit,
        options: BaseProcessingOptions | Omit = omit,
        priority: bool | Omit = omit,
        async_: parse_run_params.ParseConfigAsync | Omit = omit,
        config: parse_run_params.ParseConfigConfig | Omit = omit,
        user_config: Dict[str, object] | Omit = omit,
        input: parse_run_params.SyncParseConfigInput | Omit = omit,
        enhance: parse_run_params.SyncParseConfigEnhance | Omit = omit,
        formatting: parse_run_params.SyncParseConfigFormatting | Omit = omit,
        retrieval: parse_run_params.SyncParseConfigRetrieval | Omit = omit,
        settings: parse_run_params.SyncParseConfigSettings | Omit = omit,
        spreadsheet: parse_run_params.SyncParseConfigSpreadsheet | Omit = omit,
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
                        "document_url": document_url,
                        "advanced_options": advanced_options,
                        "experimental_options": experimental_options,
                        "options": options,
                        "priority": priority,
                        "async_": async_,
                        "config": config,
                        "user_config": user_config,
                        "input": input,
                        "enhance": enhance,
                        "formatting": formatting,
                        "retrieval": retrieval,
                        "settings": settings,
                        "spreadsheet": spreadsheet,
                    },
                    parse_run_params.ParseRunParams,
                ),
                options=make_request_options(
                    extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
                ),
                cast_to=cast(Any, ParseRunResponse),  # Union types cannot be passed in as arguments in the type system
            ),
        )

    @overload
    def run_job(
        self,
        *,
        document_url: parse_run_job_params.AsyncParseConfigNewDocumentURL,
        advanced_options: AdvancedProcessingOptions | Omit = omit,
        experimental_options: ExperimentalProcessingOptions | Omit = omit,
        options: BaseProcessingOptions | Omit = omit,
        priority: bool | Omit = omit,
        webhook: WebhookConfigNew | Omit = omit,
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
        ...

    @overload
    def run_job(
        self,
        *,
        input: parse_run_job_params.AsyncParseConfigInput,
        async_: parse_run_job_params.AsyncParseConfigAsync | Omit = omit,
        enhance: parse_run_job_params.AsyncParseConfigEnhance | Omit = omit,
        formatting: parse_run_job_params.AsyncParseConfigFormatting | Omit = omit,
        retrieval: parse_run_job_params.AsyncParseConfigRetrieval | Omit = omit,
        settings: parse_run_job_params.AsyncParseConfigSettings | Omit = omit,
        spreadsheet: parse_run_job_params.AsyncParseConfigSpreadsheet | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ParseRunJobResponse:
        """Async Parse

        Args:
          input: The URL of the document to be processed.

        You can provide one of the
              following: 1. A publicly available URL 2. A presigned S3 URL 3. A reducto://
              prefixed URL obtained from the /upload endpoint after directly uploading a
              document 4. A jobid:// prefixed URL obtained from a previous /parse invocation

          async_: The configuration options for asynchronous processing (default synchronous).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @required_args(["document_url"], ["input"])
    def run_job(
        self,
        *,
        document_url: parse_run_job_params.AsyncParseConfigNewDocumentURL | Omit = omit,
        advanced_options: AdvancedProcessingOptions | Omit = omit,
        experimental_options: ExperimentalProcessingOptions | Omit = omit,
        options: BaseProcessingOptions | Omit = omit,
        priority: bool | Omit = omit,
        webhook: WebhookConfigNew | Omit = omit,
        input: parse_run_job_params.AsyncParseConfigInput | Omit = omit,
        async_: parse_run_job_params.AsyncParseConfigAsync | Omit = omit,
        enhance: parse_run_job_params.AsyncParseConfigEnhance | Omit = omit,
        formatting: parse_run_job_params.AsyncParseConfigFormatting | Omit = omit,
        retrieval: parse_run_job_params.AsyncParseConfigRetrieval | Omit = omit,
        settings: parse_run_job_params.AsyncParseConfigSettings | Omit = omit,
        spreadsheet: parse_run_job_params.AsyncParseConfigSpreadsheet | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ParseRunJobResponse:
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
        document_url: parse_run_params.ParseConfigDocumentURL,
        advanced_options: AdvancedProcessingOptions | Omit = omit,
        experimental_options: ExperimentalProcessingOptions | Omit = omit,
        options: BaseProcessingOptions | Omit = omit,
        priority: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ParseRunResponse:
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
        ...

    @overload
    async def run(
        self,
        *,
        document_url: Union[str, SequenceNotStr[str]],
        async_: parse_run_params.ParseConfigAsync | Omit = omit,
        config: parse_run_params.ParseConfigConfig | Omit = omit,
        priority: bool | Omit = omit,
        user_config: Dict[str, object] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ParseRunResponse:
        """Parse

        Args:
          document_url: The URL of the document to process.

        Either a public URL or a presigned URL with
              a valid expiration time.

          async_: The configuration options for asynchronous processing (default synchronous).

          config: The configuration options for processing the document.

          priority: If True, attempts to process the job with priority if the user has priority
              processing budget available; by default, sync jobs are prioritized above async
              jobs.

          user_config: User-specific configuration options.

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
        input: parse_run_params.SyncParseConfigInput,
        enhance: parse_run_params.SyncParseConfigEnhance | Omit = omit,
        formatting: parse_run_params.SyncParseConfigFormatting | Omit = omit,
        retrieval: parse_run_params.SyncParseConfigRetrieval | Omit = omit,
        settings: parse_run_params.SyncParseConfigSettings | Omit = omit,
        spreadsheet: parse_run_params.SyncParseConfigSpreadsheet | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ParseRunResponse:
        """Parse

        Args:
          input: The URL of the document to be processed.

        You can provide one of the
              following: 1. A publicly available URL 2. A presigned S3 URL 3. A reducto://
              prefixed URL obtained from the /upload endpoint after directly uploading a
              document 4. A jobid:// prefixed URL obtained from a previous /parse invocation

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @required_args(["document_url"], ["input"])
    async def run(
        self,
        *,
        document_url: parse_run_params.ParseConfigDocumentURL | Union[str, SequenceNotStr[str]] | Omit = omit,
        advanced_options: AdvancedProcessingOptions | Omit = omit,
        experimental_options: ExperimentalProcessingOptions | Omit = omit,
        options: BaseProcessingOptions | Omit = omit,
        priority: bool | Omit = omit,
        async_: parse_run_params.ParseConfigAsync | Omit = omit,
        config: parse_run_params.ParseConfigConfig | Omit = omit,
        user_config: Dict[str, object] | Omit = omit,
        input: parse_run_params.SyncParseConfigInput | Omit = omit,
        enhance: parse_run_params.SyncParseConfigEnhance | Omit = omit,
        formatting: parse_run_params.SyncParseConfigFormatting | Omit = omit,
        retrieval: parse_run_params.SyncParseConfigRetrieval | Omit = omit,
        settings: parse_run_params.SyncParseConfigSettings | Omit = omit,
        spreadsheet: parse_run_params.SyncParseConfigSpreadsheet | Omit = omit,
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
                        "document_url": document_url,
                        "advanced_options": advanced_options,
                        "experimental_options": experimental_options,
                        "options": options,
                        "priority": priority,
                        "async_": async_,
                        "config": config,
                        "user_config": user_config,
                        "input": input,
                        "enhance": enhance,
                        "formatting": formatting,
                        "retrieval": retrieval,
                        "settings": settings,
                        "spreadsheet": spreadsheet,
                    },
                    parse_run_params.ParseRunParams,
                ),
                options=make_request_options(
                    extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
                ),
                cast_to=cast(Any, ParseRunResponse),  # Union types cannot be passed in as arguments in the type system
            ),
        )

    @overload
    async def run_job(
        self,
        *,
        document_url: parse_run_job_params.AsyncParseConfigNewDocumentURL,
        advanced_options: AdvancedProcessingOptions | Omit = omit,
        experimental_options: ExperimentalProcessingOptions | Omit = omit,
        options: BaseProcessingOptions | Omit = omit,
        priority: bool | Omit = omit,
        webhook: WebhookConfigNew | Omit = omit,
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
        ...

    @overload
    async def run_job(
        self,
        *,
        input: parse_run_job_params.AsyncParseConfigInput,
        async_: parse_run_job_params.AsyncParseConfigAsync | Omit = omit,
        enhance: parse_run_job_params.AsyncParseConfigEnhance | Omit = omit,
        formatting: parse_run_job_params.AsyncParseConfigFormatting | Omit = omit,
        retrieval: parse_run_job_params.AsyncParseConfigRetrieval | Omit = omit,
        settings: parse_run_job_params.AsyncParseConfigSettings | Omit = omit,
        spreadsheet: parse_run_job_params.AsyncParseConfigSpreadsheet | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ParseRunJobResponse:
        """Async Parse

        Args:
          input: The URL of the document to be processed.

        You can provide one of the
              following: 1. A publicly available URL 2. A presigned S3 URL 3. A reducto://
              prefixed URL obtained from the /upload endpoint after directly uploading a
              document 4. A jobid:// prefixed URL obtained from a previous /parse invocation

          async_: The configuration options for asynchronous processing (default synchronous).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @required_args(["document_url"], ["input"])
    async def run_job(
        self,
        *,
        document_url: parse_run_job_params.AsyncParseConfigNewDocumentURL | Omit = omit,
        advanced_options: AdvancedProcessingOptions | Omit = omit,
        experimental_options: ExperimentalProcessingOptions | Omit = omit,
        options: BaseProcessingOptions | Omit = omit,
        priority: bool | Omit = omit,
        webhook: WebhookConfigNew | Omit = omit,
        input: parse_run_job_params.AsyncParseConfigInput | Omit = omit,
        async_: parse_run_job_params.AsyncParseConfigAsync | Omit = omit,
        enhance: parse_run_job_params.AsyncParseConfigEnhance | Omit = omit,
        formatting: parse_run_job_params.AsyncParseConfigFormatting | Omit = omit,
        retrieval: parse_run_job_params.AsyncParseConfigRetrieval | Omit = omit,
        settings: parse_run_job_params.AsyncParseConfigSettings | Omit = omit,
        spreadsheet: parse_run_job_params.AsyncParseConfigSpreadsheet | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ParseRunJobResponse:
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
