import numpy as np

import re
import os


INPUT_DATA_PATH = os.path.join("data", "day14.txt")
MAP_SIZE_X = 101
MAP_SIZE_Y = 103
N_STEPS = 100


def parse_data(text: str) -> list[tuple[int, int, int, int]]:

    robots = []
    for line in text.split("\n"):
        px, py, vx, vy = map(int, re.findall(r"(-?\d+)", line))
        robots.append((px, py, vx, vy))

    return robots


def part1(robots: list[tuple[int, int, int, int]]) -> int:

    matrix = get_matrix_after_n_steps(robots, N_STEPS, MAP_SIZE_X, MAP_SIZE_Y)
    q1, q2, q3, q4 = count_robots_in_quadrants(matrix)
    part1_result = q1 * q2 * q3 * q4

    return part1_result


def get_matrix_after_n_steps(
    robots: list[tuple[int, int, int, int]],
    n_steps: int,
    map_size_x: int,
    map_size_y: int,
) -> np.ndarray:

    matrix = np.zeros((map_size_x, map_size_y), dtype=np.int64)
    for px, py, vx, vy in robots:
        new_px, new_py = get_position_after_n_steps(
            px, py, vx, vy, n_steps, map_size_x, map_size_y
        )
        matrix[new_px, new_py] += 1

    return matrix


def get_position_after_n_steps(
    px: int,
    py: int,
    vx: int,
    vy: int,
    n_steps: int,
    map_size_x: int = MAP_SIZE_X,
    map_size_y: int = MAP_SIZE_Y,
) -> tuple[int, int]:

    px = (px + (vx * n_steps)) % map_size_x
    py = (py + (vy * n_steps)) % map_size_y

    if px < 0:
        px += map_size_x
    if py < 0:
        py += map_size_y

    return px, py


def count_robots_in_quadrants(matrix: np.ndarray) -> tuple[int, int, int, int]:

    map_size_x, map_size_y = matrix.shape

    q1 = matrix[:map_size_x//2, :map_size_y//2].sum()
    q2 = matrix[(map_size_x//2)+1:, :map_size_y//2].sum()
    q3 = matrix[:map_size_x//2, (map_size_y//2)+1:].sum()
    q4 = matrix[(map_size_x//2)+1:, (map_size_y//2)+1:].sum()

    return q1, q2, q3, q4


if __name__ == "__main__":

    text = open(INPUT_DATA_PATH, "r").read().strip()
    robots = parse_data(text)

    part1_result = part1(robots)

    print(part1_result)
