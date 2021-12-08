from __future__ import annotations

import pandas as pd

from shared import * 

SIGNALS = "a", "b", "c", "d", "f", "g"

LEN_RULE = {
    2: 1,
    3: 7,
    4: 4,
    7: 8
}


def generate_lookup_table(signal_patterns: list[str]) -> dict[str, int]:
    lookup_table = {}

    # Easy
    for sp in signal_patterns:
        sp_len = len(sp)
        if sp_len not in LEN_RULE.keys():
            continue
        lookup_table[sp] = LEN_RULE[sp_len]
    
    # Hard
    ln6_sps = [sp for sp in signal_patterns if len(sp) == 6]
    
    for sp in ln6_sps:
        for sig in SIGNALS:
            if all([sig in _sp for _sp in ln6_sps if _sp != sp]) and sig not in sp:
                lookup_table[sp] = 0
    print(lookup_table)


    return lookup_table


def main() -> int:
    input_content = read_raw_input("input.txt")
    entries = parse_input(input_content)


    numbers = []
    for signal_patterns, output_values in entries[:1]:
        lookup_table = generate_lookup_table(signal_patterns)
        digit_seq = [lookup_table[output_value] for output_value in output_values]
        numbers.append(
            int("".join(list(map(str, digit_seq))))
        )

    print(sum(numbers))


    return 0


if __name__ == "__main__":
    raise SystemExit(main())
