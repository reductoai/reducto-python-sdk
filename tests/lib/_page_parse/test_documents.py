from __future__ import annotations

import io
import zipfile
import warnings
from pathlib import Path

import pytest
from PIL import Image

from reducto import ReductoError, UnsupportedOnProviderError
from reducto.lib._page_parse.errors import PageError
from reducto.lib._page_parse.render import ENDPOINT_DEFAULT_IMAGE_PIXELS
from reducto.lib._page_parse.runner import parse_pages
from reducto.lib._page_parse.options import ParseOptions
from reducto.lib._page_parse.documents import sniff, plan_pages, open_document

from ._helpers import reply, always, make_pdf, image_bytes, encrypted_pdf

HEIC_PHOTO = Path(__file__).parents[2] / "fixtures" / "sagemaker" / "photo.heic"


def _docx() -> bytes:
    buffer = io.BytesIO()
    with zipfile.ZipFile(buffer, "w") as archive:
        archive.writestr("[Content_Types].xml", "<Types/>")
        archive.writestr("word/document.xml", "<document/>")
    return buffer.getvalue()


def _render(data: bytes, page: int = 1, password: str | None = None) -> Image.Image:
    document = open_document(data, password)
    try:
        return document.render(page)
    finally:
        document.close()


@pytest.mark.parametrize(
    ("image_format", "expected"),
    [("PNG", "png"), ("JPEG", "jpeg"), ("TIFF", "tiff"), ("WEBP", "webp"), ("GIF", "gif"), ("BMP", "bmp")],
)
def test_sniff_reads_each_image_header(image_format: str, expected: str) -> None:
    """Catches a supported image type that the sniffer rejects."""
    assert sniff(image_bytes(Image.new("RGB", (8, 8)), image_format)) == expected


def test_sniff_finds_pdf_header_after_leading_bytes() -> None:
    """Catches a PDF with junk before %PDF that pdfium opens but the sniffer rejects."""
    assert sniff(b"\r\n garbage" + make_pdf(1)) == "pdf"


def test_sniff_reads_heic_brand() -> None:
    """Catches a phone HEIC photo that the sniffer rejects."""
    assert sniff(b"\x00\x00\x00\x1cftypheic\x00\x00\x00\x00mif1heic") == "heic"


@pytest.mark.parametrize("data", [b"plain text", b"BM is not a bitmap header", b"<svg></svg>"])
def test_sniff_never_defaults_to_pdf(data: bytes) -> None:
    """Catches an unknown file sent to pdfium as a PDF, which fails late with a confusing error."""
    assert sniff(data) is None


def test_docx_raises_unsupported_with_type_and_hosted_hint() -> None:
    """Catches an Office file that fails late, or an error that does not name the way out."""
    with pytest.raises(UnsupportedOnProviderError) as raised:
        open_document(_docx(), None)
    message = str(raised.value)
    assert message == (
        "DOCX files are not supported when you call your own r-1 endpoint. The hosted Reducto API parses them."
    )


def test_unknown_file_is_named_by_its_suffix(tmp_path: Path) -> None:
    """Catches an error message that does not say which file type was rejected."""
    path = tmp_path / "notes.txt"
    path.write_text("hello")
    with pytest.raises(
        UnsupportedOnProviderError, match="^TXT files are not supported .* The hosted Reducto API parses them."
    ):
        open_document(path, None)


def test_url_input_raises_unsupported() -> None:
    """Catches a URL read as a local path, which fails with a confusing file-not-found error."""
    with pytest.raises(UnsupportedOnProviderError, match="URL input"):
        open_document("https://example.com/a.pdf", None)


def test_avif_is_rejected_by_name() -> None:
    """Catches an AVIF file sniffed as HEIC because both use the mif1 brand."""
    avif = b"\x00\x00\x00\x1cftypmif1\x00\x00\x00\x00mif1avifmiaf" + b"\x00" * 16
    assert sniff(avif) is None
    with pytest.raises(UnsupportedOnProviderError, match="^AVIF files are not supported"):
        open_document(avif, None)


def test_input_shapes_open_the_same_pdf(tmp_path: Path) -> None:
    """Catches an input form (path, PathLike, bytes, file object) that the SDK cannot read."""
    data = make_pdf(2)
    path = tmp_path / "doc.pdf"
    path.write_bytes(data)
    for source in (str(path), path, data, io.BytesIO(data)):
        document = open_document(source, None)
        assert document.page_count == 2
        document.close()


def test_empty_input_raises() -> None:
    """Catches an empty upload sent to pdfium, which fails with a confusing error."""
    with pytest.raises(ReductoError, match="empty"):
        open_document(b"", None)


@pytest.mark.parametrize(("password", "message"), [(None, "is encrypted"), ("wrong", "is wrong")])
def test_bad_password_raises_clear_error(password: str | None, message: str) -> None:
    """Catches a missing or wrong password that surfaces as a generic pdfium error."""
    with pytest.raises(ReductoError, match=message):
        open_document(encrypted_pdf("secret"), password)


def test_right_password_renders_the_page() -> None:
    """Catches settings.document_password that never reaches pdfium."""
    assert _render(encrypted_pdf("secret"), password="secret").mode == "RGB"


def test_corrupt_pdf_raises_a_read_error() -> None:
    """Catches a corrupt PDF that escapes as a raw pdfium exception."""
    with pytest.raises(ReductoError, match="cannot be opened"):
        open_document(b"%PDF-1.7 not really a pdf", None)


def test_zero_page_pdf_raises() -> None:
    """Catches an empty PDF that reports success with no pages."""
    with pytest.raises(ReductoError):
        parse_pages(make_pdf(0), always(reply()))


@pytest.mark.parametrize(
    "size", [(612, 792), (1224, 612), (300, 900), (3000, 3000)], ids=["letter", "wide-2-1", "tall-1-3", "poster"]
)
def test_pdf_page_renders_just_under_the_endpoint_image_size(size: tuple[float, float]) -> None:
    """Catches a render over the endpoint's documented default image size, or one far under it,
    which loses small print."""
    image = _render(make_pdf(1, size))
    assert ENDPOINT_DEFAULT_IMAGE_PIXELS * 0.99 <= image.width * image.height <= ENDPOINT_DEFAULT_IMAGE_PIXELS


def test_small_pdf_page_renders_at_300_dpi_and_no_larger() -> None:
    """Catches a 3 x 5 inch receipt scaled up to fill the image size, which wastes upload and adds blur."""
    width, height = _render(make_pdf(1, (216, 360))).size
    assert abs(width - 900) <= 1 and abs(height - 1500) <= 1


def test_multi_frame_tiff_gives_one_page_per_frame() -> None:
    """Catches a multi-page TIFF parsed as its first frame only."""
    frames = [Image.new("RGB", (10 + index, 10), color) for index, color in enumerate(["red", "green", "blue"])]
    data = image_bytes(frames[0], "TIFF", save_all=True, append_images=frames[1:])
    document = open_document(data, None)
    try:
        assert document.page_count == 3
        third = document.render(3)
        assert third.size == (12, 10)
        assert third.getpixel((0, 0)) == (0, 0, 255)
    finally:
        document.close()


def test_exif_orientation_is_applied() -> None:
    """Catches a rotated phone photo sent sideways to the endpoint."""
    exif = Image.Exif()
    exif[0x0112] = 6
    assert _render(image_bytes(Image.new("RGB", (40, 20)), "JPEG", exif=exif)).size == (20, 40)


def test_transparent_pixels_are_flattened_on_white() -> None:
    """Catches alpha dropped to black, which hides black text on a transparent PNG."""
    image = Image.new("RGBA", (20, 20), (0, 0, 0, 0))
    image.paste(Image.new("RGBA", (10, 10), (0, 0, 0, 255)), (5, 5))
    page = _render(image_bytes(image, "PNG"))
    assert page.getpixel((0, 0)) == (255, 255, 255)
    assert page.getpixel((10, 10)) == (0, 0, 0)


@pytest.fixture
def small_decode_limit(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setattr("reducto.lib._page_parse.documents.MAX_DECODE_PIXELS", 1_000_000)


@pytest.mark.usefixtures("small_decode_limit")
def test_jpeg_over_the_decode_limit_decodes_at_reduced_scale() -> None:
    """Catches a huge scan rejected, or decoded at full size into memory."""
    data = image_bytes(Image.new("L", (2_000, 1_000), 200), "JPEG")
    assert _render(data).size == (1_000, 500)


@pytest.mark.usefixtures("small_decode_limit")
def test_png_over_the_decode_limit_is_rejected() -> None:
    """Catches a decompression bomb that the SDK tries to decode."""
    data = image_bytes(Image.new("1", (2_000, 1_000)), "PNG")
    with pytest.raises(ReductoError, match="larger than 1,000,000 pixels"):
        open_document(data, None)


@pytest.mark.usefixtures("small_decode_limit")
def test_oversized_tiff_frame_fails_only_that_page() -> None:
    """Catches a huge later frame decoded in full because only the first frame was checked."""
    frames = [Image.new("1", (8, 8)), Image.new("1", (2_000, 1_000))]
    data = image_bytes(frames[0], "TIFF", save_all=True, append_images=frames[1:])
    document = open_document(data, None)
    try:
        assert document.render(1).size == (8, 8)
        with pytest.raises(PageError, match="Frame 2 of the image is larger"):
            document.render(2)
    finally:
        document.close()


def test_12_bit_scan_keeps_its_full_range() -> None:
    """Catches a 12-bit scan clipped to white."""
    image = Image.new("I;16", (3, 1))
    for x, value in enumerate([0, 2048, 4095]):
        image.putpixel((x, 0), value)
    page = _render(image_bytes(image, "PNG"))
    assert [page.getpixel((x, 0)) for x in range(3)] == [(0, 0, 0), (127, 127, 127), (255, 255, 255)]


def test_gif_frame_that_grows_the_canvas_past_the_limit_raises_a_read_error() -> None:
    """Catches Pillow's DecompressionBombError raised raw from a crafted GIF instead of a ReductoError."""
    frames = [Image.new("P", (8, 8), 0), Image.new("P", (8, 8), 1)]
    for frame in frames:
        frame.putpalette([0, 0, 0, 255, 255, 255] + [0] * 762)
    data = bytearray(image_bytes(frames[0], "GIF", save_all=True, append_images=frames[1:], optimize=False, disposal=1))
    descriptor = max(index for index in range(13, len(data) - 9) if data[index] == 0x2C)
    data[descriptor + 1 : descriptor + 5] = (20_000).to_bytes(2, "little") * 2
    with pytest.raises(ReductoError, match="cannot be read"):
        open_document(bytes(data), None)


def test_truncated_jpeg_fails_its_page() -> None:
    """Catches a cut-off upload that escapes as a raw Pillow OSError."""
    data = image_bytes(Image.effect_noise((64, 64), 50).convert("RGB"), "JPEG")
    with pytest.raises(PageError, match="Frame 1 of the image cannot be read"):
        _render(data[: len(data) // 2])


def test_render_after_close_raises_instead_of_crashing() -> None:
    """Catches a late worker that calls pdfium on a closed document, which crashes the process."""
    document = open_document(make_pdf(1), None)
    document.close()
    document.close()
    with pytest.raises(PageError, match="closed"):
        document.render(1)


def test_heic_photo_opens() -> None:
    """Catches a HEIC photo that sniffs but cannot be decoded, because the SDK never registers its opener."""
    assert _render(HEIC_PHOTO.read_bytes()).mode == "RGB"


def _plan(page_range: object, page_count: int = 5) -> list[int]:
    spans = ParseOptions.from_run_kwargs({"settings": {"page_range": page_range}}).page_spans
    return plan_pages(spans, page_count)


@pytest.mark.parametrize(
    ("page_range", "expected"),
    [
        (None, [1, 2, 3, 4, 5]),
        ({"start": 2, "end": 4}, [2, 3, 4]),
        ({"start": 4}, [4, 5]),
        ({"end": 2}, [1, 2]),
        ({"start": 3, "end": 99}, [3, 4, 5]),
        ([{"start": 4, "end": 5}, {"start": 1, "end": 1}], [1, 4, 5]),
        ([5, 1, 1, 9], [1, 5]),
    ],
    ids=["all", "range", "open-end", "open-start", "clamped", "range-list", "ints"],
)
def test_page_range_plans_the_right_pages(page_range: object, expected: list[int]) -> None:
    """Catches a page_range that plans the wrong pages, pages out of order, or pages past the end."""
    assert _plan(page_range) == expected


@pytest.mark.parametrize("page_range", [{"start": 9, "end": 12}, [0, 6]], ids=["past-the-end", "no-valid-int"])
def test_page_range_with_no_page_in_the_document_raises(page_range: object) -> None:
    """Catches a parse that silently returns no pages."""
    with pytest.raises(ValueError, match="No pages found"):
        _plan(page_range)


@pytest.mark.parametrize("header", [b"II+\x00", b"MM\x00+"], ids=["little-endian", "big-endian"])
def test_sniff_reads_bigtiff(header: bytes) -> None:
    """Catches a BigTIFF scan rejected as an unsupported file type."""
    assert sniff(header + b"\x08\x00\x00\x00" + b"\x00" * 16) == "tiff"


@pytest.mark.parametrize("wrap", [bytearray, memoryview], ids=["bytearray", "memoryview"])
def test_byte_buffer_inputs_open(wrap: type) -> None:
    """Catches a bytearray or memoryview input rejected or read as a file path."""
    document = open_document(wrap(make_pdf(2)), None)
    try:
        assert document.page_count == 2
    finally:
        document.close()


def test_image_between_pillow_warning_and_sdk_limit_opens_with_warnings_as_errors(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    """Catches Pillow's DecompressionBombWarning escaping raw, under -W error, for an image the SDK accepts."""
    monkeypatch.setattr(Image, "MAX_IMAGE_PIXELS", 1_000)
    monkeypatch.setattr("reducto.lib._page_parse.documents.MAX_DECODE_PIXELS", 1_900)
    data = image_bytes(Image.new("RGB", (40, 40), "white"), "PNG")
    with warnings.catch_warnings():
        warnings.simplefilter("error")
        assert _render(data).size == (40, 40)
