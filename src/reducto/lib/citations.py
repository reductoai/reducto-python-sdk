from __future__ import annotations

import re
import json
from typing import Any, Union, Literal, Optional, cast
from pathlib import Path
from dataclasses import field, dataclass

import numpy as np
import numpy.typing as npt
from pydantic import BaseModel

from reducto.types import BoundingBox
from reducto.lib.helpers import ParseResponse, FullParseResponse, handle_url_response


def compute_iou_matrix(
    contained: npt.NDArray[Any],
    container: npt.NDArray[Any],
    mode: Literal["iou", "max", "containment", "edge_containment"] = "iou",
) -> npt.NDArray[np.float64]:
    """Calculate IoU or edge containment for all pairs of boxes between two lists.

    Args:
        contained (npt.NDArray[np.int32 | np.float32]): First list of boxes (e.g., proposals)
        container (npt.NDArray[np.int32 | np.float32]): Second list of boxes (e.g., ground truth)
        mode (str): Calculation mode ("iou", "max", "containment", or "edge_containment")

    Returns:
        npt.NDArray[np.float64]: Matrix of calculated values with shape [len(contained), len(container)]
    """
    x1 = np.maximum(contained[:, None, 0], container[:, 0])
    y1 = np.maximum(contained[:, None, 1], container[:, 1])
    x2 = np.minimum(contained[:, None, 2], container[:, 2])
    y2 = np.minimum(contained[:, None, 3], container[:, 3])

    overlap_w = np.maximum(0, x2 - x1)
    overlap_h = np.maximum(0, y2 - y1)
    intersection = overlap_w * overlap_h

    area1 = (contained[:, 2] - contained[:, 0]) * (contained[:, 3] - contained[:, 1])
    area2 = (container[:, 2] - container[:, 0]) * (container[:, 3] - container[:, 1])

    if mode == "max":
        denominator = np.minimum(area1[:, None], area2)
        result = np.divide(
            intersection,
            denominator,
            out=np.zeros_like(intersection, dtype=np.float64),
            where=denominator != 0,
        )
    elif mode == "containment":
        denominator = area1[:, None]
        result = np.divide(
            intersection,
            denominator,
            out=np.zeros_like(intersection, dtype=np.float64),
            where=denominator != 0,
        )
    elif mode == "edge_containment":
        width1 = contained[:, 2] - contained[:, 0]
        height1 = contained[:, 3] - contained[:, 1]

        percent_overlap_w = np.divide(
            overlap_w,
            width1[:, None],
            out=np.zeros_like(overlap_w, dtype=np.float64),
            where=width1[:, None] != 0,
        )
        percent_overlap_h = np.divide(
            overlap_h,
            height1[:, None],
            out=np.zeros_like(overlap_h, dtype=np.float64),
            where=height1[:, None] != 0,
        )

        result = np.minimum(percent_overlap_w, percent_overlap_h)
    else:
        # Default is IoU
        denominator = area1[:, None] + area2 - intersection
        result = np.divide(
            intersection,
            denominator,
            out=np.zeros_like(intersection, dtype=np.float64),
            where=denominator != 0,
        )
    return result


def normalize_string(text: str) -> str:
    """Normalize punctuation in a string."""
    normalized = re.sub(r"[^a-zA-Z0-9]", " ", text)
    normalized = " ".join(normalized.split())
    return normalized.lower()


class Citation(BaseModel):
    """A citation representing one occurrence of the target phrase."""

    page: int
    bboxes: list[BoundingBox]


@dataclass
class _PageDataBuilder:
    """Internal helper for building page data."""

    blocks: list[list[float]] = field(default_factory=lambda: [])
    lines: list[list[float]] = field(default_factory=lambda: [])
    words: list[list[float]] = field(default_factory=lambda: [])
    block_text: list[str] = field(default_factory=lambda: [])
    line_text: list[str] = field(default_factory=lambda: [])
    word_text: list[str] = field(default_factory=lambda: [])


@dataclass
class PageData:
    blocks: npt.NDArray[np.float64]  # n, xyxy (transform from xywh)
    lines: npt.NDArray[np.float64]  # n, xyxy (transform from xywh)
    words: npt.NDArray[np.float64]  # n, xyxy (transform from xywh)
    block_text: list[str]
    line_text: list[str]
    word_text: list[str]
    word_to_line: dict[int, int]
    line_to_block: dict[int, int]


class CitationFinder:
    def __init__(self, result: Union[Path, ParseResponse]) -> None:
        data: FullParseResponse
        if isinstance(result, Path):
            with open(result, "r") as f:
                parsed = ParseResponse.model_validate(json.load(f))
                data = handle_url_response(parsed)
        else:
            data = handle_url_response(result)

        self.data = data

        assert self.data.result.ocr is not None, "Enable return_ocr_data to continue."

        self.page_numbers, self.page_data = self._transform_ocr_to_page_data()

    def _transform_ocr_to_page_data(self) -> tuple[list[int], list[PageData]]:
        """Transform OCR data into PageData structure for each page for efficient computation."""

        pages_data: dict[int, _PageDataBuilder] = {}

        # Initialize page builders
        for chunk in self.data.result.chunks:
            for block in chunk.blocks:
                page_num = block.bbox.page
                if page_num not in pages_data:
                    pages_data[page_num] = _PageDataBuilder()

        # Collect block data
        for chunk in self.data.result.chunks:
            for block in chunk.blocks:
                page_num = block.bbox.page
                builder = pages_data[page_num]

                bbox = block.bbox
                xyxy_bbox = [
                    bbox.left,
                    bbox.top,
                    bbox.left + bbox.width,
                    bbox.top + bbox.height,
                ]

                builder.blocks.append(xyxy_bbox)
                builder.block_text.append(normalize_string(block.content))

        # Collect line and word data
        if self.data.result.ocr is not None:
            for line in self.data.result.ocr.lines:
                page_num = line.bbox.page
                builder = pages_data[page_num]

                bbox = line.bbox
                xyxy_bbox = [
                    bbox.left,
                    bbox.top,
                    bbox.left + bbox.width,
                    bbox.top + bbox.height,
                ]

                builder.lines.append(xyxy_bbox)
                builder.line_text.append(normalize_string(line.text))

            for word in self.data.result.ocr.words:
                page_num = word.bbox.page
                builder = pages_data[page_num]

                bbox = word.bbox
                xyxy_bbox = [
                    bbox.left,
                    bbox.top,
                    bbox.left + bbox.width,
                    bbox.top + bbox.height,
                ]

                builder.words.append(xyxy_bbox)
                builder.word_text.append(normalize_string(word.text))

        # Build PageData objects
        page_numbers = sorted(pages_data.keys())

        page_data_list: list[PageData] = []
        for page_num in page_numbers:
            builder = pages_data[page_num]
            blocks_arr = cast(npt.NDArray[np.float64], np.array(builder.blocks, dtype=np.float64).reshape(-1, 4))
            lines_arr = cast(npt.NDArray[np.float64], np.array(builder.lines, dtype=np.float64).reshape(-1, 4))
            words_arr = cast(npt.NDArray[np.float64], np.array(builder.words, dtype=np.float64).reshape(-1, 4))
            page_data = PageData(
                blocks=blocks_arr,
                lines=lines_arr,
                words=words_arr,
                block_text=builder.block_text,
                line_text=builder.line_text,
                word_text=builder.word_text,
                word_to_line={},
                line_to_block={},
            )
            page_data_list.append(page_data)

        for page_data in page_data_list:
            word_to_line: dict[int, int] = {}
            if page_data.words.shape[0] > 0 and page_data.lines.shape[0] > 0:
                word_line_matrix = compute_iou_matrix(page_data.words, page_data.lines, mode="containment")
                if word_line_matrix.size > 0:
                    word_to_line_indices = np.argmax(word_line_matrix, axis=1)
                    word_to_line = {
                        i: int(word_to_line_indices[i]) for i in range(len(word_to_line_indices))
                    }

            line_to_block: dict[int, int] = {}
            if page_data.lines.shape[0] > 0 and page_data.blocks.shape[0] > 0:
                line_block_matrix = compute_iou_matrix(page_data.lines, page_data.blocks, mode="containment")
                if line_block_matrix.size > 0:
                    line_to_block_indices = np.argmax(line_block_matrix, axis=1)
                    line_to_block = {
                        i: int(line_to_block_indices[i]) for i in range(len(line_to_block_indices))
                    }

            page_data.word_to_line = word_to_line
            page_data.line_to_block = line_to_block

        return page_numbers, page_data_list

    def cite(self, target: str, bbox_filter: Optional[BoundingBox] = None) -> list[Citation]:
        target = normalize_string(target)
        target_words = target.split()

        citations: list[Citation] = []

        matching_blocks: list[tuple[int, int, int, str]] = []
        for page_idx, page_data in enumerate(self.page_data):
            page_num = self.page_numbers[page_idx]
            for block_idx, block_text in enumerate(page_data.block_text):
                if bbox_filter is not None:
                    if bbox_filter.page != page_num:
                        continue

                    block_bbox = page_data.blocks[block_idx]

                    x1 = max(bbox_filter.left, block_bbox[0])
                    y1 = max(bbox_filter.top, block_bbox[1])
                    x2 = min(bbox_filter.left + bbox_filter.width, block_bbox[2])
                    y2 = min(bbox_filter.top + bbox_filter.height, block_bbox[3])

                    if x2 <= x1 or y2 <= y1:
                        continue

                    intersection_area = (x2 - x1) * (y2 - y1)
                    filter_area = bbox_filter.width * bbox_filter.height

                    if intersection_area / filter_area < 0.5:
                        continue

                if target in block_text:
                    matching_blocks.append((page_idx, page_num, block_idx, block_text))

        for page_idx, page_num, block_idx, _ in matching_blocks:
            page_data = self.page_data[page_idx]

            lines_in_block: list[int] = []
            for line_idx, mapped_block_idx in page_data.line_to_block.items():
                if mapped_block_idx == block_idx:
                    lines_in_block.append(line_idx)

            lines_in_block.sort(key=lambda line_idx: float(page_data.lines[line_idx][1]))

            words_in_block: list[str] = []
            word_indices_in_block: list[int] = []
            for line_idx in lines_in_block:
                words_in_line: list[int] = []
                for word_idx, mapped_line_idx in page_data.word_to_line.items():
                    if mapped_line_idx == line_idx:
                        words_in_line.append(word_idx)

                words_in_line.sort(key=lambda word_idx: float(page_data.words[word_idx][0]))

                for word_idx in words_in_line:
                    words_in_block.append(page_data.word_text[word_idx])
                    word_indices_in_block.append(word_idx)

            if len(target_words) == 0:
                continue

            match_start_indices: list[int] = []
            for i in range(len(words_in_block) - len(target_words) + 1):
                if words_in_block[i : i + len(target_words)] == target_words:
                    match_start_indices.append(i)

            for match_start_idx in match_start_indices:
                matching_word_indices = word_indices_in_block[match_start_idx : match_start_idx + len(target_words)]

                line_to_word_indices: dict[int, list[int]] = {}
                for word_idx in matching_word_indices:
                    line_idx = page_data.word_to_line[word_idx]
                    if line_idx not in line_to_word_indices:
                        line_to_word_indices[line_idx] = []
                    line_to_word_indices[line_idx].append(word_idx)

                line_bboxes: list[BoundingBox] = []
                for line_idx in sorted(line_to_word_indices.keys()):
                    word_indices = line_to_word_indices[line_idx]

                    word_boxes = page_data.words[word_indices]

                    left = np.min(word_boxes[:, 0])
                    top = np.min(word_boxes[:, 1])
                    right = np.max(word_boxes[:, 2])
                    bottom = np.max(word_boxes[:, 3])

                    bbox = BoundingBox(
                        page=page_num,
                        left=float(left),
                        top=float(top),
                        width=float(right - left),
                        height=float(bottom - top),
                    )
                    line_bboxes.append(bbox)

                citation = Citation(page=page_num, bboxes=line_bboxes)
                citations.append(citation)

        return citations
