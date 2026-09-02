# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union, Iterable, Optional
from typing_extensions import Literal, Required, TypeAlias, TypedDict

from .._types import SequenceNotStr
from .shared_params import page_range

__all__ = ["SettingsParam", "HybridVpc", "PageRange", "TenantThrottling"]


class HybridVpc(TypedDict, total=False):
    """Hybrid VPC request-scoped settings."""

    environment: Optional[str]
    """Named Hybrid VPC environment to use for this request.

    Only applies when your organization has Hybrid VPC environments configured.
    """


PageRange: TypeAlias = Union[page_range.PageRange, Iterable[page_range.PageRange], Iterable[int], SequenceNotStr[str]]


class TenantThrottling(TypedDict, total=False):
    """Per-tenant throttling for multi-tenant applications.

    Tag each request with your tenant's id to bound how much of your account's concurrency a single tenant can consume. Account-level throttles still apply.
    """

    tenant_id: Required[str]
    """
    Your identifier for the tenant (customer, workspace, organization) this request
    belongs to. Used only for noisy-neighbor throttling inside your account.
    """

    max_share: float
    """
    Maximum fraction of your account's concurrency ceiling this tenant may use,
    between 0 (exclusive) and 1. Defaults to 0.5.
    """


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

    extract_document_properties: bool
    """If True, return properties embedded in the original document.

    Defaults to False.
    """

    extraction_mode: Literal["ocr", "hybrid"]
    """The text extraction method for legacy Parse.

    OCR uses optical character recognition only. Hybrid combines OCR with embedded
    PDF text. r-1 uses native full-page processing and ignores this setting.
    Defaults to hybrid.
    """

    force_file_extension: Optional[str]
    """Force the URL to be downloaded as a specific file extension (e.g. `.png`)."""

    force_url_result: bool
    """Force the result to be returned in URL form."""

    hybrid_vpc: HybridVpc
    """Hybrid VPC request-scoped settings."""

    model: Optional[Literal["r-1", "legacy"]]
    """The parse model to use.

    'r-1' is the R-1 full-page parse model, which parses each page in a single
    generation. 'legacy' is the previous parsing pipeline. Defaults to 'legacy'
    unless your organization was created on the r-1 plan, in which case it defaults
    to 'r-1'.
    """

    ocr_system: Literal["standard", "legacy"]
    """The OCR system for legacy Parse.

    Standard is the best multilingual OCR system. Legacy supports Germanic languages
    and remains available for backwards compatibility. r-1 uses native full-page
    processing and ignores this setting. Defaults to standard.
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

    tenant_throttling: Optional[TenantThrottling]
    """Per-tenant throttling for multi-tenant applications.

    Tag each request with your tenant's id to bound how much of your account's
    concurrency a single tenant can consume. Account-level throttles still apply.
    """

    timeout: Optional[float]
    """The timeout for the job in seconds."""
