"""
End-to-end tests for the Reducto Python SDK.

These tests exercise the SDK against the live Reducto API to verify
that the SDK contract is working correctly. They are not testing the
actual parsing/extraction quality, just that the endpoints respond
with the expected structure.

Required environment variable: REDUCTO_API_KEY
"""

from __future__ import annotations

import os
import time
import tempfile
from typing import Any, Dict, List, Union
from pathlib import Path

import pytest

import reducto
from reducto import Reducto
from reducto.types import (
    URLResult,
    V3Extract,
    ErrorDetail,
    ParseResponse,
    SplitResponse,
    ExtractResponse,
    ClassifyResponse,
    JobDeleteResponse,
    AsyncParseResponse,
    DocumentProperties,
    AsyncExtractResponse,
)
from reducto.types.job_get_response import JobGetResponse, AsyncJobResponse, EnhancedAsyncJobResponse

DOCUMENT_URL = "https://ci.reducto.ai/onepager.pdf"
MISSING_DOCUMENT_URL = "https://ci.reducto.ai/does-not-exist-e2e.pdf"

TRIVIAL_SCHEMA: Dict[str, Any] = {
    "type": "object",
    "properties": {
        "title": {
            "type": "string",
            "description": "The title of the document.",
        },
    },
    "required": ["title"],
}

CLASSIFICATION_SCHEMA: List[Dict[str, Any]] = [
    {"category": "invoice", "criteria": ["an invoice or bill"]},
    {"category": "report", "criteria": ["a narrative report"]},
]

# The API returns ExtractResponse or V3Extract from /extract depending on the account.
SyncExtractResponse = Union[ExtractResponse, V3Extract]


@pytest.fixture(scope="module")
def client() -> Reducto:
    api_key = os.environ.get("REDUCTO_API_KEY")
    if not api_key:
        pytest.fail("REDUCTO_API_KEY environment variable is required for E2E tests")
    return Reducto(api_key=api_key)


@pytest.fixture(scope="module")
def parse_response(client: Reducto) -> ParseResponse:
    """One parse call that sends every newer parse option."""
    return client.parse.run(
        input=DOCUMENT_URL,
        enhance={
            "advanced_chart_agent": True,
            "agentic": [{"scope": "table", "mode": "default"}],
        },
        settings={
            "embed_pdf_metadata": True,
            "embed_pdf_metadata_dpi": 72,
            "extract_document_properties": True,
            "force_url_result": True,
            "tenant_throttling": {"tenant_id": "sdk-e2e", "max_share": 0.5},
        },
        spreadsheet={"max_cell_count": 100_000},
    )


@pytest.fixture(scope="module")
def extract_response(client: Reducto) -> SyncExtractResponse:
    """One extract call that sends every newer extract option."""
    response = client.extract.run(
        input=DOCUMENT_URL,
        instructions={"schema": TRIVIAL_SCHEMA},
        settings={
            "force_url_result": True,
            "page_range": {"start": 1, "end": 1},
            "citations": {"enabled": True, "parent_block": "bbox_only"},
        },
    )
    assert isinstance(response, (ExtractResponse, V3Extract))
    return response


@pytest.fixture(scope="module")
def split_response(client: Reducto) -> SplitResponse:
    return client.split.run(
        input=DOCUMENT_URL,
        split_description=[
            {"name": "invoice", "description": "An invoice or bill"},
            {"name": "other", "description": "Anything else"},
        ],
        settings={
            "allow_page_overlap": True,
            "auto_partition": True,
            "deep_split": False,
            "force_url_result": True,
        },
    )


def wait_for_job(client: Reducto, job_id: str, timeout_s: int = 120) -> JobGetResponse:
    deadline = time.monotonic() + timeout_s
    while time.monotonic() < deadline:
        job = client.job.get(job_id)
        assert isinstance(job, (AsyncJobResponse, EnhancedAsyncJobResponse))
        if job.status in ("Completed", "Failed"):
            return job
        time.sleep(2)
    pytest.fail(f"Job {job_id} did not finish within {timeout_s}s")


class TestParse:
    """Tests for the /parse endpoint (client.parse.run)."""

    def test_parse_sync(self, client: Reducto) -> None:
        response = client.parse.run(input=DOCUMENT_URL)
        assert isinstance(response, ParseResponse)
        assert response.job_id
        assert response.duration >= 0
        assert response.result is not None

    def test_parse_returns_chunks(self, client: Reducto) -> None:
        response = client.parse.run(input=DOCUMENT_URL)
        assert isinstance(response, ParseResponse)
        result = response.result
        assert result.type == "full"
        assert len(result.chunks) > 0  # type: ignore[union-attr]

    def test_response_type(self, parse_response: ParseResponse) -> None:
        assert parse_response.response_type == "parse"

    def test_force_url_result(self, parse_response: ParseResponse) -> None:
        assert parse_response.result.type == "url"
        assert parse_response.result.url.startswith("https://")

    def test_document_properties(self, parse_response: ParseResponse) -> None:
        assert isinstance(parse_response.document_properties, DocumentProperties)
        assert parse_response.document_properties.title

    def test_embed_pdf_metadata(self, parse_response: ParseResponse) -> None:
        assert parse_response.pdf_url

    def test_usage_page_billing_breakdown(self, parse_response: ParseResponse) -> None:
        breakdown = parse_response.usage.page_billing_breakdown
        assert breakdown is not None
        assert "1" in breakdown
        assert "page" in breakdown["1"]


class TestParseAsync:
    """Tests for the /parse_async endpoint (client.parse.run_job)."""

    def test_parse_async_returns_job_id(self, client: Reducto) -> None:
        response = client.parse.run_job(input=DOCUMENT_URL)
        assert isinstance(response, AsyncParseResponse)
        assert response.job_id

    def test_parse_async_job_completes(self, client: Reducto) -> None:
        response = client.parse.run_job(input=DOCUMENT_URL)
        assert isinstance(response, AsyncParseResponse)
        job = wait_for_job(client, response.job_id)
        if job.status == "Failed":
            pytest.fail(f"Parse async job failed: {job.reason}")
        assert job.result is not None

    def test_queue_priority_standard(self, client: Reducto) -> None:
        response = client.parse.run_job(input=DOCUMENT_URL, queue_priority="standard")
        assert isinstance(response, AsyncParseResponse)
        assert response.job_id


class TestExtract:
    """Tests for the /extract endpoint (client.extract.run)."""

    def test_extract_sync(self, client: Reducto) -> None:
        response = client.extract.run(
            input=DOCUMENT_URL,
            instructions={"schema": TRIVIAL_SCHEMA},
        )
        assert isinstance(response, (ExtractResponse, V3Extract))
        assert response.result is not None

    def test_extract_returns_result(self, client: Reducto) -> None:
        response = client.extract.run(
            input=DOCUMENT_URL,
            instructions={"schema": TRIVIAL_SCHEMA},
        )
        assert isinstance(response, (ExtractResponse, V3Extract))
        assert isinstance(response.result, list)
        assert len(response.result) > 0

    def test_response_type_matches_class(self, extract_response: SyncExtractResponse) -> None:
        expected = "extract" if isinstance(extract_response, ExtractResponse) else "v3_extract"
        assert extract_response.response_type == expected

    def test_force_url_result(self, extract_response: SyncExtractResponse) -> None:
        if isinstance(extract_response, ExtractResponse):
            assert isinstance(extract_response.result, URLResult)
            assert extract_response.result.url.startswith("https://")
        else:
            assert isinstance(extract_response.result, dict)
            assert extract_response.result["type"] == "url"
            assert str(extract_response.result["url"]).startswith("https://")

    def test_confidence_fields_present(self, extract_response: SyncExtractResponse) -> None:
        if isinstance(extract_response, V3Extract):
            assert extract_response.confidence in (None, "high", "low")
            assert extract_response.confidence_reason is None or isinstance(extract_response.confidence_reason, str)
        else:
            assert extract_response.response_confidence is None or isinstance(
                extract_response.response_confidence, dict
            )


class TestExtractAsync:
    """Tests for the /extract_async endpoint (client.extract.run_job)."""

    def test_extract_async_returns_job_id(self, client: Reducto) -> None:
        response = client.extract.run_job(
            input=DOCUMENT_URL,
            instructions={"schema": TRIVIAL_SCHEMA},
        )
        assert isinstance(response, AsyncExtractResponse)
        assert response.job_id

    def test_extract_async_job_completes(self, client: Reducto) -> None:
        response = client.extract.run_job(
            input=DOCUMENT_URL,
            instructions={"schema": TRIVIAL_SCHEMA},
        )
        assert isinstance(response, AsyncExtractResponse)
        job = wait_for_job(client, response.job_id)
        if job.status == "Failed":
            pytest.fail(f"Extract async job failed: {job.reason}")
        assert job.result is not None

    def test_queue_priority_standard(self, client: Reducto) -> None:
        response = client.extract.run_job(
            input=DOCUMENT_URL,
            instructions={"schema": TRIVIAL_SCHEMA},
            queue_priority="standard",
        )
        assert isinstance(response, AsyncExtractResponse)
        assert response.job_id


class TestSplit:
    """Tests for the /split endpoint (client.split.run)."""

    def test_response_type(self, split_response: SplitResponse) -> None:
        assert split_response.response_type == "split"

    def test_job_id_and_duration(self, split_response: SplitResponse) -> None:
        assert split_response.job_id
        assert split_response.duration is not None and split_response.duration >= 0

    def test_force_url_result(self, split_response: SplitResponse) -> None:
        assert isinstance(split_response.result, URLResult)
        assert split_response.result.url.startswith("https://")


class TestClassify:
    """Tests for the /classify endpoint (client.classify.run)."""

    def test_category_groups_and_model(self, client: Reducto) -> None:
        response = client.classify.run(
            input=DOCUMENT_URL,
            classification_schema=CLASSIFICATION_SCHEMA,
            category_groups={"financial": ["invoice"]},
            model="default",
            priority=True,
        )
        assert isinstance(response, ClassifyResponse)
        assert response.response_type == "classify"
        assert not isinstance(response.result, URLResult)
        assert response.result.category in ("invoice", "report")
        assert response.extra_metadata is not None
        assert response.extra_metadata["grouping"] in ("financial", "ungrouped")
        assert response.usage is not None
        assert response.usage.num_categories == len(CLASSIFICATION_SCHEMA)

    def test_force_url_result(self, client: Reducto) -> None:
        response = client.classify.run(
            input=DOCUMENT_URL,
            classification_schema=CLASSIFICATION_SCHEMA,
            force_url_result=True,
        )
        assert isinstance(response.result, URLResult)
        assert response.result.url.startswith("https://")


class TestUpload:
    """Tests for the /upload endpoints (client.upload, client.delete_upload)."""

    def test_upload_returns_file_id(self, client: Reducto) -> None:
        response = client.upload()
        assert response.file_id
        assert response.presigned_url

    def test_upload_with_extension(self, client: Reducto) -> None:
        upload = client.upload(extension="pdf")
        assert upload.file_id
        assert upload.presigned_url
        # Verify the file_id is a valid reducto:// URI format
        assert upload.file_id.startswith("reducto://")

    def test_upload_with_file_path(self, client: Reducto) -> None:
        """Test upload with file=Path() — verifies the SDK handles local file paths."""
        # Create a minimal PDF file for upload
        with tempfile.NamedTemporaryFile(suffix=".pdf", delete=False) as f:
            f.write(b"%PDF-1.4 minimal test file")
            tmp_path = Path(f.name)
        try:
            upload = client.upload(file=tmp_path)
            assert upload.file_id
            assert upload.file_id.startswith("reducto://")
        finally:
            tmp_path.unlink()

    def test_delete_uploaded_file(self, client: Reducto) -> None:
        with tempfile.NamedTemporaryFile(suffix=".pdf", delete=False) as f:
            f.write(b"%PDF-1.4 minimal test file")
            tmp_path = Path(f.name)
        try:
            upload = client.upload(file=tmp_path)
        finally:
            tmp_path.unlink()
        assert upload.file_id.startswith("reducto://")

        deleted = client.delete_upload(upload.file_id)
        assert deleted.file_id == upload.file_id

        with pytest.raises(reducto.NotFoundError):
            client.delete_upload(upload.file_id)


class TestJob:
    """Tests for the /job/{job_id} endpoints (client.job.get, client.job.delete)."""

    def test_job_get_with_parse_job(self, client: Reducto) -> None:
        # Create an async parse job first
        async_response = client.parse.run_job(input=DOCUMENT_URL)
        assert isinstance(async_response, AsyncParseResponse)
        job_id = async_response.job_id

        # Immediately poll the job - should be Pending or Completed
        job = client.job.get(job_id)
        assert isinstance(job, (AsyncJobResponse, EnhancedAsyncJobResponse))
        assert job.status in ("Pending", "Completed", "Idle")

    def test_job_get_completed(self, client: Reducto) -> None:
        async_response = client.parse.run_job(input=DOCUMENT_URL)
        assert isinstance(async_response, AsyncParseResponse)
        job = wait_for_job(client, async_response.job_id)
        if job.status == "Failed":
            pytest.fail(f"Job failed: {job.reason}")
        assert job.result is not None

    def test_delete_job(self, client: Reducto) -> None:
        job_id = client.parse.run_job(input=DOCUMENT_URL).job_id
        assert wait_for_job(client, job_id).status == "Completed"

        deleted = client.job.delete(job_id)
        assert isinstance(deleted, JobDeleteResponse)
        assert deleted.job_id == job_id

        with pytest.raises(reducto.APIStatusError) as exc_info:
            client.job.get(job_id)
        assert exc_info.value.status_code in (409, 410)

    def test_delete_job_with_include_persisted(self, client: Reducto) -> None:
        job_id = client.parse.run_job(input=DOCUMENT_URL).job_id
        wait_for_job(client, job_id)
        deleted = client.job.delete(job_id, include_persisted=True)
        assert deleted.job_id == job_id

    def test_failed_job_has_error_detail(self, client: Reducto) -> None:
        job_id = client.parse.run_job(input=MISSING_DOCUMENT_URL).job_id
        job = wait_for_job(client, job_id)
        assert job.status == "Failed"
        assert isinstance(job.error, ErrorDetail)
        assert job.error.name == "INVALID_CONFIG"
        assert job.error.code == 400
        assert job.error.message
