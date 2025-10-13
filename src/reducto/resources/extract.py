# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Any, Dict, Union, cast
from typing_extensions import overload

import httpx

from ..types import extract_run_params, extract_run_job_params
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
from ..types.extract_run_response import ExtractRunResponse
from ..types.extract_run_job_response import ExtractRunJobResponse
from ..types.shared_params.webhook_config_new import WebhookConfigNew
from ..types.shared_params.array_extract_config import ArrayExtractConfig
from ..types.shared_params.base_processing_options import BaseProcessingOptions
from ..types.shared_params.advanced_citations_config import AdvancedCitationsConfig
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

    @overload
    def run(
        self,
        *,
        document_url: extract_run_params.ExtractConfigDocumentURL,
        schema: object,
        advanced_options: AdvancedProcessingOptions | Omit = omit,
        agent_extract: extract_run_params.ExtractConfigAgentExtract | Omit = omit,
        array_extract: ArrayExtractConfig | Omit = omit,
        citations_options: AdvancedCitationsConfig | Omit = omit,
        experimental_options: ExperimentalProcessingOptions | Omit = omit,
        experimental_table_citations: bool | Omit = omit,
        generate_citations: bool | Omit = omit,
        include_images: bool | Omit = omit,
        latency_sensitive: bool | Omit = omit,
        options: BaseProcessingOptions | Omit = omit,
        priority: bool | Omit = omit,
        spreadsheet_agent: bool | Omit = omit,
        system_prompt: str | Omit = omit,
        use_chunking: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ExtractRunResponse:
        """Extract

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

          schema: The JSON schema to use for extraction.

          agent_extract: The configuration options for agent extract

          array_extract: The configuration options for array extract

          citations_options: The configuration options for citations.

          experimental_table_citations: If table citations should be generated for the extracted content.

          generate_citations: If citations should be generated for the extracted content.

          include_images: If images should be passed directly for extractions. Can only be enabled for
              documents with less than 10 pages. Defaults to False.

          latency_sensitive: If True, the job will be processed with lower latency and higher priority. Uses
              2x the cost of a regular job. Defaults to False.

          priority: If True, attempts to process the job with priority if the user has priority
              processing budget available; by default, sync jobs are prioritized above async
              jobs.

          spreadsheet_agent: If spreadsheet agent should be used for extraction.

          system_prompt: A system prompt to use for the extraction. This is a general prompt that is
              applied to the entire document before any other prompts.

          use_chunking: If chunking should be used for the extraction. Defaults to False.

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
        schema: object,
        agent_extract: bool | Omit = omit,
        alpha_big_extraction_model: bool | Omit = omit,
        alpha_deep_extract: bool | Omit = omit,
        alpha_table_citations: bool | Omit = omit,
        async_: extract_run_params.ExtractConfigAsync | Omit = omit,
        include_images: bool | Omit = omit,
        latency_sensitive: bool | Omit = omit,
        normalized_schema: object | Omit = omit,
        options: extract_run_params.ExtractConfigOptions | Omit = omit,
        parse_config: extract_run_params.ExtractConfigParseConfig | Omit = omit,
        priority: bool | Omit = omit,
        system_prompt: str | Omit = omit,
        user_config: Dict[str, object] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ExtractRunResponse:
        """
        Extract

        Args:
          schema: The JSON schema to use for extraction.

          agent_extract: If agent extraction should be used for extraction.

          async_: The configuration options for asynchronous processing (default synchronous).

          latency_sensitive: If True, the job will be processed with lower latency and higher priority. Uses
              2x the cost of a regular job. Defaults to False.

          normalized_schema: The normalized JSON schema to use for extraction.

          options: The configuration options for extraction.

          parse_config: The configuration options for extraction.

          priority: If True, attempts to process the job with priority if the user has priority
              processing budget available; by default, sync jobs are prioritized above async
              jobs.

          system_prompt: A system prompt to use for the extraction. This is a general prompt that is
              applied to the entire document before any other prompts.

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
        input: extract_run_params.SyncExtractConfigInput,
        instructions: extract_run_params.SyncExtractConfigInstructions | Omit = omit,
        parsing: extract_run_params.SyncExtractConfigParsing | Omit = omit,
        settings: extract_run_params.SyncExtractConfigSettings | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ExtractRunResponse:
        """Extract

        Args:
          input: The URL of the document to be processed.

        You can provide one of the
              following: 1. A publicly available URL 2. A presigned S3 URL 3. A reducto://
              prefixed URL obtained from the /upload endpoint after directly uploading a
              document 4. A jobid:// prefixed URL obtained from a previous /parse invocation

          instructions: The instructions to use for the extraction.

          parsing: The configuration options for parsing the document. If you are passing in a
              jobid:// URL for the file, then this configuration will be ignored.

          settings: The settings to use for the extraction.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @required_args(["document_url", "schema"], ["input"])
    def run(
        self,
        *,
        document_url: extract_run_params.ExtractConfigDocumentURL | Union[str, SequenceNotStr[str]] | Omit = omit,
        schema: object | Omit = omit,
        advanced_options: AdvancedProcessingOptions | Omit = omit,
        agent_extract: extract_run_params.ExtractConfigAgentExtract | bool | Omit = omit,
        array_extract: ArrayExtractConfig | Omit = omit,
        citations_options: AdvancedCitationsConfig | Omit = omit,
        experimental_options: ExperimentalProcessingOptions | Omit = omit,
        experimental_table_citations: bool | Omit = omit,
        generate_citations: bool | Omit = omit,
        include_images: bool | Omit = omit,
        latency_sensitive: bool | Omit = omit,
        options: BaseProcessingOptions | extract_run_params.ExtractConfigOptions | Omit = omit,
        priority: bool | Omit = omit,
        spreadsheet_agent: bool | Omit = omit,
        system_prompt: str | Omit = omit,
        use_chunking: bool | Omit = omit,
        alpha_big_extraction_model: bool | Omit = omit,
        alpha_deep_extract: bool | Omit = omit,
        alpha_table_citations: bool | Omit = omit,
        async_: extract_run_params.ExtractConfigAsync | Omit = omit,
        normalized_schema: object | Omit = omit,
        parse_config: extract_run_params.ExtractConfigParseConfig | Omit = omit,
        user_config: Dict[str, object] | Omit = omit,
        input: extract_run_params.SyncExtractConfigInput | Omit = omit,
        instructions: extract_run_params.SyncExtractConfigInstructions | Omit = omit,
        parsing: extract_run_params.SyncExtractConfigParsing | Omit = omit,
        settings: extract_run_params.SyncExtractConfigSettings | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ExtractRunResponse:
        return cast(
            ExtractRunResponse,
            self._post(
                "/extract",
                body=maybe_transform(
                    {
                        "document_url": document_url,
                        "schema": schema,
                        "advanced_options": advanced_options,
                        "agent_extract": agent_extract,
                        "array_extract": array_extract,
                        "citations_options": citations_options,
                        "experimental_options": experimental_options,
                        "experimental_table_citations": experimental_table_citations,
                        "generate_citations": generate_citations,
                        "include_images": include_images,
                        "latency_sensitive": latency_sensitive,
                        "options": options,
                        "priority": priority,
                        "spreadsheet_agent": spreadsheet_agent,
                        "system_prompt": system_prompt,
                        "use_chunking": use_chunking,
                        "alpha_big_extraction_model": alpha_big_extraction_model,
                        "alpha_deep_extract": alpha_deep_extract,
                        "alpha_table_citations": alpha_table_citations,
                        "async_": async_,
                        "normalized_schema": normalized_schema,
                        "parse_config": parse_config,
                        "user_config": user_config,
                        "input": input,
                        "instructions": instructions,
                        "parsing": parsing,
                        "settings": settings,
                    },
                    extract_run_params.ExtractRunParams,
                ),
                options=make_request_options(
                    extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
                ),
                cast_to=cast(
                    Any, ExtractRunResponse
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )

    @overload
    def run_job(
        self,
        *,
        document_url: extract_run_job_params.AsyncExtractConfigNewDocumentURL,
        schema: object,
        advanced_options: AdvancedProcessingOptions | Omit = omit,
        agent_extract: extract_run_job_params.AsyncExtractConfigNewAgentExtract | Omit = omit,
        array_extract: ArrayExtractConfig | Omit = omit,
        citations_options: AdvancedCitationsConfig | Omit = omit,
        experimental_options: ExperimentalProcessingOptions | Omit = omit,
        experimental_table_citations: bool | Omit = omit,
        generate_citations: bool | Omit = omit,
        include_images: bool | Omit = omit,
        latency_sensitive: bool | Omit = omit,
        options: BaseProcessingOptions | Omit = omit,
        priority: bool | Omit = omit,
        spreadsheet_agent: bool | Omit = omit,
        system_prompt: str | Omit = omit,
        use_chunking: bool | Omit = omit,
        webhook: WebhookConfigNew | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
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
              4. A job_id (jobid://) or a list of job_ids (jobid://) obtained from a previous
                 /parse endpoint

          schema: The JSON schema to use for extraction.

          agent_extract: The configuration options for agent extract

          array_extract: The configuration options for array extract

          citations_options: The configuration options for citations.

          experimental_table_citations: If table citations should be generated for the extracted content.

          generate_citations: If citations should be generated for the extracted content.

          include_images: If images should be passed directly for extractions. Can only be enabled for
              documents with less than 10 pages. Defaults to False.

          latency_sensitive: If True, the job will be processed with lower latency and higher priority. Uses
              2x the cost of a regular job. Defaults to False.

          priority: If True, attempts to process the job with priority if the user has priority
              processing budget available; by default, sync jobs are prioritized above async
              jobs.

          spreadsheet_agent: If spreadsheet agent should be used for extraction.

          system_prompt: A system prompt to use for the extraction. This is a general prompt that is
              applied to the entire document before any other prompts.

          use_chunking: If chunking should be used for the extraction. Defaults to False.

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
        input: extract_run_job_params.AsyncExtractConfigInput,
        async_: extract_run_job_params.AsyncExtractConfigAsync | Omit = omit,
        instructions: extract_run_job_params.AsyncExtractConfigInstructions | Omit = omit,
        parsing: extract_run_job_params.AsyncExtractConfigParsing | Omit = omit,
        settings: extract_run_job_params.AsyncExtractConfigSettings | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ExtractRunJobResponse:
        """Extract Async

        Args:
          input: The URL of the document to be processed.

        You can provide one of the
              following: 1. A publicly available URL 2. A presigned S3 URL 3. A reducto://
              prefixed URL obtained from the /upload endpoint after directly uploading a
              document 4. A jobid:// prefixed URL obtained from a previous /parse invocation

          async_: The configuration options for asynchronous processing (default synchronous).

          instructions: The instructions to use for the extraction.

          parsing: The configuration options for parsing the document. If you are passing in a
              jobid:// URL for the file, then this configuration will be ignored.

          settings: The settings to use for the extraction.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @required_args(["document_url", "schema"], ["input"])
    def run_job(
        self,
        *,
        document_url: extract_run_job_params.AsyncExtractConfigNewDocumentURL | Omit = omit,
        schema: object | Omit = omit,
        advanced_options: AdvancedProcessingOptions | Omit = omit,
        agent_extract: extract_run_job_params.AsyncExtractConfigNewAgentExtract | Omit = omit,
        array_extract: ArrayExtractConfig | Omit = omit,
        citations_options: AdvancedCitationsConfig | Omit = omit,
        experimental_options: ExperimentalProcessingOptions | Omit = omit,
        experimental_table_citations: bool | Omit = omit,
        generate_citations: bool | Omit = omit,
        include_images: bool | Omit = omit,
        latency_sensitive: bool | Omit = omit,
        options: BaseProcessingOptions | Omit = omit,
        priority: bool | Omit = omit,
        spreadsheet_agent: bool | Omit = omit,
        system_prompt: str | Omit = omit,
        use_chunking: bool | Omit = omit,
        webhook: WebhookConfigNew | Omit = omit,
        input: extract_run_job_params.AsyncExtractConfigInput | Omit = omit,
        async_: extract_run_job_params.AsyncExtractConfigAsync | Omit = omit,
        instructions: extract_run_job_params.AsyncExtractConfigInstructions | Omit = omit,
        parsing: extract_run_job_params.AsyncExtractConfigParsing | Omit = omit,
        settings: extract_run_job_params.AsyncExtractConfigSettings | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ExtractRunJobResponse:
        return self._post(
            "/extract_async",
            body=maybe_transform(
                {
                    "document_url": document_url,
                    "schema": schema,
                    "advanced_options": advanced_options,
                    "agent_extract": agent_extract,
                    "array_extract": array_extract,
                    "citations_options": citations_options,
                    "experimental_options": experimental_options,
                    "experimental_table_citations": experimental_table_citations,
                    "generate_citations": generate_citations,
                    "include_images": include_images,
                    "latency_sensitive": latency_sensitive,
                    "options": options,
                    "priority": priority,
                    "spreadsheet_agent": spreadsheet_agent,
                    "system_prompt": system_prompt,
                    "use_chunking": use_chunking,
                    "webhook": webhook,
                    "input": input,
                    "async_": async_,
                    "instructions": instructions,
                    "parsing": parsing,
                    "settings": settings,
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

    @overload
    async def run(
        self,
        *,
        document_url: extract_run_params.ExtractConfigDocumentURL,
        schema: object,
        advanced_options: AdvancedProcessingOptions | Omit = omit,
        agent_extract: extract_run_params.ExtractConfigAgentExtract | Omit = omit,
        array_extract: ArrayExtractConfig | Omit = omit,
        citations_options: AdvancedCitationsConfig | Omit = omit,
        experimental_options: ExperimentalProcessingOptions | Omit = omit,
        experimental_table_citations: bool | Omit = omit,
        generate_citations: bool | Omit = omit,
        include_images: bool | Omit = omit,
        latency_sensitive: bool | Omit = omit,
        options: BaseProcessingOptions | Omit = omit,
        priority: bool | Omit = omit,
        spreadsheet_agent: bool | Omit = omit,
        system_prompt: str | Omit = omit,
        use_chunking: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ExtractRunResponse:
        """Extract

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

          schema: The JSON schema to use for extraction.

          agent_extract: The configuration options for agent extract

          array_extract: The configuration options for array extract

          citations_options: The configuration options for citations.

          experimental_table_citations: If table citations should be generated for the extracted content.

          generate_citations: If citations should be generated for the extracted content.

          include_images: If images should be passed directly for extractions. Can only be enabled for
              documents with less than 10 pages. Defaults to False.

          latency_sensitive: If True, the job will be processed with lower latency and higher priority. Uses
              2x the cost of a regular job. Defaults to False.

          priority: If True, attempts to process the job with priority if the user has priority
              processing budget available; by default, sync jobs are prioritized above async
              jobs.

          spreadsheet_agent: If spreadsheet agent should be used for extraction.

          system_prompt: A system prompt to use for the extraction. This is a general prompt that is
              applied to the entire document before any other prompts.

          use_chunking: If chunking should be used for the extraction. Defaults to False.

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
        schema: object,
        agent_extract: bool | Omit = omit,
        alpha_big_extraction_model: bool | Omit = omit,
        alpha_deep_extract: bool | Omit = omit,
        alpha_table_citations: bool | Omit = omit,
        async_: extract_run_params.ExtractConfigAsync | Omit = omit,
        include_images: bool | Omit = omit,
        latency_sensitive: bool | Omit = omit,
        normalized_schema: object | Omit = omit,
        options: extract_run_params.ExtractConfigOptions | Omit = omit,
        parse_config: extract_run_params.ExtractConfigParseConfig | Omit = omit,
        priority: bool | Omit = omit,
        system_prompt: str | Omit = omit,
        user_config: Dict[str, object] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ExtractRunResponse:
        """
        Extract

        Args:
          schema: The JSON schema to use for extraction.

          agent_extract: If agent extraction should be used for extraction.

          async_: The configuration options for asynchronous processing (default synchronous).

          latency_sensitive: If True, the job will be processed with lower latency and higher priority. Uses
              2x the cost of a regular job. Defaults to False.

          normalized_schema: The normalized JSON schema to use for extraction.

          options: The configuration options for extraction.

          parse_config: The configuration options for extraction.

          priority: If True, attempts to process the job with priority if the user has priority
              processing budget available; by default, sync jobs are prioritized above async
              jobs.

          system_prompt: A system prompt to use for the extraction. This is a general prompt that is
              applied to the entire document before any other prompts.

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
        input: extract_run_params.SyncExtractConfigInput,
        instructions: extract_run_params.SyncExtractConfigInstructions | Omit = omit,
        parsing: extract_run_params.SyncExtractConfigParsing | Omit = omit,
        settings: extract_run_params.SyncExtractConfigSettings | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ExtractRunResponse:
        """Extract

        Args:
          input: The URL of the document to be processed.

        You can provide one of the
              following: 1. A publicly available URL 2. A presigned S3 URL 3. A reducto://
              prefixed URL obtained from the /upload endpoint after directly uploading a
              document 4. A jobid:// prefixed URL obtained from a previous /parse invocation

          instructions: The instructions to use for the extraction.

          parsing: The configuration options for parsing the document. If you are passing in a
              jobid:// URL for the file, then this configuration will be ignored.

          settings: The settings to use for the extraction.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @required_args(["document_url", "schema"], ["input"])
    async def run(
        self,
        *,
        document_url: extract_run_params.ExtractConfigDocumentURL | Union[str, SequenceNotStr[str]] | Omit = omit,
        schema: object | Omit = omit,
        advanced_options: AdvancedProcessingOptions | Omit = omit,
        agent_extract: extract_run_params.ExtractConfigAgentExtract | bool | Omit = omit,
        array_extract: ArrayExtractConfig | Omit = omit,
        citations_options: AdvancedCitationsConfig | Omit = omit,
        experimental_options: ExperimentalProcessingOptions | Omit = omit,
        experimental_table_citations: bool | Omit = omit,
        generate_citations: bool | Omit = omit,
        include_images: bool | Omit = omit,
        latency_sensitive: bool | Omit = omit,
        options: BaseProcessingOptions | extract_run_params.ExtractConfigOptions | Omit = omit,
        priority: bool | Omit = omit,
        spreadsheet_agent: bool | Omit = omit,
        system_prompt: str | Omit = omit,
        use_chunking: bool | Omit = omit,
        alpha_big_extraction_model: bool | Omit = omit,
        alpha_deep_extract: bool | Omit = omit,
        alpha_table_citations: bool | Omit = omit,
        async_: extract_run_params.ExtractConfigAsync | Omit = omit,
        normalized_schema: object | Omit = omit,
        parse_config: extract_run_params.ExtractConfigParseConfig | Omit = omit,
        user_config: Dict[str, object] | Omit = omit,
        input: extract_run_params.SyncExtractConfigInput | Omit = omit,
        instructions: extract_run_params.SyncExtractConfigInstructions | Omit = omit,
        parsing: extract_run_params.SyncExtractConfigParsing | Omit = omit,
        settings: extract_run_params.SyncExtractConfigSettings | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ExtractRunResponse:
        return cast(
            ExtractRunResponse,
            await self._post(
                "/extract",
                body=await async_maybe_transform(
                    {
                        "document_url": document_url,
                        "schema": schema,
                        "advanced_options": advanced_options,
                        "agent_extract": agent_extract,
                        "array_extract": array_extract,
                        "citations_options": citations_options,
                        "experimental_options": experimental_options,
                        "experimental_table_citations": experimental_table_citations,
                        "generate_citations": generate_citations,
                        "include_images": include_images,
                        "latency_sensitive": latency_sensitive,
                        "options": options,
                        "priority": priority,
                        "spreadsheet_agent": spreadsheet_agent,
                        "system_prompt": system_prompt,
                        "use_chunking": use_chunking,
                        "alpha_big_extraction_model": alpha_big_extraction_model,
                        "alpha_deep_extract": alpha_deep_extract,
                        "alpha_table_citations": alpha_table_citations,
                        "async_": async_,
                        "normalized_schema": normalized_schema,
                        "parse_config": parse_config,
                        "user_config": user_config,
                        "input": input,
                        "instructions": instructions,
                        "parsing": parsing,
                        "settings": settings,
                    },
                    extract_run_params.ExtractRunParams,
                ),
                options=make_request_options(
                    extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
                ),
                cast_to=cast(
                    Any, ExtractRunResponse
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )

    @overload
    async def run_job(
        self,
        *,
        document_url: extract_run_job_params.AsyncExtractConfigNewDocumentURL,
        schema: object,
        advanced_options: AdvancedProcessingOptions | Omit = omit,
        agent_extract: extract_run_job_params.AsyncExtractConfigNewAgentExtract | Omit = omit,
        array_extract: ArrayExtractConfig | Omit = omit,
        citations_options: AdvancedCitationsConfig | Omit = omit,
        experimental_options: ExperimentalProcessingOptions | Omit = omit,
        experimental_table_citations: bool | Omit = omit,
        generate_citations: bool | Omit = omit,
        include_images: bool | Omit = omit,
        latency_sensitive: bool | Omit = omit,
        options: BaseProcessingOptions | Omit = omit,
        priority: bool | Omit = omit,
        spreadsheet_agent: bool | Omit = omit,
        system_prompt: str | Omit = omit,
        use_chunking: bool | Omit = omit,
        webhook: WebhookConfigNew | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
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
              4. A job_id (jobid://) or a list of job_ids (jobid://) obtained from a previous
                 /parse endpoint

          schema: The JSON schema to use for extraction.

          agent_extract: The configuration options for agent extract

          array_extract: The configuration options for array extract

          citations_options: The configuration options for citations.

          experimental_table_citations: If table citations should be generated for the extracted content.

          generate_citations: If citations should be generated for the extracted content.

          include_images: If images should be passed directly for extractions. Can only be enabled for
              documents with less than 10 pages. Defaults to False.

          latency_sensitive: If True, the job will be processed with lower latency and higher priority. Uses
              2x the cost of a regular job. Defaults to False.

          priority: If True, attempts to process the job with priority if the user has priority
              processing budget available; by default, sync jobs are prioritized above async
              jobs.

          spreadsheet_agent: If spreadsheet agent should be used for extraction.

          system_prompt: A system prompt to use for the extraction. This is a general prompt that is
              applied to the entire document before any other prompts.

          use_chunking: If chunking should be used for the extraction. Defaults to False.

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
        input: extract_run_job_params.AsyncExtractConfigInput,
        async_: extract_run_job_params.AsyncExtractConfigAsync | Omit = omit,
        instructions: extract_run_job_params.AsyncExtractConfigInstructions | Omit = omit,
        parsing: extract_run_job_params.AsyncExtractConfigParsing | Omit = omit,
        settings: extract_run_job_params.AsyncExtractConfigSettings | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ExtractRunJobResponse:
        """Extract Async

        Args:
          input: The URL of the document to be processed.

        You can provide one of the
              following: 1. A publicly available URL 2. A presigned S3 URL 3. A reducto://
              prefixed URL obtained from the /upload endpoint after directly uploading a
              document 4. A jobid:// prefixed URL obtained from a previous /parse invocation

          async_: The configuration options for asynchronous processing (default synchronous).

          instructions: The instructions to use for the extraction.

          parsing: The configuration options for parsing the document. If you are passing in a
              jobid:// URL for the file, then this configuration will be ignored.

          settings: The settings to use for the extraction.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @required_args(["document_url", "schema"], ["input"])
    async def run_job(
        self,
        *,
        document_url: extract_run_job_params.AsyncExtractConfigNewDocumentURL | Omit = omit,
        schema: object | Omit = omit,
        advanced_options: AdvancedProcessingOptions | Omit = omit,
        agent_extract: extract_run_job_params.AsyncExtractConfigNewAgentExtract | Omit = omit,
        array_extract: ArrayExtractConfig | Omit = omit,
        citations_options: AdvancedCitationsConfig | Omit = omit,
        experimental_options: ExperimentalProcessingOptions | Omit = omit,
        experimental_table_citations: bool | Omit = omit,
        generate_citations: bool | Omit = omit,
        include_images: bool | Omit = omit,
        latency_sensitive: bool | Omit = omit,
        options: BaseProcessingOptions | Omit = omit,
        priority: bool | Omit = omit,
        spreadsheet_agent: bool | Omit = omit,
        system_prompt: str | Omit = omit,
        use_chunking: bool | Omit = omit,
        webhook: WebhookConfigNew | Omit = omit,
        input: extract_run_job_params.AsyncExtractConfigInput | Omit = omit,
        async_: extract_run_job_params.AsyncExtractConfigAsync | Omit = omit,
        instructions: extract_run_job_params.AsyncExtractConfigInstructions | Omit = omit,
        parsing: extract_run_job_params.AsyncExtractConfigParsing | Omit = omit,
        settings: extract_run_job_params.AsyncExtractConfigSettings | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ExtractRunJobResponse:
        return await self._post(
            "/extract_async",
            body=await async_maybe_transform(
                {
                    "document_url": document_url,
                    "schema": schema,
                    "advanced_options": advanced_options,
                    "agent_extract": agent_extract,
                    "array_extract": array_extract,
                    "citations_options": citations_options,
                    "experimental_options": experimental_options,
                    "experimental_table_citations": experimental_table_citations,
                    "generate_citations": generate_citations,
                    "include_images": include_images,
                    "latency_sensitive": latency_sensitive,
                    "options": options,
                    "priority": priority,
                    "spreadsheet_agent": spreadsheet_agent,
                    "system_prompt": system_prompt,
                    "use_chunking": use_chunking,
                    "webhook": webhook,
                    "input": input,
                    "async_": async_,
                    "instructions": instructions,
                    "parsing": parsing,
                    "settings": settings,
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
