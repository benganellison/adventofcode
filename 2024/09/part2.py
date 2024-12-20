#! /usr/bin/env python
import json


def find_map_disk(input) -> str:
    map_disk = []
    free_space_map = {}
    file_blocks = {}
    for i, row in enumerate(input):
        lenght_of_diskblock = int(row)
        id = int(i / 2)
        if i % 2 == 0:
            file_blocks[id] = (len(map_disk), lenght_of_diskblock)
            map_disk.extend([str(id)] * lenght_of_diskblock)
        else:
            if lenght_of_diskblock != 0 and len(map_disk) not in free_space_map:
                free_space_map[len(map_disk)] = lenght_of_diskblock
            elif lenght_of_diskblock != 0:
                free_space_map[len(map_disk)].append(lenght_of_diskblock)
            map_disk.extend(["."] * lenght_of_diskblock)

    return map_disk, free_space_map, file_blocks


def move_to_free_space(map_disk, free_space_map, file_blocks):
    new_map_disk = map_disk.copy()

    new_file_blocks = {}
    i = 0
    while i < len(new_map_disk):
        if new_map_disk[i] != ".":
            block_id = new_map_disk[i]
            start = i
            while i < len(new_map_disk) and new_map_disk[i] == block_id:
                i += 1
            new_file_blocks[block_id] = (start, i - start)
        else:
            i += 1

    # with open("new_file_blocks.json", "w") as f:
    #     json.dump(
    #         [block_id for block_id in sorted(new_file_blocks.keys(), reverse=True)], f, indent=4
    #     )
    # with open("new_file_blocks_reversed.json", "w") as f:
    #     json.dump(list(reversed(list(new_file_blocks.keys()))), f, indent=4)

    file_blocks = new_file_blocks

    for block_id in reversed(list(file_blocks.keys())):
        start, length = file_blocks[block_id]
        for free_start in sorted(free_space_map.keys()):
            free_length = free_space_map[free_start]
            if free_length >= length and free_start <= start:
                del free_space_map[free_start]
                if free_length > length:
                    free_space_map[free_start + length] = free_length - length

                new_map_disk[free_start:free_start + length] = [str(block_id)] * length
                new_map_disk[start:start + length] = ["."] * length
                break

    return new_map_disk


def main(input):
    map_disk, free_space_map, file_blocks = find_map_disk(input)
    new_map_disk = move_to_free_space(map_disk, free_space_map, file_blocks)
    result = 0
    for i, block_id in enumerate(new_map_disk):
        if block_id != ".":
            result += int(block_id) * (i)
    return result


if __name__ == "__main__":
    # Read the strategy from the input file.
    with open("input.txt") as f:
        input = f.read().strip()

    # Calculate and print the total score for the strategy.
    result = main(input)
    print("final result: ", result)
