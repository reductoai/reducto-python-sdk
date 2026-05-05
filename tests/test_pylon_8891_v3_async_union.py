"""
Regression repro for Pylon #8891 (Kalepa).

Symptom: after API PR #5420 (2026-04-24) stopped rewriting v3 extract responses
to v2 ExtractResponse on the wire, customers polling /job/{job_id} see typed
accessors return None even though the JSON body contains their extracted fields.

Root cause (verified): construct_type tries pydantic smart-union validation
first (src/reducto/_models.py:515). For the AsyncJobResponseResult union, that
validation succeeds on PipelineResponse because PipelineResponse.result is a
Result model with all-Optional fields and the SDK's BaseModel uses
extra="allow". The customer's v3 payload is absorbed into Result with all four
typed fields (extract / parse / split / edit) defaulting to None and the actual
data attached as untyped extras.

Full RCA + diagrams: api/users/sravan/pylon-8891-rca.pdf in the API repo.

These tests are marked xfail(strict=True): they fail on main today (proving the
bug); once the fix lands they will start passing, at which point strict=True
makes pytest fail the test as XPASSED and forces removal of the xfail marker.
"""

from __future__ import annotations

from typing import Any

import pydantic
import pytest

from reducto._models import construct_type
from reducto.types.extract_run_response import ExtractRunResponse
from reducto.types.job_get_response import (
    AsyncJobResponse,
    AsyncJobResponseResult,
    EnhancedAsyncJobResponse,
)
from reducto.types.shared.pipeline_response import PipelineResponse
from reducto.types.v3_extract import V3Extract


XFAIL_REASON = (
    "Pylon #8891: SDK union resolution picks PipelineResponse for v3 payloads. "
    "See api/users/sravan/pylon-8891-rca.pdf."
)


def _v3_inner_payload() -> dict[str, Any]:
    """Representative v3 extract response as the server emits it post-PR #5420."""
    return {
        "result": {
            "company_name": {
                "value": "Acme Corp",
                "citations": [{"page": 1, "bbox": [0, 0, 100, 20]}],
            },
            "total_amount": {
                "value": 1234.56,
                "citations": [{"page": 2, "bbox": [10, 30, 80, 50]}],
            },
        },
        "usage": {"num_fields": 2, "num_pages": 2},
        "job_id": "ee9734ef-95b2-48f9-b62a-47664fbe8edc",
        "studio_link": "https://studio.reducto.ai/job/ee9734ef-95b2-48f9-b62a-47664fbe8edc",
    }


@pytest.mark.xfail(strict=True, reason=XFAIL_REASON)
def test_pydantic_smart_union_picks_v3extract_for_v3_payload() -> None:
    """Pydantic smart-union should pick V3Extract; today it picks PipelineResponse."""
    adapter = pydantic.TypeAdapter(AsyncJobResponseResult)
    resolved = adapter.validate_python(_v3_inner_payload())

    assert isinstance(resolved, V3Extract), (
        f"Expected V3Extract, got {type(resolved).__name__}. "
        f"PipelineResponse.Result is all-Optional with extra='allow' and "
        f"absorbs the v3 dict, beating V3Extract in smart-union scoring."
    )
    assert not isinstance(resolved, PipelineResponse)


@pytest.mark.xfail(strict=True, reason=XFAIL_REASON)
def test_async_job_response_result_resolves_to_v3extract() -> None:
    """The full client.job.get(...) path should produce V3Extract on the inner result."""
    payload = {
        "status": "Completed",
        "progress": 1.0,
        "result": _v3_inner_payload(),
    }
    obj = construct_type(type_=AsyncJobResponse, value=payload)
    assert isinstance(obj, AsyncJobResponse)
    assert isinstance(obj.result, V3Extract), (
        f"Expected obj.result to be V3Extract, got {type(obj.result).__name__}."
    )


@pytest.mark.xfail(strict=True, reason=XFAIL_REASON)
def test_enhanced_async_job_response_result_resolves_to_v3extract() -> None:
    """EnhancedAsyncJobResponse (the canonical /job/{id} cast target) hits the same bug."""
    payload = {
        "status": "Completed",
        "progress": 1.0,
        "type": "Extract",
        "result": _v3_inner_payload(),
    }
    obj = construct_type(type_=EnhancedAsyncJobResponse, value=payload)
    assert isinstance(obj, EnhancedAsyncJobResponse)
    assert isinstance(obj.result, V3Extract)


def test_sync_path_resolves_to_v3extract_correctly() -> None:
    """
    Positive control: the sync endpoint's cast type
    `ExtractRunResponse = Union[V3Extract, AsyncExtractResponse]`
    does NOT contain PipelineResponse, so the same v3 payload resolves
    correctly there. This is why the customer reported the bug only on
    the async path and worked around it by switching to sync. Guards
    against any future change that adds PipelineResponse (or another
    permissive variant) to the sync union.
    """
    sync_obj = construct_type(type_=ExtractRunResponse, value=_v3_inner_payload())
    assert isinstance(sync_obj, V3Extract), (
        f"Sync path should resolve v3 payload to V3Extract; got {type(sync_obj).__name__}. "
        f"If this fails, the sync union has gained a permissive variant -- "
        f"check ExtractRunResponse in src/reducto/types/extract_run_response.py."
    )
    assert isinstance(sync_obj.result, dict)
    assert "company_name" in sync_obj.result


@pytest.mark.xfail(strict=True, reason=XFAIL_REASON)
def test_v3_extracted_fields_are_reachable_via_typed_path() -> None:
    """
    Customer-facing assertion: the extracted fields must reach the typed path.
    On main, the variant is PipelineResponse and the customer's keys land on
    Result as untyped extras, so this dotted access raises AttributeError or
    returns the wrong shape.
    """
    payload = {"status": "Completed", "progress": 1.0, "result": _v3_inner_payload()}
    obj = construct_type(type_=AsyncJobResponse, value=payload)

    inner = obj.result
    assert isinstance(inner, V3Extract)
    extracted = inner.result
    assert isinstance(extracted, dict)
    assert "company_name" in extracted
    assert extracted["company_name"]["value"] == "Acme Corp"
