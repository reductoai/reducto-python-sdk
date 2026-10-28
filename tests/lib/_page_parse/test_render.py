from __future__ import annotations

import io
import json
import base64
import random

import pytest
from PIL import Image, ImageDraw

from reducto.lib._page_parse.errors import PageError
from reducto.lib._page_parse.render import ENDPOINT_DEFAULT_IMAGE_PIXELS, encode_page

from ._helpers import BODY_LIMIT


def _sent(body: bytes) -> tuple[dict[str, object], Image.Image]:
    payload = json.loads(body)
    return payload, Image.open(io.BytesIO(base64.b64decode(payload["image_b64"])))


def _noise(width: int, height: int) -> Image.Image:
    return Image.frombytes("RGB", (width, height), random.Random(0).randbytes(width * height * 3))


def test_default_body_holds_only_the_image() -> None:
    """Catches any field other than the page image sent in the request."""
    payload, _ = _sent(encode_page(Image.new("RGB", (10, 10)), BODY_LIMIT))
    assert list(payload) == ["image_b64"]


def test_small_image_is_sent_untouched() -> None:
    """Catches an upscale or a re-sample of an image that is already under the endpoint's image size."""
    original = _noise(300, 200)
    _, image = _sent(encode_page(original, BODY_LIMIT))
    assert image.format == "PNG"
    assert image.size == (300, 200)
    assert image.convert("RGB").tobytes() == original.tobytes()


def test_large_image_is_scaled_to_the_endpoint_image_size() -> None:
    """Catches a large photo sent over the endpoint's documented default image size,
    or one sent with a changed aspect ratio."""
    _, image = _sent(encode_page(Image.new("RGB", (4_000, 3_000), "white"), BODY_LIMIT))
    pixels = image.width * image.height
    assert ENDPOINT_DEFAULT_IMAGE_PIXELS * 0.99 <= pixels <= ENDPOINT_DEFAULT_IMAGE_PIXELS
    assert abs(image.width / image.height - 4 / 3) < 0.01


def test_text_page_at_the_full_image_size_goes_out_as_png() -> None:
    """Catches a normal text page sent as lossy JPEG, which blurs small print."""
    page = Image.new("RGB", (1536, 2048), "white")
    draw = ImageDraw.Draw(page)
    for line in range(80):
        draw.text((100, 50 + line * 24), f"Line {line}: The quick brown fox jumps over the lazy dog.", fill="black")
    _, image = _sent(encode_page(page, BODY_LIMIT))
    assert image.format == "PNG"
    assert image.size == (1536, 2048)


def test_body_over_the_limit_falls_back_to_jpeg() -> None:
    """Catches a noisy photo page whose PNG body is over the 6 MB request limit."""
    body = encode_page(_noise(2048, 1536), BODY_LIMIT)
    _, image = _sent(body)
    assert image.format == "JPEG"
    assert image.size == (2048, 1536)
    assert len(body) <= BODY_LIMIT


def test_page_still_over_the_limit_as_jpeg_is_scaled_down() -> None:
    """Catches a page that fails when a smaller JPEG would fit the request limit."""
    body = encode_page(_noise(256, 256), 30_000)
    _, image = _sent(body)
    assert len(body) <= 30_000
    assert image.format == "JPEG"
    assert image.width < 256 and image.width == image.height


def test_page_that_never_fits_raises() -> None:
    """Catches a body over the limit sent anyway, which the endpoint refuses."""
    with pytest.raises(PageError, match="request limit"):
        encode_page(Image.new("RGB", (64, 64), "white"), 100)
