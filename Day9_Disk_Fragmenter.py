import os


INPUT_DATA_PATH = os.path.join("data", "day9.txt")


def part1(disk_map: str) -> int:

    pointer_l = 0
    id_num_l, is_file_l, block_size_l = read(pointer_l, disk_map)
    pointer_r = len(disk_map) - 1
    id_num_r, is_file_r, block_size_r = read(pointer_r, disk_map)
    checksum = 0
    index = 0
    while pointer_l != pointer_r:

        # если слева файл, то просто считаем по нему контрольную сумму
        if is_file_l:
            for _ in range(block_size_l):
                checksum += index * id_num_l
                index += 1
            pointer_l += 1
            id_num_l, is_file_l, block_size_l = read(pointer_l, disk_map)

        # если слева пустое пространство, то заполняем его
        else:
            # если справа файл,
            if is_file_r:
                # то перетаскиваем его направо, считая контрольную сумму
                while block_size_l > 0 and block_size_r > 0:
                    checksum += index * id_num_r
                    index += 1
                    block_size_l -= 1
                    block_size_r -= 1
                # если закончилось свободное пространство слева
                if block_size_l == 0:
                    pointer_l += 1
                    id_num_l, is_file_l, block_size_l = read(pointer_l, disk_map)
                # если закончился файл справа
                elif block_size_r == 0:
                    pointer_r -= 1
                    id_num_r, is_file_r, block_size_r = read(pointer_r, disk_map)

            # если справа пустое пространство, то пропускаем его
            else:
                pointer_r -= 1
                id_num_r, is_file_r, block_size_r = read(pointer_r, disk_map)

    # добавляем в контрольную сумму последний блок, который мог сдвинуться
    # указатели на карте диска на нём сошлись
    for _ in range(block_size_r):
        checksum += index * id_num_r
        index += 1

    return checksum


def part2(disk_map: str) -> int:

    free_spaces = []
    pointer_l = 0
    id_num_l, is_file_l, block_size_l = read(pointer_l, disk_map)
    pointer_r = len(disk_map) - 1
    id_num_r, is_file_r, block_size_r = read(pointer_r, disk_map)
    checksum = 0
    index = 0
    while pointer_r != pointer_l:

        # если справа файл, то пытаемся ему найти место слева
        if is_file_r:
            # ищем место в кусках
            if free_spaces:
                for block_size, start_index in free_spaces:
                    if block_size
            # если слева файл, то просто считаем по нему контрольную сумму
            if is_file_l:
                for _ in range(block_size_l):
                    checksum += index * id_num_l
                    index += 1
                pointer_l += 1
                id_num_l, is_file_l, block_size_l = read(pointer_l, disk_map)
            # если слева свободное пространство,
            else:
                # если можем в него засунуть файл справа,
                if block_size_l >= block_size_r:
                    # то засовываем
                    while block_size_r > 0:
                        checksum += index * id_num_r
                        index += 1
                        block_size_l -= 1
                        block_size_r -= 1
                    # если закончилось свободное пространство слева
                    if block_size_l == 0:
                        pointer_l += 1
                        id_num_l, is_file_l, block_size_l = read(pointer_l, disk_map)
                    # если остался свободный кусок пространства слева
                    elif block_size_l > 0:
                        free_spaces.append((block_size_l, index))

                    pointer_r -= 1
                    id_num_r, is_file_r, block_size_r = read(pointer_r, disk_map)

        # если справа пустое пространство, то пропускаем его
        else:
            pointer_r -= 1
            id_num_r, is_file_r, block_size_r = read(pointer_r, disk_map)

    return checksum


def read(pointer: int, disk_map: str) -> tuple[int, bool, int]:

    id_num, is_free_space = divmod(pointer, 2)
    is_file = not bool(is_free_space)
    block_size = int(disk_map[pointer])

    return id_num, is_file, block_size


if __name__ == "__main__":

    disk_map = open(INPUT_DATA_PATH, "r").read().strip()

    part1_result = part1(disk_map)

    print(part1_result)
