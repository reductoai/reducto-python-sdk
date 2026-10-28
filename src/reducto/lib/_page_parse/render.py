from __future__ import annotations

import io
import math
import base64
from typing import TYPE_CHECKING
from typing_extensions import Literal

from ._deps import Image
from .errors import PageError
from .request import page_body

if TYPE_CHECKING:
    from PIL.Image import Image as PILImage

__all__ = ["ENDPOINT_DEFAULT_IMAGE_PIXELS", "PDF_DPI", "capped_size", "encode_page", "pdf_scale"]

ENDPOINT_DEFAULT_IMAGE_PIXELS = 3_145_728
"""The endpoint's documented default image size, in pixels. The SDK sizes every page image to at most this."""

PDF_DPI = 300
"""The highest PDF render resolution, a common scan resolution. It keeps a small page from rendering too large."""

_MEGABYTE = 1024 * 1024
_JPEG_QUALITIES = (90, 80, 70)
_SHRINK_STEP = 0.75
"""Each step scales both sides by this factor when the lowest JPEG quality still does not fit the body limit."""


def pdf_scale(width_pt: float, height_pt: float) -> float:
    """The PDF render scale that fills ENDPOINT_DEFAULT_IMAGE_PIXELS, at most 300 DPI.

    pdfium sizes the bitmap as ceil(points * scale) on each side. When that rounds the area over the
    budget, the scale drops until the longer side loses one pixel, until the bitmap fits.
    """
    scale = PDF_DPI / 72
    if width_pt <= 0 or height_pt <= 0:
        return scale
    scale = min(scale, math.sqrt(ENDPOINT_DEFAULT_IMAGE_PIXELS / (width_pt * height_pt)))
    longer = max(width_pt, height_pt)
    while math.ceil(width_pt * scale) * math.ceil(height_pt * scale) > ENDPOINT_DEFAULT_IMAGE_PIXELS:
        scale = math.nextafter((math.ceil(longer * scale) - 1) / longer, 0.0)
    return scale


def capped_size(width: int, height: int, limit: int = ENDPOINT_DEFAULT_IMAGE_PIXELS) -> tuple[int, int]:
    """The size within `limit` pixels, with the same aspect ratio. Never scales up."""
    if width * height <= limit:
        return width, height
    scale = math.sqrt(limit / float(width * height))
    return max(1, math.floor(width * scale)), max(1, math.floor(height * scale))


def encode_page(image: PILImage, body_limit: int) -> bytes:
    """The request body for one page: PNG, or JPEG at falling quality when the PNG body is over `body_limit`
    bytes. When the lowest JPEG quality is still over the limit, the image is scaled down until it fits."""
    rgb = image if image.mode == "RGB" else image.convert("RGB")
    rgb = _resized(rgb, capped_size(rgb.width, rgb.height))
    body = page_body(_base64(rgb, "PNG"))
    if len(body) <= body_limit:
        return body
    for quality in _JPEG_QUALITIES:
        body = page_body(_base64(rgb, "JPEG", quality=quality))
        if len(body) <= body_limit:
            return body
    while rgb.width > 1 or rgb.height > 1:
        size = max(1, math.floor(rgb.width * _SHRINK_STEP)), max(1, math.floor(rgb.height * _SHRINK_STEP))
        rgb = _resized(rgb, size)
        body = page_body(_base64(rgb, "JPEG", quality=_JPEG_QUALITIES[-1]))
        if len(body) <= body_limit:
            return body
    raise PageError(f"The page does not fit the {body_limit / _MEGABYTE:g} MB request limit.")


def _resized(image: PILImage, size: tuple[int, int]) -> PILImage:
    if size == image.size:
        return image
    return image.resize(size, Image.Resampling.LANCZOS)  # pyright: ignore[reportUnknownMemberType]


def _base64(image: PILImage, image_format: Literal["PNG", "JPEG"], **save_options: int) -> str:
    with io.BytesIO() as buffer:
        try:
            image.save(buffer, format=image_format, **save_options)
        except (OSError, ValueError) as error:
            raise PageError(f"The page cannot be encoded as {image_format}: {error}") from error
        return base64.b64encode(buffer.getvalue()).decode("ascii")
