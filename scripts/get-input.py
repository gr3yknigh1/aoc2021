import argparse
import datetime
import requests


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("day", type=int)
    parser.add_argument("--year", type=int, default=datetime.datetime.now().year)

    args = parser.parse_args()
    year = args.year
    day = args.day

    url = f"https://adventofcode.com/{year}/day/{day}/input"

    res = requests.get(url)
    print(res.text)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
