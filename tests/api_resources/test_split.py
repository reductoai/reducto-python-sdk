# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from reducto import Reducto, AsyncReducto
from tests.utils import assert_matches_type
from reducto.types import SplitRunJobResponse
from reducto.types.shared import SplitResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestSplit:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_run(self, client: Reducto) -> None:
        split = client.split.run(
            input="string",
            split_description=[
                {
                    "description": "description",
                    "name": "name",
                }
            ],
        )
        assert_matches_type(SplitResponse, split, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_run_with_all_params(self, client: Reducto) -> None:
        split = client.split.run(
            input="string",
            split_description=[
                {
                    "description": "description",
                    "name": "name",
                    "partition_key": "partition_key",
                }
            ],
            parsing={
                "enhance": {
                    "agentic": [
                        {
                            "scope": "table",
                            "prompt": "prompt",
                        }
                    ],
                    "summarize_figures": True,
                },
                "formatting": {
                    "add_page_markers": True,
                    "include": ["change_tracking"],
                    "merge_tables": True,
                    "table_output_format": "html",
                },
                "retrieval": {
                    "chunking": {
                        "chunk_mode": "variable",
                        "chunk_size": 0,
                    },
                    "embedding_optimized": True,
                    "filter_blocks": ["Header"],
                },
                "settings": {
                    "document_password": "document_password",
                    "embed_pdf_metadata": True,
                    "force_file_extension": "force_file_extension",
                    "force_url_result": True,
                    "ocr_system": "standard",
                    "page_range": {
                        "end": 0,
                        "start": 0,
                    },
                    "persist_results": True,
                    "return_images": ["figure"],
                    "return_ocr_data": True,
                    "timeout": 0,
                },
                "spreadsheet": {
                    "clustering": "accurate",
                    "exclude": ["hidden_sheets"],
                    "include": ["cell_colors"],
                    "split_large_tables": {
                        "enabled": True,
                        "size": 0,
                    },
                },
            },
            settings={"table_cutoff": "truncate"},
            split_rules="split_rules",
        )
        assert_matches_type(SplitResponse, split, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_run(self, client: Reducto) -> None:
        response = client.split.with_raw_response.run(
            input="string",
            split_description=[
                {
                    "description": "description",
                    "name": "name",
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        split = response.parse()
        assert_matches_type(SplitResponse, split, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_run(self, client: Reducto) -> None:
        with client.split.with_streaming_response.run(
            input="string",
            split_description=[
                {
                    "description": "description",
                    "name": "name",
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            split = response.parse()
            assert_matches_type(SplitResponse, split, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_run_job(self, client: Reducto) -> None:
        split = client.split.run_job(
            input="string",
            split_description=[
                {
                    "description": "description",
                    "name": "name",
                }
            ],
        )
        assert_matches_type(SplitRunJobResponse, split, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_run_job_with_all_params(self, client: Reducto) -> None:
        split = client.split.run_job(
            input="string",
            split_description=[
                {
                    "description": "description",
                    "name": "name",
                    "partition_key": "partition_key",
                }
            ],
            async_={
                "metadata": {},
                "priority": True,
                "webhook": {
                    "channels": ["string"],
                    "mode": "svix",
                },
            },
            parsing={
                "enhance": {
                    "agentic": [
                        {
                            "scope": "table",
                            "prompt": "prompt",
                        }
                    ],
                    "summarize_figures": True,
                },
                "formatting": {
                    "add_page_markers": True,
                    "include": ["change_tracking"],
                    "merge_tables": True,
                    "table_output_format": "html",
                },
                "retrieval": {
                    "chunking": {
                        "chunk_mode": "variable",
                        "chunk_size": 0,
                    },
                    "embedding_optimized": True,
                    "filter_blocks": ["Header"],
                },
                "settings": {
                    "document_password": "document_password",
                    "embed_pdf_metadata": True,
                    "force_file_extension": "force_file_extension",
                    "force_url_result": True,
                    "ocr_system": "standard",
                    "page_range": {
                        "end": 0,
                        "start": 0,
                    },
                    "persist_results": True,
                    "return_images": ["figure"],
                    "return_ocr_data": True,
                    "timeout": 0,
                },
                "spreadsheet": {
                    "clustering": "accurate",
                    "exclude": ["hidden_sheets"],
                    "include": ["cell_colors"],
                    "split_large_tables": {
                        "enabled": True,
                        "size": 0,
                    },
                },
            },
            settings={"table_cutoff": "truncate"},
            split_rules="split_rules",
        )
        assert_matches_type(SplitRunJobResponse, split, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_run_job(self, client: Reducto) -> None:
        response = client.split.with_raw_response.run_job(
            input="string",
            split_description=[
                {
                    "description": "description",
                    "name": "name",
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        split = response.parse()
        assert_matches_type(SplitRunJobResponse, split, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_run_job(self, client: Reducto) -> None:
        with client.split.with_streaming_response.run_job(
            input="string",
            split_description=[
                {
                    "description": "description",
                    "name": "name",
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            split = response.parse()
            assert_matches_type(SplitRunJobResponse, split, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncSplit:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_run(self, async_client: AsyncReducto) -> None:
        split = await async_client.split.run(
            input="string",
            split_description=[
                {
                    "description": "description",
                    "name": "name",
                }
            ],
        )
        assert_matches_type(SplitResponse, split, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_run_with_all_params(self, async_client: AsyncReducto) -> None:
        split = await async_client.split.run(
            input="string",
            split_description=[
                {
                    "description": "description",
                    "name": "name",
                    "partition_key": "partition_key",
                }
            ],
            parsing={
                "enhance": {
                    "agentic": [
                        {
                            "scope": "table",
                            "prompt": "prompt",
                        }
                    ],
                    "summarize_figures": True,
                },
                "formatting": {
                    "add_page_markers": True,
                    "include": ["change_tracking"],
                    "merge_tables": True,
                    "table_output_format": "html",
                },
                "retrieval": {
                    "chunking": {
                        "chunk_mode": "variable",
                        "chunk_size": 0,
                    },
                    "embedding_optimized": True,
                    "filter_blocks": ["Header"],
                },
                "settings": {
                    "document_password": "document_password",
                    "embed_pdf_metadata": True,
                    "force_file_extension": "force_file_extension",
                    "force_url_result": True,
                    "ocr_system": "standard",
                    "page_range": {
                        "end": 0,
                        "start": 0,
                    },
                    "persist_results": True,
                    "return_images": ["figure"],
                    "return_ocr_data": True,
                    "timeout": 0,
                },
                "spreadsheet": {
                    "clustering": "accurate",
                    "exclude": ["hidden_sheets"],
                    "include": ["cell_colors"],
                    "split_large_tables": {
                        "enabled": True,
                        "size": 0,
                    },
                },
            },
            settings={"table_cutoff": "truncate"},
            split_rules="split_rules",
        )
        assert_matches_type(SplitResponse, split, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_run(self, async_client: AsyncReducto) -> None:
        response = await async_client.split.with_raw_response.run(
            input="string",
            split_description=[
                {
                    "description": "description",
                    "name": "name",
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        split = await response.parse()
        assert_matches_type(SplitResponse, split, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_run(self, async_client: AsyncReducto) -> None:
        async with async_client.split.with_streaming_response.run(
            input="string",
            split_description=[
                {
                    "description": "description",
                    "name": "name",
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            split = await response.parse()
            assert_matches_type(SplitResponse, split, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_run_job(self, async_client: AsyncReducto) -> None:
        split = await async_client.split.run_job(
            input="string",
            split_description=[
                {
                    "description": "description",
                    "name": "name",
                }
            ],
        )
        assert_matches_type(SplitRunJobResponse, split, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_run_job_with_all_params(self, async_client: AsyncReducto) -> None:
        split = await async_client.split.run_job(
            input="string",
            split_description=[
                {
                    "description": "description",
                    "name": "name",
                    "partition_key": "partition_key",
                }
            ],
            async_={
                "metadata": {},
                "priority": True,
                "webhook": {
                    "channels": ["string"],
                    "mode": "svix",
                },
            },
            parsing={
                "enhance": {
                    "agentic": [
                        {
                            "scope": "table",
                            "prompt": "prompt",
                        }
                    ],
                    "summarize_figures": True,
                },
                "formatting": {
                    "add_page_markers": True,
                    "include": ["change_tracking"],
                    "merge_tables": True,
                    "table_output_format": "html",
                },
                "retrieval": {
                    "chunking": {
                        "chunk_mode": "variable",
                        "chunk_size": 0,
                    },
                    "embedding_optimized": True,
                    "filter_blocks": ["Header"],
                },
                "settings": {
                    "document_password": "document_password",
                    "embed_pdf_metadata": True,
                    "force_file_extension": "force_file_extension",
                    "force_url_result": True,
                    "ocr_system": "standard",
                    "page_range": {
                        "end": 0,
                        "start": 0,
                    },
                    "persist_results": True,
                    "return_images": ["figure"],
                    "return_ocr_data": True,
                    "timeout": 0,
                },
                "spreadsheet": {
                    "clustering": "accurate",
                    "exclude": ["hidden_sheets"],
                    "include": ["cell_colors"],
                    "split_large_tables": {
                        "enabled": True,
                        "size": 0,
                    },
                },
            },
            settings={"table_cutoff": "truncate"},
            split_rules="split_rules",
        )
        assert_matches_type(SplitRunJobResponse, split, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_run_job(self, async_client: AsyncReducto) -> None:
        response = await async_client.split.with_raw_response.run_job(
            input="string",
            split_description=[
                {
                    "description": "description",
                    "name": "name",
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        split = await response.parse()
        assert_matches_type(SplitRunJobResponse, split, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_run_job(self, async_client: AsyncReducto) -> None:
        async with async_client.split.with_streaming_response.run_job(
            input="string",
            split_description=[
                {
                    "description": "description",
                    "name": "name",
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            split = await response.parse()
            assert_matches_type(SplitRunJobResponse, split, path=["response"])

        assert cast(Any, response.is_closed) is True
