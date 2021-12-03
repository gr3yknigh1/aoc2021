from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from typing import TypeAlias
    from typing import Literal
    from typing import Any

    BitRow: TypeAlias = list[int]
import os
import collections


BASE_PATH =  os.path.dirname(__file__) 
INPUT_PATH = os.path.join(BASE_PATH, "input.txt")


def read_input() -> list[BitRow]:
    with open(INPUT_PATH, mode='r', encoding="utf-8") as f:
        buffer = f.read()
    lines = buffer.splitlines()
    return [[int(str_bit) for str_bit in line] for line in lines]


def convert_to_int(bit_row: BitRow) -> int:
    str_bit_row = "".join([str(bit) for bit in bit_row])
    return int(bin(int(str_bit_row, base=2)), base=2)


def get_oxygen_generator_rating(bit_rows: list[BitRow]) -> int:
    counter = collections.Counter()
    row_len = len(bit_rows[0])
    
    for i in range(row_len):
        
        if len(bit_rows) <= 1:
            return convert_to_int(bit_rows[0])
        
        for bit_row in bit_rows:
            counter[bit_row[i]] += 1
        
        mc_values = counter.most_common()
        
        if len(mc_values) > 2:
            raise ValueError
        
        if mc_values[0][1] == mc_values[1][1]:
            mc_value = sorted(mc_values, key=lambda x: x[0], reverse=True)[0][0]
        else:
            mc_value = mc_values[0][0]
        
        bit_rows = [bit_row for bit_row in bit_rows if bit_row[i] == mc_value]
        
        counter.clear()
    
    raise ValueError


def get_co2_scrubber_rating(bit_rows: list[BitRow]) -> int:
    counter = collections.Counter()
    row_len = len(bit_rows[0])
    
    for i in range(row_len):
        
        if len(bit_rows) <= 1:
            return convert_to_int(bit_rows[0])
        
        for bit_row in bit_rows:
            counter[bit_row[i]] += 1
        
        mc_values = counter.most_common()
        
        if len(mc_values) > 2:
            raise ValueError
        
        if mc_values[0][1] == mc_values[1][1]:
            mc_value = sorted(mc_values, key=lambda x: x[0], reverse=False)[0][0]
        else:
            mc_value = mc_values[1][0]
        
        bit_rows = [bit_row for bit_row in bit_rows if bit_row[i] == mc_value]
        
        counter.clear()
    
    raise ValueError


def main() -> int:
    bit_rows = read_input()
    
    oxygen_generator_rating = get_oxygen_generator_rating(bit_rows)
    co2_scrubber_rating = get_co2_scrubber_rating(bit_rows)
    
    print(oxygen_generator_rating)
    print(co2_scrubber_rating)
    print(oxygen_generator_rating * co2_scrubber_rating)

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
