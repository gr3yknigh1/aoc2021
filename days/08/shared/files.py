from __future__ import annotations

def read_raw_input(input_path: str) -> str:
    with open(input_path, mode="r") as file:
        return file.read()
