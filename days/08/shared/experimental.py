from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from typing import Iterable
    from shared.segment import Segment
    
    SegmentTable = dict[int, Iterable[Segment]]
import collections

DIGIT_CONFIGURATION_TEMPLATE = \
"""
 {0}{0}{0}{0}
{1}    {2}
{1}    {2}
{1}    {2}
{1}    {2}
 {3}{3}{3}{3}
{4}    {5}
{4}    {5}
{4}    {5}
{4}    {5}
 {6}{6}{6}{6}
"""


DEFAULT_NUMBERS_SEGMENTS: SegmentTable = {
    0: "abcefg",
    1: "cf",
    2: "acdeg",
    3: "acdfg",
    4: "bcdf",
    5: "abdfg",
    6: "abdefg",
    7: "acf",
    8: "abcdefg",
    9: "abcdfg"
}

def print_digit_info() -> None:
    # Collecting
    segment_use_counter = collections.Counter()
    for number, segments in DEFAULT_NUMBERS_SEGMENTS.items():
        segment_use_counter[number] = len(segments)
    
    # Printing
    for k, v in segment_use_counter.items():
        print(f"Number '{k}' uses {v} segments")
