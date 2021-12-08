from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from typing import TypeVar
    from typing import Iterable

    T = TypeVar("T")

import os


BASE_PATH = os.path.dirname(__file__)
INPUT_PATH = os.path.join(BASE_PATH, "input.txt")


def median(iterable: Iterable[T]) -> T:
    return iterable[len(iterable) // 2]

# def average(iterable: Iterable[int | float]) -> int | float:
#     return sum(iterable) / len(iterable)


def main() -> int:
    print(f"Day №{os.path.basename(BASE_PATH)}")
    print(f"Part №1")


    with open(INPUT_PATH, mode="r") as f:
        positions = list(map(int, (f.read().splitlines()[0].split(","))))

    print(f"Raw input: {positions}")
    print(f"Sorted input: {sorted(positions)}")

    target_position = median(sorted(positions))
    print(f"Target: {target_position}")

    fuels = [abs(target_position - position) for position in positions]
    fuel_sum = sum(fuels)
    
    for i, fuel in enumerate(fuels):
        print(f"Move from {positions[i]} to {target_position}: {fuel} fuel")
    print(f"Total: {fuel_sum}")


    return 0


if __name__ == "__main__":
    raise SystemExit(main())
