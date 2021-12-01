from __future__ import annotations
import collections
import os


BASE_PATH =  os.path.dirname(__file__) 
INPUT_PATH = os.path.join(BASE_PATH, "input.txt")
OUTPUT_PATH = os.path.join(BASE_PATH, "output.txt")


def proceed_buffer(buffer: str) -> list[int]:
    return [int(line) for line in buffer.splitlines()]


def get_measurement_sums(measurements: list[int]) -> list[int]:
    measurement_sums: list[int] = []

    for i, m in enumerate(measurements):
        if i == len(measurements) - 2:
            break
        print(f"{m}=sum({measurements[i:i+3]})={sum(measurements[i:i+3])}")
        measurement_sums.append(
            sum(measurements[i:i+3])
        )

    return measurement_sums


def count_changes(measurement_sums: list[int], output_buffer: str="") -> tuple[collections.Counter, str]:
    measurement_sums_counter = collections.Counter()
    prev = None

    for i in measurement_sums:
        if prev is None:
            output_buffer += f"{i} (N/A - no previous measurement)\n"
            measurement_sums_counter["None"] += 1
        elif prev > i:
            output_buffer += f"{i} (decrease)\n"
            measurement_sums_counter["Decreased"] += 1
        elif prev < i:
            output_buffer += f"{i} (increase)\n"
            measurement_sums_counter["Increased"] += 1
        elif prev == i:
            output_buffer += f"{i} (not changed)\n"
            measurement_sums_counter["Equal"] += 1
        prev = i 
    
    return measurement_sums_counter, output_buffer


def main() -> int:

    buffer = ""
    with open(INPUT_PATH, mode='r', encoding="utf-8") as f:
        buffer = f.read()
    
    measurements = proceed_buffer(buffer)
    measurement_sums = get_measurement_sums(measurements)
    measurement_sums_counter, output_buffer = count_changes(measurement_sums)

    output_buffer += "\n====\n"
    output_buffer += "Total:\n"
    output_buffer += f": {measurement_sums_counter}"

    with open(OUTPUT_PATH, mode='w', encoding="utf-8") as f:
        f.write(output_buffer)

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
