from itertools import product
import re
import os
from typing import Literal


INPUT_DATA_PATH = os.path.join("data", "day7.txt")


def main(equations: list[tuple[int, list[int]]]) -> tuple[int, int]:

    part1_result = 0
    part2_result = 0
    for test_value, numbers in equations:
        if could_be_true(test_value, numbers, operators=["+", "*"]):
            part1_result += test_value
        if could_be_true(test_value, numbers, operators=["+", "*", "||"]):
            part2_result += test_value

    return part1_result, part2_result


def could_be_true(
    test_value: int,
    numbers: list[int],
    operators: list[Literal["+", "*", "||"]],
) -> bool:

    n = len(numbers)
    operator_combinations = product(operators, repeat=n-1)

    answer = False
    for ops in operator_combinations:
        expression = create_expression(numbers, ops)
        if evaluate_expression(expression) == test_value:
            answer = True

    return answer


def create_expression(numbers: list[int], ops: list[Literal["+", "*", "||"]]) -> str:

    expression = [str(numbers[0])]
    for i in range(len(ops)):
        expression.append(ops[i])
        expression.append(str(numbers[i+1]))
    expression = "".join(expression)

    return expression


def evaluate_expression(expression: str) -> int:

    elements = re.findall(r"\d+|\+|\*|\|\|", expression)

    result = 0
    operator = "+"
    for element in elements:
        if element.isdigit():
            result = apply_operation(operator, result, int(element))
        else:
            operator = element

    return result


def apply_operation(operator: Literal["+", "*", "||"], a: int, b: int) -> int:

    match operator:
        case "+":
            result = a + b
        case "*":
            result = a * b
        case "||":
            result = int(str(a) + str(b))

    return result


if __name__ == "__main__":

    equations = []
    for equation in open(INPUT_DATA_PATH, "r").read().strip().split("\n"):

        test_value, numbers = equation.split(":")
        test_value = int(test_value)
        numbers = [int(number) for number in numbers.strip().split(" ")]

        equations.append((test_value, numbers))

    part1_result, part2_result = main(equations)

    print(part1_result)
    print(part2_result)
