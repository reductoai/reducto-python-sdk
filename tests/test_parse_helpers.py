from typing import Any, Dict, Optional

import httpx
import respx
import pytest

from reducto.types import ParseResponse
from reducto._compat import PYDANTIC_V1
from reducto.lib.helpers import handle_url_response


@pytest.mark.skipif(PYDANTIC_V1, reason="Parse helpers currently require Pydantic v2")
@pytest.mark.parametrize("result_type", ["full", "url"])
@pytest.mark.parametrize("pdf_url", [None, "https://storage.example.com/converted.pdf?signature=example"])
def test_handle_url_response_preserves_pdf_url(result_type: str, pdf_url: Optional[str]) -> None:
    full_result: Dict[str, Any] = {
        "type": "full",
        "chunks": [{"content": "document text", "embed": "document text", "blocks": []}],
    }
    response = ParseResponse.model_validate(
        {
            "duration": 1.25,
            "job_id": "job-example",
            "response_type": "parse",
            "usage": {"num_pages": 2},
            "pdf_url": pdf_url,
            "result": full_result
            if result_type == "full"
            else {
                "type": "url",
                "result_id": "result-example",
                "url": "https://storage.example.com/result.json",
            },
        }
    )

    with respx.mock(assert_all_called=False) as router:
        route = router.get("https://storage.example.com/result.json").mock(
            return_value=httpx.Response(200, json=full_result)
        )
        hydrated = handle_url_response(response)
        assert route.call_count == (1 if result_type == "url" else 0)

    assert hydrated.pdf_url == pdf_url
    assert hydrated.duration == response.duration
    assert hydrated.job_id == response.job_id
    assert hydrated.usage == response.usage
    assert hydrated.result.type == "full"
    assert hydrated.result.chunks[0].content == "document text"
