import os

INPUT_DATA_PATH = os.path.join("data", "day2.txt")


def part1(report: list[int]) -> bool:

    is_decreasing = False
    is_increasing = False
    is_equal = False
    is_too_large = False

    for i in range(1, len(report)):

        diff = report[i] - report[i-1]

        if abs(diff) > 3:
            is_too_large = True
        elif diff > 0:
            is_increasing = True
        elif diff < 0:
            is_decreasing = True
        elif diff == 0:
            is_equal = True

    return not is_too_large and not is_equal and not (is_decreasing and is_increasing)


def part2(report: list[int]) -> bool:

    is_safe = []
    for i in range(len(report)):
        subreport = report[:i] + report[i+1:]
        is_safe.append(part1(subreport))

    return any(is_safe)


if __name__ == "__main__":

    with open(INPUT_DATA_PATH, "r") as file:
        part1_result = 0
        part2_preresult = 0
        for line in file:
            report = list(map(int, line.split()))
            if part1(report):
                part1_result += 1
            elif part2(report):
                part2_preresult += 1

    print(part1_result)

    part2_reult = part1_result + part2_preresult
    print(part2_reult)
