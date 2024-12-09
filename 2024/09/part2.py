#! /usr/bin/env python
import json

def find_map_disk(input) -> str:
    """Find the map disk.

    Args:
        input (str): The input.

    Returns:
        list: The map disk.
    """
    map_disk = []
    free_space_map = {}
    for i, row in enumerate(input):
        lenght_of_diskblock = int(row)
        id = int(i / 2)
        if i % 2 == 0:
            # print("i: ", i, "row: ", row, "lenght_of_diskblock: ", lenght_of_diskblock)
            # print("str(id): ", str(id), str(id) * lenght_of_diskblock)
            map_disk.extend([str(id)] * lenght_of_diskblock)
        else:
            if lenght_of_diskblock != 0 and len(map_disk) not in free_space_map:
                free_space_map[len(map_disk)] = lenght_of_diskblock
            elif lenght_of_diskblock != 0:
                free_space_map[len(map_disk)].append(lenght_of_diskblock)
            map_disk.extend(["."] * lenght_of_diskblock)

    return map_disk, free_space_map


def move_to_free_space(map_disk, free_space_map):
    """Move whole files to the leftmost span of free space blocks that could fit the file.

    Args:
        map_disk (list): The map disk.
        free_space_map (dict): The free space map.

    """
    new_map_disk = [*map_disk]
    file_blocks = {}
    i = 0
    while i < len(new_map_disk):
        if new_map_disk[i] != ".":
            block_id = new_map_disk[i]
            start = i
            while i < len(new_map_disk) and new_map_disk[i] == block_id:
                i += 1
            file_blocks[block_id] = (start, i - start)
        else:
            i += 1

    for block_id in sorted(file_blocks.keys(), reverse=True):
        start, length = file_blocks[block_id]
        for free_start in sorted(free_space_map.keys()):
            free_length = free_space_map[free_start]
            if free_length >= length and free_start <= start:
                del free_space_map[free_start]
                if free_length > length:
                    free_space_map[free_start + length] = free_length - length

                new_map_disk[free_start:free_start + length] = [block_id] * length
                new_map_disk[start:start + length] = ["."] * length
                break
    # print("free_space_map: ", dict(sorted(free_space_map.items(), key=lambda item: item[1])))

    return new_map_disk


def main(input):
    # print("input: ", input)
    map_disk, free_space_map = find_map_disk(input)
    new_map_disk = move_to_free_space(map_disk, free_space_map)
    result = 0
    for i, block_id in enumerate(new_map_disk):
        if block_id != ".":
            result += int(block_id) * (i)

    # print("map_disk: ", map_disk)
    # if len(new_map_disk) < 100:
    #     print("new_map_disk: ", ''.join(new_map_disk))
    # with open("map_disk.json", "w") as f:
    #     f.write(json.dumps(map_disk))
    # with open("newmapdisk.json", "w") as f:
    #     f.write(json.dumps(new_map_disk))
    # print("new_map_disk: ", new_map_disk)
    return result


if __name__ == "__main__":
    # Read the strategy from the input file.
    with open("input.txt") as f:
        input = f.read().strip()

    # Calculate and print the total score for the strategy.
    result = main(input)
    print("final result: ", result)
