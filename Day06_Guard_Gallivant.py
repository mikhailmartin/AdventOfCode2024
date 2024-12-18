import os
from typing import Literal

import numpy as np


INPUT_DATA_PATH = os.path.join("data", "day06.txt")


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


def pp(m):
    for i in m:
        print(" ".join(i))
    print()


def main(init_map) -> tuple[int, int]:

    out_min_x, out_min_y = -1, -1
    out_max_x, out_max_y = init_map.shape

    init_x, init_y = np.where(init_map == "^")
    init_x, init_y = init_x[0], init_y[0]
    guard = Guard("north", init_x, init_y)

    wayout_map = init_map.copy()

    path = []
    inside_map = True
    while inside_map:  # пока не вышли за пределы карты

        # вычисляем координаты клетки перед охранником
        forward_x, forward_y = guard.forward()

        # обработка случая, когда следующая клетка вне карты
        if forward_x in [out_min_x, out_max_x] or forward_y in [out_min_y, out_max_y]:
            wayout_map[guard.x, guard.y] = "X"
            path.append((guard.x, guard.y))
            inside_map = False

        # обработка встречи препятствия
        elif wayout_map[forward_x, forward_y] == "#":
            guard.rotate()

        else:
            wayout_map[guard.x, guard.y] = "X"
            path.append((guard.x, guard.y))
            guard.step()

    part1_result = (wayout_map == "X").sum()


    # имеет смысл пробовать ставить препятствия на исходном пути охранника
    part2_result = 0
    init_x, init_y = path[0]
    path = set(path[1:])  # дедублицируем места на пути
    for new_obstruction_x, new_obstruction_y in path:

        if (init_x, init_y) == (new_obstruction_x, new_obstruction_y):
            continue

        loop_map = init_map.copy()
        counter_map = np.full_like(init_map, fill_value=0, dtype=np.int64)
        # ставим новое препятствие на пути охранника
        loop_map[new_obstruction_x, new_obstruction_y] = "#"
        # и самого охранника перед ним
        guard = Guard("north", init_x, init_y)

        inside_map = True
        inside_loop = False
        while inside_map and not inside_loop:

            # вычисляем координаты клетки перед охранником
            forward_x, forward_y = guard.forward()

            # обработка случая, когда следующая клетка вне карты
            if forward_x in [out_min_x, out_max_x] or forward_y in [out_min_y, out_max_y]:
                inside_map = False

            # обработка встречи препятствия
            elif loop_map[forward_x, forward_y] == "#":
                guard.rotate()

            else:
                if counter_map[guard.x, guard.y] == 4:
                    inside_loop = True
                else:
                    counter_map[guard.x, guard.y] += 1
                guard.step()

        if inside_loop:
            part2_result += 1

    return part1_result, part2_result


if __name__ == "__main__":

    text = open(INPUT_DATA_PATH, "r").read().strip()

    init_map = []
    for line in text.split("\n"):
        init_map.append(list(line))
    init_map = np.array(init_map)

    part1_result, part2_result = main(init_map)

    print(part1_result)
    print(part2_result)  # не 1723
