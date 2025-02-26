# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..types import extract_run_params, extract_run_job_params
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
from ..types.shared.extract_response import ExtractResponse
from ..types.extract_run_job_response import ExtractRunJobResponse
from ..types.shared_params.webhook_config_new import WebhookConfigNew
from ..types.shared_params.array_extract_config import ArrayExtractConfig
from ..types.shared_params.base_processing_options import BaseProcessingOptions
from ..types.shared_params.advanced_processing_options import AdvancedProcessingOptions
from ..types.shared_params.experimental_processing_options import ExperimentalProcessingOptions

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

    def run(
        self,
        *,
        document_url: extract_run_params.DocumentURL,
        schema: object,
        advanced_options: AdvancedProcessingOptions | NotGiven = NOT_GIVEN,
        array_extract: ArrayExtractConfig | NotGiven = NOT_GIVEN,
        experimental_options: ExperimentalProcessingOptions | NotGiven = NOT_GIVEN,
        generate_citations: bool | NotGiven = NOT_GIVEN,
        options: BaseProcessingOptions | NotGiven = NOT_GIVEN,
        system_prompt: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ExtractResponse:
        """Extract

        Args:
          document_url:
              The URL of the document to be processed.

        You can provide one of the following:

              1. A publicly available URL
              2. A presigned S3 URL
              3. A reducto:// prefixed URL obtained from the /upload endpoint after directly
                 uploading a document

          schema: The JSON schema to use for extraction.

          array_extract: The configuration options for array extract

          generate_citations: If citations should be generated for the extracted content.

          system_prompt: A system prompt to use for the extraction. This is a general prompt that is
              applied to the entire document before any other prompts.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/extract",
            body=maybe_transform(
                {
                    "document_url": document_url,
                    "schema": schema,
                    "advanced_options": advanced_options,
                    "array_extract": array_extract,
                    "experimental_options": experimental_options,
                    "generate_citations": generate_citations,
                    "options": options,
                    "system_prompt": system_prompt,
                },
                extract_run_params.ExtractRunParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ExtractResponse,
        )

    def run_job(
        self,
        *,
        document_url: extract_run_job_params.DocumentURL,
        schema: object,
        advanced_options: AdvancedProcessingOptions | NotGiven = NOT_GIVEN,
        array_extract: ArrayExtractConfig | NotGiven = NOT_GIVEN,
        experimental_options: ExperimentalProcessingOptions | NotGiven = NOT_GIVEN,
        generate_citations: bool | NotGiven = NOT_GIVEN,
        options: BaseProcessingOptions | NotGiven = NOT_GIVEN,
        priority: bool | NotGiven = NOT_GIVEN,
        system_prompt: str | NotGiven = NOT_GIVEN,
        webhook: WebhookConfigNew | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ExtractRunJobResponse:
        """
        Extract Async

        Args:
          document_url:
              The URL of the document to be processed. You can provide one of the following:

              1. A publicly available URL
              2. A presigned S3 URL
              3. A reducto:// prefixed URL obtained from the /upload endpoint after directly
                 uploading a document

          schema: The JSON schema to use for extraction.

          array_extract: The configuration options for array extract

          generate_citations: If citations should be generated for the extracted content.

          priority: If True, attempts to process the job with priority if the user has priority
              processing budget available; by default, sync jobs are prioritized above async
              jobs.

          system_prompt: A system prompt to use for the extraction. This is a general prompt that is
              applied to the entire document before any other prompts.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/extract_async",
            body=maybe_transform(
                {
                    "document_url": document_url,
                    "schema": schema,
                    "advanced_options": advanced_options,
                    "array_extract": array_extract,
                    "experimental_options": experimental_options,
                    "generate_citations": generate_citations,
                    "options": options,
                    "priority": priority,
                    "system_prompt": system_prompt,
                    "webhook": webhook,
                },
                extract_run_job_params.ExtractRunJobParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ExtractRunJobResponse,
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

    async def run(
        self,
        *,
        document_url: extract_run_params.DocumentURL,
        schema: object,
        advanced_options: AdvancedProcessingOptions | NotGiven = NOT_GIVEN,
        array_extract: ArrayExtractConfig | NotGiven = NOT_GIVEN,
        experimental_options: ExperimentalProcessingOptions | NotGiven = NOT_GIVEN,
        generate_citations: bool | NotGiven = NOT_GIVEN,
        options: BaseProcessingOptions | NotGiven = NOT_GIVEN,
        system_prompt: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ExtractResponse:
        """Extract

        Args:
          document_url:
              The URL of the document to be processed.

        You can provide one of the following:

              1. A publicly available URL
              2. A presigned S3 URL
              3. A reducto:// prefixed URL obtained from the /upload endpoint after directly
                 uploading a document

          schema: The JSON schema to use for extraction.

          array_extract: The configuration options for array extract

          generate_citations: If citations should be generated for the extracted content.

          system_prompt: A system prompt to use for the extraction. This is a general prompt that is
              applied to the entire document before any other prompts.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/extract",
            body=await async_maybe_transform(
                {
                    "document_url": document_url,
                    "schema": schema,
                    "advanced_options": advanced_options,
                    "array_extract": array_extract,
                    "experimental_options": experimental_options,
                    "generate_citations": generate_citations,
                    "options": options,
                    "system_prompt": system_prompt,
                },
                extract_run_params.ExtractRunParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ExtractResponse,
        )

    async def run_job(
        self,
        *,
        document_url: extract_run_job_params.DocumentURL,
        schema: object,
        advanced_options: AdvancedProcessingOptions | NotGiven = NOT_GIVEN,
        array_extract: ArrayExtractConfig | NotGiven = NOT_GIVEN,
        experimental_options: ExperimentalProcessingOptions | NotGiven = NOT_GIVEN,
        generate_citations: bool | NotGiven = NOT_GIVEN,
        options: BaseProcessingOptions | NotGiven = NOT_GIVEN,
        priority: bool | NotGiven = NOT_GIVEN,
        system_prompt: str | NotGiven = NOT_GIVEN,
        webhook: WebhookConfigNew | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ExtractRunJobResponse:
        """
        Extract Async

        Args:
          document_url:
              The URL of the document to be processed. You can provide one of the following:

              1. A publicly available URL
              2. A presigned S3 URL
              3. A reducto:// prefixed URL obtained from the /upload endpoint after directly
                 uploading a document

          schema: The JSON schema to use for extraction.

          array_extract: The configuration options for array extract

          generate_citations: If citations should be generated for the extracted content.

          priority: If True, attempts to process the job with priority if the user has priority
              processing budget available; by default, sync jobs are prioritized above async
              jobs.

          system_prompt: A system prompt to use for the extraction. This is a general prompt that is
              applied to the entire document before any other prompts.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/extract_async",
            body=await async_maybe_transform(
                {
                    "document_url": document_url,
                    "schema": schema,
                    "advanced_options": advanced_options,
                    "array_extract": array_extract,
                    "experimental_options": experimental_options,
                    "generate_citations": generate_citations,
                    "options": options,
                    "priority": priority,
                    "system_prompt": system_prompt,
                    "webhook": webhook,
                },
                extract_run_job_params.ExtractRunJobParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ExtractRunJobResponse,
        )


class ExtractResourceWithRawResponse:
    def __init__(self, extract: ExtractResource) -> None:
        self._extract = extract

        self.run = to_raw_response_wrapper(
            extract.run,
        )
        self.run_job = to_raw_response_wrapper(
            extract.run_job,
        )


class AsyncExtractResourceWithRawResponse:
    def __init__(self, extract: AsyncExtractResource) -> None:
        self._extract = extract

        self.run = async_to_raw_response_wrapper(
            extract.run,
        )
        self.run_job = async_to_raw_response_wrapper(
            extract.run_job,
        )


class ExtractResourceWithStreamingResponse:
    def __init__(self, extract: ExtractResource) -> None:
        self._extract = extract

        self.run = to_streamed_response_wrapper(
            extract.run,
        )
        self.run_job = to_streamed_response_wrapper(
            extract.run_job,
        )


class AsyncExtractResourceWithStreamingResponse:
    def __init__(self, extract: AsyncExtractResource) -> None:
        self._extract = extract

        self.run = async_to_streamed_response_wrapper(
            extract.run,
        )
        self.run_job = async_to_streamed_response_wrapper(
            extract.run_job,
        )
