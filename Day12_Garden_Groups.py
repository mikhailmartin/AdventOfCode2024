from itertools import product
import os
import numpy as np


INPUT_DATA_PATH = os.path.join("data", "day12.txt")


def part1(garden_map: np.ndarray) -> int:

    busy = np.full_like(garden_map, fill_value=False, dtype=bool)
    max_rows, max_cols = garden_map.shape

    def depth_first_search(x: int, y: int, plant_type_region: str) -> tuple[int, int]:

        is_inside_garden = 0 <= x < max_rows and 0 <= y < max_cols

        if not is_inside_garden or garden_map[x, y] != plant_type_region:
            perimeter = 1
        else:
            perimeter = 0

        if not perimeter and not busy[x, y]:
            busy[x, y] = True
            area = 1
            for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nx, ny = x + dx, y + dy
                area_, perimeter_ = depth_first_search(nx, ny, plant_type_region)
                area += area_
                perimeter += perimeter_
        else:
            area = 0

        return area, perimeter

    total_cost = 0
    for x, y in product(range(max_rows), range(max_cols)):
        if not busy[x, y]:
            plant_type_region = garden_map[x, y]
            area, perimeter = depth_first_search(x, y, plant_type_region)
            total_cost += area * perimeter

    return total_cost


if __name__ == "__main__":

    text = open(INPUT_DATA_PATH, "r").read().strip()

    garden_map = []
    for line in text.split("\n"):
        garden_map.append(list(line))
    garden_map = np.array(garden_map)

    part1_result = part1(garden_map)

    print(part1_result)
