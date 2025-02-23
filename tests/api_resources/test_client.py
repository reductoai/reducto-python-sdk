# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from reductoai import Reductoai, AsyncReductoai
from tests.utils import assert_matches_type
from reductoai.types import (
    RetrieveJobResponse,
    CreateUploadResponse,
    CreateParseAsyncResponse,
    CreateSplitAsyncResponse,
    CreateExtractAsyncResponse,
)
from reductoai.types.shared import ParseResponse, SplitResponse, ExtractResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestClient:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_cancel_job(self, client: Reductoai) -> None:
        client_ = client.cancel_job(
            "job_id",
        )
        assert_matches_type(object, client_, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_cancel_job(self, client: Reductoai) -> None:
        response = client.with_raw_response.cancel_job(
            "job_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        client_ = response.parse()
        assert_matches_type(object, client_, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_cancel_job(self, client: Reductoai) -> None:
        with client.with_streaming_response.cancel_job(
            "job_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            client_ = response.parse()
            assert_matches_type(object, client_, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_cancel_job(self, client: Reductoai) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `job_id` but received ''"):
            client.with_raw_response.cancel_job(
                "",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_configure_webhook(self, client: Reductoai) -> None:
        client_ = client.configure_webhook()
        assert_matches_type(str, client_, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_configure_webhook(self, client: Reductoai) -> None:
        response = client.with_raw_response.configure_webhook()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        client_ = response.parse()
        assert_matches_type(str, client_, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_configure_webhook(self, client: Reductoai) -> None:
        with client.with_streaming_response.configure_webhook() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            client_ = response.parse()
            assert_matches_type(str, client_, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_method_create_extract(self, client: Reductoai) -> None:
        client_ = client.create_extract(
            document_url="document_url",
            schema={},
        )
        assert_matches_type(ExtractResponse, client_, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_create_extract_with_all_params(self, client: Reductoai) -> None:
        client_ = client.create_extract(
            document_url="document_url",
            schema={},
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
            array_extract={
                "enabled": True,
                "mode": "auto",
                "pages_per_segment": 0,
                "streaming_extract_item_density": 0,
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
                "table_summary": {
                    "enabled": True,
                    "prompt": "prompt",
                },
            },
            system_prompt="system_prompt",
        )
        assert_matches_type(ExtractResponse, client_, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_create_extract(self, client: Reductoai) -> None:
        response = client.with_raw_response.create_extract(
            document_url="document_url",
            schema={},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        client_ = response.parse()
        assert_matches_type(ExtractResponse, client_, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_create_extract(self, client: Reductoai) -> None:
        with client.with_streaming_response.create_extract(
            document_url="document_url",
            schema={},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            client_ = response.parse()
            assert_matches_type(ExtractResponse, client_, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_method_create_extract_async(self, client: Reductoai) -> None:
        client_ = client.create_extract_async(
            document_url="document_url",
            schema={},
        )
        assert_matches_type(CreateExtractAsyncResponse, client_, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_create_extract_async_with_all_params(self, client: Reductoai) -> None:
        client_ = client.create_extract_async(
            document_url="document_url",
            schema={},
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
            array_extract={
                "enabled": True,
                "mode": "auto",
                "pages_per_segment": 0,
                "streaming_extract_item_density": 0,
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
                "table_summary": {
                    "enabled": True,
                    "prompt": "prompt",
                },
            },
            priority=True,
            system_prompt="system_prompt",
            webhook={
                "channels": ["string"],
                "metadata": {},
                "mode": "disabled",
                "url": "url",
            },
        )
        assert_matches_type(CreateExtractAsyncResponse, client_, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_create_extract_async(self, client: Reductoai) -> None:
        response = client.with_raw_response.create_extract_async(
            document_url="document_url",
            schema={},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        client_ = response.parse()
        assert_matches_type(CreateExtractAsyncResponse, client_, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_create_extract_async(self, client: Reductoai) -> None:
        with client.with_streaming_response.create_extract_async(
            document_url="document_url",
            schema={},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            client_ = response.parse()
            assert_matches_type(CreateExtractAsyncResponse, client_, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_method_create_parse(self, client: Reductoai) -> None:
        client_ = client.create_parse(
            document_url="document_url",
        )
        assert_matches_type(ParseResponse, client_, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_create_parse_with_all_params(self, client: Reductoai) -> None:
        client_ = client.create_parse(
            document_url="document_url",
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
        )
        assert_matches_type(ParseResponse, client_, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_create_parse(self, client: Reductoai) -> None:
        response = client.with_raw_response.create_parse(
            document_url="document_url",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        client_ = response.parse()
        assert_matches_type(ParseResponse, client_, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_create_parse(self, client: Reductoai) -> None:
        with client.with_streaming_response.create_parse(
            document_url="document_url",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            client_ = response.parse()
            assert_matches_type(ParseResponse, client_, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_method_create_parse_async(self, client: Reductoai) -> None:
        client_ = client.create_parse_async(
            document_url="document_url",
        )
        assert_matches_type(CreateParseAsyncResponse, client_, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_create_parse_async_with_all_params(self, client: Reductoai) -> None:
        client_ = client.create_parse_async(
            document_url="document_url",
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
            webhook={
                "channels": ["string"],
                "metadata": {},
                "mode": "disabled",
                "url": "url",
            },
        )
        assert_matches_type(CreateParseAsyncResponse, client_, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_create_parse_async(self, client: Reductoai) -> None:
        response = client.with_raw_response.create_parse_async(
            document_url="document_url",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        client_ = response.parse()
        assert_matches_type(CreateParseAsyncResponse, client_, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_create_parse_async(self, client: Reductoai) -> None:
        with client.with_streaming_response.create_parse_async(
            document_url="document_url",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            client_ = response.parse()
            assert_matches_type(CreateParseAsyncResponse, client_, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_method_create_split(self, client: Reductoai) -> None:
        client_ = client.create_split(
            document_url="document_url",
            split_description=[
                {
                    "description": "description",
                    "name": "name",
                }
            ],
        )
        assert_matches_type(SplitResponse, client_, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_create_split_with_all_params(self, client: Reductoai) -> None:
        client_ = client.create_split(
            document_url="document_url",
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
        assert_matches_type(SplitResponse, client_, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_create_split(self, client: Reductoai) -> None:
        response = client.with_raw_response.create_split(
            document_url="document_url",
            split_description=[
                {
                    "description": "description",
                    "name": "name",
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        client_ = response.parse()
        assert_matches_type(SplitResponse, client_, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_create_split(self, client: Reductoai) -> None:
        with client.with_streaming_response.create_split(
            document_url="document_url",
            split_description=[
                {
                    "description": "description",
                    "name": "name",
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            client_ = response.parse()
            assert_matches_type(SplitResponse, client_, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_method_create_split_async(self, client: Reductoai) -> None:
        client_ = client.create_split_async(
            document_url="document_url",
            split_description=[
                {
                    "description": "description",
                    "name": "name",
                }
            ],
        )
        assert_matches_type(CreateSplitAsyncResponse, client_, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_create_split_async_with_all_params(self, client: Reductoai) -> None:
        client_ = client.create_split_async(
            document_url="document_url",
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
        assert_matches_type(CreateSplitAsyncResponse, client_, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_create_split_async(self, client: Reductoai) -> None:
        response = client.with_raw_response.create_split_async(
            document_url="document_url",
            split_description=[
                {
                    "description": "description",
                    "name": "name",
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        client_ = response.parse()
        assert_matches_type(CreateSplitAsyncResponse, client_, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_create_split_async(self, client: Reductoai) -> None:
        with client.with_streaming_response.create_split_async(
            document_url="document_url",
            split_description=[
                {
                    "description": "description",
                    "name": "name",
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            client_ = response.parse()
            assert_matches_type(CreateSplitAsyncResponse, client_, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_method_create_upload(self, client: Reductoai) -> None:
        client_ = client.create_upload()
        assert_matches_type(CreateUploadResponse, client_, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_create_upload_with_all_params(self, client: Reductoai) -> None:
        client_ = client.create_upload(
            extension="extension",
            file=b"raw file contents",
        )
        assert_matches_type(CreateUploadResponse, client_, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_create_upload(self, client: Reductoai) -> None:
        response = client.with_raw_response.create_upload()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        client_ = response.parse()
        assert_matches_type(CreateUploadResponse, client_, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_create_upload(self, client: Reductoai) -> None:
        with client.with_streaming_response.create_upload() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            client_ = response.parse()
            assert_matches_type(CreateUploadResponse, client_, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_method_get_version(self, client: Reductoai) -> None:
        client_ = client.get_version()
        assert_matches_type(object, client_, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_get_version(self, client: Reductoai) -> None:
        response = client.with_raw_response.get_version()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        client_ = response.parse()
        assert_matches_type(object, client_, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_get_version(self, client: Reductoai) -> None:
        with client.with_streaming_response.get_version() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            client_ = response.parse()
            assert_matches_type(object, client_, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_method_retrieve_job(self, client: Reductoai) -> None:
        client_ = client.retrieve_job(
            "job_id",
        )
        assert_matches_type(RetrieveJobResponse, client_, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_retrieve_job(self, client: Reductoai) -> None:
        response = client.with_raw_response.retrieve_job(
            "job_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        client_ = response.parse()
        assert_matches_type(RetrieveJobResponse, client_, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_retrieve_job(self, client: Reductoai) -> None:
        with client.with_streaming_response.retrieve_job(
            "job_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            client_ = response.parse()
            assert_matches_type(RetrieveJobResponse, client_, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_retrieve_job(self, client: Reductoai) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `job_id` but received ''"):
            client.with_raw_response.retrieve_job(
                "",
            )


class TestAsyncClient:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_cancel_job(self, async_client: AsyncReductoai) -> None:
        client = await async_client.cancel_job(
            "job_id",
        )
        assert_matches_type(object, client, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_cancel_job(self, async_client: AsyncReductoai) -> None:
        response = await async_client.with_raw_response.cancel_job(
            "job_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        client = await response.parse()
        assert_matches_type(object, client, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_cancel_job(self, async_client: AsyncReductoai) -> None:
        async with async_client.with_streaming_response.cancel_job(
            "job_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            client = await response.parse()
            assert_matches_type(object, client, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_cancel_job(self, async_client: AsyncReductoai) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `job_id` but received ''"):
            await async_client.with_raw_response.cancel_job(
                "",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_configure_webhook(self, async_client: AsyncReductoai) -> None:
        client = await async_client.configure_webhook()
        assert_matches_type(str, client, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_configure_webhook(self, async_client: AsyncReductoai) -> None:
        response = await async_client.with_raw_response.configure_webhook()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        client = await response.parse()
        assert_matches_type(str, client, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_configure_webhook(self, async_client: AsyncReductoai) -> None:
        async with async_client.with_streaming_response.configure_webhook() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            client = await response.parse()
            assert_matches_type(str, client, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_method_create_extract(self, async_client: AsyncReductoai) -> None:
        client = await async_client.create_extract(
            document_url="document_url",
            schema={},
        )
        assert_matches_type(ExtractResponse, client, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_create_extract_with_all_params(self, async_client: AsyncReductoai) -> None:
        client = await async_client.create_extract(
            document_url="document_url",
            schema={},
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
            array_extract={
                "enabled": True,
                "mode": "auto",
                "pages_per_segment": 0,
                "streaming_extract_item_density": 0,
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
                "table_summary": {
                    "enabled": True,
                    "prompt": "prompt",
                },
            },
            system_prompt="system_prompt",
        )
        assert_matches_type(ExtractResponse, client, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_create_extract(self, async_client: AsyncReductoai) -> None:
        response = await async_client.with_raw_response.create_extract(
            document_url="document_url",
            schema={},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        client = await response.parse()
        assert_matches_type(ExtractResponse, client, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_create_extract(self, async_client: AsyncReductoai) -> None:
        async with async_client.with_streaming_response.create_extract(
            document_url="document_url",
            schema={},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            client = await response.parse()
            assert_matches_type(ExtractResponse, client, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_method_create_extract_async(self, async_client: AsyncReductoai) -> None:
        client = await async_client.create_extract_async(
            document_url="document_url",
            schema={},
        )
        assert_matches_type(CreateExtractAsyncResponse, client, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_create_extract_async_with_all_params(self, async_client: AsyncReductoai) -> None:
        client = await async_client.create_extract_async(
            document_url="document_url",
            schema={},
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
            array_extract={
                "enabled": True,
                "mode": "auto",
                "pages_per_segment": 0,
                "streaming_extract_item_density": 0,
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
                "table_summary": {
                    "enabled": True,
                    "prompt": "prompt",
                },
            },
            priority=True,
            system_prompt="system_prompt",
            webhook={
                "channels": ["string"],
                "metadata": {},
                "mode": "disabled",
                "url": "url",
            },
        )
        assert_matches_type(CreateExtractAsyncResponse, client, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_create_extract_async(self, async_client: AsyncReductoai) -> None:
        response = await async_client.with_raw_response.create_extract_async(
            document_url="document_url",
            schema={},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        client = await response.parse()
        assert_matches_type(CreateExtractAsyncResponse, client, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_create_extract_async(self, async_client: AsyncReductoai) -> None:
        async with async_client.with_streaming_response.create_extract_async(
            document_url="document_url",
            schema={},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            client = await response.parse()
            assert_matches_type(CreateExtractAsyncResponse, client, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_method_create_parse(self, async_client: AsyncReductoai) -> None:
        client = await async_client.create_parse(
            document_url="document_url",
        )
        assert_matches_type(ParseResponse, client, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_create_parse_with_all_params(self, async_client: AsyncReductoai) -> None:
        client = await async_client.create_parse(
            document_url="document_url",
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
        )
        assert_matches_type(ParseResponse, client, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_create_parse(self, async_client: AsyncReductoai) -> None:
        response = await async_client.with_raw_response.create_parse(
            document_url="document_url",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        client = await response.parse()
        assert_matches_type(ParseResponse, client, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_create_parse(self, async_client: AsyncReductoai) -> None:
        async with async_client.with_streaming_response.create_parse(
            document_url="document_url",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            client = await response.parse()
            assert_matches_type(ParseResponse, client, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_method_create_parse_async(self, async_client: AsyncReductoai) -> None:
        client = await async_client.create_parse_async(
            document_url="document_url",
        )
        assert_matches_type(CreateParseAsyncResponse, client, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_create_parse_async_with_all_params(self, async_client: AsyncReductoai) -> None:
        client = await async_client.create_parse_async(
            document_url="document_url",
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
            webhook={
                "channels": ["string"],
                "metadata": {},
                "mode": "disabled",
                "url": "url",
            },
        )
        assert_matches_type(CreateParseAsyncResponse, client, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_create_parse_async(self, async_client: AsyncReductoai) -> None:
        response = await async_client.with_raw_response.create_parse_async(
            document_url="document_url",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        client = await response.parse()
        assert_matches_type(CreateParseAsyncResponse, client, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_create_parse_async(self, async_client: AsyncReductoai) -> None:
        async with async_client.with_streaming_response.create_parse_async(
            document_url="document_url",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            client = await response.parse()
            assert_matches_type(CreateParseAsyncResponse, client, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_method_create_split(self, async_client: AsyncReductoai) -> None:
        client = await async_client.create_split(
            document_url="document_url",
            split_description=[
                {
                    "description": "description",
                    "name": "name",
                }
            ],
        )
        assert_matches_type(SplitResponse, client, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_create_split_with_all_params(self, async_client: AsyncReductoai) -> None:
        client = await async_client.create_split(
            document_url="document_url",
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
        assert_matches_type(SplitResponse, client, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_create_split(self, async_client: AsyncReductoai) -> None:
        response = await async_client.with_raw_response.create_split(
            document_url="document_url",
            split_description=[
                {
                    "description": "description",
                    "name": "name",
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        client = await response.parse()
        assert_matches_type(SplitResponse, client, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_create_split(self, async_client: AsyncReductoai) -> None:
        async with async_client.with_streaming_response.create_split(
            document_url="document_url",
            split_description=[
                {
                    "description": "description",
                    "name": "name",
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            client = await response.parse()
            assert_matches_type(SplitResponse, client, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_method_create_split_async(self, async_client: AsyncReductoai) -> None:
        client = await async_client.create_split_async(
            document_url="document_url",
            split_description=[
                {
                    "description": "description",
                    "name": "name",
                }
            ],
        )
        assert_matches_type(CreateSplitAsyncResponse, client, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_create_split_async_with_all_params(self, async_client: AsyncReductoai) -> None:
        client = await async_client.create_split_async(
            document_url="document_url",
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
        assert_matches_type(CreateSplitAsyncResponse, client, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_create_split_async(self, async_client: AsyncReductoai) -> None:
        response = await async_client.with_raw_response.create_split_async(
            document_url="document_url",
            split_description=[
                {
                    "description": "description",
                    "name": "name",
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        client = await response.parse()
        assert_matches_type(CreateSplitAsyncResponse, client, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_create_split_async(self, async_client: AsyncReductoai) -> None:
        async with async_client.with_streaming_response.create_split_async(
            document_url="document_url",
            split_description=[
                {
                    "description": "description",
                    "name": "name",
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            client = await response.parse()
            assert_matches_type(CreateSplitAsyncResponse, client, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_method_create_upload(self, async_client: AsyncReductoai) -> None:
        client = await async_client.create_upload()
        assert_matches_type(CreateUploadResponse, client, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_create_upload_with_all_params(self, async_client: AsyncReductoai) -> None:
        client = await async_client.create_upload(
            extension="extension",
            file=b"raw file contents",
        )
        assert_matches_type(CreateUploadResponse, client, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_create_upload(self, async_client: AsyncReductoai) -> None:
        response = await async_client.with_raw_response.create_upload()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        client = await response.parse()
        assert_matches_type(CreateUploadResponse, client, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_create_upload(self, async_client: AsyncReductoai) -> None:
        async with async_client.with_streaming_response.create_upload() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            client = await response.parse()
            assert_matches_type(CreateUploadResponse, client, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_method_get_version(self, async_client: AsyncReductoai) -> None:
        client = await async_client.get_version()
        assert_matches_type(object, client, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_get_version(self, async_client: AsyncReductoai) -> None:
        response = await async_client.with_raw_response.get_version()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        client = await response.parse()
        assert_matches_type(object, client, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_get_version(self, async_client: AsyncReductoai) -> None:
        async with async_client.with_streaming_response.get_version() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            client = await response.parse()
            assert_matches_type(object, client, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_method_retrieve_job(self, async_client: AsyncReductoai) -> None:
        client = await async_client.retrieve_job(
            "job_id",
        )
        assert_matches_type(RetrieveJobResponse, client, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_retrieve_job(self, async_client: AsyncReductoai) -> None:
        response = await async_client.with_raw_response.retrieve_job(
            "job_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        client = await response.parse()
        assert_matches_type(RetrieveJobResponse, client, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_retrieve_job(self, async_client: AsyncReductoai) -> None:
        async with async_client.with_streaming_response.retrieve_job(
            "job_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            client = await response.parse()
            assert_matches_type(RetrieveJobResponse, client, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_retrieve_job(self, async_client: AsyncReductoai) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `job_id` but received ''"):
            await async_client.with_raw_response.retrieve_job(
                "",
            )
