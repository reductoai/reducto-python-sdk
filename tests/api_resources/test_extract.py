# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from reducto import Reducto, AsyncReducto
from tests.utils import assert_matches_type
from reducto.types import ExtractRunJobResponse
from reducto.types.shared import ExtractResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestExtract:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_run(self, client: Reducto) -> None:
        extract = client.extract.run(
            document_url="string",
            schema={},
        )
        assert_matches_type(ExtractResponse, extract, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_run_with_all_params(self, client: Reducto) -> None:
        extract = client.extract.run(
            document_url="string",
            schema={},
            advanced_options={
                "add_page_markers": True,
                "continue_hierarchy": True,
                "document_password": "document_password",
                "enable_change_tracking": True,
                "exclude_hidden_rows_cols": True,
                "exclude_hidden_sheets": True,
                "filter_line_numbers": True,
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
                "persist_results": True,
                "read_comments": True,
                "remove_text_formatting": True,
                "return_ocr_data": True,
                "spreadsheet_table_clustering": "default",
                "table_output_format": "html",
            },
            array_extract={
                "enabled": True,
                "mode": "auto",
                "pages_per_segment": 0,
                "streaming_extract_item_density": 0,
            },
            experimental_options={
                "danger_filter_wide_boxes": True,
                "embed_text_metadata_pdf": True,
                "enable_checkboxes": True,
                "enable_equations": True,
                "enable_scripts": True,
                "enrich": {
                    "enabled": True,
                    "mode": "standard",
                    "prompt": "prompt",
                },
                "layout_model": "default",
                "native_office_conversion": True,
                "return_figure_images": True,
                "return_table_images": True,
                "rotate_figures": True,
                "rotate_pages": True,
            },
            generate_citations=True,
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
                "ocr_mode": "standard",
                "table_summary": {
                    "enabled": True,
                    "prompt": "prompt",
                },
            },
            priority=True,
            system_prompt="system_prompt",
            use_chunking=True,
        )
        assert_matches_type(ExtractResponse, extract, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_run(self, client: Reducto) -> None:
        response = client.extract.with_raw_response.run(
            document_url="string",
            schema={},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        extract = response.parse()
        assert_matches_type(ExtractResponse, extract, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_run(self, client: Reducto) -> None:
        with client.extract.with_streaming_response.run(
            document_url="string",
            schema={},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            extract = response.parse()
            assert_matches_type(ExtractResponse, extract, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_method_run_job(self, client: Reducto) -> None:
        extract = client.extract.run_job(
            document_url="string",
            schema={},
        )
        assert_matches_type(ExtractRunJobResponse, extract, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_run_job_with_all_params(self, client: Reducto) -> None:
        extract = client.extract.run_job(
            document_url="string",
            schema={},
            advanced_options={
                "add_page_markers": True,
                "continue_hierarchy": True,
                "document_password": "document_password",
                "enable_change_tracking": True,
                "exclude_hidden_rows_cols": True,
                "exclude_hidden_sheets": True,
                "filter_line_numbers": True,
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
                "persist_results": True,
                "read_comments": True,
                "remove_text_formatting": True,
                "return_ocr_data": True,
                "spreadsheet_table_clustering": "default",
                "table_output_format": "html",
            },
            array_extract={
                "enabled": True,
                "mode": "auto",
                "pages_per_segment": 0,
                "streaming_extract_item_density": 0,
            },
            experimental_options={
                "danger_filter_wide_boxes": True,
                "embed_text_metadata_pdf": True,
                "enable_checkboxes": True,
                "enable_equations": True,
                "enable_scripts": True,
                "enrich": {
                    "enabled": True,
                    "mode": "standard",
                    "prompt": "prompt",
                },
                "layout_model": "default",
                "native_office_conversion": True,
                "return_figure_images": True,
                "return_table_images": True,
                "rotate_figures": True,
                "rotate_pages": True,
            },
            generate_citations=True,
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
                "ocr_mode": "standard",
                "table_summary": {
                    "enabled": True,
                    "prompt": "prompt",
                },
            },
            priority=True,
            system_prompt="system_prompt",
            use_chunking=True,
            webhook={
                "channels": ["string"],
                "metadata": {},
                "mode": "disabled",
                "url": "url",
            },
        )
        assert_matches_type(ExtractRunJobResponse, extract, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_run_job(self, client: Reducto) -> None:
        response = client.extract.with_raw_response.run_job(
            document_url="string",
            schema={},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        extract = response.parse()
        assert_matches_type(ExtractRunJobResponse, extract, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_run_job(self, client: Reducto) -> None:
        with client.extract.with_streaming_response.run_job(
            document_url="string",
            schema={},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            extract = response.parse()
            assert_matches_type(ExtractRunJobResponse, extract, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncExtract:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip()
    @parametrize
    async def test_method_run(self, async_client: AsyncReducto) -> None:
        extract = await async_client.extract.run(
            document_url="string",
            schema={},
        )
        assert_matches_type(ExtractResponse, extract, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_run_with_all_params(self, async_client: AsyncReducto) -> None:
        extract = await async_client.extract.run(
            document_url="string",
            schema={},
            advanced_options={
                "add_page_markers": True,
                "continue_hierarchy": True,
                "document_password": "document_password",
                "enable_change_tracking": True,
                "exclude_hidden_rows_cols": True,
                "exclude_hidden_sheets": True,
                "filter_line_numbers": True,
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
                "persist_results": True,
                "read_comments": True,
                "remove_text_formatting": True,
                "return_ocr_data": True,
                "spreadsheet_table_clustering": "default",
                "table_output_format": "html",
            },
            array_extract={
                "enabled": True,
                "mode": "auto",
                "pages_per_segment": 0,
                "streaming_extract_item_density": 0,
            },
            experimental_options={
                "danger_filter_wide_boxes": True,
                "embed_text_metadata_pdf": True,
                "enable_checkboxes": True,
                "enable_equations": True,
                "enable_scripts": True,
                "enrich": {
                    "enabled": True,
                    "mode": "standard",
                    "prompt": "prompt",
                },
                "layout_model": "default",
                "native_office_conversion": True,
                "return_figure_images": True,
                "return_table_images": True,
                "rotate_figures": True,
                "rotate_pages": True,
            },
            generate_citations=True,
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
                "ocr_mode": "standard",
                "table_summary": {
                    "enabled": True,
                    "prompt": "prompt",
                },
            },
            priority=True,
            system_prompt="system_prompt",
            use_chunking=True,
        )
        assert_matches_type(ExtractResponse, extract, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_run(self, async_client: AsyncReducto) -> None:
        response = await async_client.extract.with_raw_response.run(
            document_url="string",
            schema={},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        extract = await response.parse()
        assert_matches_type(ExtractResponse, extract, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_run(self, async_client: AsyncReducto) -> None:
        async with async_client.extract.with_streaming_response.run(
            document_url="string",
            schema={},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            extract = await response.parse()
            assert_matches_type(ExtractResponse, extract, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_method_run_job(self, async_client: AsyncReducto) -> None:
        extract = await async_client.extract.run_job(
            document_url="string",
            schema={},
        )
        assert_matches_type(ExtractRunJobResponse, extract, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_run_job_with_all_params(self, async_client: AsyncReducto) -> None:
        extract = await async_client.extract.run_job(
            document_url="string",
            schema={},
            advanced_options={
                "add_page_markers": True,
                "continue_hierarchy": True,
                "document_password": "document_password",
                "enable_change_tracking": True,
                "exclude_hidden_rows_cols": True,
                "exclude_hidden_sheets": True,
                "filter_line_numbers": True,
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
                "persist_results": True,
                "read_comments": True,
                "remove_text_formatting": True,
                "return_ocr_data": True,
                "spreadsheet_table_clustering": "default",
                "table_output_format": "html",
            },
            array_extract={
                "enabled": True,
                "mode": "auto",
                "pages_per_segment": 0,
                "streaming_extract_item_density": 0,
            },
            experimental_options={
                "danger_filter_wide_boxes": True,
                "embed_text_metadata_pdf": True,
                "enable_checkboxes": True,
                "enable_equations": True,
                "enable_scripts": True,
                "enrich": {
                    "enabled": True,
                    "mode": "standard",
                    "prompt": "prompt",
                },
                "layout_model": "default",
                "native_office_conversion": True,
                "return_figure_images": True,
                "return_table_images": True,
                "rotate_figures": True,
                "rotate_pages": True,
            },
            generate_citations=True,
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
                "ocr_mode": "standard",
                "table_summary": {
                    "enabled": True,
                    "prompt": "prompt",
                },
            },
            priority=True,
            system_prompt="system_prompt",
            use_chunking=True,
            webhook={
                "channels": ["string"],
                "metadata": {},
                "mode": "disabled",
                "url": "url",
            },
        )
        assert_matches_type(ExtractRunJobResponse, extract, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_run_job(self, async_client: AsyncReducto) -> None:
        response = await async_client.extract.with_raw_response.run_job(
            document_url="string",
            schema={},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        extract = await response.parse()
        assert_matches_type(ExtractRunJobResponse, extract, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_run_job(self, async_client: AsyncReducto) -> None:
        async with async_client.extract.with_streaming_response.run_job(
            document_url="string",
            schema={},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            extract = await response.parse()
            assert_matches_type(ExtractRunJobResponse, extract, path=["response"])

        assert cast(Any, response.is_closed) is True
