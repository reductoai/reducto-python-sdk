from __future__ import annotations

import json

__all__ = ["page_body"]


def page_body(image_b64: str) -> bytes:
    """The page-parse body for one page image (base64 PNG or JPEG): exactly `{"image_b64": ...}`."""
    return json.dumps({"image_b64": image_b64}, separators=(",", ":")).encode()
