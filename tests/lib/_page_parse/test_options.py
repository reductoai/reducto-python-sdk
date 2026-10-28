from __future__ import annotations

import pytest

from reducto import UnsupportedOnProviderError
from reducto._types import omit, not_given
from reducto.lib._page_parse.options import ParseOptions


def test_allowed_options_are_read() -> None:
    """Catches page_range or document_password dropped on the way to the runner."""
    options = ParseOptions.from_run_kwargs(
        {
            "settings": {"page_range": {"start": 2}, "document_password": "secret", "timeout": omit},
            "formatting": {},
            "enhance": omit,
            "spreadsheet": not_given,
        }
    )
    assert options == ParseOptions(page_spans=((2, None),), document_password="secret")


@pytest.mark.parametrize(
    ("options", "named"),
    [
        ({"enhance": {"agentic": []}}, "`enhance.agentic`"),
        ({"settings": {"return_images": ["figure"]}}, "`settings.return_images`"),
        ({"settings": {"model": "r-1"}}, "`settings.model`"),
        ({"settings": {"hybrid_vpc": {"environment": "eu"}}}, "`settings.hybrid_vpc.environment`"),
        ({"formatting": {"add_page_markers": False}}, "`formatting.add_page_markers`"),
        ({"formatting": {"table_output_format": "html"}}, "`formatting.table_output_format`"),
        ({"retrieval": {"chunking": {"chunk_mode": "page"}}}, "`retrieval.chunking.chunk_mode`"),
        ({"spreadsheet": {"split_large_tables": {"enabled": True}}}, "`spreadsheet.split_large_tables.enabled`"),
        ({"settings": {"unknown_option": 1}}, "`settings.unknown_option`"),
    ],
)
def test_option_off_the_allowlist_raises_and_names_it(options: dict[str, object], named: str) -> None:
    """Catches an option that the client cannot honor and silently ignores."""
    with pytest.raises(UnsupportedOnProviderError, match="cannot be used") as raised:
        ParseOptions.from_run_kwargs(options)
    assert named in str(raised.value)


def test_non_string_password_raises() -> None:
    """Catches a password of the wrong type that reaches pdfium."""
    with pytest.raises(TypeError):
        ParseOptions.from_run_kwargs({"settings": {"document_password": 1234}})


def test_non_mapping_group_raises() -> None:
    """Catches `settings="..."` read as no settings, which silently drops the caller's options."""
    with pytest.raises(TypeError, match="`settings` must be a mapping"):
        ParseOptions.from_run_kwargs({"settings": "page_range=1"})


def test_omitted_settings_are_not_given() -> None:
    """Catches `omit` passed on to pdfium as the password or read as a page range."""
    assert ParseOptions.from_run_kwargs({"settings": {"document_password": omit, "page_range": omit}}) == ParseOptions()


def _spans(page_range: object) -> object:
    return ParseOptions.from_run_kwargs({"settings": {"page_range": page_range}}).page_spans


@pytest.mark.parametrize(
    ("page_range", "spans"),
    [
        ({"start": 2, "end": 4}, ((2, 4),)),
        ({"end": 2}, ((None, 2),)),
        ([{"start": 4, "end": 5}, {"start": 1, "end": 1}], ((4, 5), (1, 1))),
        ([5, 1], ((5, 5), (1, 1))),
        ((page for page in [3]), ((3, 3),)),
    ],
    ids=["range", "open-start", "range-list", "ints", "iterable"],
)
def test_page_range_shapes_are_read(page_range: object, spans: object) -> None:
    """Catches a valid page_range shape (a range, a list of ranges or ints, any iterable) that is rejected."""
    assert _spans(page_range) == spans


@pytest.mark.parametrize(
    ("page_range", "message"),
    [
        ([], "empty list"),
        (["Sheet1"], "only supported for spreadsheet"),
        ([{"start": 1}, {"start": 3, "end": 4}], "integer end"),
        (3, "Wrap one page in a list"),
        ("1-3", "Wrap one page in a list"),
        ({"start": "2"}, "^page_range needs an integer start"),
        ([1, {"start": 2, "end": 3}], "only page ranges, only ints"),
        (1.5, "must be a page range"),
    ],
    ids=["empty-list", "strings", "half-open-in-list", "bare-int", "string", "string-start", "mixed", "float"],
)
def test_bad_page_range_shape_raises_before_the_document_is_read(page_range: object, message: str) -> None:
    """Catches a bad page_range found only after the document is read, or read as some other range."""
    with pytest.raises(ValueError, match=message):
        _spans(page_range)
