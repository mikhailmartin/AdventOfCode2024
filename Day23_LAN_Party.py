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


def part2(text: str) -> str:

    node_neighbours = parse_data(text)

    maximal_cliques = set()
    for node, neighbours in node_neighbours.items():
        maximal_clique = {node}
        for neighbour in neighbours:
            if all(neighbour in node_neighbours[n] for n in maximal_clique):
                maximal_clique.add(neighbour)
        maximal_cliques.add(frozenset(maximal_clique))

    maximum_clique = max(maximal_cliques, key=len)

    return ",".join(sorted(maximum_clique))


def part2_alt(text: str) -> str:

    node_neighbours = parse_data(text)

    cliques = find_cliques(node_neighbours)
    largest_clique = max(cliques, key=len)

    return ",".join(sorted(largest_clique))


def find_cliques(graph: defaultdict[str, set[str]]):
    """
    https://en.wikipedia.org/wiki/Clique_(graph_theory)
    https://networkx.org/documentation/stable/reference/algorithms/generated/networkx.algorithms.clique.find_cliques.html#find-cliques
    https://www.youtube.com/watch?v=e5DKnpcmvMM
    """
    candidates = set(graph.keys())

    subgraph = candidates.copy()
    stack = []
    clique = [None]

    # узел с самым большим количеством соседей-кандидатов
    u = max(subgraph, key=lambda node: len(candidates & graph[node]))
    # узлы из кандидатов, что не являются соседями узла выше
    ext_u = candidates - graph[u]

    try:
        while True:
            if ext_u:
                q = ext_u.pop()
                candidates.remove(q)
                clique[-1] = q
                neighbours_q = graph[q]
                subgraph_q = subgraph & neighbours_q
                if not subgraph_q:
                    yield clique.copy()
                else:
                    candidates_q = candidates & neighbours_q
                    if candidates_q:
                        stack.append((subgraph, candidates, ext_u))
                        clique.append(None)
                        subgraph = subgraph_q
                        candidates = candidates_q
                        u = max(subgraph, key=lambda node: len(candidates & graph[node]))
                        ext_u = candidates - graph[u]
            else:
                clique.pop()
                subgraph, candidates, ext_u = stack.pop()
    except IndexError:
        pass


if __name__ == "__main__":

    text = open(INPUT_DATA_PATH, "r").read().strip()

    part1_result = part1(text)
    part2_result = part2(text)

    print(part1_result)
    print(part2_result)
