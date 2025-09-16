# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from reducto import Reducto, AsyncReducto
from tests.utils import assert_matches_type
from reducto.types import PipelineRunJobResponse
from reducto.types.shared import PipelineResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestPipeline:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_run(self, client: Reducto) -> None:
        pipeline = client.pipeline.run(
            document_url="string",
            pipeline_id="pipeline_id",
        )
        assert_matches_type(PipelineResponse, pipeline, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_run_with_all_params(self, client: Reducto) -> None:
        pipeline = client.pipeline.run(
            document_url="string",
            pipeline_id="pipeline_id",
        )
        assert_matches_type(PipelineResponse, pipeline, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_run(self, client: Reducto) -> None:
        response = client.pipeline.with_raw_response.run(
            document_url="string",
            pipeline_id="pipeline_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        pipeline = response.parse()
        assert_matches_type(PipelineResponse, pipeline, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_run(self, client: Reducto) -> None:
        with client.pipeline.with_streaming_response.run(
            document_url="string",
            pipeline_id="pipeline_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            pipeline = response.parse()
            assert_matches_type(PipelineResponse, pipeline, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_run_job(self, client: Reducto) -> None:
        pipeline = client.pipeline.run_job(
            document_url="string",
            pipeline_id="pipeline_id",
        )
        assert_matches_type(PipelineRunJobResponse, pipeline, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_run_job_with_all_params(self, client: Reducto) -> None:
        pipeline = client.pipeline.run_job(
            document_url="string",
            pipeline_id="pipeline_id",
            priority=True,
            webhook={
                "channels": ["string"],
                "metadata": {},
                "mode": "disabled",
                "url": "url",
            },
        )
        assert_matches_type(PipelineRunJobResponse, pipeline, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_run_job(self, client: Reducto) -> None:
        response = client.pipeline.with_raw_response.run_job(
            document_url="string",
            pipeline_id="pipeline_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        pipeline = response.parse()
        assert_matches_type(PipelineRunJobResponse, pipeline, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_run_job(self, client: Reducto) -> None:
        with client.pipeline.with_streaming_response.run_job(
            document_url="string",
            pipeline_id="pipeline_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            pipeline = response.parse()
            assert_matches_type(PipelineRunJobResponse, pipeline, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncPipeline:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_run(self, async_client: AsyncReducto) -> None:
        pipeline = await async_client.pipeline.run(
            document_url="string",
            pipeline_id="pipeline_id",
        )
        assert_matches_type(PipelineResponse, pipeline, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_run_with_all_params(self, async_client: AsyncReducto) -> None:
        pipeline = await async_client.pipeline.run(
            document_url="string",
            pipeline_id="pipeline_id",
        )
        assert_matches_type(PipelineResponse, pipeline, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_run(self, async_client: AsyncReducto) -> None:
        response = await async_client.pipeline.with_raw_response.run(
            document_url="string",
            pipeline_id="pipeline_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        pipeline = await response.parse()
        assert_matches_type(PipelineResponse, pipeline, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_run(self, async_client: AsyncReducto) -> None:
        async with async_client.pipeline.with_streaming_response.run(
            document_url="string",
            pipeline_id="pipeline_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            pipeline = await response.parse()
            assert_matches_type(PipelineResponse, pipeline, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_run_job(self, async_client: AsyncReducto) -> None:
        pipeline = await async_client.pipeline.run_job(
            document_url="string",
            pipeline_id="pipeline_id",
        )
        assert_matches_type(PipelineRunJobResponse, pipeline, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_run_job_with_all_params(self, async_client: AsyncReducto) -> None:
        pipeline = await async_client.pipeline.run_job(
            document_url="string",
            pipeline_id="pipeline_id",
            priority=True,
            webhook={
                "channels": ["string"],
                "metadata": {},
                "mode": "disabled",
                "url": "url",
            },
        )
        assert_matches_type(PipelineRunJobResponse, pipeline, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_run_job(self, async_client: AsyncReducto) -> None:
        response = await async_client.pipeline.with_raw_response.run_job(
            document_url="string",
            pipeline_id="pipeline_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        pipeline = await response.parse()
        assert_matches_type(PipelineRunJobResponse, pipeline, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_run_job(self, async_client: AsyncReducto) -> None:
        async with async_client.pipeline.with_streaming_response.run_job(
            document_url="string",
            pipeline_id="pipeline_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            pipeline = await response.parse()
            assert_matches_type(PipelineRunJobResponse, pipeline, path=["response"])

        assert cast(Any, response.is_closed) is True
