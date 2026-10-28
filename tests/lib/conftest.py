from __future__ import annotations

import pytest


@pytest.fixture(autouse=True)
def no_backoff(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setattr("reducto.lib._page_parse.runner.backoff_seconds", _no_delay)


def _no_delay(_retry: int) -> float:
    return 0.0
