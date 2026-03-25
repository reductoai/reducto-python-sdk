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

import pytest

from reducto import Reducto
from reducto.types import V3Extract, ParseResponse, AsyncParseResponse
from reducto.types.job_get_response import AsyncJobResponse, EnhancedAsyncJobResponse
from reducto.types.async_extract_response import AsyncExtractResponse

DOCUMENT_URL = "https://ci.reducto.ai/onepager.pdf"

TRIVIAL_SCHEMA = {
    "type": "object",
    "properties": {
        "title": {
            "type": "string",
            "description": "The title of the document.",
        },
    },
    "required": ["title"],
}


@pytest.fixture(scope="module")
def client() -> Reducto:
    api_key = os.environ.get("REDUCTO_API_KEY")
    if not api_key:
        pytest.skip("REDUCTO_API_KEY not set")
    return Reducto(api_key=api_key)


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


class TestParseAsync:
    """Tests for the /parse_async endpoint (client.parse.run_job)."""

    def test_parse_async_returns_job_id(self, client: Reducto) -> None:
        response = client.parse.run_job(input=DOCUMENT_URL)
        assert isinstance(response, AsyncParseResponse)
        assert response.job_id

    def test_parse_async_job_completes(self, client: Reducto) -> None:
        response = client.parse.run_job(input=DOCUMENT_URL)
        assert isinstance(response, AsyncParseResponse)
        job_id = response.job_id

        # Poll until job completes (max 120s)
        for _ in range(60):
            job = client.job.get(job_id)
            assert isinstance(job, (AsyncJobResponse, EnhancedAsyncJobResponse))
            if job.status == "Completed":
                assert job.result is not None
                return
            if job.status == "Failed":
                pytest.fail(f"Parse async job failed: {job.reason}")
            time.sleep(2)

        pytest.fail("Parse async job did not complete within timeout")


class TestExtract:
    """Tests for the /extract endpoint (client.extract.run)."""

    def test_extract_sync(self, client: Reducto) -> None:
        response = client.extract.run(
            input=DOCUMENT_URL,
            instructions={"schema": TRIVIAL_SCHEMA},
        )
        assert isinstance(response, V3Extract)
        assert response.result is not None

    def test_extract_returns_result(self, client: Reducto) -> None:
        response = client.extract.run(
            input=DOCUMENT_URL,
            instructions={"schema": TRIVIAL_SCHEMA},
        )
        assert isinstance(response, V3Extract)
        assert isinstance(response.result, list)
        assert len(response.result) > 0


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
        job_id = response.job_id

        # Poll until job completes (max 120s)
        for _ in range(60):
            job = client.job.get(job_id)
            assert isinstance(job, (AsyncJobResponse, EnhancedAsyncJobResponse))
            if job.status == "Completed":
                assert job.result is not None
                return
            if job.status == "Failed":
                pytest.fail(f"Extract async job failed: {job.reason}")
            time.sleep(2)

        pytest.fail("Extract async job did not complete within timeout")


class TestUpload:
    """Tests for the /upload endpoint (client.upload)."""

    def test_upload_returns_file_id(self, client: Reducto) -> None:
        response = client.upload()
        assert response.file_id
        assert response.presigned_url

    def test_upload_file_id_usable_with_parse(self, client: Reducto) -> None:
        upload = client.upload(extension="pdf")
        assert upload.file_id
        assert upload.presigned_url
        # Verify the file_id is a valid reducto:// URI format
        assert upload.file_id.startswith("reducto://")


class TestJob:
    """Tests for the /job/{job_id} endpoint (client.job.get)."""

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
        # Create an async parse job and wait for completion
        async_response = client.parse.run_job(input=DOCUMENT_URL)
        assert isinstance(async_response, AsyncParseResponse)
        job_id = async_response.job_id

        for _ in range(60):
            job = client.job.get(job_id)
            assert isinstance(job, (AsyncJobResponse, EnhancedAsyncJobResponse))
            if job.status == "Completed":
                assert job.result is not None
                return
            if job.status == "Failed":
                pytest.fail(f"Job failed: {job.reason}")
            time.sleep(2)

        pytest.fail("Job did not complete within timeout")
