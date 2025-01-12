from collections import deque
import os
import numpy as np


INPUT_DATA_PATH = os.path.join("data", "day18.txt")
N_ROWS = N_COLS = 71


def parse_data(text: str) -> list[tuple[int, int]]:
    return [tuple(map(int, line.split(","))) for line in text.split("\n")]


def part1(text: str) -> int:

    falling_bytes = parse_data(text)

    RAM = np.full((N_ROWS, N_COLS), fill_value=".")
    rows, cols = zip(*falling_bytes[:1024])
    RAM[rows, cols] = "#"

    # breadth-first search
    start = (0, 0)
    finish = (N_ROWS-1, N_COLS-1)
    distance = 0
    queue = deque([(start, distance)])
    visited = {start}
    while queue:
        (x, y), distance = queue.popleft()

        if (x, y) == finish:
            break

        for dx, dy in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
            nx, ny = x+dx, y+dy
            if (
                0 <= nx <= N_ROWS-1 and 0 <= ny <= N_COLS-1
                and (nx, ny) not in visited
                and RAM[nx, ny] != "#"
            ):
                visited.add((nx, ny))
                queue.append(((nx, ny), distance+1))

    return distance


if __name__ == "__main__":

    text = open(INPUT_DATA_PATH, "r").read().strip()

    part1_result = part1(text)

    print(part1_result)
