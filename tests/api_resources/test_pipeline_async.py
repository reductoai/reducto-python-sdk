# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from reducto import Reducto, AsyncReducto
from tests.utils import assert_matches_type
from reducto.types import PipelineAsyncCreateResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestPipelineAsync:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create(self, client: Reducto) -> None:
        pipeline_async = client.pipeline_async.create(
            input="string",
            pipeline_id="pipeline_id",
        )
        assert_matches_type(PipelineAsyncCreateResponse, pipeline_async, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create_with_all_params(self, client: Reducto) -> None:
        pipeline_async = client.pipeline_async.create(
            input="string",
            pipeline_id="pipeline_id",
            async_={
                "metadata": {},
                "priority": True,
                "webhook": {
                    "channels": ["string"],
                    "mode": "svix",
                },
            },
            settings={"document_password": "document_password"},
        )
        assert_matches_type(PipelineAsyncCreateResponse, pipeline_async, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: Reducto) -> None:
        response = client.pipeline_async.with_raw_response.create(
            input="string",
            pipeline_id="pipeline_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        pipeline_async = response.parse()
        assert_matches_type(PipelineAsyncCreateResponse, pipeline_async, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: Reducto) -> None:
        with client.pipeline_async.with_streaming_response.create(
            input="string",
            pipeline_id="pipeline_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            pipeline_async = response.parse()
            assert_matches_type(PipelineAsyncCreateResponse, pipeline_async, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncPipelineAsync:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncReducto) -> None:
        pipeline_async = await async_client.pipeline_async.create(
            input="string",
            pipeline_id="pipeline_id",
        )
        assert_matches_type(PipelineAsyncCreateResponse, pipeline_async, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncReducto) -> None:
        pipeline_async = await async_client.pipeline_async.create(
            input="string",
            pipeline_id="pipeline_id",
            async_={
                "metadata": {},
                "priority": True,
                "webhook": {
                    "channels": ["string"],
                    "mode": "svix",
                },
            },
            settings={"document_password": "document_password"},
        )
        assert_matches_type(PipelineAsyncCreateResponse, pipeline_async, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncReducto) -> None:
        response = await async_client.pipeline_async.with_raw_response.create(
            input="string",
            pipeline_id="pipeline_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        pipeline_async = await response.parse()
        assert_matches_type(PipelineAsyncCreateResponse, pipeline_async, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncReducto) -> None:
        async with async_client.pipeline_async.with_streaming_response.create(
            input="string",
            pipeline_id="pipeline_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            pipeline_async = await response.parse()
            assert_matches_type(PipelineAsyncCreateResponse, pipeline_async, path=["response"])

        assert cast(Any, response.is_closed) is True
