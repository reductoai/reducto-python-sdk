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

    @pytest.mark.skip()
    @parametrize
    def test_method_run(self, client: Reducto) -> None:
        split = client.split.run(
            document_url="string",
            split_description=[
                {
                    "description": "description",
                    "name": "name",
                }
            ],
        )
        assert_matches_type(SplitResponse, split, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_run_with_all_params(self, client: Reducto) -> None:
        split = client.split.run(
            document_url="string",
            split_description=[
                {
                    "description": "description",
                    "name": "name",
                    "partition_key": "partition_key",
                }
            ],
            advanced_options={
                "add_page_markers": True,
                "continue_hierarchy": True,
                "document_password": "document_password",
                "force_file_extension": "force_file_extension",
                "keep_line_breaks": True,
                "large_table_chunking": {
                    "enabled": True,
                    "size": 0,
                },
                "merge_tables": True,
                "ocr_system": "highres",
                "page_range": {
                    "end": 0,
                    "start": 0,
                },
                "remove_text_formatting": True,
                "return_ocr_data": True,
                "spreadsheet_table_clustering": "default",
                "table_output_format": "html",
            },
            experimental_options={
                "danger_filter_wide_boxes": True,
                "enable_checkboxes": True,
                "enable_equations": True,
                "enable_scripts": True,
                "enable_underlines": True,
                "enrich": {
                    "enabled": True,
                    "prompt": "prompt",
                },
                "native_office_conversion": True,
                "return_figure_images": True,
                "rotate_pages": True,
            },
            options={
                "chunking": {
                    "chunk_mode": "variable",
                    "chunk_size": 0,
                },
                "extraction_mode": "ocr",
                "figure_summary": {
                    "enabled": True,
                    "override": True,
                    "prompt": "prompt",
                },
                "filter_blocks": ["Header"],
                "force_url_result": True,
                "table_summary": {
                    "enabled": True,
                    "prompt": "prompt",
                },
            },
            split_rules="split_rules",
        )
        assert_matches_type(SplitResponse, split, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_run(self, client: Reducto) -> None:
        response = client.split.with_raw_response.run(
            document_url="string",
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

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_run(self, client: Reducto) -> None:
        with client.split.with_streaming_response.run(
            document_url="string",
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

    @pytest.mark.skip()
    @parametrize
    def test_method_run_job(self, client: Reducto) -> None:
        split = client.split.run_job(
            document_url="string",
            split_description=[
                {
                    "description": "description",
                    "name": "name",
                }
            ],
        )
        assert_matches_type(SplitRunJobResponse, split, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_run_job_with_all_params(self, client: Reducto) -> None:
        split = client.split.run_job(
            document_url="string",
            split_description=[
                {
                    "description": "description",
                    "name": "name",
                    "partition_key": "partition_key",
                }
            ],
            advanced_options={
                "add_page_markers": True,
                "continue_hierarchy": True,
                "document_password": "document_password",
                "force_file_extension": "force_file_extension",
                "keep_line_breaks": True,
                "large_table_chunking": {
                    "enabled": True,
                    "size": 0,
                },
                "merge_tables": True,
                "ocr_system": "highres",
                "page_range": {
                    "end": 0,
                    "start": 0,
                },
                "remove_text_formatting": True,
                "return_ocr_data": True,
                "spreadsheet_table_clustering": "default",
                "table_output_format": "html",
            },
            experimental_options={
                "danger_filter_wide_boxes": True,
                "enable_checkboxes": True,
                "enable_equations": True,
                "enable_scripts": True,
                "enable_underlines": True,
                "enrich": {
                    "enabled": True,
                    "prompt": "prompt",
                },
                "native_office_conversion": True,
                "return_figure_images": True,
                "rotate_pages": True,
            },
            options={
                "chunking": {
                    "chunk_mode": "variable",
                    "chunk_size": 0,
                },
                "extraction_mode": "ocr",
                "figure_summary": {
                    "enabled": True,
                    "override": True,
                    "prompt": "prompt",
                },
                "filter_blocks": ["Header"],
                "force_url_result": True,
                "table_summary": {
                    "enabled": True,
                    "prompt": "prompt",
                },
            },
            priority=True,
            split_rules="split_rules",
            webhook={
                "channels": ["string"],
                "metadata": {},
                "mode": "disabled",
                "url": "url",
            },
        )
        assert_matches_type(SplitRunJobResponse, split, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_run_job(self, client: Reducto) -> None:
        response = client.split.with_raw_response.run_job(
            document_url="string",
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

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_run_job(self, client: Reducto) -> None:
        with client.split.with_streaming_response.run_job(
            document_url="string",
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
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_run(self, async_client: AsyncReducto) -> None:
        split = await async_client.split.run(
            document_url="string",
            split_description=[
                {
                    "description": "description",
                    "name": "name",
                }
            ],
        )
        assert_matches_type(SplitResponse, split, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_run_with_all_params(self, async_client: AsyncReducto) -> None:
        split = await async_client.split.run(
            document_url="string",
            split_description=[
                {
                    "description": "description",
                    "name": "name",
                    "partition_key": "partition_key",
                }
            ],
            advanced_options={
                "add_page_markers": True,
                "continue_hierarchy": True,
                "document_password": "document_password",
                "force_file_extension": "force_file_extension",
                "keep_line_breaks": True,
                "large_table_chunking": {
                    "enabled": True,
                    "size": 0,
                },
                "merge_tables": True,
                "ocr_system": "highres",
                "page_range": {
                    "end": 0,
                    "start": 0,
                },
                "remove_text_formatting": True,
                "return_ocr_data": True,
                "spreadsheet_table_clustering": "default",
                "table_output_format": "html",
            },
            experimental_options={
                "danger_filter_wide_boxes": True,
                "enable_checkboxes": True,
                "enable_equations": True,
                "enable_scripts": True,
                "enable_underlines": True,
                "enrich": {
                    "enabled": True,
                    "prompt": "prompt",
                },
                "native_office_conversion": True,
                "return_figure_images": True,
                "rotate_pages": True,
            },
            options={
                "chunking": {
                    "chunk_mode": "variable",
                    "chunk_size": 0,
                },
                "extraction_mode": "ocr",
                "figure_summary": {
                    "enabled": True,
                    "override": True,
                    "prompt": "prompt",
                },
                "filter_blocks": ["Header"],
                "force_url_result": True,
                "table_summary": {
                    "enabled": True,
                    "prompt": "prompt",
                },
            },
            split_rules="split_rules",
        )
        assert_matches_type(SplitResponse, split, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_run(self, async_client: AsyncReducto) -> None:
        response = await async_client.split.with_raw_response.run(
            document_url="string",
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

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_run(self, async_client: AsyncReducto) -> None:
        async with async_client.split.with_streaming_response.run(
            document_url="string",
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

    @pytest.mark.skip()
    @parametrize
    async def test_method_run_job(self, async_client: AsyncReducto) -> None:
        split = await async_client.split.run_job(
            document_url="string",
            split_description=[
                {
                    "description": "description",
                    "name": "name",
                }
            ],
        )
        assert_matches_type(SplitRunJobResponse, split, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_run_job_with_all_params(self, async_client: AsyncReducto) -> None:
        split = await async_client.split.run_job(
            document_url="string",
            split_description=[
                {
                    "description": "description",
                    "name": "name",
                    "partition_key": "partition_key",
                }
            ],
            advanced_options={
                "add_page_markers": True,
                "continue_hierarchy": True,
                "document_password": "document_password",
                "force_file_extension": "force_file_extension",
                "keep_line_breaks": True,
                "large_table_chunking": {
                    "enabled": True,
                    "size": 0,
                },
                "merge_tables": True,
                "ocr_system": "highres",
                "page_range": {
                    "end": 0,
                    "start": 0,
                },
                "remove_text_formatting": True,
                "return_ocr_data": True,
                "spreadsheet_table_clustering": "default",
                "table_output_format": "html",
            },
            experimental_options={
                "danger_filter_wide_boxes": True,
                "enable_checkboxes": True,
                "enable_equations": True,
                "enable_scripts": True,
                "enable_underlines": True,
                "enrich": {
                    "enabled": True,
                    "prompt": "prompt",
                },
                "native_office_conversion": True,
                "return_figure_images": True,
                "rotate_pages": True,
            },
            options={
                "chunking": {
                    "chunk_mode": "variable",
                    "chunk_size": 0,
                },
                "extraction_mode": "ocr",
                "figure_summary": {
                    "enabled": True,
                    "override": True,
                    "prompt": "prompt",
                },
                "filter_blocks": ["Header"],
                "force_url_result": True,
                "table_summary": {
                    "enabled": True,
                    "prompt": "prompt",
                },
            },
            priority=True,
            split_rules="split_rules",
            webhook={
                "channels": ["string"],
                "metadata": {},
                "mode": "disabled",
                "url": "url",
            },
        )
        assert_matches_type(SplitRunJobResponse, split, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_run_job(self, async_client: AsyncReducto) -> None:
        response = await async_client.split.with_raw_response.run_job(
            document_url="string",
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

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_run_job(self, async_client: AsyncReducto) -> None:
        async with async_client.split.with_streaming_response.run_job(
            document_url="string",
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
