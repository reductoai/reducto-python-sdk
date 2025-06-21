# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from reducto import Reducto, AsyncReducto
from tests.utils import assert_matches_type

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestWebhook:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_run(self, client: Reducto) -> None:
        webhook = client.webhook.run()
        assert_matches_type(str, webhook, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_run(self, client: Reducto) -> None:
        response = client.webhook.with_raw_response.run()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        webhook = response.parse()
        assert_matches_type(str, webhook, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_run(self, client: Reducto) -> None:
        with client.webhook.with_streaming_response.run() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            webhook = response.parse()
            assert_matches_type(str, webhook, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncWebhook:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip()
    @parametrize
    async def test_method_run(self, async_client: AsyncReducto) -> None:
        webhook = await async_client.webhook.run()
        assert_matches_type(str, webhook, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_run(self, async_client: AsyncReducto) -> None:
        response = await async_client.webhook.with_raw_response.run()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        webhook = await response.parse()
        assert_matches_type(str, webhook, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_run(self, async_client: AsyncReducto) -> None:
        async with async_client.webhook.with_streaming_response.run() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            webhook = await response.parse()
            assert_matches_type(str, webhook, path=["response"])

        assert cast(Any, response.is_closed) is True
