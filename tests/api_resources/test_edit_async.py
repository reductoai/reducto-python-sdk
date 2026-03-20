# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from reducto import Reducto, AsyncReducto
from tests.utils import assert_matches_type
from reducto.types import EditAsyncCreateResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestEditAsync:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create(self, client: Reducto) -> None:
        edit_async = client.edit_async.create(
            document_url="string",
            edit_instructions="edit_instructions",
        )
        assert_matches_type(EditAsyncCreateResponse, edit_async, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create_with_all_params(self, client: Reducto) -> None:
        edit_async = client.edit_async.create(
            document_url="string",
            edit_instructions="edit_instructions",
            edit_options={
                "color": "#e1cb97",
                "enable_overflow_pages": True,
                "flatten": True,
                "font_size": 1,
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
                    "fill": True,
                    "font_size": 1,
                    "value": "value",
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
        assert_matches_type(EditAsyncCreateResponse, edit_async, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: Reducto) -> None:
        response = client.edit_async.with_raw_response.create(
            document_url="string",
            edit_instructions="edit_instructions",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        edit_async = response.parse()
        assert_matches_type(EditAsyncCreateResponse, edit_async, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: Reducto) -> None:
        with client.edit_async.with_streaming_response.create(
            document_url="string",
            edit_instructions="edit_instructions",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            edit_async = response.parse()
            assert_matches_type(EditAsyncCreateResponse, edit_async, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncEditAsync:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncReducto) -> None:
        edit_async = await async_client.edit_async.create(
            document_url="string",
            edit_instructions="edit_instructions",
        )
        assert_matches_type(EditAsyncCreateResponse, edit_async, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncReducto) -> None:
        edit_async = await async_client.edit_async.create(
            document_url="string",
            edit_instructions="edit_instructions",
            edit_options={
                "color": "#e1cb97",
                "enable_overflow_pages": True,
                "flatten": True,
                "font_size": 1,
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
                    "fill": True,
                    "font_size": 1,
                    "value": "value",
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
        assert_matches_type(EditAsyncCreateResponse, edit_async, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncReducto) -> None:
        response = await async_client.edit_async.with_raw_response.create(
            document_url="string",
            edit_instructions="edit_instructions",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        edit_async = await response.parse()
        assert_matches_type(EditAsyncCreateResponse, edit_async, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncReducto) -> None:
        async with async_client.edit_async.with_streaming_response.create(
            document_url="string",
            edit_instructions="edit_instructions",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            edit_async = await response.parse()
            assert_matches_type(EditAsyncCreateResponse, edit_async, path=["response"])

        assert cast(Any, response.is_closed) is True
