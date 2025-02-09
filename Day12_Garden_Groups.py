from itertools import product
import os
import numpy as np


INPUT_DATA_PATH = os.path.join("data", "day12.txt")


UP = (-1, 0)
RIGHT = (0, 1)
DOWN = (1, 0)
LEFT = (0, -1)
DIRECTIONS = (UP, RIGHT, DOWN, LEFT)


def parse_data(text: str) -> np.ndarray:

    garden_map = []
    for line in text.split("\n"):
        garden_map.append(list(line))
    garden_map = np.array(garden_map)

    return garden_map


class Solution:
    def __init__(self, garden_map: np.ndarray) -> None:
        self.garden_map = garden_map
        self.garden_groups = None

    def part1(self) -> int:

        if self.garden_groups is None:
            self.garden_groups = self.get_garden_groups()

        total_cost = 0
        for garden_group in self.garden_groups:
            area = self.get_area(garden_group)
            perimeter = self.get_perimeter(garden_group)
            total_cost += area * perimeter

        return total_cost

    def part2(self) -> int:

        if self.garden_groups is None:
            self.garden_groups = self.get_garden_groups()

        total_cost = 0
        for garden_group in self.garden_groups:
            area = self.get_area(garden_group)
            number_of_sides = self.get_number_of_sides(garden_group)
            total_cost += area * number_of_sides

        return total_cost

    def get_garden_groups(self) -> list:

        visited = np.full_like(self.garden_map, fill_value=False, dtype=bool)
        max_rows, max_cols = self.garden_map.shape

        garden_groups = []
        for x, y in product(range(max_rows), range(max_cols)):
            if not visited[x, y]:
                plant_type_region = self.garden_map[x, y]
                garden_group = []
                queue = [(x, y)]
                while queue:
                    x, y = queue.pop()
                    if not visited[x, y]:
                        visited[x, y] = True
                        garden_group.append((x, y))
                        for dx, dy in DIRECTIONS:
                            nx, ny = x + dx, y + dy
                            if (
                                0 <= nx < max_rows and 0 <= ny < max_cols
                                and self.garden_map[nx, ny] == plant_type_region
                            ):
                                queue.append((nx, ny))
                garden_groups.append(garden_group)

        return garden_groups

    @staticmethod
    def get_area(garden_group: list) -> int:
        return len(garden_group)

    def get_perimeter(self, garden_group: list) -> int:

        plant_type_region = self.garden_map[garden_group[0]]
        max_rows, max_cols = self.garden_map.shape

        perimeter = 0
        for x, y in garden_group:
            for dx, dy in DIRECTIONS:
                nx, ny = x + dx, y + dy
                if (
                    not (0 <= nx < max_rows and 0 <= ny < max_cols)
                    or self.garden_map[nx, ny] != plant_type_region
                ):
                    perimeter += 1

        return perimeter

    def get_number_of_sides(self, garden_group: list) -> int:

        plant_type_region = self.garden_map[garden_group[0]]
        max_rows, max_cols = self.garden_map.shape
        max_x = max([x for x, _ in garden_group])
        min_x = min([x for x, _ in garden_group])
        max_y = max([y for _, y in garden_group])
        min_y = min([y for _, y in garden_group])

        number_of_sides = 0
        # подсчёт горизонтальных сторон
        for x in range(min_x, max_x+1):
            # формируем стороны
            top = []
            bottom = []
            for y in range(min_y, max_y+1):
                if (x, y) not in garden_group:
                    top.append(0)
                    bottom.append(0)
                else:
                    if (
                        not (0 <= x-1 < max_rows and 0 <= y < max_cols)
                        or self.garden_map[x-1, y] != plant_type_region
                    ):
                        top.append(1)
                    else:
                        top.append(0)

                    if (
                        not (0 <= x+1 < max_rows and 0 <= y < max_cols)
                        or self.garden_map[x+1, y] != plant_type_region
                    ):
                        bottom.append(1)
                    else:
                        bottom.append(0)
            # считаем количество сторон
            number_of_sides += self.foo(top)
            number_of_sides += self.foo(bottom)
        # подсчёт вертикальных сторон
        for y in range(min_y, max_y+1):
            # формируем стороны
            left = []
            right = []
            for x in range(min_x, max_x+1):
                if (x, y) not in garden_group:
                    left.append(0)
                    right.append(0)
                else:
                    if (
                        not (0 <= x < max_rows and 0 <= y-1 < max_cols)
                        or self.garden_map[x, y-1] != plant_type_region
                    ):
                        left.append(1)
                    else:
                        left.append(0)

                    if (
                        not (0 <= x < max_rows and 0 <= y+1 < max_cols)
                        or self.garden_map[x, y+1] != plant_type_region
                    ):
                        right.append(1)
                    else:
                        right.append(0)
            # считаем количество сторон
            number_of_sides += self.foo(left)
            number_of_sides += self.foo(right)

        return number_of_sides

    @staticmethod
    def foo(lst: list):

        c = 0
        for i in range(len(lst)-1):
            if lst[i] == 1 and lst[i+1] == 1:
                c += 1

        s = 0
        for n in lst:
            s += n

        return s - c


if __name__ == "__main__":

    text = open(INPUT_DATA_PATH, "r").read().strip()

    garden_map = parse_data(text)
    solution = Solution(garden_map)

    part1_result = solution.part1()
    part2_result = solution.part2()

    print(part1_result)
    print(part2_result)
