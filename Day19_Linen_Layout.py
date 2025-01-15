import os


INPUT_DATA_PATH = os.path.join("data", "day19.txt")


def parse_data(text: str) -> tuple[list[str], list[str]]:

    available_towels, designs = text.split("\n\n")
    available_towels = available_towels.split(", ")
    designs = designs.split("\n")

    return available_towels, designs


def part1(text: str):

    available_towels, designs = parse_data(text)
    available_towels = sorted(available_towels, key=len)

    part1_result = 0
    for design in designs:
        if is_possible(design, available_towels):
            part1_result += 1

    return part1_result


def is_possible(design: str, available_towels: list[str], pointer: int = 0) -> bool:

    if pointer == len(design):
        return True

    for towel in available_towels:
        next_pointer = pointer + len(towel)
        if next_pointer <= len(design) and design[pointer:next_pointer] == towel:
            if is_possible(design, available_towels, next_pointer):
                return True

    return False


if __name__ == "__main__":

    text = open(INPUT_DATA_PATH, "r").read().strip()

    part1_result = part1(text)

    print(part1_result)
