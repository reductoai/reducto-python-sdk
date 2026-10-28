from __future__ import annotations

from typing import Tuple, Mapping, Optional, cast
from dataclasses import dataclass
from typing_extensions import TypeAlias

from .errors import UnsupportedOnProviderError
from ..._utils import is_given, is_mapping

__all__ = ["PageSpan", "ParseOptions", "is_int"]

PageSpan: TypeAlias = Tuple[Optional[int], Optional[int]]
"""A 1-indexed, inclusive page range. None is an open end."""

_ALLOWED = frozenset({("settings", "page_range"), ("settings", "document_password")})


@dataclass(frozen=True)
class ParseOptions:
    page_spans: Optional[Tuple[PageSpan, ...]] = None
    """The requested pages as ranges, or None for every page."""

    document_password: Optional[str] = None

    @classmethod
    def from_run_kwargs(cls, groups: Mapping[str, object]) -> ParseOptions:
        """Reads the `parse.run` option groups, such as `settings`. Raises for every option that is not allowed,
        and for a page_range of the wrong shape, before the document is read."""
        for name, value in groups.items():
            if _given(value) is None:
                continue
            if not is_mapping(value):
                raise TypeError(f"`{name}` must be a mapping of options.")
            _check(value, (name,))
        settings = groups.get("settings")
        if not is_mapping(settings):
            return cls()
        password = _given(settings.get("document_password"))
        if password is not None and not isinstance(password, str):
            raise TypeError("settings.document_password must be a string.")
        page_range = _given(settings.get("page_range"))
        return cls(page_spans=None if page_range is None else _page_spans(page_range), document_password=password)


def is_int(value: object) -> bool:
    return isinstance(value, int) and not isinstance(value, bool)


def _check(options: Mapping[str, object], parent: tuple[str, ...]) -> None:
    """Raises for the first option under `parent` that is given and not on the allowlist."""
    for name, value in options.items():
        path = (*parent, name)
        if _given(value) is None or path in _ALLOWED:
            continue
        if is_mapping(value):
            _check(value, path)
        else:
            raise UnsupportedOnProviderError(f"The `{'.'.join(path)}` option")


def _given(value: object) -> object:
    """The value, or None when it is None, `omit`, or `NOT_GIVEN`."""
    return value if is_given(value) else None


def _page_spans(page_range: object) -> Tuple[PageSpan, ...]:
    """Checks the shape of page_range: a range, or a list of ranges or of page numbers."""
    if isinstance(page_range, (int, str)):
        raise ValueError(
            "page_range must be a page range, or a list of them or of page numbers. Wrap one page in a list."
        )
    if is_mapping(page_range):
        return (_span(page_range, open_ends=True),)
    try:
        items = list(cast("list[object]", page_range))
    except TypeError as error:
        raise ValueError("page_range must be a page range, or a list of them or of page numbers.") from error
    if not items:
        raise ValueError("page_range cannot be an empty list.")
    if all(is_mapping(item) for item in items):
        return tuple(_span(cast("Mapping[str, object]", item), open_ends=False) for item in items)
    if all(is_int(item) for item in items):
        return tuple((cast(int, item), cast(int, item)) for item in items)
    if all(isinstance(item, str) for item in items):
        raise ValueError("String page ranges are only supported for spreadsheet documents.")
    raise ValueError("page_range must hold only page ranges, only ints, or only strings.")


def _span(page_range: Mapping[str, object], *, open_ends: bool) -> PageSpan:
    """One range. Only a lone range can leave out its start or end."""
    return _bound(page_range, "start", open_ends), _bound(page_range, "end", open_ends)


def _bound(page_range: Mapping[str, object], key: str, open_ends: bool) -> Optional[int]:
    value = page_range.get(key)
    if value is None and open_ends:
        return None
    if not is_int(value):
        where = "page_range" if open_ends else "Each page range in a list"
        raise ValueError(f"{where} needs an integer {key}.")
    return cast(int, value)
