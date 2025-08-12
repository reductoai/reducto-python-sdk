# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from reducto import Reducto, AsyncReducto
from tests.utils import assert_matches_type
from reducto.types import EditRunResponse, EditRunJobResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestEdit:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_run(self, client: Reducto) -> None:
        edit = client.edit.run(
            document_url="string",
            edit_instructions="edit_instructions",
        )
        assert_matches_type(EditRunResponse, edit, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_run_with_all_params(self, client: Reducto) -> None:
        edit = client.edit.run(
            document_url="string",
            edit_instructions="edit_instructions",
            edit_options={
                "color": "#e1cb97",
                "llm_provider_preference": "openai",
            },
            form_schema=[
                {
                    "bbox": {
                        "height": 0,
                        "left": 0,
                        "page": 0,
                        "top": 0,
                        "width": 0,
                        "original_page": 0,
                    },
                    "description": "description",
                    "type": "text",
                }
            ],
            priority=True,
        )
        assert_matches_type(EditRunResponse, edit, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_run(self, client: Reducto) -> None:
        response = client.edit.with_raw_response.run(
            document_url="string",
            edit_instructions="edit_instructions",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        edit = response.parse()
        assert_matches_type(EditRunResponse, edit, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_run(self, client: Reducto) -> None:
        with client.edit.with_streaming_response.run(
            document_url="string",
            edit_instructions="edit_instructions",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            edit = response.parse()
            assert_matches_type(EditRunResponse, edit, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_run_job(self, client: Reducto) -> None:
        edit = client.edit.run_job(
            document_url="string",
            edit_instructions="edit_instructions",
        )
        assert_matches_type(EditRunJobResponse, edit, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_run_job_with_all_params(self, client: Reducto) -> None:
        edit = client.edit.run_job(
            document_url="string",
            edit_instructions="edit_instructions",
            edit_options={
                "color": "#e1cb97",
                "llm_provider_preference": "openai",
            },
            form_schema=[
                {
                    "bbox": {
                        "height": 0,
                        "left": 0,
                        "page": 0,
                        "top": 0,
                        "width": 0,
                        "original_page": 0,
                    },
                    "description": "description",
                    "type": "text",
                }
            ],
            priority=True,
            webhook={
                "channels": ["string"],
                "metadata": {},
                "mode": "disabled",
                "url": "url",
            },
        )
        assert_matches_type(EditRunJobResponse, edit, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_run_job(self, client: Reducto) -> None:
        response = client.edit.with_raw_response.run_job(
            document_url="string",
            edit_instructions="edit_instructions",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        edit = response.parse()
        assert_matches_type(EditRunJobResponse, edit, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_run_job(self, client: Reducto) -> None:
        with client.edit.with_streaming_response.run_job(
            document_url="string",
            edit_instructions="edit_instructions",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            edit = response.parse()
            assert_matches_type(EditRunJobResponse, edit, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncEdit:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_run(self, async_client: AsyncReducto) -> None:
        edit = await async_client.edit.run(
            document_url="string",
            edit_instructions="edit_instructions",
        )
        assert_matches_type(EditRunResponse, edit, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_run_with_all_params(self, async_client: AsyncReducto) -> None:
        edit = await async_client.edit.run(
            document_url="string",
            edit_instructions="edit_instructions",
            edit_options={
                "color": "#e1cb97",
                "llm_provider_preference": "openai",
            },
            form_schema=[
                {
                    "bbox": {
                        "height": 0,
                        "left": 0,
                        "page": 0,
                        "top": 0,
                        "width": 0,
                        "original_page": 0,
                    },
                    "description": "description",
                    "type": "text",
                }
            ],
            priority=True,
        )
        assert_matches_type(EditRunResponse, edit, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_run(self, async_client: AsyncReducto) -> None:
        response = await async_client.edit.with_raw_response.run(
            document_url="string",
            edit_instructions="edit_instructions",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        edit = await response.parse()
        assert_matches_type(EditRunResponse, edit, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_run(self, async_client: AsyncReducto) -> None:
        async with async_client.edit.with_streaming_response.run(
            document_url="string",
            edit_instructions="edit_instructions",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            edit = await response.parse()
            assert_matches_type(EditRunResponse, edit, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_run_job(self, async_client: AsyncReducto) -> None:
        edit = await async_client.edit.run_job(
            document_url="string",
            edit_instructions="edit_instructions",
        )
        assert_matches_type(EditRunJobResponse, edit, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_run_job_with_all_params(self, async_client: AsyncReducto) -> None:
        edit = await async_client.edit.run_job(
            document_url="string",
            edit_instructions="edit_instructions",
            edit_options={
                "color": "#e1cb97",
                "llm_provider_preference": "openai",
            },
            form_schema=[
                {
                    "bbox": {
                        "height": 0,
                        "left": 0,
                        "page": 0,
                        "top": 0,
                        "width": 0,
                        "original_page": 0,
                    },
                    "description": "description",
                    "type": "text",
                }
            ],
            priority=True,
            webhook={
                "channels": ["string"],
                "metadata": {},
                "mode": "disabled",
                "url": "url",
            },
        )
        assert_matches_type(EditRunJobResponse, edit, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_run_job(self, async_client: AsyncReducto) -> None:
        response = await async_client.edit.with_raw_response.run_job(
            document_url="string",
            edit_instructions="edit_instructions",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        edit = await response.parse()
        assert_matches_type(EditRunJobResponse, edit, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_run_job(self, async_client: AsyncReducto) -> None:
        async with async_client.edit.with_streaming_response.run_job(
            document_url="string",
            edit_instructions="edit_instructions",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            edit = await response.parse()
            assert_matches_type(EditRunJobResponse, edit, path=["response"])

        assert cast(Any, response.is_closed) is True
