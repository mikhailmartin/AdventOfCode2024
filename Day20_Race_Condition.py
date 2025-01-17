from itertools import product
import os
import numpy as np


INPUT_DATA_PATH = os.path.join("data", "day20.txt")

UP = (-1, 0)
RIGHT = (0, 1)
DOWN = (1, 0)
LEFT = (0, -1)
DIRECTIONS = (UP, RIGHT, DOWN, LEFT)


def parse_data(text: str) -> np.ndarray:
    return np.array([list(line) for line in text.split("\n")], dtype="object")


def part1(text):

    racetrack_map = parse_data(text)

    racetrack, colored_racetrack_map = color_racetrack(racetrack_map)

    max_rows, max_cols = colored_racetrack_map.shape

    best_cheats_counter = 0
    for x, y in racetrack:
        for nx, ny, s in foo(x, y, max_rows, max_cols, size=2):
            if (
                isinstance(colored_racetrack_map[nx, ny], int)
                and colored_racetrack_map[nx, ny] - colored_racetrack_map[x, y] - s >= 100
            ):
                best_cheats_counter += 1

    return best_cheats_counter


def color_racetrack(racetrack_map: np.ndarray):

    colored_racetrack_map = racetrack_map.copy()

    x_start, y_start = np.where(colored_racetrack_map == "S")
    x_start, y_start = int(x_start[0]), int(y_start[0])
    x_end, y_end = np.where(colored_racetrack_map == "E")
    x_end, y_end = int(x_end[0]), int(y_end[0])

    racetrack = [(x_start, y_start)]
    x, y = x_start, y_start
    index = 0
    while (x, y) != (x_end, y_end):
        colored_racetrack_map[x, y] = index
        for dx, dy in DIRECTIONS:
            nx, ny = x + dx, y + dy
            if colored_racetrack_map[nx, ny] != "#" and (nx, ny) not in racetrack:
                racetrack.append((nx, ny))
                x, y = nx, ny
                index += 1
                break
    colored_racetrack_map[x_end, y_end] = index

    return racetrack, colored_racetrack_map


def foo(
    x: int, y: int, max_x: int, max_y: int, size: int
) -> list[tuple[int, int, int]]:

    result = []
    for s in range(1, size+1):
        for nx, ny in product(range(x-s, x+s+1), range(y-s, y+s+1)):
            if (
                0 <= nx <= max_x-1 and 0 <= ny <= max_y-1
                and abs(x - nx) + abs(y - ny) == s
            ):
                result.append((nx, ny, s))

    return result


if __name__ == "__main__":

    text = open(INPUT_DATA_PATH, "r").read().strip()

    part1_result = part1(text)

    print(part1_result)
