"""
Regression repro for Pylon #8891 (Kalepa).

Symptom: after API PR #5420 (2026-04-24) stopped rewriting v3 extract responses
to v2 ExtractResponse on the wire, customers polling /job/{job_id} see typed
accessors return None even though the JSON body contains their extracted fields.

Root cause: Stainless lossy-translates the server-side `T | None` (required-
nullable) shape of `PipelineResult.parse/extract/split` into the SDK-side
`Optional[T] = None` (optional-with-default). On the server this means
`PipelineResult.model_validate(v3_json)` correctly fails (missing required
keys) and `handlers/job.py`'s ordered loop falls through to V3ExtractResponse.
On the SDK, the all-Optional `Result` model + the BaseModel `extra="allow"`
default makes Result validate against any dict, which is what makes
PipelineResponse the smart-union winner for v3 payloads.

The bug therefore lives entirely in the regenerated SDK, not in the server.
Fix path: add a Pydantic Discriminator to the spec-side union variants in
`src/config/internal.py` so dispatch becomes structural and Stainless emits
the discriminator; smart-union scoring stops mattering.

Full RCA + diagrams: docs/rca/pylon-8891-rca.tex (compile with pdflatex) in the API repo.

Test markers:
- async-path bug tests use @pytest.mark.xfail(strict=True): they fail on main
  today (proving the bug). Once the fix lands they will start passing, at
  which point strict=True makes pytest fail XPASSED and forces removal of
  the marker, turning each test into a permanent regression check.
- snapshot tests pinning the current (buggy) shape of `Result` are NOT marked
  xfail. They pass today; once the spec fix lands they will start failing,
  and that failure is the signal to delete or invert the test.
- the proposed-fix proof-of-concept test is a self-contained Pydantic example
  using a local mini-union, independent of the SDK's generated types.
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
    "See docs/rca/pylon-8891-rca.tex (compile with pdflatex)."
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


# ---------------------------------------------------------------------------
# Snapshot tests pinning the SDK-side Result constraint that enables the bug.
# These tests pass today (they document the lossy-translation result). When
# the spec is fixed and Stainless regens, they will start failing -- that
# failure is the signal to delete or invert these tests.
# ---------------------------------------------------------------------------


def test_pipeline_response_result_validates_empty_dict_today() -> None:
    """
    Snapshot: SDK-side `PipelineResponse.Result` accepts an empty dict.

    On the server (src/config/internal.py:1132), PipelineResult.parse/extract/
    split are required-nullable (`T | None` with no default), so the analogous
    server-side validate would fail on an empty dict for missing required keys.
    Stainless's regen drops that constraint by inserting `= None` defaults on
    every field. This test pins that lossy translation: an empty dict validates
    cleanly today, which is the constraint that makes PipelineResponse a
    smart-union magnet for v3 payloads.

    Action when this test fails: the SDK's Result has been regenerated against
    a tighter spec (discriminator added, or required-without-default), the bug
    is fixed at the spec level, and this snapshot can be removed.
    """
    from reducto.types.shared.pipeline_response import Result

    instance = Result.model_validate({})
    assert instance.extract is None
    assert instance.parse is None
    assert instance.split is None
    assert instance.edit is None


def test_pipeline_response_result_absorbs_arbitrary_keys_today() -> None:
    """
    Snapshot: SDK-side Result inherits `extra="allow"` from the base BaseModel
    (src/reducto/_models.py:110), so a v3 payload's keys (`company_name`,
    `total_amount`, etc.) attach as untyped extras while every typed field
    stays None. Combined with the empty-dict tolerance above, this is what
    lets PipelineResponse claim a v3 payload during smart-union scoring.

    Action when this test fails: same as above -- the spec has tightened.
    """
    from reducto.types.shared.pipeline_response import Result

    payload = _v3_inner_payload()["result"]  # the dict-shaped v3 result
    instance = Result.model_validate(payload)

    assert instance.extract is None
    assert instance.parse is None
    assert instance.split is None
    assert instance.edit is None

    dumped = instance.model_dump()
    assert "company_name" in dumped
    assert "total_amount" in dumped


# ---------------------------------------------------------------------------
# Proof-of-concept: the recommended fix (discriminator on each union variant)
# routes correctly without depending on smart-union scoring or field counts.
# Uses local Pydantic models so it runs independently of the generated SDK.
# ---------------------------------------------------------------------------


def test_proposed_discriminator_fix_routes_v3_correctly() -> None:
    """
    Sketch of the recommended fix from the RCA. Adding a `response_type`
    Literal field to each variant in src/config/internal.py converts the
    union into a Pydantic discriminated union. Discriminator dispatch in
    construct_type runs before smart-union scoring (_models.py:533), so
    field counts and `extra="allow"` permissiveness stop affecting routing.
    """
    from typing import Annotated, Literal, Union

    from pydantic import BaseModel as PydBaseModel
    from pydantic import Discriminator, TypeAdapter

    class TaggedV3Extract(PydBaseModel):
        response_type: Literal["v3_extract"] = "v3_extract"
        result: dict[str, object]

    class TaggedPipeline(PydBaseModel):
        response_type: Literal["pipeline"] = "pipeline"
        # all-Optional, exactly as the SDK Result is today -- the discriminator
        # must override smart-union even when this remains permissive.
        extract: object | None = None
        parse:   object | None = None
        split:   object | None = None
        edit:    object | None = None

    Discriminated = Annotated[
        Union[TaggedPipeline, TaggedV3Extract], Discriminator("response_type")
    ]
    adapter = TypeAdapter(Discriminated)

    v3_payload = {"response_type": "v3_extract", "result": {"company_name": {"value": "X"}}}
    resolved = adapter.validate_python(v3_payload)
    assert isinstance(resolved, TaggedV3Extract), (
        f"Discriminator should route v3_extract payload to TaggedV3Extract; "
        f"got {type(resolved).__name__}."
    )

    pipeline_payload = {"response_type": "pipeline", "extract": None, "parse": None, "split": None, "edit": None}
    resolved = adapter.validate_python(pipeline_payload)
    assert isinstance(resolved, TaggedPipeline)
