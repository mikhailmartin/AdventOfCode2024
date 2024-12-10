from itertools import permutations, product
import os

import numpy as np


INPUT_DATA_PATH = os.path.join("data", "day8.txt")


def part1(matrix) -> int:

    max_rows, max_cols = matrix.shape

    antennas = {}
    for x, y in product(range(max_rows), range(max_cols)):
        content = matrix[x, y]
        if content == ".":
            continue
        if content not in antennas:
            antennas[content] = []
        antennas[content].append((x, y))

    antinodes = set()
    for ants in antennas.values():
        for antenna1, antenna2 in permutations(ants, r=2):

            antinode1 = symmetrical(antenna1, antenna2)
            antinode2 = symmetrical(antenna2, antenna1)

            if is_inside_map(antinode1, max_rows, max_cols):
                antinodes.add(antinode1)
            if is_inside_map(antinode2, max_rows, max_cols):
                antinodes.add(antinode2)

    return len(antinodes)


def part2(matrix) -> int:

    max_rows, max_cols = matrix.shape

    antennas = {}
    for x, y in product(range(max_rows), range(max_cols)):
        content = matrix[x, y]
        if content == ".":
            continue
        if content not in antennas:
            antennas[content] = []
        antennas[content].append((x, y))

    antinodes = set()
    for ants in antennas.values():
        for antenna1, antenna2 in permutations(ants, r=2):

            smth = foo(antenna1, antenna2, max_rows, max_cols)
            antinodes = antinodes | smth

    return len(antinodes)


def foo(antenna1, antenna2, max_rows, max_cols):

    antinodes = {antenna1, antenna2}

    # в одну сторону
    dx = antenna2[0] - antenna1[0]
    dy = antenna2[1] - antenna1[1]
    antinode = antenna2
    while is_inside_map(antinode, max_rows, max_cols):
        antinodes.add(antinode)
        antinode = antinode[0] + dx, antinode[1] + dy

    # в другую сторону
    dx = antenna1[0] - antenna2[0]
    dy = antenna1[1] - antenna2[1]
    antinode = antenna1
    while is_inside_map(antinode, max_rows, max_cols):
        antinodes.add(antinode)
        antinode = antinode[0] + dx, antinode[1] + dy

    return antinodes


def symmetrical(point: tuple[int, int], axis: tuple[int, int]) -> tuple[int, int]:

    x = 2 * axis[0] - point[0]
    y = 2 * axis[1] - point[1]

    return x, y


def is_inside_map(point: tuple[int, int], max_rows: int, max_cols: int) -> bool:
    return (0 <= point[0] < max_rows) and (0 <= point[1] < max_cols)


if __name__ == "__main__":

    text = open(INPUT_DATA_PATH, "r").read().strip()

    matrix = []
    for line in text.split("\n"):
        matrix.append(list(line))
    matrix = np.array(matrix)

    part1_result = part1(matrix)
    part2_result = part2(matrix)

    print(part1_result)
    print(part2_result)
