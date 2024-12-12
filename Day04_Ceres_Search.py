from itertools import product
import os
import numpy as np


INPUT_DATA_PATH = os.path.join("data", "day04.txt")


def part1(matrix: np.ndarray) -> int:

    max_rows, max_cols = matrix.shape
    min_length = len("XMAS")

    # все горизонтальные строки слева-направо
    horizontal_left_right = ["".join(line) for line in matrix]
    # все горизонтальные строки справа-налево
    horizontal_right_left = ["".join(reversed(line)) for line in matrix]
    # все вертикальные строки сверху-вниз
    vertical_top_bottom = ["".join(line) for line in matrix.T]
    # все вертикальные строки снизу-вверх
    vertical_bottom_top = ["".join(reversed(line)) for line in matrix.T]
    # все диагональные строки сверху-вниз, слева-направо
    diagonal_top_bottom_left_right = [
        "".join(np.diag(matrix, k))
        for k in range(-max_rows + min_length, max_cols - min_length + 1)
    ]
    # все диагональные строки снизу-вверх, справа-налево
    diagonal_bottom_top_right_left = [
        "".join(reversed(np.diag(matrix, k)))
        for k in range(-max_rows + min_length, max_cols - min_length + 1)
    ]
    # все диагональные строки сверху-вниз, справа-налево
    diagonal_top_bottom_right_left = [
        "".join(np.diag(np.fliplr(matrix), k))
        for k in range(-max_rows + min_length, max_cols - min_length + 1)
    ]
    # все диагональные строки снизу-вверх, слева-направо
    diagonal_bottom_top_left_right = [
        "".join(reversed(np.diag(np.fliplr(matrix), k)))
        for k in range(-max_rows + min_length, max_cols - min_length + 1)
    ]

    all = (
        horizontal_left_right + horizontal_right_left +
        vertical_top_bottom + vertical_bottom_top +
        diagonal_top_bottom_left_right + diagonal_bottom_top_right_left +
        diagonal_top_bottom_right_left + diagonal_bottom_top_left_right
    )

    count = 0
    for string in all:
        count += string.count("XMAS")

    return count


def part2(matrix: np.ndarray) -> int:

    max_rows, max_cols = matrix.shape

    counter = 0
    for i, j in product(range(1, max_rows-1), range(1, max_cols-1)):
        if matrix[i, j] == "A":
            diag1 = "".join([matrix[i-1, j-1], "A", matrix[i+1, j+1]])
            diag2 = "".join([matrix[i-1, j+1], "A", matrix[i+1, j-1]])
            if (diag1 == "MAS" or diag1 == "SAM") and (diag2 == "MAS" or diag2 == "SAM"):
                counter += 1

    return counter


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
