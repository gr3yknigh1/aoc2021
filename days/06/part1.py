from __future__ import annotations
import os


BASE_PATH = os.path.dirname(__file__)
INPUT_PATH = os.path.join(BASE_PATH, "input.txt")


def main() -> int:
    print(f"Day №{os.path.basename(BASE_PATH)}")
    print(f"Part №1")

    with open(INPUT_PATH, mode="r") as file:
        raw_input = file.read()

    fishes = list(map(int, raw_input.split(",")))
    days = 256 
    value_after_breed = 6
    initial_value = 8

    print(f"Initial state: {fishes}")


    for d in range(days):

        new_f = []
        updated_f = []

        for f in fishes:
            if f == 0:
                updated_f.append(value_after_breed)
                new_f.append(initial_value)
                continue
            updated_f.append(f - 1)

        fishes = updated_f
        fishes.extend(new_f)
        # print(f"After {d + 1} day:  {fishes}")

    print(f"Total: {len(fishes)}")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
