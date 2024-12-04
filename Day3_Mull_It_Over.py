import re
import os

INPUT_DATA_PATH = os.path.join("data", "day3.txt")


def main(pattern: str, text: str) -> int:

    operations = re.findall(pattern, text)
    do = True
    sum_mul = 0
    for operation in operations:
        if operation == "do()":
            do = True
        elif operation == "don't()":
            do = False
        elif do:
            num1, num2 = map(int, *re.findall(r"mul\((\d{1,3}),(\d{1,3})\)", operation))
            mul = num1 * num2
            sum_mul += mul

    return sum_mul


if __name__ == "__main__":

    text = open(INPUT_DATA_PATH, "r").read()

    part1_pattern = r"mul\(\d{1,3},\d{1,3}\)"
    part2_pattern = r"mul\(\d{1,3},\d{1,3}\)|do\(\)|don't\(\)"

    part1_result = main(part1_pattern, text)
    part2_result = main(part2_pattern, text)

    print(part1_result)
    print(part2_result)
