# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union, Iterable, Optional
from typing_extensions import Literal, TypeAlias, TypedDict

from .._types import SequenceNotStr
from .shared_params import page_range

__all__ = ["SettingsParam", "HybridVpc", "PageRange"]


class HybridVpc(TypedDict, total=False):
    """Hybrid VPC request-scoped settings."""

    environment: Optional[str]
    """Named Hybrid VPC environment to use for this request.

    Only applies when your organization has Hybrid VPC environments configured.
    """


PageRange: TypeAlias = Union[page_range.PageRange, Iterable[page_range.PageRange], Iterable[int], SequenceNotStr[str]]


class SettingsParam(TypedDict, total=False):
    document_password: Optional[str]
    """Password to decrypt password-protected documents."""

    embed_pdf_metadata: bool
    """If True, embed OCR metadata into the returned PDF. Defaults to False."""

    embed_pdf_metadata_dpi: int
    """
    Render DPI used when rasterizing the source PDF before embedding the OCR text
    layer (only applies when `embed_pdf_metadata` is True). Lower values produce
    dramatically smaller output PDFs; higher values preserve more detail when zoomed
    past 200%. Defaults to 100 (good for on-screen viewing); raise toward the source
    scan DPI for crisper output. Min 50, max 250.
    """

    extraction_mode: Literal["ocr", "hybrid"]
    """The mode to use for text extraction from PDFs.

    OCR mode uses optical character recognition only. Hybrid mode combines OCR with
    embedded PDF text for best accuracy (default).
    """

    force_file_extension: Optional[str]
    """Force the URL to be downloaded as a specific file extension (e.g. `.png`)."""

    force_url_result: bool
    """Force the result to be returned in URL form."""

    hybrid_vpc: HybridVpc
    """Hybrid VPC request-scoped settings."""

    ocr_system: Literal["standard", "legacy"]
    """Standard is our best multilingual OCR system.

    Legacy only supports germanic languages and is available for backwards
    compatibility.
    """

    page_range: Optional[PageRange]
    """The page range to process (1-indexed).

    By default, the entire document is processed. For spreadsheets, you can also
    provide a list of sheet names.
    """

    persist_results: bool
    """If True, persist the results indefinitely. Defaults to False."""

    return_images: List[Literal["figure", "table", "page"]]
    """Whether to return images for the specified block types.

    'page' returns full page images. By default, no images are returned.
    """

    return_ocr_data: bool
    """If True, return OCR data in the result. Defaults to False."""

    timeout: Optional[float]
    """The timeout for the job in seconds."""
