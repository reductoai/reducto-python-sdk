# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, Union, Mapping, Iterable, Optional, cast
from typing_extensions import Self, override

import httpx

from . import _exceptions
from ._qs import Querystring
from .types import (
    client_create_parse_params,
    client_create_split_params,
    client_create_upload_params,
    client_create_extract_params,
    client_create_parse_async_params,
    client_create_split_async_params,
    client_create_extract_async_params,
)
from ._types import (
    NOT_GIVEN,
    Body,
    Omit,
    Query,
    Headers,
    Timeout,
    NotGiven,
    FileTypes,
    Transport,
    ProxiesTypes,
    RequestOptions,
)
from ._utils import (
    is_given,
    extract_files,
    maybe_transform,
    deepcopy_minimal,
    get_async_library,
    async_maybe_transform,
)
from ._version import __version__
from ._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ._streaming import Stream as Stream, AsyncStream as AsyncStream
from ._exceptions import APIStatusError, ReductoaiError
from ._base_client import (
    DEFAULT_MAX_RETRIES,
    SyncAPIClient,
    AsyncAPIClient,
    make_request_options,
)
from .types.retrieve_job_response import RetrieveJobResponse
from .types.shared.parse_response import ParseResponse
from .types.shared.split_response import SplitResponse
from .types.create_upload_response import CreateUploadResponse
from .types.shared.extract_response import ExtractResponse
from .types.create_parse_async_response import CreateParseAsyncResponse
from .types.create_split_async_response import CreateSplitAsyncResponse
from .types.shared_params.split_category import SplitCategory
from .types.create_extract_async_response import CreateExtractAsyncResponse
from .types.shared_params.webhook_config_new import WebhookConfigNew
from .types.shared_params.array_extract_config import ArrayExtractConfig
from .types.shared_params.base_processing_options import BaseProcessingOptions
from .types.shared_params.advanced_processing_options import AdvancedProcessingOptions
from .types.shared_params.experimental_processing_options import ExperimentalProcessingOptions

__all__ = [
    "Timeout",
    "Transport",
    "ProxiesTypes",
    "RequestOptions",
    "Reductoai",
    "AsyncReductoai",
    "Client",
    "AsyncClient",
]


class Reductoai(SyncAPIClient):
    with_raw_response: ReductoaiWithRawResponse
    with_streaming_response: ReductoaiWithStreamedResponse

    # client options
    bearer_token: str

    def __init__(
        self,
        *,
        bearer_token: str | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
        max_retries: int = DEFAULT_MAX_RETRIES,
        default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        # Configure a custom httpx client.
        # We provide a `DefaultHttpxClient` class that you can pass to retain the default values we use for `limits`, `timeout` & `follow_redirects`.
        # See the [httpx documentation](https://www.python-httpx.org/api/#client) for more details.
        http_client: httpx.Client | None = None,
        # Enable or disable schema validation for data returned by the API.
        # When enabled an error APIResponseValidationError is raised
        # if the API responds with invalid data for the expected schema.
        #
        # This parameter may be removed or changed in the future.
        # If you rely on this feature, please open a GitHub issue
        # outlining your use-case to help us decide if it should be
        # part of our public interface in the future.
        _strict_response_validation: bool = False,
    ) -> None:
        """Construct a new synchronous reductoai client instance.

        This automatically infers the `bearer_token` argument from the `REDUCTOAI_BEARER_TOKEN` environment variable if it is not provided.
        """
        if bearer_token is None:
            bearer_token = os.environ.get("REDUCTOAI_BEARER_TOKEN")
        if bearer_token is None:
            raise ReductoaiError(
                "The bearer_token client option must be set either by passing bearer_token to the client or by setting the REDUCTOAI_BEARER_TOKEN environment variable"
            )
        self.bearer_token = bearer_token

        if base_url is None:
            base_url = os.environ.get("REDUCTOAI_BASE_URL")
        if base_url is None:
            base_url = f"https://platform.reducto.ai"

        super().__init__(
            version=__version__,
            base_url=base_url,
            max_retries=max_retries,
            timeout=timeout,
            http_client=http_client,
            custom_headers=default_headers,
            custom_query=default_query,
            _strict_response_validation=_strict_response_validation,
        )

        self.with_raw_response = ReductoaiWithRawResponse(self)
        self.with_streaming_response = ReductoaiWithStreamedResponse(self)

    @property
    @override
    def qs(self) -> Querystring:
        return Querystring(array_format="comma")

    @property
    @override
    def auth_headers(self) -> dict[str, str]:
        bearer_token = self.bearer_token
        return {"Authorization": f"Bearer {bearer_token}"}

    @property
    @override
    def default_headers(self) -> dict[str, str | Omit]:
        return {
            **super().default_headers,
            "X-Stainless-Async": "false",
            **self._custom_headers,
        }

    def copy(
        self,
        *,
        bearer_token: str | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: float | Timeout | None | NotGiven = NOT_GIVEN,
        http_client: httpx.Client | None = None,
        max_retries: int | NotGiven = NOT_GIVEN,
        default_headers: Mapping[str, str] | None = None,
        set_default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        set_default_query: Mapping[str, object] | None = None,
        _extra_kwargs: Mapping[str, Any] = {},
    ) -> Self:
        """
        Create a new client instance re-using the same options given to the current client with optional overriding.
        """
        if default_headers is not None and set_default_headers is not None:
            raise ValueError("The `default_headers` and `set_default_headers` arguments are mutually exclusive")

        if default_query is not None and set_default_query is not None:
            raise ValueError("The `default_query` and `set_default_query` arguments are mutually exclusive")

        headers = self._custom_headers
        if default_headers is not None:
            headers = {**headers, **default_headers}
        elif set_default_headers is not None:
            headers = set_default_headers

        params = self._custom_query
        if default_query is not None:
            params = {**params, **default_query}
        elif set_default_query is not None:
            params = set_default_query

        http_client = http_client or self._client
        return self.__class__(
            bearer_token=bearer_token or self.bearer_token,
            base_url=base_url or self.base_url,
            timeout=self.timeout if isinstance(timeout, NotGiven) else timeout,
            http_client=http_client,
            max_retries=max_retries if is_given(max_retries) else self.max_retries,
            default_headers=headers,
            default_query=params,
            **_extra_kwargs,
        )

    # Alias for `copy` for nicer inline usage, e.g.
    # client.with_options(timeout=10).foo.create(...)
    with_options = copy

    def cancel_job(
        self,
        job_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
        """
        Cancel Job

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not job_id:
            raise ValueError(f"Expected a non-empty value for `job_id` but received {job_id!r}")
        return self.post(
            f"/cancel/{job_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )

    def configure_webhook(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> str:
        """Webhook Portal"""
        return self.post(
            "/configure_webhook",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=str,
        )

    def create_extract(
        self,
        *,
        document_url: str,
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
        return self.post(
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
                client_create_extract_params.ClientCreateExtractParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ExtractResponse,
        )

    def create_extract_async(
        self,
        *,
        document_url: str,
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
    ) -> CreateExtractAsyncResponse:
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
        return self.post(
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
                client_create_extract_async_params.ClientCreateExtractAsyncParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CreateExtractAsyncResponse,
        )

    def create_parse(
        self,
        *,
        document_url: str,
        advanced_options: AdvancedProcessingOptions | NotGiven = NOT_GIVEN,
        experimental_options: ExperimentalProcessingOptions | NotGiven = NOT_GIVEN,
        options: BaseProcessingOptions | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ParseResponse:
        """Parse

        Args:
          document_url:
              The URL of the document to be processed.

        You can provide one of the following:

              1. A publicly available URL
              2. A presigned S3 URL
              3. A reducto:// prefixed URL obtained from the /upload endpoint after directly
                 uploading a document

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self.post(
            "/parse",
            body=maybe_transform(
                {
                    "document_url": document_url,
                    "advanced_options": advanced_options,
                    "experimental_options": experimental_options,
                    "options": options,
                },
                client_create_parse_params.ClientCreateParseParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ParseResponse,
        )

    def create_parse_async(
        self,
        *,
        document_url: str,
        advanced_options: AdvancedProcessingOptions | NotGiven = NOT_GIVEN,
        experimental_options: ExperimentalProcessingOptions | NotGiven = NOT_GIVEN,
        options: BaseProcessingOptions | NotGiven = NOT_GIVEN,
        priority: bool | NotGiven = NOT_GIVEN,
        webhook: WebhookConfigNew | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CreateParseAsyncResponse:
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
        return self.post(
            "/parse_async",
            body=maybe_transform(
                {
                    "document_url": document_url,
                    "advanced_options": advanced_options,
                    "experimental_options": experimental_options,
                    "options": options,
                    "priority": priority,
                    "webhook": webhook,
                },
                client_create_parse_async_params.ClientCreateParseAsyncParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CreateParseAsyncResponse,
        )

    def create_split(
        self,
        *,
        document_url: str,
        split_description: Iterable[SplitCategory],
        advanced_options: AdvancedProcessingOptions | NotGiven = NOT_GIVEN,
        experimental_options: ExperimentalProcessingOptions | NotGiven = NOT_GIVEN,
        options: BaseProcessingOptions | NotGiven = NOT_GIVEN,
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

          split_description: The configuration options for processing the document.

          split_rules: The rules for splitting the document.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self.post(
            "/split",
            body=maybe_transform(
                {
                    "document_url": document_url,
                    "split_description": split_description,
                    "advanced_options": advanced_options,
                    "experimental_options": experimental_options,
                    "options": options,
                    "split_rules": split_rules,
                },
                client_create_split_params.ClientCreateSplitParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SplitResponse,
        )

    def create_split_async(
        self,
        *,
        document_url: str,
        split_description: Iterable[SplitCategory],
        advanced_options: AdvancedProcessingOptions | NotGiven = NOT_GIVEN,
        experimental_options: ExperimentalProcessingOptions | NotGiven = NOT_GIVEN,
        options: BaseProcessingOptions | NotGiven = NOT_GIVEN,
        priority: bool | NotGiven = NOT_GIVEN,
        split_rules: str | NotGiven = NOT_GIVEN,
        webhook: WebhookConfigNew | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CreateSplitAsyncResponse:
        """
        Split Async

        Args:
          document_url:
              The URL of the document to be processed. You can provide one of the following:

              1. A publicly available URL
              2. A presigned S3 URL
              3. A reducto:// prefixed URL obtained from the /upload endpoint after directly
                 uploading a document

          split_description: The configuration options for processing the document.

          priority: If True, attempts to process the job with priority if the user has priority
              processing budget available; by default, sync jobs are prioritized above async
              jobs.

          split_rules: The rules for splitting the document.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self.post(
            "/split_async",
            body=maybe_transform(
                {
                    "document_url": document_url,
                    "split_description": split_description,
                    "advanced_options": advanced_options,
                    "experimental_options": experimental_options,
                    "options": options,
                    "priority": priority,
                    "split_rules": split_rules,
                    "webhook": webhook,
                },
                client_create_split_async_params.ClientCreateSplitAsyncParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CreateSplitAsyncResponse,
        )

    def create_upload(
        self,
        *,
        extension: Optional[str] | NotGiven = NOT_GIVEN,
        file: FileTypes | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CreateUploadResponse:
        """
        Upload

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        body = deepcopy_minimal({"file": file})
        files = extract_files(cast(Mapping[str, object], body), paths=[["file"]])
        # It should be noted that the actual Content-Type header that will be
        # sent to the server will contain a `boundary` parameter, e.g.
        # multipart/form-data; boundary=---abc--
        extra_headers = {"Content-Type": "multipart/form-data", **(extra_headers or {})}
        return self.post(
            "/upload",
            body=maybe_transform(body, client_create_upload_params.ClientCreateUploadParams),
            files=files,
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"extension": extension}, client_create_upload_params.ClientCreateUploadParams),
            ),
            cast_to=CreateUploadResponse,
        )

    def get_version(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
        """Get Version"""
        return self.get(
            "/version",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )

    def retrieve_job(
        self,
        job_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> RetrieveJobResponse:
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
        return self.get(
            f"/job/{job_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=RetrieveJobResponse,
        )

    @override
    def _make_status_error(
        self,
        err_msg: str,
        *,
        body: object,
        response: httpx.Response,
    ) -> APIStatusError:
        if response.status_code == 400:
            return _exceptions.BadRequestError(err_msg, response=response, body=body)

        if response.status_code == 401:
            return _exceptions.AuthenticationError(err_msg, response=response, body=body)

        if response.status_code == 403:
            return _exceptions.PermissionDeniedError(err_msg, response=response, body=body)

        if response.status_code == 404:
            return _exceptions.NotFoundError(err_msg, response=response, body=body)

        if response.status_code == 409:
            return _exceptions.ConflictError(err_msg, response=response, body=body)

        if response.status_code == 422:
            return _exceptions.UnprocessableEntityError(err_msg, response=response, body=body)

        if response.status_code == 429:
            return _exceptions.RateLimitError(err_msg, response=response, body=body)

        if response.status_code >= 500:
            return _exceptions.InternalServerError(err_msg, response=response, body=body)
        return APIStatusError(err_msg, response=response, body=body)


class AsyncReductoai(AsyncAPIClient):
    with_raw_response: AsyncReductoaiWithRawResponse
    with_streaming_response: AsyncReductoaiWithStreamedResponse

    # client options
    bearer_token: str

    def __init__(
        self,
        *,
        bearer_token: str | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
        max_retries: int = DEFAULT_MAX_RETRIES,
        default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        # Configure a custom httpx client.
        # We provide a `DefaultAsyncHttpxClient` class that you can pass to retain the default values we use for `limits`, `timeout` & `follow_redirects`.
        # See the [httpx documentation](https://www.python-httpx.org/api/#asyncclient) for more details.
        http_client: httpx.AsyncClient | None = None,
        # Enable or disable schema validation for data returned by the API.
        # When enabled an error APIResponseValidationError is raised
        # if the API responds with invalid data for the expected schema.
        #
        # This parameter may be removed or changed in the future.
        # If you rely on this feature, please open a GitHub issue
        # outlining your use-case to help us decide if it should be
        # part of our public interface in the future.
        _strict_response_validation: bool = False,
    ) -> None:
        """Construct a new async reductoai client instance.

        This automatically infers the `bearer_token` argument from the `REDUCTOAI_BEARER_TOKEN` environment variable if it is not provided.
        """
        if bearer_token is None:
            bearer_token = os.environ.get("REDUCTOAI_BEARER_TOKEN")
        if bearer_token is None:
            raise ReductoaiError(
                "The bearer_token client option must be set either by passing bearer_token to the client or by setting the REDUCTOAI_BEARER_TOKEN environment variable"
            )
        self.bearer_token = bearer_token

        if base_url is None:
            base_url = os.environ.get("REDUCTOAI_BASE_URL")
        if base_url is None:
            base_url = f"https://platform.reducto.ai"

        super().__init__(
            version=__version__,
            base_url=base_url,
            max_retries=max_retries,
            timeout=timeout,
            http_client=http_client,
            custom_headers=default_headers,
            custom_query=default_query,
            _strict_response_validation=_strict_response_validation,
        )

        self.with_raw_response = AsyncReductoaiWithRawResponse(self)
        self.with_streaming_response = AsyncReductoaiWithStreamedResponse(self)

    @property
    @override
    def qs(self) -> Querystring:
        return Querystring(array_format="comma")

    @property
    @override
    def auth_headers(self) -> dict[str, str]:
        bearer_token = self.bearer_token
        return {"Authorization": f"Bearer {bearer_token}"}

    @property
    @override
    def default_headers(self) -> dict[str, str | Omit]:
        return {
            **super().default_headers,
            "X-Stainless-Async": f"async:{get_async_library()}",
            **self._custom_headers,
        }

    def copy(
        self,
        *,
        bearer_token: str | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: float | Timeout | None | NotGiven = NOT_GIVEN,
        http_client: httpx.AsyncClient | None = None,
        max_retries: int | NotGiven = NOT_GIVEN,
        default_headers: Mapping[str, str] | None = None,
        set_default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        set_default_query: Mapping[str, object] | None = None,
        _extra_kwargs: Mapping[str, Any] = {},
    ) -> Self:
        """
        Create a new client instance re-using the same options given to the current client with optional overriding.
        """
        if default_headers is not None and set_default_headers is not None:
            raise ValueError("The `default_headers` and `set_default_headers` arguments are mutually exclusive")

        if default_query is not None and set_default_query is not None:
            raise ValueError("The `default_query` and `set_default_query` arguments are mutually exclusive")

        headers = self._custom_headers
        if default_headers is not None:
            headers = {**headers, **default_headers}
        elif set_default_headers is not None:
            headers = set_default_headers

        params = self._custom_query
        if default_query is not None:
            params = {**params, **default_query}
        elif set_default_query is not None:
            params = set_default_query

        http_client = http_client or self._client
        return self.__class__(
            bearer_token=bearer_token or self.bearer_token,
            base_url=base_url or self.base_url,
            timeout=self.timeout if isinstance(timeout, NotGiven) else timeout,
            http_client=http_client,
            max_retries=max_retries if is_given(max_retries) else self.max_retries,
            default_headers=headers,
            default_query=params,
            **_extra_kwargs,
        )

    # Alias for `copy` for nicer inline usage, e.g.
    # client.with_options(timeout=10).foo.create(...)
    with_options = copy

    async def cancel_job(
        self,
        job_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
        """
        Cancel Job

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not job_id:
            raise ValueError(f"Expected a non-empty value for `job_id` but received {job_id!r}")
        return await self.post(
            f"/cancel/{job_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )

    async def configure_webhook(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> str:
        """Webhook Portal"""
        return await self.post(
            "/configure_webhook",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=str,
        )

    async def create_extract(
        self,
        *,
        document_url: str,
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
        return await self.post(
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
                client_create_extract_params.ClientCreateExtractParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ExtractResponse,
        )

    async def create_extract_async(
        self,
        *,
        document_url: str,
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
    ) -> CreateExtractAsyncResponse:
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
        return await self.post(
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
                client_create_extract_async_params.ClientCreateExtractAsyncParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CreateExtractAsyncResponse,
        )

    async def create_parse(
        self,
        *,
        document_url: str,
        advanced_options: AdvancedProcessingOptions | NotGiven = NOT_GIVEN,
        experimental_options: ExperimentalProcessingOptions | NotGiven = NOT_GIVEN,
        options: BaseProcessingOptions | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ParseResponse:
        """Parse

        Args:
          document_url:
              The URL of the document to be processed.

        You can provide one of the following:

              1. A publicly available URL
              2. A presigned S3 URL
              3. A reducto:// prefixed URL obtained from the /upload endpoint after directly
                 uploading a document

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self.post(
            "/parse",
            body=await async_maybe_transform(
                {
                    "document_url": document_url,
                    "advanced_options": advanced_options,
                    "experimental_options": experimental_options,
                    "options": options,
                },
                client_create_parse_params.ClientCreateParseParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ParseResponse,
        )

    async def create_parse_async(
        self,
        *,
        document_url: str,
        advanced_options: AdvancedProcessingOptions | NotGiven = NOT_GIVEN,
        experimental_options: ExperimentalProcessingOptions | NotGiven = NOT_GIVEN,
        options: BaseProcessingOptions | NotGiven = NOT_GIVEN,
        priority: bool | NotGiven = NOT_GIVEN,
        webhook: WebhookConfigNew | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CreateParseAsyncResponse:
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
        return await self.post(
            "/parse_async",
            body=await async_maybe_transform(
                {
                    "document_url": document_url,
                    "advanced_options": advanced_options,
                    "experimental_options": experimental_options,
                    "options": options,
                    "priority": priority,
                    "webhook": webhook,
                },
                client_create_parse_async_params.ClientCreateParseAsyncParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CreateParseAsyncResponse,
        )

    async def create_split(
        self,
        *,
        document_url: str,
        split_description: Iterable[SplitCategory],
        advanced_options: AdvancedProcessingOptions | NotGiven = NOT_GIVEN,
        experimental_options: ExperimentalProcessingOptions | NotGiven = NOT_GIVEN,
        options: BaseProcessingOptions | NotGiven = NOT_GIVEN,
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

          split_description: The configuration options for processing the document.

          split_rules: The rules for splitting the document.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self.post(
            "/split",
            body=await async_maybe_transform(
                {
                    "document_url": document_url,
                    "split_description": split_description,
                    "advanced_options": advanced_options,
                    "experimental_options": experimental_options,
                    "options": options,
                    "split_rules": split_rules,
                },
                client_create_split_params.ClientCreateSplitParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SplitResponse,
        )

    async def create_split_async(
        self,
        *,
        document_url: str,
        split_description: Iterable[SplitCategory],
        advanced_options: AdvancedProcessingOptions | NotGiven = NOT_GIVEN,
        experimental_options: ExperimentalProcessingOptions | NotGiven = NOT_GIVEN,
        options: BaseProcessingOptions | NotGiven = NOT_GIVEN,
        priority: bool | NotGiven = NOT_GIVEN,
        split_rules: str | NotGiven = NOT_GIVEN,
        webhook: WebhookConfigNew | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CreateSplitAsyncResponse:
        """
        Split Async

        Args:
          document_url:
              The URL of the document to be processed. You can provide one of the following:

              1. A publicly available URL
              2. A presigned S3 URL
              3. A reducto:// prefixed URL obtained from the /upload endpoint after directly
                 uploading a document

          split_description: The configuration options for processing the document.

          priority: If True, attempts to process the job with priority if the user has priority
              processing budget available; by default, sync jobs are prioritized above async
              jobs.

          split_rules: The rules for splitting the document.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self.post(
            "/split_async",
            body=await async_maybe_transform(
                {
                    "document_url": document_url,
                    "split_description": split_description,
                    "advanced_options": advanced_options,
                    "experimental_options": experimental_options,
                    "options": options,
                    "priority": priority,
                    "split_rules": split_rules,
                    "webhook": webhook,
                },
                client_create_split_async_params.ClientCreateSplitAsyncParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CreateSplitAsyncResponse,
        )

    async def create_upload(
        self,
        *,
        extension: Optional[str] | NotGiven = NOT_GIVEN,
        file: FileTypes | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CreateUploadResponse:
        """
        Upload

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        body = deepcopy_minimal({"file": file})
        files = extract_files(cast(Mapping[str, object], body), paths=[["file"]])
        # It should be noted that the actual Content-Type header that will be
        # sent to the server will contain a `boundary` parameter, e.g.
        # multipart/form-data; boundary=---abc--
        extra_headers = {"Content-Type": "multipart/form-data", **(extra_headers or {})}
        return await self.post(
            "/upload",
            body=await async_maybe_transform(body, client_create_upload_params.ClientCreateUploadParams),
            files=files,
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"extension": extension}, client_create_upload_params.ClientCreateUploadParams
                ),
            ),
            cast_to=CreateUploadResponse,
        )

    async def get_version(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
        """Get Version"""
        return await self.get(
            "/version",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )

    async def retrieve_job(
        self,
        job_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> RetrieveJobResponse:
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
        return await self.get(
            f"/job/{job_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=RetrieveJobResponse,
        )

    @override
    def _make_status_error(
        self,
        err_msg: str,
        *,
        body: object,
        response: httpx.Response,
    ) -> APIStatusError:
        if response.status_code == 400:
            return _exceptions.BadRequestError(err_msg, response=response, body=body)

        if response.status_code == 401:
            return _exceptions.AuthenticationError(err_msg, response=response, body=body)

        if response.status_code == 403:
            return _exceptions.PermissionDeniedError(err_msg, response=response, body=body)

        if response.status_code == 404:
            return _exceptions.NotFoundError(err_msg, response=response, body=body)

        if response.status_code == 409:
            return _exceptions.ConflictError(err_msg, response=response, body=body)

        if response.status_code == 422:
            return _exceptions.UnprocessableEntityError(err_msg, response=response, body=body)

        if response.status_code == 429:
            return _exceptions.RateLimitError(err_msg, response=response, body=body)

        if response.status_code >= 500:
            return _exceptions.InternalServerError(err_msg, response=response, body=body)
        return APIStatusError(err_msg, response=response, body=body)


class ReductoaiWithRawResponse:
    def __init__(self, client: Reductoai) -> None:
        self.cancel_job = to_raw_response_wrapper(
            client.cancel_job,
        )
        self.configure_webhook = to_raw_response_wrapper(
            client.configure_webhook,
        )
        self.create_extract = to_raw_response_wrapper(
            client.create_extract,
        )
        self.create_extract_async = to_raw_response_wrapper(
            client.create_extract_async,
        )
        self.create_parse = to_raw_response_wrapper(
            client.create_parse,
        )
        self.create_parse_async = to_raw_response_wrapper(
            client.create_parse_async,
        )
        self.create_split = to_raw_response_wrapper(
            client.create_split,
        )
        self.create_split_async = to_raw_response_wrapper(
            client.create_split_async,
        )
        self.create_upload = to_raw_response_wrapper(
            client.create_upload,
        )
        self.get_version = to_raw_response_wrapper(
            client.get_version,
        )
        self.retrieve_job = to_raw_response_wrapper(
            client.retrieve_job,
        )


class AsyncReductoaiWithRawResponse:
    def __init__(self, client: AsyncReductoai) -> None:
        self.cancel_job = async_to_raw_response_wrapper(
            client.cancel_job,
        )
        self.configure_webhook = async_to_raw_response_wrapper(
            client.configure_webhook,
        )
        self.create_extract = async_to_raw_response_wrapper(
            client.create_extract,
        )
        self.create_extract_async = async_to_raw_response_wrapper(
            client.create_extract_async,
        )
        self.create_parse = async_to_raw_response_wrapper(
            client.create_parse,
        )
        self.create_parse_async = async_to_raw_response_wrapper(
            client.create_parse_async,
        )
        self.create_split = async_to_raw_response_wrapper(
            client.create_split,
        )
        self.create_split_async = async_to_raw_response_wrapper(
            client.create_split_async,
        )
        self.create_upload = async_to_raw_response_wrapper(
            client.create_upload,
        )
        self.get_version = async_to_raw_response_wrapper(
            client.get_version,
        )
        self.retrieve_job = async_to_raw_response_wrapper(
            client.retrieve_job,
        )


class ReductoaiWithStreamedResponse:
    def __init__(self, client: Reductoai) -> None:
        self.cancel_job = to_streamed_response_wrapper(
            client.cancel_job,
        )
        self.configure_webhook = to_streamed_response_wrapper(
            client.configure_webhook,
        )
        self.create_extract = to_streamed_response_wrapper(
            client.create_extract,
        )
        self.create_extract_async = to_streamed_response_wrapper(
            client.create_extract_async,
        )
        self.create_parse = to_streamed_response_wrapper(
            client.create_parse,
        )
        self.create_parse_async = to_streamed_response_wrapper(
            client.create_parse_async,
        )
        self.create_split = to_streamed_response_wrapper(
            client.create_split,
        )
        self.create_split_async = to_streamed_response_wrapper(
            client.create_split_async,
        )
        self.create_upload = to_streamed_response_wrapper(
            client.create_upload,
        )
        self.get_version = to_streamed_response_wrapper(
            client.get_version,
        )
        self.retrieve_job = to_streamed_response_wrapper(
            client.retrieve_job,
        )


class AsyncReductoaiWithStreamedResponse:
    def __init__(self, client: AsyncReductoai) -> None:
        self.cancel_job = async_to_streamed_response_wrapper(
            client.cancel_job,
        )
        self.configure_webhook = async_to_streamed_response_wrapper(
            client.configure_webhook,
        )
        self.create_extract = async_to_streamed_response_wrapper(
            client.create_extract,
        )
        self.create_extract_async = async_to_streamed_response_wrapper(
            client.create_extract_async,
        )
        self.create_parse = async_to_streamed_response_wrapper(
            client.create_parse,
        )
        self.create_parse_async = async_to_streamed_response_wrapper(
            client.create_parse_async,
        )
        self.create_split = async_to_streamed_response_wrapper(
            client.create_split,
        )
        self.create_split_async = async_to_streamed_response_wrapper(
            client.create_split_async,
        )
        self.create_upload = async_to_streamed_response_wrapper(
            client.create_upload,
        )
        self.get_version = async_to_streamed_response_wrapper(
            client.get_version,
        )
        self.retrieve_job = async_to_streamed_response_wrapper(
            client.retrieve_job,
        )


Client = Reductoai

AsyncClient = AsyncReductoai
