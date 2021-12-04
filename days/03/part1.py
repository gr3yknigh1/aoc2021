import os
import collections


BASE_PATH = os.path.dirname(__file__)
INPUT_PATH = os.path.join(BASE_PATH, "input.txt")


with open(INPUT_PATH, mode="r", encoding="utf-8") as f:
    buffer = f.read()


lines = buffer.splitlines()
bits = [[int(str_bit) for str_bit in line] for line in lines]


def most_common_in_colomn(table, idx):
    counter = collections.Counter()

    for row in table:
        counter[row[idx]] += 1

    return counter.most_common()[0][0]


def revert_bit_row(bit_row):
    return [(1 if not bit else 0) for bit in bit_row]


def convert_to_int(bit_row):
    str_bit_row = "".join([str(bit) for bit in bit_row])
    return int(bin(int(str_bit_row, base=2)), base=2)


gamma_rate = [most_common_in_colomn(bits, i) for i in range(len(bits[0]))]
print(gamma_rate)
epsilon_rate = revert_bit_row(gamma_rate)
print(epsilon_rate)


print(convert_to_int(gamma_rate) * convert_to_int(epsilon_rate))
