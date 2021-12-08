from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from typing import TypeVar
    from typing import Iterable

    T = TypeVar("T")
    Index = int

import os
import collections


BASE_PATH = os.path.dirname(__file__)
INPUT_PATH = os.path.join(BASE_PATH, "input.txt")


def median(iterable: Iterable[T]) -> T:
    return iterable[len(iterable) // 2]

def average(iterable: Iterable[int | float]) -> int | float:
    return sum(iterable) / len(iterable)

def find_closest(x: int, iterable: Iterable[int]) -> tuple[Index, int]:
    closest: int = iterable[0] 
    for i in iterable:
        if abs(x - i) < abs(x - closest):
            closest = i
    return closest


def gauss_sum(first: int, ln: int, last: int) -> int:
    return (ln * (first + last)) // 2


def main() -> int:
    print(f"Day №{os.path.basename(BASE_PATH)}")
    print(f"Part №2")


    with open(INPUT_PATH, mode="r") as f:
        positions = list(map(int, (f.read().splitlines()[0].split(","))))

    positions = sorted(positions)



    print(positions)

    diffs = []
    for i, p in enumerate(positions):
        if i == len(positions) - 1:
            break
        d = abs(positions[i + 1] - p)
        # print(f"{p} - {positions[i + 1]} = {d}")
        diffs.append(d)
    
    print(diffs)
    diff_sums = [sum(diffs[0:i+1]) - sum(diffs[i + 1:]) for i, _ in enumerate(diffs)]
    print(diff_sums)
    zero_closest_diff = find_closest(0, diff_sums)
    print(zero_closest_diff)
    target_diff = diffs[diff_sums.index(zero_closest_diff)] 
    target_diff_index = diffs.index(target_diff)
    
    fuel_sums = []
    for i in range(1000):
        # print(
        #     positions[target_diff_index],
        #     positions[target_diff_index+1],
        # )
        target_position = int(average((
                positions[target_diff_index],
                positions[target_diff_index+1],
        ))) + i
        # print(target_position)

        fuels = [gauss_sum(1, abs(target_position - position), abs(target_position - position)) for position in positions]
        fuel_sums.append(sum(fuels))
        
        # for i, fuel in enumerate(fuels):
        #     print(f"Move from {positions[i]} to {target_position}: {fuel} fuel")
        # print(f"Total: {fuel_sum}")

    mn_fuel = min(fuel_sums)
    print(
        f"Min: {mn_fuel}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
