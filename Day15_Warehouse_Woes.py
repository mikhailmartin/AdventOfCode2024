import os
from typing import Literal
import numpy as np


INPUT_DATA_PATH = os.path.join("data", "day15.txt")


def parse_data(text: str) -> tuple:

    text1, text2 = text.split("\n\n")

    warehouse_map = []
    for line in text1.split("\n"):
        warehouse_map.append(list(line))
    warehouse_map = np.array(warehouse_map)

    movements = []
    for line in text2.split("\n"):
        movements.extend(list(line))

    return warehouse_map, movements


def part1(warehouse_map: np.ndarray, movements: list[Literal["^", ">", "v", "<"]]):

    # находим координаты робота
    x_robot, y_robot = np.where(warehouse_map == "@")
    x_robot = x_robot[0]
    y_robot = y_robot[0]

    for movement in movements:

        x_forward, y_forward = get_forward_position(x_robot, y_robot, movement)

        match warehouse_map[x_forward, y_forward]:
            # если впереди препятствие,
            case "#":
                # то остаёмся на месте
                pass
            # если впереди свободное пространство,
            case ".":
                # то шагаем на него
                warehouse_map[x_robot, y_robot] = "."
                x_robot = x_forward
                y_robot = y_forward
                warehouse_map[x_robot, y_robot] = "@"
            # если впереди ящик,
            case "O":
                # то проверяем, можем ли его сдвинуть
                x_ = x_forward
                y_ = y_forward
                v_ = warehouse_map[x_, y_]
                # смотрим, что находится за ящик[ом|ами]
                while v_ == "O":
                    x_, y_ = get_forward_position(x_, y_, movement)
                    v_ = warehouse_map[x_, y_]
                # если впереди есть свободное пространство,
                if v_ == ".":
                    # то двигаем на него ящик[и]
                    warehouse_map[x_, y_] = "O"
                    warehouse_map[x_robot, y_robot] = "."
                    x_robot = x_forward
                    y_robot = y_forward
                    warehouse_map[x_robot, y_robot] = "@"
                else:
                    # иначе остаёмся на месте
                    pass

    return checksum(warehouse_map)


def get_forward_position(
    x: int,
    y: int,
    movement: Literal["^", ">", "v", "<"],
) -> tuple[int, int]:

    match movement:
        case "^":
            x_forward = x - 1
            y_forward = y
        case ">":
            x_forward = x
            y_forward = y + 1
        case "v":
            x_forward = x + 1
            y_forward = y
        case "<":
            x_forward = x
            y_forward = y - 1

    return x_forward, y_forward


def checksum(matrix) -> int:

    result = 0
    for x, y in zip(*np.where(matrix == "O")):
        result += 100 * x + y

    return result


if __name__ == "__main__":

    text = open(INPUT_DATA_PATH, "r").read().strip()
    warehouse_map, movements = parse_data(text)

    part1_result = part1(warehouse_map, movements)

    print(part1_result)
