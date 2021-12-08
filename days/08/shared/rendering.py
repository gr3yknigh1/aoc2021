from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from typing import Iterable
    from shared.segment import Segment

from shared.segment import DEFAULT_DIGIT_CONFIGURATION
from shared.segment import SEGMENTS_CHARS
from shared.segment import EMPTY_CHAR


def render_digit(segments: Iterable[Segment], digit_config: str=DEFAULT_DIGIT_CONFIGURATION) -> str:
    output_digit = digit_config
    for seg_char in SEGMENTS_CHARS:
        if seg_char not in segments:
            output_digit = output_digit.replace(seg_char, EMPTY_CHAR)
    return output_digit
