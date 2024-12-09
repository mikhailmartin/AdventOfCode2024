from itertools import product
import os


INPUT_DATA_PATH = os.path.join("data", "day7.txt")


def part1(equations) -> int:

    result = 0
    for equation in equations:
        if could_be_true(equation):
            result += equation[0]

    return result


def could_be_true(equation) -> bool:

    test_value, numbers = equation

    n = len(numbers)
    operators = ["+", "*"]
    operator_combinations = product(operators, repeat=n-1)

    answer = False
    for ops in operator_combinations:
        if evaluate_expression(ops, numbers) == test_value:
            answer = True

    return answer


def evaluate_expression(ops, numbers):

    result = numbers[0]
    for op, number in zip(ops, numbers[1:]):
        if op == "+":
            result += number
        elif op == "*":
            result *= number

    return result


if __name__ == "__main__":

    equations = []
    for equation in open(INPUT_DATA_PATH, "r").read().strip().split("\n"):

        test_value, numbers = equation.split(":")
        test_value = int(test_value)
        numbers = [int(number) for number in numbers.strip().split(" ")]

        equations.append((test_value, numbers))

    part1_result = part1(equations)

    print(part1_result)
