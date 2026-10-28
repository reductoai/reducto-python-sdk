from __future__ import annotations

import pytest

from reducto import UnsupportedOnProviderError
from reducto.lib._page_parse.client import PageParseClient, AsyncPageParseClient, check_client_settings
from reducto.lib._page_parse.transport import PageTransport

from ._helpers import FakeTransport, titled, make_pdf


class _OtherProvider(PageParseClient):
    """A provider client that brings only a transport."""

    def __init__(self, transport: PageTransport) -> None:
        check_client_settings(max_concurrency=2, max_retries=0, timeout=10.0)
        super().__init__(transport=transport, max_concurrency=2, max_retries=0)


class _AsyncOtherProvider(AsyncPageParseClient):
    def __init__(self, transport: PageTransport) -> None:
        check_client_settings(max_concurrency=2, max_retries=0, timeout=10.0)
        super().__init__(transport=transport, max_concurrency=2, max_retries=0)


def _numbered() -> FakeTransport:
    return FakeTransport(lambda call: titled(call + 1))


def test_a_second_provider_needs_only_a_transport() -> None:
    """Catches provider-specific code in the shared client, which a second provider would have to copy."""
    transport = _numbered()
    with _OtherProvider(transport) as client:
        response = client.parse.run(input=make_pdf(3), settings={"page_range": [1, 3]})
    assert sorted(chunk.content for chunk in response.result.chunks) == ["Page 1", "Page 2"]
    assert [chunk.blocks[0].bbox.original_page for chunk in response.result.chunks] == [1, 3]
    assert len(transport.bodies) == 2
    with pytest.raises(UnsupportedOnProviderError, match="`client.extract` cannot be used"):
        getattr(client, "extract")  # noqa: B009


async def test_a_second_async_provider_needs_only_a_transport() -> None:
    """Catches an async wrapper that only works with the SageMaker transport."""
    transport = _numbered()
    async with _AsyncOtherProvider(transport) as client:
        response = await client.parse.run(input=make_pdf(2))
    assert len(response.result.chunks) == 2
    assert len(transport.bodies) == 2
