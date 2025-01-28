from collections import defaultdict
from functools import lru_cache
from itertools import product
import os


INPUT_DATA_PATH = os.path.join("data", "day21.txt")


def parse_data(text: str) -> list[str]:
    return text.split("\n")


class Solution:
    numeric_keypad = [
        "789",
        "456",
        "123",
        "#0A",
    ]
    directional_keypad = [
        "#^A",
        "<v>",
    ]

    def __init__(self) -> None:
        self.paths_numeric_keypad = None
        self.paths_directional_keypad = None

    def part1(self, door_codes: list[str]):

        self.paths_numeric_keypad = self.get_paths(self.numeric_keypad)
        self.paths_directional_keypad = self.get_paths(self.directional_keypad)

        complexities = 0
        for door_code in door_codes:
            complexity = int(door_code[:-1]) * self.get_min_length(door_code, 2)
            complexities += complexity

        return complexities

    def part2(self, door_codes: list[str]):

        self.paths_numeric_keypad = self.get_paths(self.numeric_keypad)
        self.paths_directional_keypad = self.get_paths(self.directional_keypad)

        complexities = 0
        for door_code in door_codes:
            complexity = int(door_code[:-1]) * self.get_min_length(door_code, 25)
            complexities += complexity

        return complexities

    @staticmethod
    def get_paths(keypad: list[str]) -> defaultdict[tuple[str, str], list[str]]:

        button_position = {}
        for x, row in enumerate(keypad):
            for y, button in enumerate(row):
                button_position[button] = (x, y)

        gap_pos = button_position["#"]
        paths = defaultdict(list)
        for src_button, dst_button in product(button_position.keys(), repeat=2):

            src_pos = button_position[src_button]
            dst_pos = button_position[dst_button]

            dist_x = dst_pos[0] - src_pos[0]
            dist_y = dst_pos[1] - src_pos[1]
            direction_x = "v" if dist_x > 0 else "^"
            direction_y = ">" if dist_y > 0 else "<"

            # если кнопки находятся на одной горизонтали или вертикали,
            if dist_x == 0 or dist_y == 0:
                # то добавляем единственный прямой путь
                path = direction_x * abs(dist_x) + direction_y * abs(dist_y) + "A"
                paths[(src_button, dst_button)].append(path)
            # иначе пробуем добавить 2 варианта хода конём
            else:
                # 1 вариант: сначала по вертикали, затем по горизонтали
                path1 = direction_x * abs(dist_x) + direction_y * abs(dist_y) + "A"
                # 2 вариант: сначала по горизонтали, затем по вертикали
                path2 = direction_y * abs(dist_y) + direction_x * abs(dist_x) + "A"
                # если
                if src_pos[1] != gap_pos[1] or dst_pos[0] != gap_pos[0]:
                    # то сначала идём по вертикали, потом по горизонтали
                    paths[(src_button, dst_button)].append(path1)
                if src_pos[0] != gap_pos[0] or dst_pos[1] != gap_pos[1]:
                    # то сначала идём по горизонтали, потом по вертикали
                    paths[(src_button, dst_button)].append(path2)

        return paths

    @lru_cache(maxsize=None)
    def get_min_length(self, code: str, depth: int):

        if code[0].isnumeric():
            routes = self.get_routes(code, self.paths_numeric_keypad)
        else:
            routes = self.get_routes(code, self.paths_directional_keypad)

        if depth == 0:
            return min([sum(map(len, route)) for route in routes])
        else:
            return min([sum(self.get_min_length(path, depth-1) for path in route) for route in routes])

    @staticmethod
    def get_routes(code: str, paths: defaultdict[tuple[str, str], list[str]]):

        code = "A" + code

        preresult = []
        for i in range(len(code)-1):
            src = code[i]
            dst = code[i+1]
            preresult.append(paths[(src, dst)])

        routes = product(*preresult)

        return routes


if __name__ == "__main__":

    text = open(INPUT_DATA_PATH, "r").read().strip()
    door_codes = parse_data(text)

    solution = Solution()
    part1_result = solution.part1(door_codes)
    part2_result = solution.part2(door_codes)

    print(part1_result)
    print(part2_result)
