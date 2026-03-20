# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Any, Optional, cast

import httpx

from ..types import job_list_params
from .._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from .._utils import path_template, maybe_transform, async_maybe_transform
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._base_client import make_request_options
from ..types.job_list_response import JobListResponse
from ..types.job_retrieve_response import JobRetrieveResponse

__all__ = ["JobResource", "AsyncJobResource"]


class JobResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> JobResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/reductoai/reducto-python-sdk#accessing-raw-response-data-eg-headers
        """
        return JobResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> JobResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/reductoai/reducto-python-sdk#with_streaming_response
        """
        return JobResourceWithStreamingResponse(self)

    def retrieve(
        self,
        job_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> JobRetrieveResponse:
        """
        Retrieve Parse

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not job_id:
            raise ValueError(f"Expected a non-empty value for `job_id` but received {job_id!r}")
        return cast(
            JobRetrieveResponse,
            self._get(
                path_template("/job/{job_id}", job_id=job_id),
                options=make_request_options(
                    extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
                ),
                cast_to=cast(
                    Any, JobRetrieveResponse
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )

    def list(
        self,
        *,
        cursor: Optional[str] | Omit = omit,
        exclude_configs: bool | Omit = omit,
        limit: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> JobListResponse:
        """Get Jobs

        Args:
          cursor: Cursor for pagination.

        Use the next_cursor from the previous response to fetch
              the next page.

          exclude_configs: Exclude raw_config from response to reduce size

          limit: Maximum number of jobs to return per page. Defaults to 100, max 500.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/jobs",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "cursor": cursor,
                        "exclude_configs": exclude_configs,
                        "limit": limit,
                    },
                    job_list_params.JobListParams,
                ),
            ),
            cast_to=JobListResponse,
        )


class AsyncJobResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncJobResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/reductoai/reducto-python-sdk#accessing-raw-response-data-eg-headers
        """
        return AsyncJobResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncJobResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/reductoai/reducto-python-sdk#with_streaming_response
        """
        return AsyncJobResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        job_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> JobRetrieveResponse:
        """
        Retrieve Parse

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not job_id:
            raise ValueError(f"Expected a non-empty value for `job_id` but received {job_id!r}")
        return cast(
            JobRetrieveResponse,
            await self._get(
                path_template("/job/{job_id}", job_id=job_id),
                options=make_request_options(
                    extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
                ),
                cast_to=cast(
                    Any, JobRetrieveResponse
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )

    async def list(
        self,
        *,
        cursor: Optional[str] | Omit = omit,
        exclude_configs: bool | Omit = omit,
        limit: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> JobListResponse:
        """Get Jobs

        Args:
          cursor: Cursor for pagination.

        Use the next_cursor from the previous response to fetch
              the next page.

          exclude_configs: Exclude raw_config from response to reduce size

          limit: Maximum number of jobs to return per page. Defaults to 100, max 500.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/jobs",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "cursor": cursor,
                        "exclude_configs": exclude_configs,
                        "limit": limit,
                    },
                    job_list_params.JobListParams,
                ),
            ),
            cast_to=JobListResponse,
        )


class JobResourceWithRawResponse:
    def __init__(self, job: JobResource) -> None:
        self._job = job

        self.retrieve = to_raw_response_wrapper(
            job.retrieve,
        )
        self.list = to_raw_response_wrapper(
            job.list,
        )


class AsyncJobResourceWithRawResponse:
    def __init__(self, job: AsyncJobResource) -> None:
        self._job = job

        self.retrieve = async_to_raw_response_wrapper(
            job.retrieve,
        )
        self.list = async_to_raw_response_wrapper(
            job.list,
        )


class JobResourceWithStreamingResponse:
    def __init__(self, job: JobResource) -> None:
        self._job = job

        self.retrieve = to_streamed_response_wrapper(
            job.retrieve,
        )
        self.list = to_streamed_response_wrapper(
            job.list,
        )


class AsyncJobResourceWithStreamingResponse:
    def __init__(self, job: AsyncJobResource) -> None:
        self._job = job

        self.retrieve = async_to_streamed_response_wrapper(
            job.retrieve,
        )
        self.list = async_to_streamed_response_wrapper(
            job.list,
        )
