import re
import os


INPUT_DATA_PATH = os.path.join("data", "day13.txt")

COST_A = 3
COST_B = 1


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


if __name__ == "__main__":

    text = open(INPUT_DATA_PATH, "r").read().strip()

    claw_machines = parse_data(text)

    total_cost = 0
    for x_a, y_a, x_b, y_b, x_p, y_p in claw_machines:

        # решаем систему уравнений методом Крамера
        det = x_a * y_b - x_b * y_a
        det_a = x_p * y_b - x_b * y_p
        det_b = x_a * y_p - x_p * y_a

        times_a = det_a / det
        times_b = det_b / det

        if (
            # если решения целочисленны
            times_a.is_integer() and times_b.is_integer()
            # и лежат в допустимых пределах
            and 0 <= times_a <= 100 and 0 <= times_b <= 100
        ):
            total_cost += int(COST_A * times_a + COST_B * times_b)

    print(total_cost)
