import re
import os


INPUT_DATA_PATH = os.path.join("data", "day13.txt")

COST_A = 3
COST_B = 1
MAX_TIMES = 100
ERROR = 10_000_000_000_000


def parse_data(text: str) -> list[tuple[int, int, int, int, int, int]]:

    claw_machines = []
    for machine in text.split("\n\n"):

        x_a, y_a = re.findall(r"Button A: X\+(\d*), Y\+(\d*)", machine)[0]
        x_b, y_b = re.findall(r"Button B: X\+(\d*), Y\+(\d*)", machine)[0]
        x_p, y_p = re.findall(r"Prize: X=(\d*), Y=(\d*)", machine)[0]

        x_a = int(x_a)
        y_a = int(y_a)
        x_b = int(x_b)
        y_b = int(y_b)
        x_p = int(x_p)
        y_p = int(y_p)

        claw_machines.append((x_a, y_a, x_b, y_b, x_p, y_p))

    return claw_machines


def part1(x_a: int, y_a: int, x_b: int, y_b: int, x_p: int, y_p: int) -> int:

    times_a, times_b = kramer_method(x_a, y_a, x_b, y_b, x_p, y_p)

    if (
        # если решения целочисленны
        times_a.is_integer() and times_b.is_integer()
        # и лежат в допустимых пределах
        and 0 <= times_a <= MAX_TIMES and 0 <= times_b <= MAX_TIMES
    ):
        cost = int(COST_A * times_a + COST_B * times_b)
    else:
        cost = 0

    return cost


def part2(x_a: int, y_a: int, x_b: int, y_b: int, x_p: int, y_p: int) -> int:

    x_p += ERROR
    y_p += ERROR

    times_a, times_b = kramer_method(x_a, y_a, x_b, y_b, x_p, y_p)

    # если решения целочисленны
    if times_a.is_integer() and times_b.is_integer():
        cost = int(COST_A * times_a + COST_B * times_b)
    else:
        cost = 0

    return cost


def kramer_method(x_a: int, y_a: int, x_b: int, y_b: int, x_p: int, y_p: int) -> tuple:

    det = x_a * y_b - x_b * y_a
    det_a = x_p * y_b - x_b * y_p
    det_b = x_a * y_p - x_p * y_a

    times_a = det_a / det
    times_b = det_b / det

    return times_a, times_b


if __name__ == "__main__":

    text = open(INPUT_DATA_PATH, "r").read().strip()
    claw_machines = parse_data(text)

    part1_result = 0
    part2_result = 0
    for x_a, y_a, x_b, y_b, x_p, y_p in claw_machines:
        part1_result += part1(x_a, y_a, x_b, y_b, x_p, y_p)
        part2_result += part2(x_a, y_a, x_b, y_b, x_p, y_p)

    print(part1_result)
    print(part2_result)
