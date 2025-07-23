# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..types import edit_run_params, edit_run_job_params
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
from ..types.edit_run_response import EditRunResponse
from ..types.edit_run_job_response import EditRunJobResponse
from ..types.shared_params.webhook_config_new import WebhookConfigNew

__all__ = ["EditResource", "AsyncEditResource"]


class EditResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> EditResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/reductoai/reducto-python-sdk#accessing-raw-response-data-eg-headers
        """
        return EditResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> EditResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/reductoai/reducto-python-sdk#with_streaming_response
        """
        return EditResourceWithStreamingResponse(self)

    def run(
        self,
        *,
        document_url: edit_run_params.DocumentURL,
        edit_instructions: str,
        edit_options: edit_run_params.EditOptions | NotGiven = NOT_GIVEN,
        priority: bool | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> EditRunResponse:
        """Edit

        Args:
          document_url:
              The URL of the document to be processed.

        You can provide one of the following:

              1. A publicly available URL
              2. A presigned S3 URL
              3. A reducto:// prefixed URL obtained from the /upload endpoint after directly
                 uploading a document

          edit_instructions: The instructions for the edit.

          priority: If True, attempts to process the job with priority if the user has priority
              processing budget available; by default, sync jobs are prioritized above async
              jobs.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/edit",
            body=maybe_transform(
                {
                    "document_url": document_url,
                    "edit_instructions": edit_instructions,
                    "edit_options": edit_options,
                    "priority": priority,
                },
                edit_run_params.EditRunParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=EditRunResponse,
        )

    def run_job(
        self,
        *,
        document_url: edit_run_job_params.DocumentURL,
        edit_instructions: str,
        edit_options: edit_run_job_params.EditOptions | NotGiven = NOT_GIVEN,
        priority: bool | NotGiven = NOT_GIVEN,
        webhook: WebhookConfigNew | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> EditRunJobResponse:
        """Edit Async

        Args:
          document_url:
              The URL of the document to be processed.

        You can provide one of the following:

              1. A publicly available URL
              2. A presigned S3 URL
              3. A reducto:// prefixed URL obtained from the /upload endpoint after directly
                 uploading a document

          edit_instructions: The instructions for the edit.

          priority: If True, attempts to process the job with priority if the user has priority
              processing budget available; by default, sync jobs are prioritized above async
              jobs.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/edit_async",
            body=maybe_transform(
                {
                    "document_url": document_url,
                    "edit_instructions": edit_instructions,
                    "edit_options": edit_options,
                    "priority": priority,
                    "webhook": webhook,
                },
                edit_run_job_params.EditRunJobParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=EditRunJobResponse,
        )


class AsyncEditResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncEditResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/reductoai/reducto-python-sdk#accessing-raw-response-data-eg-headers
        """
        return AsyncEditResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncEditResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/reductoai/reducto-python-sdk#with_streaming_response
        """
        return AsyncEditResourceWithStreamingResponse(self)

    async def run(
        self,
        *,
        document_url: edit_run_params.DocumentURL,
        edit_instructions: str,
        edit_options: edit_run_params.EditOptions | NotGiven = NOT_GIVEN,
        priority: bool | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> EditRunResponse:
        """Edit

        Args:
          document_url:
              The URL of the document to be processed.

        You can provide one of the following:

              1. A publicly available URL
              2. A presigned S3 URL
              3. A reducto:// prefixed URL obtained from the /upload endpoint after directly
                 uploading a document

          edit_instructions: The instructions for the edit.

          priority: If True, attempts to process the job with priority if the user has priority
              processing budget available; by default, sync jobs are prioritized above async
              jobs.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/edit",
            body=await async_maybe_transform(
                {
                    "document_url": document_url,
                    "edit_instructions": edit_instructions,
                    "edit_options": edit_options,
                    "priority": priority,
                },
                edit_run_params.EditRunParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=EditRunResponse,
        )

    async def run_job(
        self,
        *,
        document_url: edit_run_job_params.DocumentURL,
        edit_instructions: str,
        edit_options: edit_run_job_params.EditOptions | NotGiven = NOT_GIVEN,
        priority: bool | NotGiven = NOT_GIVEN,
        webhook: WebhookConfigNew | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> EditRunJobResponse:
        """Edit Async

        Args:
          document_url:
              The URL of the document to be processed.

        You can provide one of the following:

              1. A publicly available URL
              2. A presigned S3 URL
              3. A reducto:// prefixed URL obtained from the /upload endpoint after directly
                 uploading a document

          edit_instructions: The instructions for the edit.

          priority: If True, attempts to process the job with priority if the user has priority
              processing budget available; by default, sync jobs are prioritized above async
              jobs.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/edit_async",
            body=await async_maybe_transform(
                {
                    "document_url": document_url,
                    "edit_instructions": edit_instructions,
                    "edit_options": edit_options,
                    "priority": priority,
                    "webhook": webhook,
                },
                edit_run_job_params.EditRunJobParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=EditRunJobResponse,
        )


class EditResourceWithRawResponse:
    def __init__(self, edit: EditResource) -> None:
        self._edit = edit

        self.run = to_raw_response_wrapper(
            edit.run,
        )
        self.run_job = to_raw_response_wrapper(
            edit.run_job,
        )


class AsyncEditResourceWithRawResponse:
    def __init__(self, edit: AsyncEditResource) -> None:
        self._edit = edit

        self.run = async_to_raw_response_wrapper(
            edit.run,
        )
        self.run_job = async_to_raw_response_wrapper(
            edit.run_job,
        )


class EditResourceWithStreamingResponse:
    def __init__(self, edit: EditResource) -> None:
        self._edit = edit

        self.run = to_streamed_response_wrapper(
            edit.run,
        )
        self.run_job = to_streamed_response_wrapper(
            edit.run_job,
        )


class AsyncEditResourceWithStreamingResponse:
    def __init__(self, edit: AsyncEditResource) -> None:
        self._edit = edit

        self.run = async_to_streamed_response_wrapper(
            edit.run,
        )
        self.run_job = async_to_streamed_response_wrapper(
            edit.run_job,
        )
