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
            document_url="string",
        )
        assert_matches_type(ParseRunResponse, parse, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_run_with_all_params_overload_1(self, client: Reducto) -> None:
        parse = client.parse.run(
            document_url="string",
            advanced_options={
                "add_page_markers": True,
                "continue_hierarchy": True,
                "document_password": "document_password",
                "enable_change_tracking": True,
                "enable_highlight_detection": True,
                "exclude_hidden_rows_cols": True,
                "exclude_hidden_sheets": True,
                "filter_line_numbers": True,
                "force_file_extension": "force_file_extension",
                "include_color_information": True,
                "include_formula_information": True,
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
            experimental_options={
                "danger_filter_wide_boxes": True,
                "detect_signatures": True,
                "embed_text_metadata_pdf": True,
                "enable_checkboxes": True,
                "enable_equations": True,
                "enable_scripts": True,
                "enrich": {
                    "enabled": True,
                    "mode": "standard",
                    "prompt": "prompt",
                },
                "layout_enrichment": True,
                "layout_model": "default",
                "native_office_conversion": True,
                "return_figure_images": True,
                "return_table_images": True,
                "rotate_figures": True,
                "rotate_pages": True,
                "user_specified_timeout_seconds": 0,
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
        )
        assert_matches_type(ParseRunResponse, parse, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_run_overload_1(self, client: Reducto) -> None:
        response = client.parse.with_raw_response.run(
            document_url="string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        parse = response.parse()
        assert_matches_type(ParseRunResponse, parse, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_run_overload_1(self, client: Reducto) -> None:
        with client.parse.with_streaming_response.run(
            document_url="string",
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
            document_url="string",
        )
        assert_matches_type(ParseRunResponse, parse, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_run_with_all_params_overload_2(self, client: Reducto) -> None:
        parse = client.parse.run(
            document_url="string",
            async_={
                "enabled": True,
                "priority": True,
                "webhook": {
                    "channels": ["string"],
                    "metadata": {},
                    "mode": "direct",
                    "url": "url",
                },
            },
            config={
                "add_page_markers": True,
                "beta_layout_enrichment": True,
                "bucket_name": "bucket_name",
                "chart_extract": True,
                "chunk_mode": "variable",
                "chunk_size": 0,
                "continue_hierarchy": True,
                "custom_format": "aml",
                "customer_id": "customer_id",
                "danger_filter_wide_boxes": True,
                "detect_signatures": True,
                "disable_chunking": True,
                "document_password": "document_password",
                "dpi": 0,
                "embed_text_metadata_pdf": True,
                "enable_change_tracking": True,
                "enable_comments": True,
                "enable_highlight_detection": True,
                "enable_scripts": True,
                "enhanced_docx_conversion": True,
                "enhanced_figure_summary": True,
                "enrich": True,
                "enrich_mode": "standard",
                "enrich_prompt": "enrich_prompt",
                "exclude_hidden_rows_cols": True,
                "exclude_hidden_sheets": True,
                "experimental_large_spreadsheet_table_chunking": True,
                "extra_metadata": {"foo": "bar"},
                "figure_summary": True,
                "figure_summary_override": True,
                "figure_summary_prompt": "figure_summary_prompt",
                "filter_line_numbers": True,
                "force_file_extension": "force_file_extension",
                "force_url_result": True,
                "ignore_blocks": ["Header"],
                "include_color_information": True,
                "include_formula_information": True,
                "infer_table_color": True,
                "json_bbox": True,
                "keep_line_breaks": True,
                "kms_arn": "kms_arn",
                "large_table_chunking": True,
                "large_table_chunking_size": 0,
                "layout_model": "default",
                "max_batch_size": 1,
                "merge_tables": True,
                "mode": "document",
                "num_ocr_crops": 1,
                "numerical_parse_confidence": True,
                "ocr_mode": "standard",
                "ocr_system": "gcloud",
                "overlap_threshold": 0,
                "page_end": 0,
                "page_range": {
                    "end": 0,
                    "start": 0,
                },
                "page_start": 0,
                "pdf_ocr": "hybrid",
                "persist_results": True,
                "region_preference": "us",
                "remove_text_formatting": True,
                "return_figure_images": True,
                "return_ocr_data": True,
                "return_table_images": True,
                "rotate_figures": True,
                "rotate_pages": True,
                "spreadsheet_table_clustering": "default",
                "summarize_all_figures": True,
                "table_output_format": "html",
                "table_summary": True,
                "table_summary_prompt": "table_summary_prompt",
                "timeout": 5,
                "use_checkboxes": True,
                "use_equations": True,
                "use_fast_inference": True,
                "use_gpu_ocr": True,
                "user_specified_timeout_seconds": 0,
                "version": "v1",
            },
            priority=True,
            user_config={"foo": "bar"},
        )
        assert_matches_type(ParseRunResponse, parse, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_run_overload_2(self, client: Reducto) -> None:
        response = client.parse.with_raw_response.run(
            document_url="string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        parse = response.parse()
        assert_matches_type(ParseRunResponse, parse, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_run_overload_2(self, client: Reducto) -> None:
        with client.parse.with_streaming_response.run(
            document_url="string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            parse = response.parse()
            assert_matches_type(ParseRunResponse, parse, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_run_overload_3(self, client: Reducto) -> None:
        parse = client.parse.run(
            input="string",
        )
        assert_matches_type(ParseRunResponse, parse, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_run_with_all_params_overload_3(self, client: Reducto) -> None:
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
    def test_raw_response_run_overload_3(self, client: Reducto) -> None:
        response = client.parse.with_raw_response.run(
            input="string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        parse = response.parse()
        assert_matches_type(ParseRunResponse, parse, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_run_overload_3(self, client: Reducto) -> None:
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
    def test_method_run_job_overload_1(self, client: Reducto) -> None:
        parse = client.parse.run_job(
            document_url="string",
        )
        assert_matches_type(ParseRunJobResponse, parse, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_run_job_with_all_params_overload_1(self, client: Reducto) -> None:
        parse = client.parse.run_job(
            document_url="string",
            advanced_options={
                "add_page_markers": True,
                "continue_hierarchy": True,
                "document_password": "document_password",
                "enable_change_tracking": True,
                "enable_highlight_detection": True,
                "exclude_hidden_rows_cols": True,
                "exclude_hidden_sheets": True,
                "filter_line_numbers": True,
                "force_file_extension": "force_file_extension",
                "include_color_information": True,
                "include_formula_information": True,
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
            experimental_options={
                "danger_filter_wide_boxes": True,
                "detect_signatures": True,
                "embed_text_metadata_pdf": True,
                "enable_checkboxes": True,
                "enable_equations": True,
                "enable_scripts": True,
                "enrich": {
                    "enabled": True,
                    "mode": "standard",
                    "prompt": "prompt",
                },
                "layout_enrichment": True,
                "layout_model": "default",
                "native_office_conversion": True,
                "return_figure_images": True,
                "return_table_images": True,
                "rotate_figures": True,
                "rotate_pages": True,
                "user_specified_timeout_seconds": 0,
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
        )
        assert_matches_type(ParseRunJobResponse, parse, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_run_job_overload_1(self, client: Reducto) -> None:
        response = client.parse.with_raw_response.run_job(
            document_url="string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        parse = response.parse()
        assert_matches_type(ParseRunJobResponse, parse, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_run_job_overload_1(self, client: Reducto) -> None:
        with client.parse.with_streaming_response.run_job(
            document_url="string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            parse = response.parse()
            assert_matches_type(ParseRunJobResponse, parse, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_run_job_overload_2(self, client: Reducto) -> None:
        parse = client.parse.run_job(
            input="string",
        )
        assert_matches_type(ParseRunJobResponse, parse, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_run_job_with_all_params_overload_2(self, client: Reducto) -> None:
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
    def test_raw_response_run_job_overload_2(self, client: Reducto) -> None:
        response = client.parse.with_raw_response.run_job(
            input="string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        parse = response.parse()
        assert_matches_type(ParseRunJobResponse, parse, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_run_job_overload_2(self, client: Reducto) -> None:
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
            document_url="string",
        )
        assert_matches_type(ParseRunResponse, parse, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_run_with_all_params_overload_1(self, async_client: AsyncReducto) -> None:
        parse = await async_client.parse.run(
            document_url="string",
            advanced_options={
                "add_page_markers": True,
                "continue_hierarchy": True,
                "document_password": "document_password",
                "enable_change_tracking": True,
                "enable_highlight_detection": True,
                "exclude_hidden_rows_cols": True,
                "exclude_hidden_sheets": True,
                "filter_line_numbers": True,
                "force_file_extension": "force_file_extension",
                "include_color_information": True,
                "include_formula_information": True,
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
            experimental_options={
                "danger_filter_wide_boxes": True,
                "detect_signatures": True,
                "embed_text_metadata_pdf": True,
                "enable_checkboxes": True,
                "enable_equations": True,
                "enable_scripts": True,
                "enrich": {
                    "enabled": True,
                    "mode": "standard",
                    "prompt": "prompt",
                },
                "layout_enrichment": True,
                "layout_model": "default",
                "native_office_conversion": True,
                "return_figure_images": True,
                "return_table_images": True,
                "rotate_figures": True,
                "rotate_pages": True,
                "user_specified_timeout_seconds": 0,
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
        )
        assert_matches_type(ParseRunResponse, parse, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_run_overload_1(self, async_client: AsyncReducto) -> None:
        response = await async_client.parse.with_raw_response.run(
            document_url="string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        parse = await response.parse()
        assert_matches_type(ParseRunResponse, parse, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_run_overload_1(self, async_client: AsyncReducto) -> None:
        async with async_client.parse.with_streaming_response.run(
            document_url="string",
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
            document_url="string",
        )
        assert_matches_type(ParseRunResponse, parse, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_run_with_all_params_overload_2(self, async_client: AsyncReducto) -> None:
        parse = await async_client.parse.run(
            document_url="string",
            async_={
                "enabled": True,
                "priority": True,
                "webhook": {
                    "channels": ["string"],
                    "metadata": {},
                    "mode": "direct",
                    "url": "url",
                },
            },
            config={
                "add_page_markers": True,
                "beta_layout_enrichment": True,
                "bucket_name": "bucket_name",
                "chart_extract": True,
                "chunk_mode": "variable",
                "chunk_size": 0,
                "continue_hierarchy": True,
                "custom_format": "aml",
                "customer_id": "customer_id",
                "danger_filter_wide_boxes": True,
                "detect_signatures": True,
                "disable_chunking": True,
                "document_password": "document_password",
                "dpi": 0,
                "embed_text_metadata_pdf": True,
                "enable_change_tracking": True,
                "enable_comments": True,
                "enable_highlight_detection": True,
                "enable_scripts": True,
                "enhanced_docx_conversion": True,
                "enhanced_figure_summary": True,
                "enrich": True,
                "enrich_mode": "standard",
                "enrich_prompt": "enrich_prompt",
                "exclude_hidden_rows_cols": True,
                "exclude_hidden_sheets": True,
                "experimental_large_spreadsheet_table_chunking": True,
                "extra_metadata": {"foo": "bar"},
                "figure_summary": True,
                "figure_summary_override": True,
                "figure_summary_prompt": "figure_summary_prompt",
                "filter_line_numbers": True,
                "force_file_extension": "force_file_extension",
                "force_url_result": True,
                "ignore_blocks": ["Header"],
                "include_color_information": True,
                "include_formula_information": True,
                "infer_table_color": True,
                "json_bbox": True,
                "keep_line_breaks": True,
                "kms_arn": "kms_arn",
                "large_table_chunking": True,
                "large_table_chunking_size": 0,
                "layout_model": "default",
                "max_batch_size": 1,
                "merge_tables": True,
                "mode": "document",
                "num_ocr_crops": 1,
                "numerical_parse_confidence": True,
                "ocr_mode": "standard",
                "ocr_system": "gcloud",
                "overlap_threshold": 0,
                "page_end": 0,
                "page_range": {
                    "end": 0,
                    "start": 0,
                },
                "page_start": 0,
                "pdf_ocr": "hybrid",
                "persist_results": True,
                "region_preference": "us",
                "remove_text_formatting": True,
                "return_figure_images": True,
                "return_ocr_data": True,
                "return_table_images": True,
                "rotate_figures": True,
                "rotate_pages": True,
                "spreadsheet_table_clustering": "default",
                "summarize_all_figures": True,
                "table_output_format": "html",
                "table_summary": True,
                "table_summary_prompt": "table_summary_prompt",
                "timeout": 5,
                "use_checkboxes": True,
                "use_equations": True,
                "use_fast_inference": True,
                "use_gpu_ocr": True,
                "user_specified_timeout_seconds": 0,
                "version": "v1",
            },
            priority=True,
            user_config={"foo": "bar"},
        )
        assert_matches_type(ParseRunResponse, parse, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_run_overload_2(self, async_client: AsyncReducto) -> None:
        response = await async_client.parse.with_raw_response.run(
            document_url="string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        parse = await response.parse()
        assert_matches_type(ParseRunResponse, parse, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_run_overload_2(self, async_client: AsyncReducto) -> None:
        async with async_client.parse.with_streaming_response.run(
            document_url="string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            parse = await response.parse()
            assert_matches_type(ParseRunResponse, parse, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_run_overload_3(self, async_client: AsyncReducto) -> None:
        parse = await async_client.parse.run(
            input="string",
        )
        assert_matches_type(ParseRunResponse, parse, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_run_with_all_params_overload_3(self, async_client: AsyncReducto) -> None:
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
    async def test_raw_response_run_overload_3(self, async_client: AsyncReducto) -> None:
        response = await async_client.parse.with_raw_response.run(
            input="string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        parse = await response.parse()
        assert_matches_type(ParseRunResponse, parse, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_run_overload_3(self, async_client: AsyncReducto) -> None:
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
    async def test_method_run_job_overload_1(self, async_client: AsyncReducto) -> None:
        parse = await async_client.parse.run_job(
            document_url="string",
        )
        assert_matches_type(ParseRunJobResponse, parse, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_run_job_with_all_params_overload_1(self, async_client: AsyncReducto) -> None:
        parse = await async_client.parse.run_job(
            document_url="string",
            advanced_options={
                "add_page_markers": True,
                "continue_hierarchy": True,
                "document_password": "document_password",
                "enable_change_tracking": True,
                "enable_highlight_detection": True,
                "exclude_hidden_rows_cols": True,
                "exclude_hidden_sheets": True,
                "filter_line_numbers": True,
                "force_file_extension": "force_file_extension",
                "include_color_information": True,
                "include_formula_information": True,
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
            experimental_options={
                "danger_filter_wide_boxes": True,
                "detect_signatures": True,
                "embed_text_metadata_pdf": True,
                "enable_checkboxes": True,
                "enable_equations": True,
                "enable_scripts": True,
                "enrich": {
                    "enabled": True,
                    "mode": "standard",
                    "prompt": "prompt",
                },
                "layout_enrichment": True,
                "layout_model": "default",
                "native_office_conversion": True,
                "return_figure_images": True,
                "return_table_images": True,
                "rotate_figures": True,
                "rotate_pages": True,
                "user_specified_timeout_seconds": 0,
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
        )
        assert_matches_type(ParseRunJobResponse, parse, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_run_job_overload_1(self, async_client: AsyncReducto) -> None:
        response = await async_client.parse.with_raw_response.run_job(
            document_url="string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        parse = await response.parse()
        assert_matches_type(ParseRunJobResponse, parse, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_run_job_overload_1(self, async_client: AsyncReducto) -> None:
        async with async_client.parse.with_streaming_response.run_job(
            document_url="string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            parse = await response.parse()
            assert_matches_type(ParseRunJobResponse, parse, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_run_job_overload_2(self, async_client: AsyncReducto) -> None:
        parse = await async_client.parse.run_job(
            input="string",
        )
        assert_matches_type(ParseRunJobResponse, parse, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_run_job_with_all_params_overload_2(self, async_client: AsyncReducto) -> None:
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
    async def test_raw_response_run_job_overload_2(self, async_client: AsyncReducto) -> None:
        response = await async_client.parse.with_raw_response.run_job(
            input="string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        parse = await response.parse()
        assert_matches_type(ParseRunJobResponse, parse, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_run_job_overload_2(self, async_client: AsyncReducto) -> None:
        async with async_client.parse.with_streaming_response.run_job(
            input="string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            parse = await response.parse()
            assert_matches_type(ParseRunJobResponse, parse, path=["response"])

        assert cast(Any, response.is_closed) is True
