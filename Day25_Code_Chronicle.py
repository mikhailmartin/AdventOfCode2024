from itertools import product
import os
import numpy as np


INPUT_DATA_PATH = os.path.join("data", "day25.txt")


def parse_data(text: str):

    text = text.replace("#", "1").replace(".", "0")

    schematics = []
    for block in text.split("\n\n"):
        schematic = []
        for line in block.strip().split("\n"):
            line = list(map(int, line))
            schematic.append(line)
        schematic = np.array(schematic, dtype="int")
        schematics.append(schematic)

    locks = []
    keys = []
    for schematic in schematics:
        r = schematic.sum(axis=1)
        if r[0] == 5 and r[-1] == 0:
            locks.append(schematic)
        elif r[0] == 0 and r[-1] == 5:
            keys.append(schematic)

    return locks, keys


def part1(text: str):

    locks, keys = parse_data(text)

    counter = 0
    for lock, key in product(locks, keys):
        lock = lock.sum(axis=0)
        key = key.sum(axis=0)
        pair = lock + key
        if all(map(lambda x: x <= 5+2, pair)):
            counter += 1

    return counter


if __name__ == "__main__":

    text = open(INPUT_DATA_PATH, "r").read().strip()

    part1_result = part1(text)

    print(part1_result)
