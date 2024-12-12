import os

INPUT_DATA_PATH = os.path.join("data", "day05.txt")


def main(rules: list[str], pages) -> tuple[int, int]:

    graph = dict()  # граф связей типа dst: [src, ..]
    for rule in rules:
        # print(rule)
        src, dst = map(int, rule.split("|"))
        if dst not in graph:
            graph[dst] = []
        graph[dst].append(src)

    part1_result = 0
    part2_result = 0
    for page in pages:
        page = list(page)
        if is_in_right_order(page, graph):
            part1_result += get_middle(page)
        else:
            page = order(page, graph)
            part2_result += get_middle(page)

    return part1_result, part2_result


def is_in_right_order(page: list[int], graph: dict[int, list[int]]) -> bool:

    flag = True
    for i in range(1, len(page)):
        if page[i] in graph[page[i-1]]:
            flag = False
            break

    return flag


def order(page: list[int], graph: dict[int, list[int]]) -> list[int]:

    i = 1
    while i != len(page):
        if page[i] in graph[page[i-1]]:
            page[i], page[i-1] = page[i-1], page[i]
            i = max(1, i-1)
        else:
            i += 1

    return page


def get_middle(lst: list):
    return lst[len(lst) // 2]


if __name__ == "__main__":

    rules, pages = open(INPUT_DATA_PATH, "r").read().strip().split("\n\n")
    rules = rules.split("\n")
    pages = map(lambda x: map(int, x.split(",")), pages.split("\n"))

    part1_result, part2_result = main(rules, pages)

    print(part1_result)
    print(part2_result)
