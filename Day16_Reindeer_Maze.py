import os
import numpy as np


INPUT_DATA_PATH = os.path.join("data", "day16.txt")


def parse_data(text: str) -> np.ndarray:

    return np.array([list(line) for line in text.split("\n")])


def wayback(x: int, y: int) -> tuple[int, int]:
    return -1*x, -1*y


def part1(reindeer_maze: np.ndarray) -> int:

    # достаём координаты старта и финиша
    x_start, y_start = np.where(reindeer_maze == "S")
    start = (x_start[0], y_start[0])
    x_end, y_end = np.where(reindeer_maze == "E")
    end = (x_end[0], y_end[0])

    directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    finish_routes = []
    visited = dict()

    direction = (0, 1)
    score = 0
    route = [start]
    queue = [(start, direction, score, route)]

    while queue:
        position, direction, score, route = queue.pop(0)

        # если достигли финиша, добавляем маршрут в финишные
        if position == end:
            finish_routes.append((route, score))
            continue

        # если мы уже посещали данную позицию в том же направлении на другом маршруте
        # и при этом счёт был меньше, то пропускаем данный маршрут: он длиннее
        if (position, direction) in visited and visited[(position, direction)] < score:
            continue
        else:
            visited[(position, direction)] = score

        # оглядываемся в поисках, куда можем пойти
        for dir_ in directions:
            # избегаем возвращения назад
            if dir_ == wayback(*direction):
                continue

            nx, ny = position[0]+dir_[0], position[1]+dir_[1]
            # если не упираемся в препятствие и
            # уже не были на следующей позиции на этом же маршруте
            if reindeer_maze[nx, ny] != "#" and (nx, ny) not in route:
                # если продолжаем двигаться в том же направлении
                if dir_ == direction:
                    queue.append(((nx, ny), dir_, score+1, route+[(nx, ny)]))
                # если же необходимо повернуть
                else:
                    queue.append(((nx, ny), dir_, score+1000+1, route+[(nx, ny)]))

    return min(score for _, score in finish_routes)


if __name__ == "__main__":

    text = open(INPUT_DATA_PATH, "r").read().strip()
    reindeer_maze = parse_data(text)

    part1_result = part1(reindeer_maze)
    print(part1_result)
