import os
from typing import Literal

import numpy as np


INPUT_DATA_PATH = os.path.join("data", "day6.txt")


class Guard:
    rule = {
        "north": "east",
        "east": "south",
        "south": "west",
        "west": "north",
    }

    def __init__(
        self,
        direction: Literal["north", "east", "south", "west"],
        x: int,
        y: int,
    ) -> None:
        self.direction = direction
        self.x = x
        self.y = y

    def rotate(self) -> None:
        self.direction = self.rule[self.direction]

    def forward(self) -> tuple[int, int]:
        """Вычисляет координаты клетки перед охранником."""
        match self.direction:
            case "north":
                forward_x = self.x - 1
                forward_y = self.y
            case "east":
                forward_x = self.x
                forward_y = self.y + 1
            case "south":
                forward_x = self.x + 1
                forward_y = self.y
            case "west":
                forward_x = self.x
                forward_y = self.y - 1

        return forward_x, forward_y

    def step(self) -> None:
        self.x, self.y = self.forward()


def part1(init_map) -> int:

    out_min_x, out_min_y = -1, -1
    out_max_x, out_max_y = init_map.shape

    init_x, init_y = np.where(init_map == "^")
    init_x, init_y = init_x[0], init_y[0]
    guard = Guard("north", init_x, init_y)

    wayout_map = init_map.copy()

    # пока не вышли за пределы карты
    inside_map = True
    while inside_map:

        # вычисляем координаты клетки перед охранником
        forward_x, forward_y = guard.forward()

        # обработка случая, когда следующая клетка вне карты
        if forward_x in [out_min_x, out_max_x] or forward_y in [out_min_y, out_max_y]:
            wayout_map[guard.x, guard.y] = "X"
            inside_map = False

        # обработка встречи препятствия
        elif wayout_map[forward_x, forward_y] == "#":
            guard.rotate()

        else:
            wayout_map[guard.x, guard.y] = "X"
            guard.step()

    part1_result = (wayout_map == "X").sum()

    return part1_result


if __name__ == "__main__":

    text = open(INPUT_DATA_PATH, "r").read().strip()

    init_map = []
    for line in text.split("\n"):
        init_map.append(list(line))
    init_map = np.array(init_map)

    part1_result = part1(init_map)

    print(part1_result)
