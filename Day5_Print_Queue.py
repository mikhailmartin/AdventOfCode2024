import os

INPUT_DATA_PATH = os.path.join("data", "day5.txt")


def part1(rules: list[str], pages) -> int:

    graph = dict()  # граф связей
    for rule in rules:
        # print(rule)
        key, value = map(int, rule.split("|"))
        if key not in graph:
            graph[key] = []
        graph[key].append(value)

    counter = 0
    for page in pages:
        page = list(page)
        if is_in_right_order(page, graph):
            counter += page[len(page) // 2]

    return counter


def is_in_right_order(page: list[int], graph: dict[int, list[int]]) -> bool:

    flag = True
    for i in range(len(page) - 1):
        if page[i] in graph[page[i+1]]:
            flag = False
            break

    return flag


if __name__ == "__main__":

    rules, pages = open(INPUT_DATA_PATH, "r").read().strip().split("\n\n")
    rules = rules.split("\n")
    pages = map(lambda x: map(int, x.split(",")), pages.split("\n"))

    part1_result = part1(rules, pages)

    print(part1_result)
