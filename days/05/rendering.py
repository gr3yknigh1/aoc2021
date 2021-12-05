from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    Matrix = list[list[int]]
    Color = tuple[int, int, int]
import pygame

from part2 import get_matrix


def clamp(mn: int, x: int, mx: int) -> int:
    if mn <= x < mx:
        return x
    elif x <= mn:
        return mn
    elif mx < x:
        return mx
    raise Exception("Unreachable")


def get_color_from_mat_value(v: int) -> Color:
    return (v, v, v)


def render_matrix(surf: pygame.surface.Surface, mat: Matrix) -> None:
    for y, row in enumerate(mat):
        for x, value in enumerate(row):
            surf.set_at((x, y), get_color_from_mat_value(clamp(0, value * 50, 255)))


def main() -> int:
    pygame.init()

    mat = get_matrix()
    mat_size = (len(mat[0]), len(mat))
    
    screen_surface = pygame.display.set_mode(mat_size)
    
    is_running = True
    clean_color = (0, 0, 0)
    
    screen_surface.fill(clean_color)
    render_matrix(screen_surface, mat)
    pygame.display.flip()

    while is_running:
        event = pygame.event.wait()
        if event.type == pygame.QUIT:
            is_running = False
    

    pygame.image.save(
        screen_surface, "output.png"
    )

    pygame.quit()

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
