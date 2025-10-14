# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from reducto import Reducto, AsyncReducto
from tests.utils import assert_matches_type
from reducto.types import ParseRunResponse, ParseRunJobResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestParse:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_run_overload_1(self, client: Reducto) -> None:
        parse = client.parse.run(
            input="string",
        )
        assert_matches_type(ParseRunResponse, parse, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_run_with_all_params_overload_1(self, client: Reducto) -> None:
        parse = client.parse.run(
            input="string",
            enhance={
                "agentic": [
                    {
                        "scope": "table",
                        "prompt": "prompt",
                    }
                ],
                "summarize_figures": True,
            },
            formatting={
                "add_page_markers": True,
                "include": ["change_tracking"],
                "merge_tables": True,
                "table_output_format": "html",
            },
            retrieval={
                "chunking": {
                    "chunk_mode": "variable",
                    "chunk_size": 0,
                },
                "embedding_optimized": True,
                "filter_blocks": ["Header"],
            },
            settings={
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
            spreadsheet={
                "clustering": "accurate",
                "exclude": ["hidden_sheets"],
                "include": ["cell_colors"],
                "split_large_tables": {
                    "enabled": True,
                    "size": 0,
                },
            },
        )
        assert_matches_type(ParseRunResponse, parse, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_run_overload_1(self, client: Reducto) -> None:
        response = client.parse.with_raw_response.run(
            input="string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        parse = response.parse()
        assert_matches_type(ParseRunResponse, parse, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_run_overload_1(self, client: Reducto) -> None:
        with client.parse.with_streaming_response.run(
            input="string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            parse = response.parse()
            assert_matches_type(ParseRunResponse, parse, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_run_overload_2(self, client: Reducto) -> None:
        parse = client.parse.run(
            input="string",
        )
        assert_matches_type(ParseRunResponse, parse, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_run_with_all_params_overload_2(self, client: Reducto) -> None:
        parse = client.parse.run(
            input="string",
            async_={
                "metadata": {},
                "priority": True,
                "webhook": {
                    "channels": ["string"],
                    "mode": "svix",
                },
            },
            enhance={
                "agentic": [
                    {
                        "scope": "table",
                        "prompt": "prompt",
                    }
                ],
                "summarize_figures": True,
            },
            formatting={
                "add_page_markers": True,
                "include": ["change_tracking"],
                "merge_tables": True,
                "table_output_format": "html",
            },
            retrieval={
                "chunking": {
                    "chunk_mode": "variable",
                    "chunk_size": 0,
                },
                "embedding_optimized": True,
                "filter_blocks": ["Header"],
            },
            settings={
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
            spreadsheet={
                "clustering": "accurate",
                "exclude": ["hidden_sheets"],
                "include": ["cell_colors"],
                "split_large_tables": {
                    "enabled": True,
                    "size": 0,
                },
            },
        )
        assert_matches_type(ParseRunResponse, parse, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_run_overload_2(self, client: Reducto) -> None:
        response = client.parse.with_raw_response.run(
            input="string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        parse = response.parse()
        assert_matches_type(ParseRunResponse, parse, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_run_overload_2(self, client: Reducto) -> None:
        with client.parse.with_streaming_response.run(
            input="string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            parse = response.parse()
            assert_matches_type(ParseRunResponse, parse, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_run_job(self, client: Reducto) -> None:
        parse = client.parse.run_job(
            input="string",
        )
        assert_matches_type(ParseRunJobResponse, parse, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_run_job_with_all_params(self, client: Reducto) -> None:
        parse = client.parse.run_job(
            input="string",
            async_={
                "metadata": {},
                "priority": True,
                "webhook": {
                    "channels": ["string"],
                    "mode": "svix",
                },
            },
            enhance={
                "agentic": [
                    {
                        "scope": "table",
                        "prompt": "prompt",
                    }
                ],
                "summarize_figures": True,
            },
            formatting={
                "add_page_markers": True,
                "include": ["change_tracking"],
                "merge_tables": True,
                "table_output_format": "html",
            },
            retrieval={
                "chunking": {
                    "chunk_mode": "variable",
                    "chunk_size": 0,
                },
                "embedding_optimized": True,
                "filter_blocks": ["Header"],
            },
            settings={
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
            spreadsheet={
                "clustering": "accurate",
                "exclude": ["hidden_sheets"],
                "include": ["cell_colors"],
                "split_large_tables": {
                    "enabled": True,
                    "size": 0,
                },
            },
        )
        assert_matches_type(ParseRunJobResponse, parse, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_run_job(self, client: Reducto) -> None:
        response = client.parse.with_raw_response.run_job(
            input="string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        parse = response.parse()
        assert_matches_type(ParseRunJobResponse, parse, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_run_job(self, client: Reducto) -> None:
        with client.parse.with_streaming_response.run_job(
            input="string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            parse = response.parse()
            assert_matches_type(ParseRunJobResponse, parse, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncParse:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_run_overload_1(self, async_client: AsyncReducto) -> None:
        parse = await async_client.parse.run(
            input="string",
        )
        assert_matches_type(ParseRunResponse, parse, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_run_with_all_params_overload_1(self, async_client: AsyncReducto) -> None:
        parse = await async_client.parse.run(
            input="string",
            enhance={
                "agentic": [
                    {
                        "scope": "table",
                        "prompt": "prompt",
                    }
                ],
                "summarize_figures": True,
            },
            formatting={
                "add_page_markers": True,
                "include": ["change_tracking"],
                "merge_tables": True,
                "table_output_format": "html",
            },
            retrieval={
                "chunking": {
                    "chunk_mode": "variable",
                    "chunk_size": 0,
                },
                "embedding_optimized": True,
                "filter_blocks": ["Header"],
            },
            settings={
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
            spreadsheet={
                "clustering": "accurate",
                "exclude": ["hidden_sheets"],
                "include": ["cell_colors"],
                "split_large_tables": {
                    "enabled": True,
                    "size": 0,
                },
            },
        )
        assert_matches_type(ParseRunResponse, parse, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_run_overload_1(self, async_client: AsyncReducto) -> None:
        response = await async_client.parse.with_raw_response.run(
            input="string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        parse = await response.parse()
        assert_matches_type(ParseRunResponse, parse, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_run_overload_1(self, async_client: AsyncReducto) -> None:
        async with async_client.parse.with_streaming_response.run(
            input="string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            parse = await response.parse()
            assert_matches_type(ParseRunResponse, parse, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_run_overload_2(self, async_client: AsyncReducto) -> None:
        parse = await async_client.parse.run(
            input="string",
        )
        assert_matches_type(ParseRunResponse, parse, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_run_with_all_params_overload_2(self, async_client: AsyncReducto) -> None:
        parse = await async_client.parse.run(
            input="string",
            async_={
                "metadata": {},
                "priority": True,
                "webhook": {
                    "channels": ["string"],
                    "mode": "svix",
                },
            },
            enhance={
                "agentic": [
                    {
                        "scope": "table",
                        "prompt": "prompt",
                    }
                ],
                "summarize_figures": True,
            },
            formatting={
                "add_page_markers": True,
                "include": ["change_tracking"],
                "merge_tables": True,
                "table_output_format": "html",
            },
            retrieval={
                "chunking": {
                    "chunk_mode": "variable",
                    "chunk_size": 0,
                },
                "embedding_optimized": True,
                "filter_blocks": ["Header"],
            },
            settings={
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
            spreadsheet={
                "clustering": "accurate",
                "exclude": ["hidden_sheets"],
                "include": ["cell_colors"],
                "split_large_tables": {
                    "enabled": True,
                    "size": 0,
                },
            },
        )
        assert_matches_type(ParseRunResponse, parse, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_run_overload_2(self, async_client: AsyncReducto) -> None:
        response = await async_client.parse.with_raw_response.run(
            input="string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        parse = await response.parse()
        assert_matches_type(ParseRunResponse, parse, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_run_overload_2(self, async_client: AsyncReducto) -> None:
        async with async_client.parse.with_streaming_response.run(
            input="string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            parse = await response.parse()
            assert_matches_type(ParseRunResponse, parse, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_run_job(self, async_client: AsyncReducto) -> None:
        parse = await async_client.parse.run_job(
            input="string",
        )
        assert_matches_type(ParseRunJobResponse, parse, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_run_job_with_all_params(self, async_client: AsyncReducto) -> None:
        parse = await async_client.parse.run_job(
            input="string",
            async_={
                "metadata": {},
                "priority": True,
                "webhook": {
                    "channels": ["string"],
                    "mode": "svix",
                },
            },
            enhance={
                "agentic": [
                    {
                        "scope": "table",
                        "prompt": "prompt",
                    }
                ],
                "summarize_figures": True,
            },
            formatting={
                "add_page_markers": True,
                "include": ["change_tracking"],
                "merge_tables": True,
                "table_output_format": "html",
            },
            retrieval={
                "chunking": {
                    "chunk_mode": "variable",
                    "chunk_size": 0,
                },
                "embedding_optimized": True,
                "filter_blocks": ["Header"],
            },
            settings={
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
            spreadsheet={
                "clustering": "accurate",
                "exclude": ["hidden_sheets"],
                "include": ["cell_colors"],
                "split_large_tables": {
                    "enabled": True,
                    "size": 0,
                },
            },
        )
        assert_matches_type(ParseRunJobResponse, parse, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_run_job(self, async_client: AsyncReducto) -> None:
        response = await async_client.parse.with_raw_response.run_job(
            input="string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        parse = await response.parse()
        assert_matches_type(ParseRunJobResponse, parse, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_run_job(self, async_client: AsyncReducto) -> None:
        async with async_client.parse.with_streaming_response.run_job(
            input="string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            parse = await response.parse()
            assert_matches_type(ParseRunJobResponse, parse, path=["response"])

        assert cast(Any, response.is_closed) is True
