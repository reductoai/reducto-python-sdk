# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import TYPE_CHECKING, Any, Dict, Mapping, cast
from typing_extensions import Self, Literal, override

import httpx

from . import _exceptions
from ._qs import Querystring
from ._types import (
    Omit,
    Timeout,
    NotGiven,
    Transport,
    ProxiesTypes,
    RequestOptions,
    not_given,
)
from ._utils import is_given, get_async_library
from ._compat import cached_property
from ._models import SecurityOptions
from ._version import __version__
from ._streaming import Stream as Stream, AsyncStream as AsyncStream
from ._exceptions import ReductoError, APIStatusError
from ._base_client import (
    DEFAULT_MAX_RETRIES,
    SyncAPIClient,
    AsyncAPIClient,
)

if TYPE_CHECKING:
    from .resources import (
        job,
        edit,
        parse,
        split,
        cancel,
        upload,
        extract,
        version,
        classify,
        pipeline,
        edit_async,
        parse_async,
        split_async,
        extract_async,
        pipeline_async,
        configure_webhook,
    )
    from .resources.job import JobResource, AsyncJobResource
    from .resources.edit import EditResource, AsyncEditResource
    from .resources.parse import ParseResource, AsyncParseResource
    from .resources.split import SplitResource, AsyncSplitResource
    from .resources.cancel import CancelResource, AsyncCancelResource
    from .resources.upload import UploadResource, AsyncUploadResource
    from .resources.extract import ExtractResource, AsyncExtractResource
    from .resources.version import VersionResource, AsyncVersionResource
    from .resources.classify import ClassifyResource, AsyncClassifyResource
    from .resources.pipeline import PipelineResource, AsyncPipelineResource
    from .resources.edit_async import EditAsyncResource, AsyncEditAsyncResource
    from .resources.parse_async import ParseAsyncResource, AsyncParseAsyncResource
    from .resources.split_async import SplitAsyncResource, AsyncSplitAsyncResource
    from .resources.extract_async import ExtractAsyncResource, AsyncExtractAsyncResource
    from .resources.pipeline_async import PipelineAsyncResource, AsyncPipelineAsyncResource
    from .resources.configure_webhook import ConfigureWebhookResource, AsyncConfigureWebhookResource

__all__ = [
    "ENVIRONMENTS",
    "Timeout",
    "Transport",
    "ProxiesTypes",
    "RequestOptions",
    "Reducto",
    "AsyncReducto",
    "Client",
    "AsyncClient",
]

ENVIRONMENTS: Dict[str, str] = {
    "production": "https://platform.reducto.ai",
    "eu": "https://eu.platform.reducto.ai",
    "au": "https://au.platform.reducto.ai",
}


class Reducto(SyncAPIClient):
    # client options
    api_key: str

    _environment: Literal["production", "eu", "au"] | NotGiven

    def __init__(
        self,
        *,
        api_key: str | None = None,
        environment: Literal["production", "eu", "au"] | NotGiven = not_given,
        base_url: str | httpx.URL | None | NotGiven = not_given,
        timeout: float | Timeout | None | NotGiven = not_given,
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
        """Construct a new synchronous Reducto client instance.

        This automatically infers the `api_key` argument from the `REDUCTO_API_KEY` environment variable if it is not provided.
        """
        if api_key is None:
            api_key = os.environ.get("REDUCTO_API_KEY")
        if api_key is None:
            raise ReductoError(
                "The api_key client option must be set either by passing api_key to the client or by setting the REDUCTO_API_KEY environment variable"
            )
        self.api_key = api_key

        self._environment = environment

        base_url_env = os.environ.get("REDUCTO_BASE_URL")
        if is_given(base_url) and base_url is not None:
            # cast required because mypy doesn't understand the type narrowing
            base_url = cast("str | httpx.URL", base_url)  # pyright: ignore[reportUnnecessaryCast]
        elif is_given(environment):
            if base_url_env and base_url is not None:
                raise ValueError(
                    "Ambiguous URL; The `REDUCTO_BASE_URL` env var and the `environment` argument are given. If you want to use the environment, you must pass base_url=None",
                )

            try:
                base_url = ENVIRONMENTS[environment]
            except KeyError as exc:
                raise ValueError(f"Unknown environment: {environment}") from exc
        elif base_url_env is not None:
            base_url = base_url_env
        else:
            self._environment = environment = "production"

            try:
                base_url = ENVIRONMENTS[environment]
            except KeyError as exc:
                raise ValueError(f"Unknown environment: {environment}") from exc

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

    @cached_property
    def parse(self) -> ParseResource:
        from .resources.parse import ParseResource

        return ParseResource(self)

    @cached_property
    def parse_async(self) -> ParseAsyncResource:
        from .resources.parse_async import ParseAsyncResource

        return ParseAsyncResource(self)

    @cached_property
    def extract(self) -> ExtractResource:
        from .resources.extract import ExtractResource

        return ExtractResource(self)

    @cached_property
    def extract_async(self) -> ExtractAsyncResource:
        from .resources.extract_async import ExtractAsyncResource

        return ExtractAsyncResource(self)

    @cached_property
    def split(self) -> SplitResource:
        from .resources.split import SplitResource

        return SplitResource(self)

    @cached_property
    def split_async(self) -> SplitAsyncResource:
        from .resources.split_async import SplitAsyncResource

        return SplitAsyncResource(self)

    @cached_property
    def edit(self) -> EditResource:
        from .resources.edit import EditResource

        return EditResource(self)

    @cached_property
    def edit_async(self) -> EditAsyncResource:
        from .resources.edit_async import EditAsyncResource

        return EditAsyncResource(self)

    @cached_property
    def pipeline(self) -> PipelineResource:
        from .resources.pipeline import PipelineResource

        return PipelineResource(self)

    @cached_property
    def pipeline_async(self) -> PipelineAsyncResource:
        from .resources.pipeline_async import PipelineAsyncResource

        return PipelineAsyncResource(self)

    @cached_property
    def classify(self) -> ClassifyResource:
        from .resources.classify import ClassifyResource

        return ClassifyResource(self)

    @cached_property
    def cancel(self) -> CancelResource:
        from .resources.cancel import CancelResource

        return CancelResource(self)

    @cached_property
    def upload(self) -> UploadResource:
        from .resources.upload import UploadResource

        return UploadResource(self)

    @cached_property
    def configure_webhook(self) -> ConfigureWebhookResource:
        from .resources.configure_webhook import ConfigureWebhookResource

        return ConfigureWebhookResource(self)

    @cached_property
    def version(self) -> VersionResource:
        from .resources.version import VersionResource

        return VersionResource(self)

    @cached_property
    def job(self) -> JobResource:
        from .resources.job import JobResource

        return JobResource(self)

    @cached_property
    def with_raw_response(self) -> ReductoWithRawResponse:
        return ReductoWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ReductoWithStreamedResponse:
        return ReductoWithStreamedResponse(self)

    @property
    @override
    def qs(self) -> Querystring:
        return Querystring(array_format="comma")

    @override
    def _auth_headers(self, security: SecurityOptions) -> dict[str, str]:
        return {
            **(self._skippable_http_bearer if security.get("skippable_http_bearer", False) else {}),
        }

    @property
    def _skippable_http_bearer(self) -> dict[str, str]:
        api_key = self.api_key
        return {"Authorization": f"Bearer {api_key}"}

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
        api_key: str | None = None,
        environment: Literal["production", "eu", "au"] | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: float | Timeout | None | NotGiven = not_given,
        http_client: httpx.Client | None = None,
        max_retries: int | NotGiven = not_given,
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
            api_key=api_key or self.api_key,
            base_url=base_url or self.base_url,
            environment=environment or self._environment,
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


class AsyncReducto(AsyncAPIClient):
    # client options
    api_key: str

    _environment: Literal["production", "eu", "au"] | NotGiven

    def __init__(
        self,
        *,
        api_key: str | None = None,
        environment: Literal["production", "eu", "au"] | NotGiven = not_given,
        base_url: str | httpx.URL | None | NotGiven = not_given,
        timeout: float | Timeout | None | NotGiven = not_given,
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
        """Construct a new async AsyncReducto client instance.

        This automatically infers the `api_key` argument from the `REDUCTO_API_KEY` environment variable if it is not provided.
        """
        if api_key is None:
            api_key = os.environ.get("REDUCTO_API_KEY")
        if api_key is None:
            raise ReductoError(
                "The api_key client option must be set either by passing api_key to the client or by setting the REDUCTO_API_KEY environment variable"
            )
        self.api_key = api_key

        self._environment = environment

        base_url_env = os.environ.get("REDUCTO_BASE_URL")
        if is_given(base_url) and base_url is not None:
            # cast required because mypy doesn't understand the type narrowing
            base_url = cast("str | httpx.URL", base_url)  # pyright: ignore[reportUnnecessaryCast]
        elif is_given(environment):
            if base_url_env and base_url is not None:
                raise ValueError(
                    "Ambiguous URL; The `REDUCTO_BASE_URL` env var and the `environment` argument are given. If you want to use the environment, you must pass base_url=None",
                )

            try:
                base_url = ENVIRONMENTS[environment]
            except KeyError as exc:
                raise ValueError(f"Unknown environment: {environment}") from exc
        elif base_url_env is not None:
            base_url = base_url_env
        else:
            self._environment = environment = "production"

            try:
                base_url = ENVIRONMENTS[environment]
            except KeyError as exc:
                raise ValueError(f"Unknown environment: {environment}") from exc

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

    @cached_property
    def parse(self) -> AsyncParseResource:
        from .resources.parse import AsyncParseResource

        return AsyncParseResource(self)

    @cached_property
    def parse_async(self) -> AsyncParseAsyncResource:
        from .resources.parse_async import AsyncParseAsyncResource

        return AsyncParseAsyncResource(self)

    @cached_property
    def extract(self) -> AsyncExtractResource:
        from .resources.extract import AsyncExtractResource

        return AsyncExtractResource(self)

    @cached_property
    def extract_async(self) -> AsyncExtractAsyncResource:
        from .resources.extract_async import AsyncExtractAsyncResource

        return AsyncExtractAsyncResource(self)

    @cached_property
    def split(self) -> AsyncSplitResource:
        from .resources.split import AsyncSplitResource

        return AsyncSplitResource(self)

    @cached_property
    def split_async(self) -> AsyncSplitAsyncResource:
        from .resources.split_async import AsyncSplitAsyncResource

        return AsyncSplitAsyncResource(self)

    @cached_property
    def edit(self) -> AsyncEditResource:
        from .resources.edit import AsyncEditResource

        return AsyncEditResource(self)

    @cached_property
    def edit_async(self) -> AsyncEditAsyncResource:
        from .resources.edit_async import AsyncEditAsyncResource

        return AsyncEditAsyncResource(self)

    @cached_property
    def pipeline(self) -> AsyncPipelineResource:
        from .resources.pipeline import AsyncPipelineResource

        return AsyncPipelineResource(self)

    @cached_property
    def pipeline_async(self) -> AsyncPipelineAsyncResource:
        from .resources.pipeline_async import AsyncPipelineAsyncResource

        return AsyncPipelineAsyncResource(self)

    @cached_property
    def classify(self) -> AsyncClassifyResource:
        from .resources.classify import AsyncClassifyResource

        return AsyncClassifyResource(self)

    @cached_property
    def cancel(self) -> AsyncCancelResource:
        from .resources.cancel import AsyncCancelResource

        return AsyncCancelResource(self)

    @cached_property
    def upload(self) -> AsyncUploadResource:
        from .resources.upload import AsyncUploadResource

        return AsyncUploadResource(self)

    @cached_property
    def configure_webhook(self) -> AsyncConfigureWebhookResource:
        from .resources.configure_webhook import AsyncConfigureWebhookResource

        return AsyncConfigureWebhookResource(self)

    @cached_property
    def version(self) -> AsyncVersionResource:
        from .resources.version import AsyncVersionResource

        return AsyncVersionResource(self)

    @cached_property
    def job(self) -> AsyncJobResource:
        from .resources.job import AsyncJobResource

        return AsyncJobResource(self)

    @cached_property
    def with_raw_response(self) -> AsyncReductoWithRawResponse:
        return AsyncReductoWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncReductoWithStreamedResponse:
        return AsyncReductoWithStreamedResponse(self)

    @property
    @override
    def qs(self) -> Querystring:
        return Querystring(array_format="comma")

    @override
    def _auth_headers(self, security: SecurityOptions) -> dict[str, str]:
        return {
            **(self._skippable_http_bearer if security.get("skippable_http_bearer", False) else {}),
        }

    @property
    def _skippable_http_bearer(self) -> dict[str, str]:
        api_key = self.api_key
        return {"Authorization": f"Bearer {api_key}"}

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
        api_key: str | None = None,
        environment: Literal["production", "eu", "au"] | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: float | Timeout | None | NotGiven = not_given,
        http_client: httpx.AsyncClient | None = None,
        max_retries: int | NotGiven = not_given,
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
            api_key=api_key or self.api_key,
            base_url=base_url or self.base_url,
            environment=environment or self._environment,
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


class ReductoWithRawResponse:
    _client: Reducto

    def __init__(self, client: Reducto) -> None:
        self._client = client

    @cached_property
    def parse(self) -> parse.ParseResourceWithRawResponse:
        from .resources.parse import ParseResourceWithRawResponse

        return ParseResourceWithRawResponse(self._client.parse)

    @cached_property
    def parse_async(self) -> parse_async.ParseAsyncResourceWithRawResponse:
        from .resources.parse_async import ParseAsyncResourceWithRawResponse

        return ParseAsyncResourceWithRawResponse(self._client.parse_async)

    @cached_property
    def extract(self) -> extract.ExtractResourceWithRawResponse:
        from .resources.extract import ExtractResourceWithRawResponse

        return ExtractResourceWithRawResponse(self._client.extract)

    @cached_property
    def extract_async(self) -> extract_async.ExtractAsyncResourceWithRawResponse:
        from .resources.extract_async import ExtractAsyncResourceWithRawResponse

        return ExtractAsyncResourceWithRawResponse(self._client.extract_async)

    @cached_property
    def split(self) -> split.SplitResourceWithRawResponse:
        from .resources.split import SplitResourceWithRawResponse

        return SplitResourceWithRawResponse(self._client.split)

    @cached_property
    def split_async(self) -> split_async.SplitAsyncResourceWithRawResponse:
        from .resources.split_async import SplitAsyncResourceWithRawResponse

        return SplitAsyncResourceWithRawResponse(self._client.split_async)

    @cached_property
    def edit(self) -> edit.EditResourceWithRawResponse:
        from .resources.edit import EditResourceWithRawResponse

        return EditResourceWithRawResponse(self._client.edit)

    @cached_property
    def edit_async(self) -> edit_async.EditAsyncResourceWithRawResponse:
        from .resources.edit_async import EditAsyncResourceWithRawResponse

        return EditAsyncResourceWithRawResponse(self._client.edit_async)

    @cached_property
    def pipeline(self) -> pipeline.PipelineResourceWithRawResponse:
        from .resources.pipeline import PipelineResourceWithRawResponse

        return PipelineResourceWithRawResponse(self._client.pipeline)

    @cached_property
    def pipeline_async(self) -> pipeline_async.PipelineAsyncResourceWithRawResponse:
        from .resources.pipeline_async import PipelineAsyncResourceWithRawResponse

        return PipelineAsyncResourceWithRawResponse(self._client.pipeline_async)

    @cached_property
    def classify(self) -> classify.ClassifyResourceWithRawResponse:
        from .resources.classify import ClassifyResourceWithRawResponse

        return ClassifyResourceWithRawResponse(self._client.classify)

    @cached_property
    def cancel(self) -> cancel.CancelResourceWithRawResponse:
        from .resources.cancel import CancelResourceWithRawResponse

        return CancelResourceWithRawResponse(self._client.cancel)

    @cached_property
    def upload(self) -> upload.UploadResourceWithRawResponse:
        from .resources.upload import UploadResourceWithRawResponse

        return UploadResourceWithRawResponse(self._client.upload)

    @cached_property
    def configure_webhook(self) -> configure_webhook.ConfigureWebhookResourceWithRawResponse:
        from .resources.configure_webhook import ConfigureWebhookResourceWithRawResponse

        return ConfigureWebhookResourceWithRawResponse(self._client.configure_webhook)

    @cached_property
    def version(self) -> version.VersionResourceWithRawResponse:
        from .resources.version import VersionResourceWithRawResponse

        return VersionResourceWithRawResponse(self._client.version)

    @cached_property
    def job(self) -> job.JobResourceWithRawResponse:
        from .resources.job import JobResourceWithRawResponse

        return JobResourceWithRawResponse(self._client.job)


class AsyncReductoWithRawResponse:
    _client: AsyncReducto

    def __init__(self, client: AsyncReducto) -> None:
        self._client = client

    @cached_property
    def parse(self) -> parse.AsyncParseResourceWithRawResponse:
        from .resources.parse import AsyncParseResourceWithRawResponse

        return AsyncParseResourceWithRawResponse(self._client.parse)

    @cached_property
    def parse_async(self) -> parse_async.AsyncParseAsyncResourceWithRawResponse:
        from .resources.parse_async import AsyncParseAsyncResourceWithRawResponse

        return AsyncParseAsyncResourceWithRawResponse(self._client.parse_async)

    @cached_property
    def extract(self) -> extract.AsyncExtractResourceWithRawResponse:
        from .resources.extract import AsyncExtractResourceWithRawResponse

        return AsyncExtractResourceWithRawResponse(self._client.extract)

    @cached_property
    def extract_async(self) -> extract_async.AsyncExtractAsyncResourceWithRawResponse:
        from .resources.extract_async import AsyncExtractAsyncResourceWithRawResponse

        return AsyncExtractAsyncResourceWithRawResponse(self._client.extract_async)

    @cached_property
    def split(self) -> split.AsyncSplitResourceWithRawResponse:
        from .resources.split import AsyncSplitResourceWithRawResponse

        return AsyncSplitResourceWithRawResponse(self._client.split)

    @cached_property
    def split_async(self) -> split_async.AsyncSplitAsyncResourceWithRawResponse:
        from .resources.split_async import AsyncSplitAsyncResourceWithRawResponse

        return AsyncSplitAsyncResourceWithRawResponse(self._client.split_async)

    @cached_property
    def edit(self) -> edit.AsyncEditResourceWithRawResponse:
        from .resources.edit import AsyncEditResourceWithRawResponse

        return AsyncEditResourceWithRawResponse(self._client.edit)

    @cached_property
    def edit_async(self) -> edit_async.AsyncEditAsyncResourceWithRawResponse:
        from .resources.edit_async import AsyncEditAsyncResourceWithRawResponse

        return AsyncEditAsyncResourceWithRawResponse(self._client.edit_async)

    @cached_property
    def pipeline(self) -> pipeline.AsyncPipelineResourceWithRawResponse:
        from .resources.pipeline import AsyncPipelineResourceWithRawResponse

        return AsyncPipelineResourceWithRawResponse(self._client.pipeline)

    @cached_property
    def pipeline_async(self) -> pipeline_async.AsyncPipelineAsyncResourceWithRawResponse:
        from .resources.pipeline_async import AsyncPipelineAsyncResourceWithRawResponse

        return AsyncPipelineAsyncResourceWithRawResponse(self._client.pipeline_async)

    @cached_property
    def classify(self) -> classify.AsyncClassifyResourceWithRawResponse:
        from .resources.classify import AsyncClassifyResourceWithRawResponse

        return AsyncClassifyResourceWithRawResponse(self._client.classify)

    @cached_property
    def cancel(self) -> cancel.AsyncCancelResourceWithRawResponse:
        from .resources.cancel import AsyncCancelResourceWithRawResponse

        return AsyncCancelResourceWithRawResponse(self._client.cancel)

    @cached_property
    def upload(self) -> upload.AsyncUploadResourceWithRawResponse:
        from .resources.upload import AsyncUploadResourceWithRawResponse

        return AsyncUploadResourceWithRawResponse(self._client.upload)

    @cached_property
    def configure_webhook(self) -> configure_webhook.AsyncConfigureWebhookResourceWithRawResponse:
        from .resources.configure_webhook import AsyncConfigureWebhookResourceWithRawResponse

        return AsyncConfigureWebhookResourceWithRawResponse(self._client.configure_webhook)

    @cached_property
    def version(self) -> version.AsyncVersionResourceWithRawResponse:
        from .resources.version import AsyncVersionResourceWithRawResponse

        return AsyncVersionResourceWithRawResponse(self._client.version)

    @cached_property
    def job(self) -> job.AsyncJobResourceWithRawResponse:
        from .resources.job import AsyncJobResourceWithRawResponse

        return AsyncJobResourceWithRawResponse(self._client.job)


class ReductoWithStreamedResponse:
    _client: Reducto

    def __init__(self, client: Reducto) -> None:
        self._client = client

    @cached_property
    def parse(self) -> parse.ParseResourceWithStreamingResponse:
        from .resources.parse import ParseResourceWithStreamingResponse

        return ParseResourceWithStreamingResponse(self._client.parse)

    @cached_property
    def parse_async(self) -> parse_async.ParseAsyncResourceWithStreamingResponse:
        from .resources.parse_async import ParseAsyncResourceWithStreamingResponse

        return ParseAsyncResourceWithStreamingResponse(self._client.parse_async)

    @cached_property
    def extract(self) -> extract.ExtractResourceWithStreamingResponse:
        from .resources.extract import ExtractResourceWithStreamingResponse

        return ExtractResourceWithStreamingResponse(self._client.extract)

    @cached_property
    def extract_async(self) -> extract_async.ExtractAsyncResourceWithStreamingResponse:
        from .resources.extract_async import ExtractAsyncResourceWithStreamingResponse

        return ExtractAsyncResourceWithStreamingResponse(self._client.extract_async)

    @cached_property
    def split(self) -> split.SplitResourceWithStreamingResponse:
        from .resources.split import SplitResourceWithStreamingResponse

        return SplitResourceWithStreamingResponse(self._client.split)

    @cached_property
    def split_async(self) -> split_async.SplitAsyncResourceWithStreamingResponse:
        from .resources.split_async import SplitAsyncResourceWithStreamingResponse

        return SplitAsyncResourceWithStreamingResponse(self._client.split_async)

    @cached_property
    def edit(self) -> edit.EditResourceWithStreamingResponse:
        from .resources.edit import EditResourceWithStreamingResponse

        return EditResourceWithStreamingResponse(self._client.edit)

    @cached_property
    def edit_async(self) -> edit_async.EditAsyncResourceWithStreamingResponse:
        from .resources.edit_async import EditAsyncResourceWithStreamingResponse

        return EditAsyncResourceWithStreamingResponse(self._client.edit_async)

    @cached_property
    def pipeline(self) -> pipeline.PipelineResourceWithStreamingResponse:
        from .resources.pipeline import PipelineResourceWithStreamingResponse

        return PipelineResourceWithStreamingResponse(self._client.pipeline)

    @cached_property
    def pipeline_async(self) -> pipeline_async.PipelineAsyncResourceWithStreamingResponse:
        from .resources.pipeline_async import PipelineAsyncResourceWithStreamingResponse

        return PipelineAsyncResourceWithStreamingResponse(self._client.pipeline_async)

    @cached_property
    def classify(self) -> classify.ClassifyResourceWithStreamingResponse:
        from .resources.classify import ClassifyResourceWithStreamingResponse

        return ClassifyResourceWithStreamingResponse(self._client.classify)

    @cached_property
    def cancel(self) -> cancel.CancelResourceWithStreamingResponse:
        from .resources.cancel import CancelResourceWithStreamingResponse

        return CancelResourceWithStreamingResponse(self._client.cancel)

    @cached_property
    def upload(self) -> upload.UploadResourceWithStreamingResponse:
        from .resources.upload import UploadResourceWithStreamingResponse

        return UploadResourceWithStreamingResponse(self._client.upload)

    @cached_property
    def configure_webhook(self) -> configure_webhook.ConfigureWebhookResourceWithStreamingResponse:
        from .resources.configure_webhook import ConfigureWebhookResourceWithStreamingResponse

        return ConfigureWebhookResourceWithStreamingResponse(self._client.configure_webhook)

    @cached_property
    def version(self) -> version.VersionResourceWithStreamingResponse:
        from .resources.version import VersionResourceWithStreamingResponse

        return VersionResourceWithStreamingResponse(self._client.version)

    @cached_property
    def job(self) -> job.JobResourceWithStreamingResponse:
        from .resources.job import JobResourceWithStreamingResponse

        return JobResourceWithStreamingResponse(self._client.job)


class AsyncReductoWithStreamedResponse:
    _client: AsyncReducto

    def __init__(self, client: AsyncReducto) -> None:
        self._client = client

    @cached_property
    def parse(self) -> parse.AsyncParseResourceWithStreamingResponse:
        from .resources.parse import AsyncParseResourceWithStreamingResponse

        return AsyncParseResourceWithStreamingResponse(self._client.parse)

    @cached_property
    def parse_async(self) -> parse_async.AsyncParseAsyncResourceWithStreamingResponse:
        from .resources.parse_async import AsyncParseAsyncResourceWithStreamingResponse

        return AsyncParseAsyncResourceWithStreamingResponse(self._client.parse_async)

    @cached_property
    def extract(self) -> extract.AsyncExtractResourceWithStreamingResponse:
        from .resources.extract import AsyncExtractResourceWithStreamingResponse

        return AsyncExtractResourceWithStreamingResponse(self._client.extract)

    @cached_property
    def extract_async(self) -> extract_async.AsyncExtractAsyncResourceWithStreamingResponse:
        from .resources.extract_async import AsyncExtractAsyncResourceWithStreamingResponse

        return AsyncExtractAsyncResourceWithStreamingResponse(self._client.extract_async)

    @cached_property
    def split(self) -> split.AsyncSplitResourceWithStreamingResponse:
        from .resources.split import AsyncSplitResourceWithStreamingResponse

        return AsyncSplitResourceWithStreamingResponse(self._client.split)

    @cached_property
    def split_async(self) -> split_async.AsyncSplitAsyncResourceWithStreamingResponse:
        from .resources.split_async import AsyncSplitAsyncResourceWithStreamingResponse

        return AsyncSplitAsyncResourceWithStreamingResponse(self._client.split_async)

    @cached_property
    def edit(self) -> edit.AsyncEditResourceWithStreamingResponse:
        from .resources.edit import AsyncEditResourceWithStreamingResponse

        return AsyncEditResourceWithStreamingResponse(self._client.edit)

    @cached_property
    def edit_async(self) -> edit_async.AsyncEditAsyncResourceWithStreamingResponse:
        from .resources.edit_async import AsyncEditAsyncResourceWithStreamingResponse

        return AsyncEditAsyncResourceWithStreamingResponse(self._client.edit_async)

    @cached_property
    def pipeline(self) -> pipeline.AsyncPipelineResourceWithStreamingResponse:
        from .resources.pipeline import AsyncPipelineResourceWithStreamingResponse

        return AsyncPipelineResourceWithStreamingResponse(self._client.pipeline)

    @cached_property
    def pipeline_async(self) -> pipeline_async.AsyncPipelineAsyncResourceWithStreamingResponse:
        from .resources.pipeline_async import AsyncPipelineAsyncResourceWithStreamingResponse

        return AsyncPipelineAsyncResourceWithStreamingResponse(self._client.pipeline_async)

    @cached_property
    def classify(self) -> classify.AsyncClassifyResourceWithStreamingResponse:
        from .resources.classify import AsyncClassifyResourceWithStreamingResponse

        return AsyncClassifyResourceWithStreamingResponse(self._client.classify)

    @cached_property
    def cancel(self) -> cancel.AsyncCancelResourceWithStreamingResponse:
        from .resources.cancel import AsyncCancelResourceWithStreamingResponse

        return AsyncCancelResourceWithStreamingResponse(self._client.cancel)

    @cached_property
    def upload(self) -> upload.AsyncUploadResourceWithStreamingResponse:
        from .resources.upload import AsyncUploadResourceWithStreamingResponse

        return AsyncUploadResourceWithStreamingResponse(self._client.upload)

    @cached_property
    def configure_webhook(self) -> configure_webhook.AsyncConfigureWebhookResourceWithStreamingResponse:
        from .resources.configure_webhook import AsyncConfigureWebhookResourceWithStreamingResponse

        return AsyncConfigureWebhookResourceWithStreamingResponse(self._client.configure_webhook)

    @cached_property
    def version(self) -> version.AsyncVersionResourceWithStreamingResponse:
        from .resources.version import AsyncVersionResourceWithStreamingResponse

        return AsyncVersionResourceWithStreamingResponse(self._client.version)

    @cached_property
    def job(self) -> job.AsyncJobResourceWithStreamingResponse:
        from .resources.job import AsyncJobResourceWithStreamingResponse

        return AsyncJobResourceWithStreamingResponse(self._client.job)


Client = Reducto

AsyncClient = AsyncReducto
