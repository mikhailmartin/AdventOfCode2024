import os

INPUT_DATA_PATH = os.path.join("data", "day22.txt")

N_TICKS = 2000


def parse_data(text: str) -> list[int]:
    return list(map(int, text.split("\n")))


def part1(initial_secret_numbers: list[int]) -> int:

    result = 0
    for secret_number in initial_secret_numbers:
        for _ in range(N_TICKS):
            secret_number = tick(secret_number)
        result += secret_number

    return result


def part2(initial_secret_numbers: list[int]):

    part2_result = dict()
    for initial_secret_number in initial_secret_numbers:
        sequence_price = get_sequence_price(initial_secret_number)
        for sequence, price in sequence_price.items():
            part2_result[sequence] = part2_result.get(sequence, 0) + price

    return max(part2_result.values())


def get_sequence_price(secret_number: int) -> dict[tuple, int]:

    prices = get_prices(secret_number, N_TICKS)
    changes = get_changes(prices)

    sequence_price = dict()
    visited = set()
    length = 4
    for i in range(len(changes)-length):
        sequence = tuple(changes[i: i+length])
        if sequence not in visited:
            price = prices[i+length]
            sequence_price[sequence] = price
            visited.add(sequence)

    return sequence_price


def get_prices(secret_number: int, n_ticks: int) -> list[int]:

    prices = [secret_number % 10]
    for _ in range(n_ticks):
        secret_number = tick(secret_number)
        prices.append(secret_number % 10)

    return prices


def get_changes(prices: list[int]) -> list[int]:
    return [right - left for left, right in zip(prices[:-1], prices[1:])]


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
    part2_result = part2(initial_secret_numbers)

    print(part1_result)
    print(part2_result)
