from __future__ import annotations
import os


BASE_PATH = os.path.dirname(__file__)
INPUT_PATH = os.path.join(BASE_PATH, "input.txt")


def main() -> int:
    print(f"Day №{os.path.basename(BASE_PATH)}")
    print(f"Part №1")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
