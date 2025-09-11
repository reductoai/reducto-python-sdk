# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable

import httpx

from ..types import split_run_params, split_run_job_params
from .._types import NOT_GIVEN, Body, Query, Headers, NotGiven
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
from ..types.shared.split_response import SplitResponse
from ..types.split_run_job_response import SplitRunJobResponse
from ..types.shared_params.split_category import SplitCategory
from ..types.shared_params.webhook_config_new import WebhookConfigNew
from ..types.shared_params.base_processing_options import BaseProcessingOptions
from ..types.shared_params.advanced_processing_options import AdvancedProcessingOptions
from ..types.shared_params.experimental_processing_options import ExperimentalProcessingOptions

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

    def run(
        self,
        *,
        document_url: split_run_params.DocumentURL,
        split_description: Iterable[SplitCategory],
        advanced_options: AdvancedProcessingOptions | NotGiven = NOT_GIVEN,
        experimental_options: ExperimentalProcessingOptions | NotGiven = NOT_GIVEN,
        options: BaseProcessingOptions | NotGiven = NOT_GIVEN,
        priority: bool | NotGiven = NOT_GIVEN,
        split_options: split_run_params.SplitOptions | NotGiven = NOT_GIVEN,
        split_rules: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SplitResponse:
        """Split

        Args:
          document_url:
              The URL of the document to be processed.

        You can provide one of the following:

              1. A publicly available URL
              2. A presigned S3 URL
              3. A reducto:// prefixed URL obtained from the /upload endpoint after directly
                 uploading a document
              4. A job_id (jobid://) or a list of job_ids (jobid://) obtained from a previous
                 /parse endpoint

          split_description: The configuration options for processing the document.

          priority: If True, attempts to process the job with priority if the user has priority
              processing budget available; by default, sync jobs are prioritized above async
              jobs.

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
                    "document_url": document_url,
                    "split_description": split_description,
                    "advanced_options": advanced_options,
                    "experimental_options": experimental_options,
                    "options": options,
                    "priority": priority,
                    "split_options": split_options,
                    "split_rules": split_rules,
                },
                split_run_params.SplitRunParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SplitResponse,
        )

    def run_job(
        self,
        *,
        document_url: split_run_job_params.DocumentURL,
        split_description: Iterable[SplitCategory],
        advanced_options: AdvancedProcessingOptions | NotGiven = NOT_GIVEN,
        experimental_options: ExperimentalProcessingOptions | NotGiven = NOT_GIVEN,
        options: BaseProcessingOptions | NotGiven = NOT_GIVEN,
        priority: bool | NotGiven = NOT_GIVEN,
        split_options: split_run_job_params.SplitOptions | NotGiven = NOT_GIVEN,
        split_rules: str | NotGiven = NOT_GIVEN,
        webhook: WebhookConfigNew | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SplitRunJobResponse:
        """
        Split Async

        Args:
          document_url:
              The URL of the document to be processed. You can provide one of the following:

              1. A publicly available URL
              2. A presigned S3 URL
              3. A reducto:// prefixed URL obtained from the /upload endpoint after directly
                 uploading a document
              4. A job_id (jobid://) or a list of job_ids (jobid://) obtained from a previous
                 /parse endpoint

          split_description: The configuration options for processing the document.

          priority: If True, attempts to process the job with priority if the user has priority
              processing budget available; by default, sync jobs are prioritized above async
              jobs.

          split_rules: The prompt that describes rules for splitting the document.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/split_async",
            body=maybe_transform(
                {
                    "document_url": document_url,
                    "split_description": split_description,
                    "advanced_options": advanced_options,
                    "experimental_options": experimental_options,
                    "options": options,
                    "priority": priority,
                    "split_options": split_options,
                    "split_rules": split_rules,
                    "webhook": webhook,
                },
                split_run_job_params.SplitRunJobParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SplitRunJobResponse,
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

    async def run(
        self,
        *,
        document_url: split_run_params.DocumentURL,
        split_description: Iterable[SplitCategory],
        advanced_options: AdvancedProcessingOptions | NotGiven = NOT_GIVEN,
        experimental_options: ExperimentalProcessingOptions | NotGiven = NOT_GIVEN,
        options: BaseProcessingOptions | NotGiven = NOT_GIVEN,
        priority: bool | NotGiven = NOT_GIVEN,
        split_options: split_run_params.SplitOptions | NotGiven = NOT_GIVEN,
        split_rules: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SplitResponse:
        """Split

        Args:
          document_url:
              The URL of the document to be processed.

        You can provide one of the following:

              1. A publicly available URL
              2. A presigned S3 URL
              3. A reducto:// prefixed URL obtained from the /upload endpoint after directly
                 uploading a document
              4. A job_id (jobid://) or a list of job_ids (jobid://) obtained from a previous
                 /parse endpoint

          split_description: The configuration options for processing the document.

          priority: If True, attempts to process the job with priority if the user has priority
              processing budget available; by default, sync jobs are prioritized above async
              jobs.

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
                    "document_url": document_url,
                    "split_description": split_description,
                    "advanced_options": advanced_options,
                    "experimental_options": experimental_options,
                    "options": options,
                    "priority": priority,
                    "split_options": split_options,
                    "split_rules": split_rules,
                },
                split_run_params.SplitRunParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SplitResponse,
        )

    async def run_job(
        self,
        *,
        document_url: split_run_job_params.DocumentURL,
        split_description: Iterable[SplitCategory],
        advanced_options: AdvancedProcessingOptions | NotGiven = NOT_GIVEN,
        experimental_options: ExperimentalProcessingOptions | NotGiven = NOT_GIVEN,
        options: BaseProcessingOptions | NotGiven = NOT_GIVEN,
        priority: bool | NotGiven = NOT_GIVEN,
        split_options: split_run_job_params.SplitOptions | NotGiven = NOT_GIVEN,
        split_rules: str | NotGiven = NOT_GIVEN,
        webhook: WebhookConfigNew | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SplitRunJobResponse:
        """
        Split Async

        Args:
          document_url:
              The URL of the document to be processed. You can provide one of the following:

              1. A publicly available URL
              2. A presigned S3 URL
              3. A reducto:// prefixed URL obtained from the /upload endpoint after directly
                 uploading a document
              4. A job_id (jobid://) or a list of job_ids (jobid://) obtained from a previous
                 /parse endpoint

          split_description: The configuration options for processing the document.

          priority: If True, attempts to process the job with priority if the user has priority
              processing budget available; by default, sync jobs are prioritized above async
              jobs.

          split_rules: The prompt that describes rules for splitting the document.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/split_async",
            body=await async_maybe_transform(
                {
                    "document_url": document_url,
                    "split_description": split_description,
                    "advanced_options": advanced_options,
                    "experimental_options": experimental_options,
                    "options": options,
                    "priority": priority,
                    "split_options": split_options,
                    "split_rules": split_rules,
                    "webhook": webhook,
                },
                split_run_job_params.SplitRunJobParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SplitRunJobResponse,
        )


class SplitResourceWithRawResponse:
    def __init__(self, split: SplitResource) -> None:
        self._split = split

        self.run = to_raw_response_wrapper(
            split.run,
        )
        self.run_job = to_raw_response_wrapper(
            split.run_job,
        )


class AsyncSplitResourceWithRawResponse:
    def __init__(self, split: AsyncSplitResource) -> None:
        self._split = split

        self.run = async_to_raw_response_wrapper(
            split.run,
        )
        self.run_job = async_to_raw_response_wrapper(
            split.run_job,
        )


class SplitResourceWithStreamingResponse:
    def __init__(self, split: SplitResource) -> None:
        self._split = split

        self.run = to_streamed_response_wrapper(
            split.run,
        )
        self.run_job = to_streamed_response_wrapper(
            split.run_job,
        )


class AsyncSplitResourceWithStreamingResponse:
    def __init__(self, split: AsyncSplitResource) -> None:
        self._split = split

        self.run = async_to_streamed_response_wrapper(
            split.run,
        )
        self.run_job = async_to_streamed_response_wrapper(
            split.run_job,
        )
