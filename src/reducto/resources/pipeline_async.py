# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..types import pipeline_async_create_params
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
from ..types.async_config_v3_param import AsyncConfigV3Param
from ..types.pipeline_settings_param import PipelineSettingsParam
from ..types.pipeline_async_create_response import PipelineAsyncCreateResponse

__all__ = ["PipelineAsyncResource", "AsyncPipelineAsyncResource"]


class PipelineAsyncResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> PipelineAsyncResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/reductoai/reducto-python-sdk#accessing-raw-response-data-eg-headers
        """
        return PipelineAsyncResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> PipelineAsyncResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/reductoai/reducto-python-sdk#with_streaming_response
        """
        return PipelineAsyncResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        input: pipeline_async_create_params.Input,
        pipeline_id: str,
        async_: AsyncConfigV3Param | Omit = omit,
        settings: PipelineSettingsParam | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PipelineAsyncCreateResponse:
        """
        Pipeline Async

        Args:
          input: For parse/split/extract pipelines, the URL of the document to be processed. You
              can provide one of the following: 1. A publicly available URL 2. A presigned S3
              URL 3. A reducto:// prefixed URL obtained from the /upload endpoint after
              directly uploading a document 4. A jobid:// prefixed URL obtained from a
              previous /parse invocation 5. A list of URLs (for multi-document pipelines, V3
              API only)

                          For edit pipelines, this should be a string containing the edit instructions

          pipeline_id: The ID of the pipeline to use for the document.

          async_: The configuration options for asynchronous processing (default synchronous).

          settings: Settings for pipeline execution that override pipeline defaults.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/pipeline_async",
            body=maybe_transform(
                {
                    "input": input,
                    "pipeline_id": pipeline_id,
                    "async_": async_,
                    "settings": settings,
                },
                pipeline_async_create_params.PipelineAsyncCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PipelineAsyncCreateResponse,
        )


class AsyncPipelineAsyncResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncPipelineAsyncResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/reductoai/reducto-python-sdk#accessing-raw-response-data-eg-headers
        """
        return AsyncPipelineAsyncResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncPipelineAsyncResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/reductoai/reducto-python-sdk#with_streaming_response
        """
        return AsyncPipelineAsyncResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        input: pipeline_async_create_params.Input,
        pipeline_id: str,
        async_: AsyncConfigV3Param | Omit = omit,
        settings: PipelineSettingsParam | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PipelineAsyncCreateResponse:
        """
        Pipeline Async

        Args:
          input: For parse/split/extract pipelines, the URL of the document to be processed. You
              can provide one of the following: 1. A publicly available URL 2. A presigned S3
              URL 3. A reducto:// prefixed URL obtained from the /upload endpoint after
              directly uploading a document 4. A jobid:// prefixed URL obtained from a
              previous /parse invocation 5. A list of URLs (for multi-document pipelines, V3
              API only)

                          For edit pipelines, this should be a string containing the edit instructions

          pipeline_id: The ID of the pipeline to use for the document.

          async_: The configuration options for asynchronous processing (default synchronous).

          settings: Settings for pipeline execution that override pipeline defaults.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/pipeline_async",
            body=await async_maybe_transform(
                {
                    "input": input,
                    "pipeline_id": pipeline_id,
                    "async_": async_,
                    "settings": settings,
                },
                pipeline_async_create_params.PipelineAsyncCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PipelineAsyncCreateResponse,
        )


class PipelineAsyncResourceWithRawResponse:
    def __init__(self, pipeline_async: PipelineAsyncResource) -> None:
        self._pipeline_async = pipeline_async

        self.create = to_raw_response_wrapper(
            pipeline_async.create,
        )


class AsyncPipelineAsyncResourceWithRawResponse:
    def __init__(self, pipeline_async: AsyncPipelineAsyncResource) -> None:
        self._pipeline_async = pipeline_async

        self.create = async_to_raw_response_wrapper(
            pipeline_async.create,
        )


class PipelineAsyncResourceWithStreamingResponse:
    def __init__(self, pipeline_async: PipelineAsyncResource) -> None:
        self._pipeline_async = pipeline_async

        self.create = to_streamed_response_wrapper(
            pipeline_async.create,
        )


class AsyncPipelineAsyncResourceWithStreamingResponse:
    def __init__(self, pipeline_async: AsyncPipelineAsyncResource) -> None:
        self._pipeline_async = pipeline_async

        self.create = async_to_streamed_response_wrapper(
            pipeline_async.create,
        )
