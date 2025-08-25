# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union, Optional
from typing_extensions import Literal, TypeAlias

from ..._models import BaseModel
from .parse_usage import ParseUsage
from .bounding_box import BoundingBox

__all__ = [
    "ParseResponse",
    "Result",
    "ResultFullResult",
    "ResultFullResultChunk",
    "ResultFullResultChunkBlock",
    "ResultFullResultChunkBlockGranularConfidence",
    "ResultFullResultOcr",
    "ResultFullResultOcrLine",
    "ResultFullResultOcrWord",
    "ResultURLResult",
]


class ResultFullResultChunkBlockGranularConfidence(BaseModel):
    extract_confidence: Optional[float] = None

    parse_confidence: Optional[float] = None


class ResultFullResultChunkBlock(BaseModel):
    bbox: BoundingBox
    """The bounding box of the block extracted from the document."""

    content: str
    """The content of the block extracted from the document."""

    type: Literal[
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
    ]
    """The type of block extracted from the document."""

    confidence: Optional[str] = None
    """The confidence for the block.

    It is either low or high and takes into account factors like OCR and table
    structure
    """

    granular_confidence: Optional[ResultFullResultChunkBlockGranularConfidence] = None
    """Granular confidence scores for the block.

    It is a dictionary of confidence scores for the block. The confidence scores
    will not be None if the user has enabled numeric confidence scores.
    """

    image_url: Optional[str] = None
    """(Experimental) The URL of the image associated with the block."""


class ResultFullResultChunk(BaseModel):
    blocks: List[ResultFullResultChunkBlock]

    content: str
    """The content of the chunk extracted from the document."""

    embed: str
    """Chunk content optimized for embedding and retrieval."""

    enriched: Optional[str] = None
    """The enriched content of the chunk extracted from the document."""

    enrichment_success: Optional[bool] = None
    """Whether the enrichment was successful."""


class ResultFullResultOcrLine(BaseModel):
    bbox: BoundingBox

    text: str

    chunk_index: Optional[int] = None
    """The index of the chunk that the line belongs to."""

    confidence: Optional[float] = None
    """OCR confidence score between 0 and 1, where 1 indicates highest confidence"""


class ResultFullResultOcrWord(BaseModel):
    bbox: BoundingBox

    text: str

    chunk_index: Optional[int] = None
    """The index of the chunk that the word belongs to."""

    confidence: Optional[float] = None
    """OCR confidence score between 0 and 1, where 1 indicates highest confidence"""


class ResultFullResultOcr(BaseModel):
    lines: List[ResultFullResultOcrLine]

    words: List[ResultFullResultOcrWord]


class ResultFullResult(BaseModel):
    chunks: List[ResultFullResultChunk]

    type: Literal["full"]
    """type = 'full'"""

    custom: Optional[object] = None

    ocr: Optional[ResultFullResultOcr] = None


class ResultURLResult(BaseModel):
    result_id: str

    type: Literal["url"]
    """type = 'url'"""

    url: str


Result: TypeAlias = Union[ResultFullResult, ResultURLResult]


class ParseResponse(BaseModel):
    duration: float
    """The duration of the parse request in seconds."""

    job_id: str

    result: Result
    """The response from the document processing service.

    Note that there can be two types of responses, Full Result and URL Result. This
    is due to limitations on the max return size on HTTPS. If the response is too
    large, it will be returned as a presigned URL in the URL response. You should
    handle this in your application.
    """

    usage: ParseUsage

    pdf_url: Optional[str] = None
    """The storage URL of the converted PDF file."""

    studio_link: Optional[str] = None
    """The link to the studio pipeline for the document."""
