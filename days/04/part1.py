from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from typing import TypeVar
    Matrix = list[list[int]]
    T = TypeVar("T")
import os


BASE_PATH = os.path.dirname(__file__)
INPUT_PATH = os.path.join(BASE_PATH, "input.txt")


class Board:

    def __init__(self, mat: Matrix):
        self.mat = mat
        self.left = set()
        for row in mat:
            for col in row:
                self.left.add(col)

    def is_win(self) -> bool:
        for row in self.mat:
            if all([i not in self.left for i in row]):
                return True
        for col in [[row[i] for row in self.mat] for i in range(len(self.mat[0]))]:
            if all([i not in self.left for i in col]):
                return True
        return False

    
    @classmethod
    def parse(cls, lines: list[str]) -> Board:
        matrix = []
        for line in lines:
            matrix.append(
                [int(i) for i in line.split(" ") if i != ""]
            )
        return cls(matrix)


def read_input() -> str:
    with open(INPUT_PATH, mode="r") as f:
        return f.read()


def batch_items(ls: list[T], batch_size: int) -> list[T]:
    batches = []
    batch = []
    for item in ls:
        batch.append(item)
        if len(batch) == batch_size:
            batches.append(batch)
            batch = []
    if len(batch) != 0:
        batches.append(batch)
    return batches


def print_mat(mat: Matrix) -> None:
    for r in mat:
        for i in r:
            print(i, end=" ")
        print()
    print()


def main() -> int:
    print(f"Day №{os.path.basename(BASE_PATH)}")
    print(f"Part №1", end="\n"*2)

    lines = [line for line in read_input().splitlines() if line != ""]
    numbers = [int(i) for i in lines[0].split(",")]
    boards = [Board.parse(batch) for batch in batch_items(lines[1:], 5)]
    

    for num in numbers:
        for i, board in enumerate(boards):
            board.left.discard(num)
            if board.is_win():
                print(f"Wins board №{i+1}", end="\n"*2)
                print_mat(board.mat)
                print(f"Score: {sum(board.left) * num}")
                return 0
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
