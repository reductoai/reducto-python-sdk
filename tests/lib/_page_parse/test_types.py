from __future__ import annotations

import pickle

from reducto import PageParseError, UnsupportedOnProviderError
from reducto._compat import parse_obj, model_dump
from reducto.lib.sagemaker import FailedPage, ProviderParseResponse

_PAYLOAD: dict[str, object] = {
    "duration": 1.0,
    "job_id": "local",
    "result": {"type": "full", "chunks": []},
    "usage": {"num_pages": 2},
    "response_type": "parse",
}


def test_provider_response_round_trips_as_a_parse_response() -> None:
    """Catches a response model that breaks under pydantic v1."""
    response = parse_obj(ProviderParseResponse, _PAYLOAD)
    assert response.result.chunks == []
    assert model_dump(response)["job_id"] == "local"


def test_unsupported_error_survives_pickling() -> None:
    """Catches an error that a process pool cannot send back, or that doubles its message on the way."""
    error = UnsupportedOnProviderError("DOCX files", kind="file_type")
    copy = pickle.loads(pickle.dumps(error))
    assert str(copy) == str(error) and (copy.feature, copy.kind) == ("DOCX files", "file_type")


def test_page_parse_error_survives_pickling() -> None:
    """Catches a page failure that a process pool cannot send back, or that loses its pages on the way."""
    failed = [FailedPage(page=2, reason="unprocessable", status=422)]
    error = PageParseError(
        "1 of 2 pages failed: page 2 (unprocessable).", failed, parse_obj(ProviderParseResponse, _PAYLOAD)
    )
    copy = pickle.loads(pickle.dumps(error))
    assert str(copy) == str(error)
    assert copy.failed_pages == failed
    assert copy.partial_response == error.partial_response
