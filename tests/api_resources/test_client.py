# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from reducto import Reducto, AsyncReducto
from tests.utils import assert_matches_type
from reducto.types.shared import Upload

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestClient:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_api_version(self, client: Reducto) -> None:
        client_ = client.api_version()
        assert_matches_type(object, client_, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_api_version(self, client: Reducto) -> None:
        response = client.with_raw_response.api_version()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        client_ = response.parse()
        assert_matches_type(object, client_, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_api_version(self, client: Reducto) -> None:
        with client.with_streaming_response.api_version() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            client_ = response.parse()
            assert_matches_type(object, client_, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_method_upload(self, client: Reducto) -> None:
        client_ = client.upload()
        assert_matches_type(Upload, client_, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_upload_with_all_params(self, client: Reducto) -> None:
        client_ = client.upload(
            extension="extension",
            file=b"raw file contents",
        )
        assert_matches_type(Upload, client_, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_upload(self, client: Reducto) -> None:
        response = client.with_raw_response.upload()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        client_ = response.parse()
        assert_matches_type(Upload, client_, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_upload(self, client: Reducto) -> None:
        with client.with_streaming_response.upload() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            client_ = response.parse()
            assert_matches_type(Upload, client_, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncClient:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_api_version(self, async_client: AsyncReducto) -> None:
        client = await async_client.api_version()
        assert_matches_type(object, client, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_api_version(self, async_client: AsyncReducto) -> None:
        response = await async_client.with_raw_response.api_version()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        client = await response.parse()
        assert_matches_type(object, client, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_api_version(self, async_client: AsyncReducto) -> None:
        async with async_client.with_streaming_response.api_version() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            client = await response.parse()
            assert_matches_type(object, client, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_method_upload(self, async_client: AsyncReducto) -> None:
        client = await async_client.upload()
        assert_matches_type(Upload, client, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_upload_with_all_params(self, async_client: AsyncReducto) -> None:
        client = await async_client.upload(
            extension="extension",
            file=b"raw file contents",
        )
        assert_matches_type(Upload, client, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_upload(self, async_client: AsyncReducto) -> None:
        response = await async_client.with_raw_response.upload()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        client = await response.parse()
        assert_matches_type(Upload, client, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_upload(self, async_client: AsyncReducto) -> None:
        async with async_client.with_streaming_response.upload() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            client = await response.parse()
            assert_matches_type(Upload, client, path=["response"])

        assert cast(Any, response.is_closed) is True
