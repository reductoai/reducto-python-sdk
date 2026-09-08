"""
End-to-end tests for the request params, response fields, and endpoints added
in the spec sync (see spec/openapi.json). Each test sends one request against
the live API and checks the response shape. Result quality is not tested.

Required environment variable: REDUCTO_API_KEY
"""

from __future__ import annotations

import os
import time
import tempfile
from typing import Any, Dict
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
    ClassifyResponse,
    JobDeleteResponse,
    AsyncParseResponse,
    DocumentProperties,
    AsyncExtractResponse,
)
from reducto.types.job_get_response import JobGetResponse

DOCUMENT_URL = "https://ci.reducto.ai/onepager.pdf"
MISSING_DOCUMENT_URL = "https://ci.reducto.ai/does-not-exist-e2e.pdf"

TRIVIAL_SCHEMA: Dict[str, Any] = {
    "type": "object",
    "properties": {"title": {"type": "string", "description": "The title of the document."}},
    "required": ["title"],
}

CLASSIFICATION_SCHEMA: list[Dict[str, Any]] = [
    {"category": "invoice", "criteria": ["an invoice or bill"]},
    {"category": "report", "criteria": ["a narrative report"]},
]


@pytest.fixture(scope="module")
def client() -> Reducto:
    api_key = os.environ.get("REDUCTO_API_KEY")
    if not api_key:
        pytest.fail("REDUCTO_API_KEY environment variable is required for E2E tests")
    return Reducto(api_key=api_key)


def wait_for_job(client: Reducto, job_id: str, timeout_s: int = 120) -> JobGetResponse:
    deadline = time.monotonic() + timeout_s
    while time.monotonic() < deadline:
        job = client.job.get(job_id)
        if job.status in ("Completed", "Failed"):
            return job
        time.sleep(2)
    pytest.fail(f"Job {job_id} did not finish within {timeout_s}s")


class TestParseNewParams:
    @pytest.fixture(scope="class")
    def response(self, client: Reducto) -> ParseResponse:
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

    def test_response_type(self, response: ParseResponse) -> None:
        assert response.response_type == "parse"

    def test_force_url_result(self, response: ParseResponse) -> None:
        assert response.result.type == "url"
        assert response.result.url.startswith("https://")

    def test_document_properties(self, response: ParseResponse) -> None:
        assert isinstance(response.document_properties, DocumentProperties)
        assert response.document_properties.title

    def test_embed_pdf_metadata_dpi(self, response: ParseResponse) -> None:
        assert response.pdf_url

    def test_usage_page_billing_breakdown(self, response: ParseResponse) -> None:
        breakdown = response.usage.page_billing_breakdown
        assert breakdown is not None
        assert "1" in breakdown
        assert "page" in breakdown["1"]

    def test_queue_priority_standard(self, client: Reducto) -> None:
        response = client.parse.run_job(input=DOCUMENT_URL, queue_priority="standard")
        assert isinstance(response, AsyncParseResponse)
        assert response.job_id


class TestExtractNewParams:
    @pytest.fixture(scope="class")
    def response(self, client: Reducto) -> V3Extract:
        response = client.extract.run(
            input=DOCUMENT_URL,
            instructions={"schema": TRIVIAL_SCHEMA},
            settings={
                "force_url_result": True,
                "page_range": {"start": 1, "end": 1},
                "citations": {"enabled": True, "parent_block": "bbox_only"},
            },
        )
        assert isinstance(response, V3Extract)
        return response

    def test_response_type(self, response: V3Extract) -> None:
        assert response.response_type == "v3_extract"

    def test_force_url_result(self, response: V3Extract) -> None:
        assert isinstance(response.result, dict)
        assert response.result["type"] == "url"
        assert str(response.result["url"]).startswith("https://")

    def test_confidence_fields_present(self, response: V3Extract) -> None:
        assert response.confidence in (None, "high", "low")
        assert response.confidence_reason is None or isinstance(response.confidence_reason, str)

    def test_queue_priority_standard(self, client: Reducto) -> None:
        response = client.extract.run_job(
            input=DOCUMENT_URL,
            instructions={"schema": TRIVIAL_SCHEMA},
            queue_priority="standard",
        )
        assert isinstance(response, AsyncExtractResponse)
        assert response.job_id


class TestSplitNewParams:
    @pytest.fixture(scope="class")
    def response(self, client: Reducto) -> SplitResponse:
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

    def test_response_type(self, response: SplitResponse) -> None:
        assert response.response_type == "split"

    def test_job_id_and_duration(self, response: SplitResponse) -> None:
        assert response.job_id
        assert response.duration is not None and response.duration >= 0

    def test_force_url_result(self, response: SplitResponse) -> None:
        assert isinstance(response.result, URLResult)
        assert response.result.url.startswith("https://")


class TestClassifyNewParams:
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


class TestJobNewEndpoints:
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


class TestDeleteUpload:
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
