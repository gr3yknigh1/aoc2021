from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    # from typing import Literal
    Matrix = list[list[int]]
import os
import dataclasses


BASE_PATH = os.path.dirname(__file__)
INPUT_PATH = os.path.join(BASE_PATH, "input.txt")


# def sign(x: int) -> Literal[-1, 1]:
#     print(f"{x=} -> {x // abs(x)}")
#     return x // abs(x)


@dataclasses.dataclass
class Vector2Int:
    x: int
    y: int

    @classmethod
    def parse(cls, string: str, sep: str=",") -> Vector2Int:
        return cls(
            *list(map(int, string.split(sep)))
        )


@dataclasses.dataclass
class Line:
    p1: Vector2Int
    p2: Vector2Int

    @classmethod
    def parse(cls, string: str, sep: str=" -> ") -> Line:
        s_point1, s_point2 = string.split(sep)
        return cls(
            Vector2Int.parse(s_point1),
            Vector2Int.parse(s_point2),
        )
    
    def is_straight(self) -> bool:
        return self.p1.x == self.p2.x or self.p1.y == self.p2.y


    def get_covered_points(self) -> list[Vector2Int]:
        if not self.is_straight():
            raise NotImplemented
        
        if self.p1.x == self.p2.x and self.p1.y == self.p2.y:
            return [self.p1]
        else:
            if self.p1.x == self.p2.x:            
                mx = max(self.p1.y, self.p2.y)
                mn = min(self.p1.y, self.p2.y)
                return [
                    Vector2Int(self.p1.x, i) for i in range(mn, mx + 1)
                ]
            elif self.p1.y == self.p2.y:
                mx = max(self.p1.x, self.p2.x)
                mn = min(self.p1.x, self.p2.x)
                return [
                    Vector2Int(i, self.p1.y) for i in range(mn, mx + 1)
                ]
        raise Exception("Unreachable")


def get_matrix_size(lines: list[Line]) -> tuple[int, int]:
    x_vals: list[int] = []
    y_vals: list[int] = []
    for line in lines:
        x_vals.extend(
            (line.p1.x, line.p2.x)
        )
        y_vals.extend(
            (line.p1.y, line.p2.y)
        )
    return (max(x_vals)+1, max(y_vals)+1)


def main() -> int:
    print(f"Day №{os.path.basename(BASE_PATH)}")
    print(f"Part №1")

    with open(INPUT_PATH, mode="r") as f:
        s_lines: list[str] = f.read().splitlines()

    lines: list[Line] = [Line.parse(s_line) for s_line in s_lines]
    
    matrix_size: tuple[int, int] = get_matrix_size(lines)
    matrix: Matrix = [[0 for _ in range(matrix_size[1])] for _ in range(matrix_size[0])]
    
    for line in lines:
        if not line.is_straight():
            continue
        covered_points = line.get_covered_points()
        for p in covered_points:
            matrix[p.y][p.x] += 1

    at_least_2_counter: int = 0
    for r in matrix:
        for c in r:
            if c >= 2:
                at_least_2_counter += 1
            print(c, end=" ")
        print()
    print(at_least_2_counter)

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
