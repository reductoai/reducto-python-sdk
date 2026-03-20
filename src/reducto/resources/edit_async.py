# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable, Optional

import httpx

from ..types import edit_async_create_params
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
from ..types.edit_widget_param import EditWidgetParam
from ..types.edit_options_param import EditOptionsParam
from ..types.edit_async_create_response import EditAsyncCreateResponse

__all__ = ["EditAsyncResource", "AsyncEditAsyncResource"]


class EditAsyncResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> EditAsyncResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/reductoai/reducto-python-sdk#accessing-raw-response-data-eg-headers
        """
        return EditAsyncResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> EditAsyncResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/reductoai/reducto-python-sdk#with_streaming_response
        """
        return EditAsyncResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        document_url: edit_async_create_params.DocumentURL,
        edit_instructions: str,
        edit_options: EditOptionsParam | Omit = omit,
        form_schema: Optional[Iterable[EditWidgetParam]] | Omit = omit,
        priority: bool | Omit = omit,
        webhook: edit_async_create_params.Webhook | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> EditAsyncCreateResponse:
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

          form_schema: Form schema for PDF forms. List of widgets with their types, descriptions, and
              bounding boxes. Only works for PDFs.

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
                    "form_schema": form_schema,
                    "priority": priority,
                    "webhook": webhook,
                },
                edit_async_create_params.EditAsyncCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=EditAsyncCreateResponse,
        )


class AsyncEditAsyncResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncEditAsyncResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/reductoai/reducto-python-sdk#accessing-raw-response-data-eg-headers
        """
        return AsyncEditAsyncResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncEditAsyncResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/reductoai/reducto-python-sdk#with_streaming_response
        """
        return AsyncEditAsyncResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        document_url: edit_async_create_params.DocumentURL,
        edit_instructions: str,
        edit_options: EditOptionsParam | Omit = omit,
        form_schema: Optional[Iterable[EditWidgetParam]] | Omit = omit,
        priority: bool | Omit = omit,
        webhook: edit_async_create_params.Webhook | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> EditAsyncCreateResponse:
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

          form_schema: Form schema for PDF forms. List of widgets with their types, descriptions, and
              bounding boxes. Only works for PDFs.

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
                    "form_schema": form_schema,
                    "priority": priority,
                    "webhook": webhook,
                },
                edit_async_create_params.EditAsyncCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=EditAsyncCreateResponse,
        )


class EditAsyncResourceWithRawResponse:
    def __init__(self, edit_async: EditAsyncResource) -> None:
        self._edit_async = edit_async

        self.create = to_raw_response_wrapper(
            edit_async.create,
        )


class AsyncEditAsyncResourceWithRawResponse:
    def __init__(self, edit_async: AsyncEditAsyncResource) -> None:
        self._edit_async = edit_async

        self.create = async_to_raw_response_wrapper(
            edit_async.create,
        )


class EditAsyncResourceWithStreamingResponse:
    def __init__(self, edit_async: EditAsyncResource) -> None:
        self._edit_async = edit_async

        self.create = to_streamed_response_wrapper(
            edit_async.create,
        )


class AsyncEditAsyncResourceWithStreamingResponse:
    def __init__(self, edit_async: AsyncEditAsyncResource) -> None:
        self._edit_async = edit_async

        self.create = async_to_streamed_response_wrapper(
            edit_async.create,
        )
