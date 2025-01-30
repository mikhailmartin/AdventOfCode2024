from collections import defaultdict
import os

INPUT_DATA_PATH = os.path.join("data", "day23.txt")


def parse_data(text: str) -> defaultdict[str, set[str]]:

    node_neighbours = defaultdict(set)
    for connection in text.split("\n"):
        left_node, right_node = connection.split("-")
        node_neighbours[left_node].add(right_node)
        node_neighbours[right_node].add(left_node)

    return node_neighbours


def part1(text: str):

    node_neighbours = parse_data(text)

    sets = set()
    # перебираем все узлы
    for node, neighbours in node_neighbours.items():
        # если узел начинается на `t`
        if node.startswith("t"):
            # то перебираем его соседей
            for neighbour in neighbours:
                # и проверяем, являются ли они соседями исходного узла
                for n in node_neighbours[neighbour]:
                    if n in neighbours:
                        sets.add(frozenset((node, neighbour, n)))

    return len(sets)


if __name__ == "__main__":

    text = open(INPUT_DATA_PATH, "r").read().strip()

    part1_result = part1(text)

    print(part1_result)
