# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union, Optional
from typing_extensions import Literal, TypeAlias

from . import page_range
from ..._models import BaseModel

__all__ = ["Settings", "PageRange"]

PageRange: TypeAlias = Union[page_range.PageRange, List[page_range.PageRange], List[int], None]


class Settings(BaseModel):
    document_password: Optional[str] = None
    """Password to decrypt password-protected documents."""

    embed_pdf_metadata: Optional[bool] = None
    """If True, embed OCR metadata into the returned PDF. Defaults to False."""

    force_file_extension: Optional[str] = None
    """Force the URL to be downloaded as a specific file extension (e.g. `.png`)."""

    force_url_result: Optional[bool] = None
    """Force the result to be returned in URL form."""

    ocr_system: Optional[Literal["standard", "legacy"]] = None
    """Standard is our best multilingual OCR system.

    Legacy only supports germanic languages and is available for backwards
    compatibility.
    """

    page_range: Optional[PageRange] = None
    """The page range to process (1-indexed).

    By default, the entire document is processed.
    """

    persist_results: Optional[bool] = None
    """If True, persist the results indefinitely. Defaults to False."""

    return_images: Optional[List[Literal["figure", "table"]]] = None
    """Whether to return images for the specified block types.

    By default, no images are returned.
    """

    return_ocr_data: Optional[bool] = None
    """If True, return OCR data in the result. Defaults to False."""

    timeout: Optional[float] = None
    """The timeout for the job in seconds."""
