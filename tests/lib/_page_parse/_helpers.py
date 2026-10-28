from __future__ import annotations

import io
import json
import struct
import hashlib
import threading
from typing import Callable, Iterable, Optional, Sequence

import pypdfium2 as pdfium  # pyright: ignore[reportMissingTypeStubs]
from PIL import Image

from reducto.lib._page_parse.transport import CANNOT_PROCESS_DETAIL, EndpointReply, EndpointOutcome

Block = tuple[str, str]
"""A block type and its content. The helpers give each block a box on the page."""

TITLE_PAGE: Sequence[Block] = (("Title", "Annual Report"), ("Text", "Revenue grew."))


def blocks_answer(blocks: Sequence[Block] = TITLE_PAGE, usage: Optional[dict[str, int]] = None) -> bytes:
    """A page-parse answer in the public blocks shape. Each block sits in its own band of the page."""
    count = max(len(blocks), 1)
    answer: dict[str, object] = {
        "blocks": [
            {
                "type": block_type,
                "bbox": {"left": 0.1, "top": row / count, "width": 0.8, "height": 0.5 / count},
                "content": content,
            }
            for row, (block_type, content) in enumerate(blocks)
        ]
    }
    if usage is not None:
        answer["usage"] = usage
    return json.dumps(answer).encode()


def reply(blocks: Sequence[Block] = TITLE_PAGE) -> EndpointReply:
    return EndpointReply(200, blocks_answer(blocks))


def titled(page: int) -> EndpointReply:
    return reply((("Title", f"Page {page}"),))


def error_reply(status: int, detail: str = "server error") -> EndpointReply:
    return EndpointReply(status, json.dumps({"detail": detail}).encode())


CANNOT_PROCESS = error_reply(422, CANNOT_PROCESS_DETAIL)


def make_pdf(page_count: int, size: tuple[float, float] = (72, 72)) -> bytes:
    """A PDF of blank pages. The default page is 1 inch square."""
    document = pdfium.PdfDocument.new()
    for _ in range(page_count):
        document.new_page(*size)  # pyright: ignore[reportUnknownMemberType]
    buffer = io.BytesIO()
    document.save(buffer)  # pyright: ignore[reportUnknownMemberType]
    document.close()
    return buffer.getvalue()


_PASSWORD_PAD = bytes.fromhex("28BF4E5E4E758A4164004E56FFFA01082E2E00B6D0683E802F0CA9FE6453697A")


def _rc4(key: bytes, data: bytes) -> bytes:
    state = list(range(256))
    j = 0
    for i in range(256):
        j = (j + state[i] + key[i % len(key)]) % 256
        state[i], state[j] = state[j], state[i]
    i = j = 0
    out = bytearray()
    for byte in data:
        i = (i + 1) % 256
        j = (j + state[i]) % 256
        state[i], state[j] = state[j], state[i]
        out.append(byte ^ state[(state[i] + state[j]) % 256])
    return bytes(out)


def encrypted_pdf(password: str) -> bytes:
    """A one-page PDF locked with `password` (standard security handler, revision 2).
    It has no strings or streams to encrypt, so only the password entries are computed."""
    padded = (password.encode("latin-1") + _PASSWORD_PAD)[:32]
    owner = _rc4(hashlib.md5(padded).digest()[:5], padded)
    file_id = b"synthetic-pdf-id"
    permissions = -4
    key = hashlib.md5(padded + owner + struct.pack("<i", permissions) + file_id).digest()[:5]
    user = _rc4(key, _PASSWORD_PAD)
    objects = [
        b"<< /Type /Catalog /Pages 2 0 R >>",
        b"<< /Type /Pages /Kids [3 0 R] /Count 1 >>",
        b"<< /Type /Page /Parent 2 0 R /MediaBox [0 0 72 72] >>",
        b"<< /Filter /Standard /V 1 /R 2 /O <%s> /U <%s> /P %d >>"
        % (owner.hex().encode(), user.hex().encode(), permissions),
    ]
    out = bytearray(b"%PDF-1.4\n")
    offsets: list[int] = []
    for number, body in enumerate(objects, start=1):
        offsets.append(len(out))
        out += b"%d 0 obj\n%s\nendobj\n" % (number, body)
    xref = len(out)
    out += b"xref\n0 %d\n0000000000 65535 f \n" % (len(objects) + 1)
    out += b"".join(b"%010d 00000 n \n" % offset for offset in offsets)
    hex_id = file_id.hex().encode()
    out += b"trailer\n<< /Size %d /Root 1 0 R /Encrypt 4 0 R /ID [<%s> <%s>] >>\n" % (len(objects) + 1, hex_id, hex_id)
    out += b"startxref\n%d\n%%%%EOF\n" % xref
    return bytes(out)


def image_bytes(image: Image.Image, image_format: str, **options: object) -> bytes:
    buffer = io.BytesIO()
    image.save(buffer, format=image_format, **options)
    return buffer.getvalue()


BODY_LIMIT = 8 * 1024 * 1024
"""The request body limit of the fake endpoint."""


class FakeTransport:
    """Replays outcomes per call and records the peak number of calls in flight."""

    body_limit = BODY_LIMIT

    def __init__(self, outcomes: Callable[[int], EndpointOutcome], barrier: threading.Barrier | None = None) -> None:
        self._outcomes = outcomes
        self._barrier = barrier
        self._lock = threading.Lock()
        self.bodies: list[bytes] = []
        self.in_flight = 0
        self.peak = 0

    def send(self, body: bytes) -> EndpointOutcome:
        with self._lock:
            call = len(self.bodies)
            self.bodies.append(body)
            self.in_flight += 1
            self.peak = max(self.peak, self.in_flight)
        try:
            if self._barrier is not None:
                self._barrier.wait()
            return self._outcomes(call)
        finally:
            with self._lock:
                self.in_flight -= 1


def replay(outcomes: Iterable[EndpointOutcome]) -> Callable[[int], EndpointOutcome]:
    """Returns the outcomes in call order."""
    remaining = list(outcomes)
    return lambda call: remaining[call]


def always(outcome: EndpointOutcome) -> FakeTransport:
    return FakeTransport(lambda _call: outcome)
