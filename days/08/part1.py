from __future__ import annotations

from shared import * 


def proceed_signal_pattern(signal_pattern: Segment) -> int:
    sp_len = len(signal_pattern)
    if sp_len == 2:
        return 1
    elif sp_len == 3:
        return 7
    elif sp_len == 4:
        return 4
    elif sp_len == 7:
        return 8
    raise NotImplementedError


def proceed_entries(entries: list[Entry]) -> list[int]:
    """Proceed input entries and returns valid segments"""
    numbers: list[int] = []

    for signal_patterns, output_values in entries:
        seg_to_num: dict[Segment: int] = {}
        for signal_pattern in signal_patterns:
            # Lazy implementations
            try:
                signal_num: int = proceed_signal_pattern(signal_pattern)
                seg_to_num[signal_pattern] = signal_num
            except NotImplementedError:
                continue

        numbers.append(
            [seg_to_num.get(output_value, None) for output_value in output_values]       
        )
    return numbers


def main() -> int:

    input_content = read_raw_input("input.txt")
    entries = parse_input(input_content)
    entry_numbers = proceed_entries(entries)
    c = 0
    for num_seq in entry_numbers:
        for num in num_seq:
            if num is None:
                continue
            c += 1
    print(c)

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
