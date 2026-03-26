# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["EnrichConfig"]


class EnrichConfig(BaseModel):
    enabled: Optional[bool] = None
    """
    If enabled, a large language/vision model will be used to postprocess the
    extracted content. Note: enabling enrich requires tables be outputted in
    markdown format. Defaults to False.
    """

    mode: Optional[Literal["standard", "page", "table"]] = None
    """The mode to use for enrichment. Defaults to standard"""

    prompt: Optional[str] = None
    """Add information to the prompt for enrichment."""
