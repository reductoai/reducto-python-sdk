from __future__ import annotations

import io
import os
import math
import struct
import zipfile
import warnings
import threading
import contextlib
from typing import IO, TYPE_CHECKING, Tuple, Union, Iterator, Optional, cast
from pathlib import Path
from typing_extensions import Literal, Protocol, TypeAlias

from ._deps import Image, ImageOps, ImageSequence, JpegImagePlugin, pdfium, pdfium_c, register_heif
from .errors import PageError, UnsupportedOnProviderError
from .render import pdf_scale
from .options import PageSpan
from ..._exceptions import ReductoError
from ..._utils._logs import logger

if TYPE_CHECKING:
    from PIL.Image import Image as PILImage

__all__ = ["MAX_DECODE_PIXELS", "Document", "DocumentInput", "DocumentType", "open_document", "plan_pages", "sniff"]

DocumentInput: TypeAlias = Union[str, "os.PathLike[str]", bytes, bytearray, memoryview, IO[bytes]]
DocumentType: TypeAlias = Literal["pdf", "png", "jpeg", "tiff", "webp", "gif", "bmp", "heic"]

MAX_DECODE_PIXELS = 100_000_000
"""The largest image that the SDK decodes (about 300 MB as RGB). It guards against decompression bombs.
A larger JPEG decodes at 1/2, 1/4, or 1/8 scale."""

_PDF_SEARCH_BYTES = 1024
_MAGIC: tuple[tuple[bytes, DocumentType], ...] = (
    (b"\x89PNG\r\n\x1a\n", "png"),
    (b"\xff\xd8\xff", "jpeg"),
    (b"II*\x00", "tiff"),
    (b"MM\x00*", "tiff"),
    (b"II+\x00", "tiff"),
    (b"MM\x00+", "tiff"),
    (b"GIF87a", "gif"),
    (b"GIF89a", "gif"),
)
_BMP_HEADER_SIZES = frozenset({12, 16, 40, 52, 56, 64, 108, 124})
_HEIF_BRANDS = frozenset({b"heic", b"heix", b"hevc", b"hevx", b"heim", b"heis", b"hevm", b"hevs"})
_IMAGE_ITEM_BRANDS = frozenset({b"mif1", b"msf1"})
_AVIF_BRANDS = frozenset({b"avif", b"avis"})
_OFFICE_FOLDERS = (("word/", "DOCX"), ("xl/", "XLSX"), ("ppt/", "PPTX"))

_PDFIUM_LOCK = threading.Lock()
"""pdfium is not thread-safe: every pdfium call in this SDK holds this lock."""

_JPEG_DRAFT_SCALES = (2, 4, 8)
_WHITE = (255, 255, 255)
_READ_ERRORS = (OSError, SyntaxError, ValueError, struct.error, IndexError, KeyError, EOFError)


class Document(Protocol):
    page_count: int

    def render(self, page: int) -> PILImage:
        """The 1-indexed page as an RGB image. Raises PageError for a page that cannot be read."""
        ...

    def close(self) -> None: ...


def open_document(source: DocumentInput, password: str | None) -> Document:
    """Opens a PDF or an image. Raises UnsupportedOnProviderError for every other file type,
    and ReductoError for a document that cannot be opened."""
    data, suffix = _read(source)
    if not data:
        raise ReductoError("The document is empty.")
    document_type = sniff(data)
    if document_type is None:
        raise UnsupportedOnProviderError(_describe(data, suffix), kind="file_type")
    if document_type == "pdf":
        return PdfPages(data, password)
    return ImageFrames(data, heif=document_type == "heic")


def sniff(data: bytes) -> DocumentType | None:
    """The supported type that the header bytes show, or None. Never guesses from a file name."""
    for magic, document_type in _MAGIC:
        if data.startswith(magic):
            return document_type
    if data.startswith(b"BM") and int.from_bytes(data[14:18], "little") in _BMP_HEADER_SIZES:
        return "bmp"
    if data[:4] == b"RIFF" and data[8:12] == b"WEBP":
        return "webp"
    if _is_heif(data):
        return "heic"
    # pdfium accepts a PDF header anywhere in the first 1 KB.
    if b"%PDF-" in data[:_PDF_SEARCH_BYTES]:
        return "pdf"
    return None


def plan_pages(page_spans: Optional[Tuple[PageSpan, ...]], page_count: int) -> list[int]:
    """The sorted 1-indexed pages to parse, with each range clamped to the document.
    Raises ValueError when no requested page is in the document."""
    if page_spans is None:
        return list(range(1, page_count + 1))
    pages = {
        page
        for start, end in page_spans
        for page in range(max(1, start or 1), min(page_count, page_count if end is None else end) + 1)
    }
    if not pages:
        raise ValueError(
            f"No pages found in the requested range. The document has {page_count} pages; "
            "page_range is 1-indexed and inclusive."
        )
    return sorted(pages)


class _Bitmap(Protocol):
    def to_pil(self) -> PILImage: ...

    def close(self) -> None: ...


class _Page(Protocol):
    def get_size(self) -> tuple[float, float]: ...

    def render(self, *, scale: float, draw_annots: bool, force_bitmap_format: int, rev_byteorder: bool) -> _Bitmap: ...

    def close(self) -> None: ...


class _Pdf(Protocol):
    """The part of pypdfium2's PdfDocument that the SDK calls."""

    def __len__(self) -> int: ...

    def init_forms(self) -> object: ...

    def get_page(self, index: int) -> _Page: ...

    def close(self) -> None: ...


class PdfPages:
    """An open PDF that renders one page at a time under the pdfium lock."""

    def __init__(self, data: bytes, password: str | None) -> None:
        self._closed = False
        with _PDFIUM_LOCK:
            try:
                self._pdf = cast(_Pdf, pdfium.PdfDocument(data, password=password))
            except pdfium.PdfiumError as error:
                raise _pdf_open_error(error, data, password) from error
            try:
                self._pdf.init_forms()
                self.page_count: int = len(self._pdf)
            except pdfium.PdfiumError as error:
                self._pdf.close()
                raise ReductoError(f"The PDF cannot be opened: {error}") from error

    def render(self, page: int) -> PILImage:
        """The 1-indexed page as RGB, with annotations and form fields drawn."""
        with _PDFIUM_LOCK:
            if self._closed:
                raise PageError("The PDF is already closed.")
            try:
                return self._render(page)
            except pdfium.PdfiumError as error:
                raise PageError(f"Page {page} of the PDF cannot be rendered: {error}") from error

    def close(self) -> None:
        with _PDFIUM_LOCK:
            if not self._closed:
                self._closed = True
                self._pdf.close()

    def _render(self, page: int) -> PILImage:
        pdf_page = self._pdf.get_page(page - 1)
        try:
            width, height = pdf_page.get_size()
            bitmap = pdf_page.render(
                scale=pdf_scale(width, height),
                draw_annots=True,
                force_bitmap_format=pdfium_c.FPDFBitmap_BGRA,
                rev_byteorder=True,
            )
            try:
                return bitmap.to_pil().convert("RGB")
            finally:
                bitmap.close()
        finally:
            pdf_page.close()


class ImageFrames:
    """An open image file. Each frame is one page."""

    def __init__(self, data: bytes, *, heif: bool) -> None:
        if heif:
            register_heif()
        self._lock = threading.Lock()
        self._closed = False
        self._image = _open_image(data)
        try:
            with _no_bomb_warning():
                self.page_count: int = 1 if self._image.format == "MPO" else _frame_count(self._image)
        except (Image.DecompressionBombError, *_READ_ERRORS) as error:
            self._image.close()
            raise ReductoError(f"The image cannot be read: {error}") from error

    def render(self, page: int) -> PILImage:
        """The 1-indexed frame, upright and flattened to RGB. The encoder scales a large frame down."""
        with self._lock:
            if self._closed:
                raise PageError("The image is already closed.")
            try:
                with _no_bomb_warning():
                    self._image.seek(page - 1)
                if self._image.width * self._image.height > MAX_DECODE_PIXELS:
                    raise PageError(_too_large_message(f"Frame {page} of the image"))
                return _flatten(_eight_bit(_upright(self._image)))
            except (Image.DecompressionBombError, *_READ_ERRORS) as error:
                raise PageError(f"Frame {page} of the image cannot be read: {error}") from error

    def close(self) -> None:
        with self._lock:
            if not self._closed:
                self._closed = True
                self._image.close()


def _read(source: DocumentInput) -> tuple[bytes, str]:
    if isinstance(source, (bytes, bytearray, memoryview)):
        return bytes(source), ""
    if isinstance(source, str) and "://" in source:
        raise UnsupportedOnProviderError("URL input")
    if isinstance(source, (str, os.PathLike)):
        path = Path(source)
        return path.read_bytes(), path.suffix
    data = cast(object, source.read())
    if not isinstance(data, bytes):
        raise TypeError("A file object input must be opened in binary mode.")
    return data, ""


def _ftyp_brands(data: bytes) -> list[bytes]:
    """The major brand, then the compatible brands, of an ISO media file."""
    if data[4:8] != b"ftyp":
        return []
    end = min(int.from_bytes(data[:4], "big"), 64)
    return [data[8:12], *(data[offset : offset + 4] for offset in range(16, end, 4))]


def _is_heif(data: bytes) -> bool:
    brands = _ftyp_brands(data)
    if not brands:
        return False
    if brands[0] in _HEIF_BRANDS:
        return True
    return brands[0] in _IMAGE_ITEM_BRANDS and not _AVIF_BRANDS.intersection(brands)


def _describe(data: bytes, suffix: str) -> str:
    label = _label(data)
    if label is None and suffix:
        label = suffix.lstrip(".").upper()
    return f"{label} files" if label else "Files of this type"


def _label(data: bytes) -> str | None:
    if data.startswith(b"PK\x03\x04"):
        return _zip_label(data)
    if data.startswith(b"\xd0\xcf\x11\xe0"):
        return "Legacy Microsoft Office"
    if data.startswith(b"{\\rtf"):
        return "RTF"
    if _AVIF_BRANDS.intersection(_ftyp_brands(data)):
        return "AVIF"
    head = data[:_PDF_SEARCH_BYTES].lstrip().lower()
    if head.startswith((b"<!doctype html", b"<html")):
        return "HTML"
    if b"<svg" in head:
        return "SVG"
    return None


def _zip_label(data: bytes) -> str:
    try:
        with zipfile.ZipFile(io.BytesIO(data)) as archive:
            names = archive.namelist()
    except zipfile.BadZipFile:
        return "ZIP"
    for folder, label in _OFFICE_FOLDERS:
        if any(name.startswith(folder) for name in names):
            return label
    return "ZIP"


def _pdf_open_error(error: pdfium.PdfiumError, data: bytes, password: str | None) -> ReductoError:
    # pdfium can leave a stale error code, so a password error also needs an /Encrypt entry.
    err_code = cast("int | None", error.err_code)  # pyright: ignore[reportUnknownMemberType]
    if err_code != pdfium_c.FPDF_ERR_PASSWORD or b"/Encrypt" not in data:
        return ReductoError(f"The PDF cannot be opened: {error}")
    if password is None:
        return ReductoError("The PDF is encrypted. Pass the document password in settings.document_password.")
    return ReductoError("The document password in settings.document_password is wrong.")


def _open_image(data: bytes) -> PILImage:
    """Opens the image, or a JPEG at 1/2, 1/4, or 1/8 scale when it is over MAX_DECODE_PIXELS."""
    try:
        with _no_bomb_warning():
            image = Image.open(io.BytesIO(data))
    except Image.DecompressionBombError:
        return _drafted_jpeg(data)
    except _READ_ERRORS as error:
        raise ReductoError(f"The image cannot be read: {error}") from error
    if image.width * image.height <= MAX_DECODE_PIXELS:
        return image
    image.close()
    return _drafted_jpeg(data)


def _drafted_jpeg(data: bytes) -> PILImage:
    try:
        with _no_bomb_warning():
            image = JpegImagePlugin.JpegImageFile(io.BytesIO(data))
    except _READ_ERRORS as error:
        raise ReductoError(_too_large_message("The image")) from error
    width, height = image.size
    for scale in _JPEG_DRAFT_SCALES:
        if math.ceil(width / scale) * math.ceil(height / scale) <= MAX_DECODE_PIXELS:
            image.draft(None, (width // scale, height // scale))
            break
    if image.width * image.height > MAX_DECODE_PIXELS:
        image.close()
        raise ReductoError(_too_large_message("The image"))
    return image


@contextlib.contextmanager
def _no_bomb_warning() -> Iterator[None]:
    """Silences Pillow's decompression bomb warning. The SDK applies MAX_DECODE_PIXELS right after."""
    with warnings.catch_warnings():
        warnings.simplefilter("ignore", Image.DecompressionBombWarning)
        yield


def _too_large_message(subject: str) -> str:
    return f"{subject} is larger than {MAX_DECODE_PIXELS:,} pixels. Downscale it and retry."


def _frame_count(image: PILImage) -> int:
    return sum(1 for _ in ImageSequence.Iterator(image))


def _upright(image: PILImage) -> PILImage:
    """Applies the EXIF orientation. A broken EXIF block keeps the stored orientation."""
    try:
        return ImageOps.exif_transpose(image)
    except (ZeroDivisionError, *_READ_ERRORS) as error:
        logger.warning("The image EXIF orientation is unreadable, so the stored orientation is used: %s", error)
        return image.copy()


def _eight_bit(image: PILImage) -> PILImage:
    """Stretches a 16-bit grayscale image to 8 bits, so RGB conversion does not clip it to white."""
    if not image.mode.startswith("I"):
        return image
    wide = image.convert("I")
    high = cast(float, wide.getextrema()[1])
    scale = 255 / high if high > 255 else 1.0
    return wide.point(lambda value: value * scale, "L")  # pyright: ignore[reportUnknownMemberType]


def _flatten(image: PILImage) -> PILImage:
    """RGB, with transparent pixels on a white background."""
    if not _has_alpha(image):
        return image.convert("RGB")
    rgba = image.convert("RGBA")
    flat = Image.new("RGB", rgba.size, _WHITE)
    flat.paste(rgba, mask=rgba.getchannel("A"))
    return flat


def _has_alpha(image: PILImage) -> bool:
    return image.mode in ("RGBA", "LA", "PA") or (image.mode == "P" and "transparency" in image.info)
