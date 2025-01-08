import os
import re


INPUT_DATA_PATH = os.path.join("data", "day17.txt")


def parse_data(text: str) -> tuple[int, int, int, list[int]]:

    register_a = int(re.findall(r"Register A: (\d+)", text)[0])
    register_b = int(re.findall(r"Register B: (\d+)", text)[0])
    register_c = int(re.findall(r"Register C: (\d+)", text)[0])
    program = re.findall(r"Program: ([\d,]+\d)", text)[0]
    program = list(map(int, program.split(",")))

    return register_a, register_b, register_c, program


class Processor:

    def __init__(
        self,
        register_a: int,
        register_b: int,
        register_c: int,
    ) -> None:
        self.instruction_pointer: int = 0
        self.register_a = register_a
        self.register_b = register_b
        self.register_c = register_c

    def run(self, program: list[int]) -> str:

        instructions = [
            self.adv,
            self.bxl,
            self.bst,
            self.jnz,
            self.bxc,
            self.out,
            self.bdv,
            self.cdv,
        ]

        outputs = []
        while self.instruction_pointer < len(program):
            opcode = program[self.instruction_pointer]
            operand = program[self.instruction_pointer+1]
            instruction = instructions[opcode]

            result = instruction(operand)
            if result is not None:
                outputs.append(str(result))

        return ",".join(outputs)

    def adv(self, operand: int) -> None:
        self.register_a //= 2 ** self.combo_operand(operand)
        self.instruction_pointer += 2

    def bxl(self, operand: int) -> None:
        self.register_b ^= operand
        self.instruction_pointer += 2

    def bst(self, operand: int) -> None:
        self.register_b = self.combo_operand(operand) % 8
        self.instruction_pointer += 2

    def jnz(self, operand: int) -> None:
        if self.register_a != 0:
            self.instruction_pointer = operand
        else:
            self.instruction_pointer += 2

    def bxc(self, operand: int) -> None:
        self.register_b ^= self.register_c
        self.instruction_pointer += 2

    def out(self, operand: int) -> int:
        self.instruction_pointer += 2
        return self.combo_operand(operand) % 8

    def bdv(self, operand: int) -> None:
        self.register_b = self.register_a // (2 ** self.combo_operand(operand))
        self.instruction_pointer += 2

    def cdv(self, operand: int) -> None:
        self.register_c = self.register_a // (2 ** self.combo_operand(operand))
        self.instruction_pointer += 2

    def combo_operand(self, operand: int) -> int:

        match operand:
            case 0 | 1 | 2 | 3:
                result = operand
            case 4:
                result = self.register_a
            case 5:
                result = self.register_b
            case 6:
                result = self.register_c

        return result


def part1(text: str) -> str:

    register_a, register_b, register_c, program = parse_data(text)

    processor = Processor(register_a, register_b, register_c)

    part1_result = processor.run(program)

    return part1_result


if __name__ == "__main__":

    text = open(INPUT_DATA_PATH, "r").read().strip()

    part1_result = part1(text)

    print(part1_result)
