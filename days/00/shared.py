from __future__ import annotations
import os


BASE_PATH = os.path.dirname(__file__)
INPUT_PATH = os.path.join(BASE_PATH, "input.txt")


def read_raw_input() -> str:
    with open(INPUT_PATH, mode="r") as file:
        return file.read()

def read_lines_input() -> list[str]:
    return read_raw_input().splitlines()
