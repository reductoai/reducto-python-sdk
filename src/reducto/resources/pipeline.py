# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..types import pipeline_run_params, pipeline_run_job_params
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
from ..types.pipeline_run_response import PipelineRunResponse
from ..types.pipeline_run_job_response import PipelineRunJobResponse
from ..types.shared_params.webhook_config_new import WebhookConfigNew

__all__ = ["PipelineResource", "AsyncPipelineResource"]


class PipelineResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> PipelineResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/reductoai/reducto-python-sdk#accessing-raw-response-data-eg-headers
        """
        return PipelineResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> PipelineResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/reductoai/reducto-python-sdk#with_streaming_response
        """
        return PipelineResourceWithStreamingResponse(self)

    def run(
        self,
        *,
        document_url: pipeline_run_params.DocumentURL,
        pipeline_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> PipelineRunResponse:
        """Pipeline

        Args:
          document_url: The URL of the document to be processed.

        You can provide one of the
              following: 1. A publicly available URL 2. A presigned S3 URL 3. A reducto://
              prefixed URL obtained from the /upload endpoint after directly uploading a
              document

          pipeline_id: The ID of the pipeline to use for the document.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/pipeline",
            body=maybe_transform(
                {
                    "document_url": document_url,
                    "pipeline_id": pipeline_id,
                },
                pipeline_run_params.PipelineRunParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PipelineRunResponse,
        )

    def run_job(
        self,
        *,
        document_url: pipeline_run_job_params.DocumentURL,
        pipeline_id: str,
        priority: bool | NotGiven = NOT_GIVEN,
        webhook: WebhookConfigNew | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> PipelineRunJobResponse:
        """Pipeline Async

        Args:
          document_url: The URL of the document to be processed.

        You can provide one of the
              following: 1. A publicly available URL 2. A presigned S3 URL 3. A reducto://
              prefixed URL obtained from the /upload endpoint after directly uploading a
              document

          pipeline_id: The ID of the pipeline to use for the document.

          priority: If True, attempts to process the job with priority if the user has priority
              processing budget available; by default, sync jobs are prioritized above async
              jobs.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/pipeline_async",
            body=maybe_transform(
                {
                    "document_url": document_url,
                    "pipeline_id": pipeline_id,
                    "priority": priority,
                    "webhook": webhook,
                },
                pipeline_run_job_params.PipelineRunJobParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PipelineRunJobResponse,
        )


class AsyncPipelineResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncPipelineResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/reductoai/reducto-python-sdk#accessing-raw-response-data-eg-headers
        """
        return AsyncPipelineResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncPipelineResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/reductoai/reducto-python-sdk#with_streaming_response
        """
        return AsyncPipelineResourceWithStreamingResponse(self)

    async def run(
        self,
        *,
        document_url: pipeline_run_params.DocumentURL,
        pipeline_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> PipelineRunResponse:
        """Pipeline

        Args:
          document_url: The URL of the document to be processed.

        You can provide one of the
              following: 1. A publicly available URL 2. A presigned S3 URL 3. A reducto://
              prefixed URL obtained from the /upload endpoint after directly uploading a
              document

          pipeline_id: The ID of the pipeline to use for the document.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/pipeline",
            body=await async_maybe_transform(
                {
                    "document_url": document_url,
                    "pipeline_id": pipeline_id,
                },
                pipeline_run_params.PipelineRunParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PipelineRunResponse,
        )

    async def run_job(
        self,
        *,
        document_url: pipeline_run_job_params.DocumentURL,
        pipeline_id: str,
        priority: bool | NotGiven = NOT_GIVEN,
        webhook: WebhookConfigNew | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> PipelineRunJobResponse:
        """Pipeline Async

        Args:
          document_url: The URL of the document to be processed.

        You can provide one of the
              following: 1. A publicly available URL 2. A presigned S3 URL 3. A reducto://
              prefixed URL obtained from the /upload endpoint after directly uploading a
              document

          pipeline_id: The ID of the pipeline to use for the document.

          priority: If True, attempts to process the job with priority if the user has priority
              processing budget available; by default, sync jobs are prioritized above async
              jobs.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/pipeline_async",
            body=await async_maybe_transform(
                {
                    "document_url": document_url,
                    "pipeline_id": pipeline_id,
                    "priority": priority,
                    "webhook": webhook,
                },
                pipeline_run_job_params.PipelineRunJobParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PipelineRunJobResponse,
        )


class PipelineResourceWithRawResponse:
    def __init__(self, pipeline: PipelineResource) -> None:
        self._pipeline = pipeline

        self.run = to_raw_response_wrapper(
            pipeline.run,
        )
        self.run_job = to_raw_response_wrapper(
            pipeline.run_job,
        )


class AsyncPipelineResourceWithRawResponse:
    def __init__(self, pipeline: AsyncPipelineResource) -> None:
        self._pipeline = pipeline

        self.run = async_to_raw_response_wrapper(
            pipeline.run,
        )
        self.run_job = async_to_raw_response_wrapper(
            pipeline.run_job,
        )


class PipelineResourceWithStreamingResponse:
    def __init__(self, pipeline: PipelineResource) -> None:
        self._pipeline = pipeline

        self.run = to_streamed_response_wrapper(
            pipeline.run,
        )
        self.run_job = to_streamed_response_wrapper(
            pipeline.run_job,
        )


class AsyncPipelineResourceWithStreamingResponse:
    def __init__(self, pipeline: AsyncPipelineResource) -> None:
        self._pipeline = pipeline

        self.run = async_to_streamed_response_wrapper(
            pipeline.run,
        )
        self.run_job = async_to_streamed_response_wrapper(
            pipeline.run_job,
        )
