from __future__ import annotations
import os
import tqdm
import collections


BASE_PATH = os.path.dirname(__file__)
INPUT_PATH = os.path.join(BASE_PATH, "input.txt")


def main() -> int:
    print(f"Day №{os.path.basename(BASE_PATH)}")
    print(f"Part №2")

    with open(INPUT_PATH, mode="r") as file:
        raw_input = file.read()

    fishes = list(map(int, raw_input.split(",")))
    days = 256
    value_after_breed = 6
    initial_value = 8

    print(f"Initial state: {fishes}")

    # Thanks to https://github.com/anthonywritescode/aoc2021/blob/main/day06/part2.py
    c = collections.Counter(fishes)
    for _ in range(days):
        c2 = collections.Counter({initial_value: c[0], value_after_breed: c[0]})
        c2.update({k - 1: v for k, v in c.items() if k > 0})
        c = c2

    print(sum(c.values()))
    
    return 0


if __name__ == "__main__":
    raise SystemExit(main())