from __future__ import annotations
import os
import collections


BASE_PATH =  os.path.dirname(__file__) 
INPUT_PATH = os.path.join(BASE_PATH, "input.txt")
OUTPUT_PATH = os.path.join(BASE_PATH, "output.txt")


def proceed_buffer(buffer: str) -> list[int]:
    return [int(line) for line in buffer.splitlines()]


def main() -> int:

    buffer: str = ""
    with open(INPUT_PATH, mode='r', encoding="utf-8") as f:
        buffer = f.read()

    measurements: list[int] = proceed_buffer(buffer)
    measurements_counter = collections.Counter()
    
    output_buffer: str = ""
    prev: int = None
    
    for i in measurements:
        if prev is None:
            output_buffer += f"{i} (N/A - no previous measurement)\n"
            measurements_counter["None"] += 1
        elif prev > i:
            output_buffer += f"{i} (decrease)\n"
            measurements_counter["Decreased"] += 1
        elif prev < i:
            output_buffer += f"{i} (increase)\n"
            measurements_counter["Increased"] += 1
        elif prev == i:
            output_buffer += f"{i} (not changed)\n"
            measurements_counter["Equal"] += 1
        prev = i 

    output_buffer += "\n====\n"
    output_buffer += "Total:\n"
    output_buffer += f": {measurements_counter}"


    with open(OUTPUT_PATH, mode='w', encoding="utf-8") as f:
        f.write(output_buffer)

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
