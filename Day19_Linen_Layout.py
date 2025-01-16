from functools import lru_cache
import os


INPUT_DATA_PATH = os.path.join("data", "day19.txt")


def parse_data(text: str) -> tuple[list[str], list[str]]:

    available_towels, designs = text.split("\n\n")
    available_towels = available_towels.split(", ")
    designs = designs.split("\n")

    return available_towels, designs


def part1(text: str) -> int:

    available_towels, designs = parse_data(text)
    available_towels = tuple(sorted(available_towels, key=len))

    part1_result = 0
    for design in designs:
        if is_possible(design, available_towels):
            part1_result += 1

    return part1_result


def is_possible(
    design: str, available_towels: tuple[str, ...], pointer: int = 0
) -> bool:

    if pointer == len(design):
        return True

    for towel in available_towels:
        next_pointer = pointer + len(towel)
        if next_pointer <= len(design) and design[pointer:next_pointer] == towel:
            if is_possible(design, available_towels, next_pointer):
                return True

    return False


def part2(text: str):

    available_towels, designs = parse_data(text)
    available_towels = sorted(available_towels, key=len)
    available_towels = tuple(available_towels)

    part2_result = 0
    for design in designs:
        part2_result += count_possible(design, available_towels)

    return part2_result


@lru_cache(maxsize=None)
def count_possible(
    design: str, available_towels: tuple[str, ...], pointer: int = 0
) -> int:

    if pointer == len(design):
        return 1

    counter = 0
    for towel in available_towels:
        next_pointer = pointer + len(towel)
        if next_pointer <= len(design) and design[pointer:next_pointer] == towel:
            counter += count_possible(design, available_towels, next_pointer)

    return counter


if __name__ == "__main__":

    text = open(INPUT_DATA_PATH, "r").read().strip()

    part1_result = part1(text)
    part2_result = part2(text)

    print(part1_result)
    print(part2_result)
