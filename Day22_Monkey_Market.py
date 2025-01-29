import os

INPUT_DATA_PATH = os.path.join("data", "day22.txt")


def parse_data(text: str) -> list[int]:
    return list(map(int, text.split("\n")))


def part1(initial_secret_numbers: list[int]) -> int:

    result = 0
    for secret_number in initial_secret_numbers:
        for _ in range(2000):
            secret_number = tick(secret_number)
        result += secret_number

    return result


def tick(secret_number: int) -> int:

    result = secret_number * 64
    secret_number = mix(result, secret_number)
    secret_number = prune(secret_number)

    result = secret_number // 32
    secret_number = mix(result, secret_number)
    secret_number = prune(secret_number)

    result = secret_number * 2048
    secret_number = mix(result, secret_number)
    secret_number = prune(secret_number)

    return secret_number


def mix(result: int, secret_number: int) -> int:
    return result ^ secret_number


def prune(secret_number: int) -> int:
    return secret_number % 16777216


if __name__ == "__main__":

    text = open(INPUT_DATA_PATH, "r").read().strip()

    initial_secret_numbers = parse_data(text)

    part1_result = part1(initial_secret_numbers)

    print(part1_result)
