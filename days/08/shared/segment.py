from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from typing import Iterable
    from typing import Literal
    Signal = Literal["a", "b", "c", "d", "f", "g"]
    Segment = Iterable(Signal)  # String
    SegmentPattern = list[Segment]


SEGMENTS_CHARS  = ["a", "b", "c", "d", "e", "f", "g"]
EMPTY_CHAR = "."
DEFAULT_DIGIT_CONFIGURATION = \
"""
 aaaa 
b    c
b    c
 dddd 
e    f
e    f
 gggg 
"""
