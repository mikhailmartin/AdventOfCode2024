from functools import lru_cache
import os


INPUT_DATA_PATH = os.path.join("data", "day11.txt")


@lru_cache(maxsize=None)
def part1(stone: int, n_blinks: int) -> int:

    if n_blinks > 0:
        result = 0
        for new_stone in blink(stone):
            result += part1(new_stone, n_blinks - 1)
    else:
        result = 1

    return result


def blink(stone: int) -> list[int]:

    if stone == 0:
        result = [1]
    elif len(str(stone)) % 2 == 0:
        result = split(stone)
    else:
        result = [stone * 2024]

    return result


def split(stone: int) -> list[int]:

    stone = str(stone)
    length = len(stone)
    center = length // 2

    return [int(stone[:center]), int(stone[center:])]


if __name__ == "__main__":

    stones = map(int, open(INPUT_DATA_PATH, "r").read().strip().split(" "))

    part1_result = 0
    for stone in stones:
        part1_result += part1(stone, 25)

    print(part1_result)
