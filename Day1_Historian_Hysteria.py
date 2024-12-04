import os
import numpy as np

INPUT_DATA_PATH = os.path.join("data", "day1.txt")


def part1(left_list: np.ndarray, right_list: np.ndarray) -> np.int64:
    """Total distance."""
    left_list = left_list.copy()
    right_list = right_list.copy()

    left_list.sort()
    right_list.sort()

    return np.sum(np.abs(left_list - right_list))


def part2(left_list: np.ndarray, right_list: np.ndarray) -> int:
    """Similarity score."""
    num_count = dict()
    for num in right_list:
        num_count[num] = num_count.get(num, 0) + 1

    similarity_score = 0
    for num in left_list:
        similarity_score += num * num_count.get(num, 0)

    return similarity_score


if __name__ == "__main__":

    with open(INPUT_DATA_PATH, "r") as file:
        left_list = []
        right_list = []
        for line in file:
            left, right = map(int, line.split())
            left_list.append(left)
            right_list.append(right)

    left_list = np.array(left_list)
    right_list = np.array(right_list)

    part1_result = part1(left_list, right_list)
    print(part1_result)

    part2_result = part2(left_list, right_list)
    print(part2_result)
