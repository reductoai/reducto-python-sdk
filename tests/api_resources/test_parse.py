# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from reducto import Reducto, AsyncReducto
from tests.utils import assert_matches_type
from reducto.types import ParseRunJobResponse
from reducto.types.shared import ParseResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestParse:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_run(self, client: Reducto) -> None:
        parse = client.parse.run(
            document_url="string",
        )
        assert_matches_type(ParseResponse, parse, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_run_with_all_params(self, client: Reducto) -> None:
        parse = client.parse.run(
            document_url="string",
            advanced_options={
                "add_page_markers": True,
                "bucket_name": "bucket_name",
                "continue_hierarchy": True,
                "document_password": "document_password",
                "force_file_extension": "force_file_extension",
                "keep_line_breaks": True,
                "kms_arn": "kms_arn",
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
                "custom_format": "aml",
                "danger_filter_wide_boxes": True,
                "enable_checkboxes": True,
                "enable_equations": True,
                "enable_scripts": True,
                "enable_underlines": True,
                "enrich": {
                    "enabled": True,
                    "mode": "standard",
                    "prompt": "prompt",
                },
                "native_office_conversion": True,
                "return_figure_images": True,
                "return_table_images": True,
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
                "ocr_mode": "standard",
                "table_summary": {
                    "enabled": True,
                    "prompt": "prompt",
                },
            },
            user_id="user-id",
        )
        assert_matches_type(ParseResponse, parse, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_run(self, client: Reducto) -> None:
        response = client.parse.with_raw_response.run(
            document_url="string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        parse = response.parse()
        assert_matches_type(ParseResponse, parse, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_run(self, client: Reducto) -> None:
        with client.parse.with_streaming_response.run(
            document_url="string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            parse = response.parse()
            assert_matches_type(ParseResponse, parse, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_method_run_job(self, client: Reducto) -> None:
        parse = client.parse.run_job(
            document_url="string",
        )
        assert_matches_type(ParseRunJobResponse, parse, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_run_job_with_all_params(self, client: Reducto) -> None:
        parse = client.parse.run_job(
            document_url="string",
            advanced_options={
                "add_page_markers": True,
                "bucket_name": "bucket_name",
                "continue_hierarchy": True,
                "document_password": "document_password",
                "force_file_extension": "force_file_extension",
                "keep_line_breaks": True,
                "kms_arn": "kms_arn",
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
                "custom_format": "aml",
                "danger_filter_wide_boxes": True,
                "enable_checkboxes": True,
                "enable_equations": True,
                "enable_scripts": True,
                "enable_underlines": True,
                "enrich": {
                    "enabled": True,
                    "mode": "standard",
                    "prompt": "prompt",
                },
                "native_office_conversion": True,
                "return_figure_images": True,
                "return_table_images": True,
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
                "ocr_mode": "standard",
                "table_summary": {
                    "enabled": True,
                    "prompt": "prompt",
                },
            },
            priority=True,
            webhook={
                "channels": ["string"],
                "metadata": {},
                "mode": "disabled",
                "url": "url",
            },
            user_id="user-id",
        )
        assert_matches_type(ParseRunJobResponse, parse, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_run_job(self, client: Reducto) -> None:
        response = client.parse.with_raw_response.run_job(
            document_url="string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        parse = response.parse()
        assert_matches_type(ParseRunJobResponse, parse, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_run_job(self, client: Reducto) -> None:
        with client.parse.with_streaming_response.run_job(
            document_url="string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            parse = response.parse()
            assert_matches_type(ParseRunJobResponse, parse, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncParse:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_run(self, async_client: AsyncReducto) -> None:
        parse = await async_client.parse.run(
            document_url="string",
        )
        assert_matches_type(ParseResponse, parse, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_run_with_all_params(self, async_client: AsyncReducto) -> None:
        parse = await async_client.parse.run(
            document_url="string",
            advanced_options={
                "add_page_markers": True,
                "bucket_name": "bucket_name",
                "continue_hierarchy": True,
                "document_password": "document_password",
                "force_file_extension": "force_file_extension",
                "keep_line_breaks": True,
                "kms_arn": "kms_arn",
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
                "custom_format": "aml",
                "danger_filter_wide_boxes": True,
                "enable_checkboxes": True,
                "enable_equations": True,
                "enable_scripts": True,
                "enable_underlines": True,
                "enrich": {
                    "enabled": True,
                    "mode": "standard",
                    "prompt": "prompt",
                },
                "native_office_conversion": True,
                "return_figure_images": True,
                "return_table_images": True,
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
                "ocr_mode": "standard",
                "table_summary": {
                    "enabled": True,
                    "prompt": "prompt",
                },
            },
            user_id="user-id",
        )
        assert_matches_type(ParseResponse, parse, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_run(self, async_client: AsyncReducto) -> None:
        response = await async_client.parse.with_raw_response.run(
            document_url="string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        parse = await response.parse()
        assert_matches_type(ParseResponse, parse, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_run(self, async_client: AsyncReducto) -> None:
        async with async_client.parse.with_streaming_response.run(
            document_url="string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            parse = await response.parse()
            assert_matches_type(ParseResponse, parse, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_method_run_job(self, async_client: AsyncReducto) -> None:
        parse = await async_client.parse.run_job(
            document_url="string",
        )
        assert_matches_type(ParseRunJobResponse, parse, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_run_job_with_all_params(self, async_client: AsyncReducto) -> None:
        parse = await async_client.parse.run_job(
            document_url="string",
            advanced_options={
                "add_page_markers": True,
                "bucket_name": "bucket_name",
                "continue_hierarchy": True,
                "document_password": "document_password",
                "force_file_extension": "force_file_extension",
                "keep_line_breaks": True,
                "kms_arn": "kms_arn",
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
                "custom_format": "aml",
                "danger_filter_wide_boxes": True,
                "enable_checkboxes": True,
                "enable_equations": True,
                "enable_scripts": True,
                "enable_underlines": True,
                "enrich": {
                    "enabled": True,
                    "mode": "standard",
                    "prompt": "prompt",
                },
                "native_office_conversion": True,
                "return_figure_images": True,
                "return_table_images": True,
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
                "ocr_mode": "standard",
                "table_summary": {
                    "enabled": True,
                    "prompt": "prompt",
                },
            },
            priority=True,
            webhook={
                "channels": ["string"],
                "metadata": {},
                "mode": "disabled",
                "url": "url",
            },
            user_id="user-id",
        )
        assert_matches_type(ParseRunJobResponse, parse, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_run_job(self, async_client: AsyncReducto) -> None:
        response = await async_client.parse.with_raw_response.run_job(
            document_url="string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        parse = await response.parse()
        assert_matches_type(ParseRunJobResponse, parse, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_run_job(self, async_client: AsyncReducto) -> None:
        async with async_client.parse.with_streaming_response.run_job(
            document_url="string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            parse = await response.parse()
            assert_matches_type(ParseRunJobResponse, parse, path=["response"])

        assert cast(Any, response.is_closed) is True
