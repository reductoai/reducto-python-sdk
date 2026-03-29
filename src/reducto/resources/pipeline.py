# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..types import pipeline_create_params
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
from ..types.pipeline_response import PipelineResponse
from ..types.pipeline_settings_param import PipelineSettingsParam

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

    def create(
        self,
        *,
        input: pipeline_create_params.Input,
        pipeline_id: str,
        settings: PipelineSettingsParam | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PipelineResponse:
        """
        Pipeline

        Args:
          input: For parse/split/extract pipelines, the URL of the document to be processed. You
              can provide one of the following: 1. A publicly available URL 2. A presigned S3
              URL 3. A reducto:// prefixed URL obtained from the /upload endpoint after
              directly uploading a document 4. A jobid:// prefixed URL obtained from a
              previous /parse invocation 5. A list of URLs (for multi-document pipelines, V3
              API only)

                          For edit pipelines, this should be a string containing the edit instructions

          pipeline_id: The ID of the pipeline to use for the document.

          settings: Settings for pipeline execution that override pipeline defaults.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/pipeline",
            body=maybe_transform(
                {
                    "input": input,
                    "pipeline_id": pipeline_id,
                    "settings": settings,
                },
                pipeline_create_params.PipelineCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PipelineResponse,
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

    async def create(
        self,
        *,
        input: pipeline_create_params.Input,
        pipeline_id: str,
        settings: PipelineSettingsParam | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PipelineResponse:
        """
        Pipeline

        Args:
          input: For parse/split/extract pipelines, the URL of the document to be processed. You
              can provide one of the following: 1. A publicly available URL 2. A presigned S3
              URL 3. A reducto:// prefixed URL obtained from the /upload endpoint after
              directly uploading a document 4. A jobid:// prefixed URL obtained from a
              previous /parse invocation 5. A list of URLs (for multi-document pipelines, V3
              API only)

                          For edit pipelines, this should be a string containing the edit instructions

          pipeline_id: The ID of the pipeline to use for the document.

          settings: Settings for pipeline execution that override pipeline defaults.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/pipeline",
            body=await async_maybe_transform(
                {
                    "input": input,
                    "pipeline_id": pipeline_id,
                    "settings": settings,
                },
                pipeline_create_params.PipelineCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PipelineResponse,
        )


class PipelineResourceWithRawResponse:
    def __init__(self, pipeline: PipelineResource) -> None:
        self._pipeline = pipeline

        self.create = to_raw_response_wrapper(
            pipeline.create,
        )


class AsyncPipelineResourceWithRawResponse:
    def __init__(self, pipeline: AsyncPipelineResource) -> None:
        self._pipeline = pipeline

        self.create = async_to_raw_response_wrapper(
            pipeline.create,
        )


class PipelineResourceWithStreamingResponse:
    def __init__(self, pipeline: PipelineResource) -> None:
        self._pipeline = pipeline

        self.create = to_streamed_response_wrapper(
            pipeline.create,
        )


class AsyncPipelineResourceWithStreamingResponse:
    def __init__(self, pipeline: AsyncPipelineResource) -> None:
        self._pipeline = pipeline

        self.create = async_to_streamed_response_wrapper(
            pipeline.create,
        )
