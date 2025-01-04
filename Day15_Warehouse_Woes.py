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


def part1(
    warehouse_map: np.ndarray,
    movements: list[Literal["^", ">", "v", "<"]]
) -> int:

    warehouse_map = warehouse_map.copy()

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

    return checksum(warehouse_map, "O")


def part2(
    warehouse_map: np.ndarray,
    movements: list[Literal["^", ">", "v", "<"]],
):

    warehouse_map = warehouse_map.copy()
    warehouse_map = doubled(warehouse_map)

    def move_horizontal(x: int, y: int, movement: Literal["^", ">", "v", "<"]) -> bool:

        x_forward, y_forward = get_forward_position(x, y, movement)
        value = warehouse_map[x, y]
        value_forward = warehouse_map[x_forward, y_forward]

        # если впереди препятствие,
        if value_forward == "#":
            # то не можем сдвинуться
            moveable = False

        # если впереди свободное пространство,
        elif value_forward == ".":
            # то двигаемся
            warehouse_map[x, y] = value_forward
            warehouse_map[x_forward, y_forward] = value
            moveable = True

        # если впереди ящик,
        elif value_forward in ["[", "]"]:
            if move_horizontal(x_forward, y_forward, movement):
                moveable = move_horizontal(x, y, movement)
            else:
                moveable = False

        return moveable

    def move_vertical(x: int, y: int, movement: Literal["^", ">", "v", "<"]):

        stack1 = [(x, y)]  # обход из начала в конец
        stack2 = []  # обход из конца в начало
        visited = set()

        while stack1:
            x, y = stack1.pop(0)
            if (x, y) not in visited:
                stack2.append((x, y))
                visited.add((x, y))
            x_forward, y_forward = get_forward_position(x, y, movement)
            value_forward = warehouse_map[x_forward, y_forward]
            if value_forward == "#":
                stack2 = []
                break
            elif value_forward == ".":
                pass
            elif value_forward == "[":
                stack1.extend([(x_forward, y_forward), (x_forward, y_forward+1)])
            elif value_forward == "]":
                stack1.extend([(x_forward, y_forward), (x_forward, y_forward-1)])

        while stack2:
            x, y = stack2.pop()
            x_forward, y_forward = get_forward_position(x, y, movement)
            value = warehouse_map[x, y]
            value_forward = warehouse_map[x_forward, y_forward]
            warehouse_map[x, y] = value_forward
            warehouse_map[x_forward, y_forward] = value

    for movement in movements:

        # находим координаты робота
        x_robot, y_robot = np.where(warehouse_map == "@")
        x_robot = x_robot[0]
        y_robot = y_robot[0]

        if movement in [">", "<"]:
            move_horizontal(x_robot, y_robot, movement)
        elif movement in ["^", "v"]:
            move_vertical(x_robot, y_robot, movement)

    return checksum(warehouse_map, "[")


def doubled(matrix: np.ndarray) -> np.ndarray:

    max_rows, max_cols = matrix.shape
    new_matrix = []
    for i in range(max_rows):
        new_line = []
        for j in range(max_cols):
            match matrix[i, j]:
                case "#":
                    new_line.extend(["#", "#"])
                case "O":
                    new_line.extend(["[", "]"])
                case ".":
                    new_line.extend([".", "."])
                case "@":
                    new_line.extend(["@", "."])
        new_matrix.append(new_line)
    new_matrix = np.array(new_matrix)

    return new_matrix


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


def checksum(matrix, sign) -> int:

    result = 0
    for x, y in zip(*np.where(matrix == sign)):
        result += 100 * x + y

    return result


if __name__ == "__main__":

    text = open(INPUT_DATA_PATH, "r").read().strip()
    warehouse_map, movements = parse_data(text)

    part1_result = part1(warehouse_map, movements)
    part2_result = part2(warehouse_map, movements)

    print(part1_result)
    print(part2_result)
