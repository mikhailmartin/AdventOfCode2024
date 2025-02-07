from itertools import product
import os
import numpy as np


INPUT_DATA_PATH = os.path.join("data", "day10.txt")


def parse_data(text: str) -> np.ndarray:

    topographic_map = []
    for line in text.split("\n"):
        line = [int(digit) for digit in line]
        topographic_map.append(line)
    topographic_map = np.array(topographic_map)

    return topographic_map


def part1(text: str) -> int:

    topographic_map = parse_data(text)

    max_rows, max_cols = topographic_map.shape

    total_score = 0
    for x, y in product(range(max_rows), range(max_cols)):
        if topographic_map[x, y] == 0:
            total_score += score(x, y, topographic_map)

    return total_score


def score(x: int, y: int, topographic_map: np.ndarray) -> int:
    """depth-first search"""
    visited = np.full_like(topographic_map, fill_value=False, dtype=bool)
    max_rows, max_cols = topographic_map.shape
    stack = [(x, y)]
    reachable_nines = 0

    while stack:
        cx, cy = stack.pop()

        visited[cx, cy] = True
        current_height = topographic_map[cx, cy]

        if current_height == 9:
            reachable_nines += 1
        else:
            for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nx, ny = cx + dx, cy + dy
                if (
                    0 <= nx < max_rows and 0 <= ny < max_cols
                    and (topographic_map[nx, ny] == current_height + 1)
                    and not visited[nx, ny]
                ):
                    stack.append((nx, ny))

    return reachable_nines


def part2(text: str) -> int:

    topographic_map = parse_data(text)

    max_rows, max_cols = topographic_map.shape

    total_rating = 0
    for x, y in product(range(max_rows), range(max_cols)):
        if topographic_map[x, y] == 0:
            total_rating += rating(x, y, topographic_map)

    return total_rating


def rating(x: int, y: int, topographic_map: np.ndarray) -> int:

    max_rows, max_cols = topographic_map.shape
    stack = [(x, y)]
    reachable_nines = 0

    while stack:
        cx, cy = stack.pop(0)

        current_height = topographic_map[cx, cy]

        if current_height == 9:
            reachable_nines += 1
        else:
            for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nx, ny = cx + dx, cy + dy
                if (
                    0 <= nx < max_rows and 0 <= ny < max_cols
                    and (topographic_map[nx, ny] == current_height + 1)
                ):
                    stack.append((nx, ny))

    return reachable_nines


if __name__ == "__main__":

    text = open(INPUT_DATA_PATH, "r").read().strip()

    part1_result = part1(text)
    part2_result = part2(text)

    print(part1_result)
    print(part2_result)
