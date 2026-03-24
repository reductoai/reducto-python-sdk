# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from .chunking import Chunking
from ..._models import BaseModel

__all__ = ["Retrieval"]


class Retrieval(BaseModel):
    chunking: Optional[Chunking] = None

    embedding_optimized: Optional[bool] = None
    """If True, use embedding optimized mode. Defaults to False."""

    filter_blocks: Optional[
        List[
            Literal[
                "Header",
                "Footer",
                "Title",
                "Section Header",
                "Page Number",
                "List Item",
                "Figure",
                "Table",
                "Key Value",
                "Text",
                "Comment",
                "Signature",
            ]
        ]
    ] = None
    """A list of block types to filter out from 'content' and 'embed' fields.

    By default, no blocks are filtered.
    """
