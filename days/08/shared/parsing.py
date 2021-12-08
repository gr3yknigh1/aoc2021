from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from shared.segment import SegmentPattern
    Entry = tuple[SegmentPattern, SegmentPattern]


DELIMITER = "|"


def parse_input(input_content: str) -> list[Entry]:
    """Returns two parts of input: `signal patterns` and `output values`"""
    lines = input_content.splitlines()
    entries = []
    for line in lines:
        s_entry = line.split(" ")
        delimiter_index = s_entry.index(DELIMITER)
        signal_patterns = s_entry[:delimiter_index]
        output_values = s_entry[delimiter_index+1:]
        
        signal_patterns = ["".join(sorted(signal_pattern)) for signal_pattern in signal_patterns]
        output_values = ["".join(sorted(output_value)) for output_value in output_values]

        entries.append(
            (signal_patterns, output_values)
        )
    return entries
