#! /usr/bin/env python
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
            free_space_map[lenght_of_diskblock] = [len(map_disk)]
            map_disk.extend(["."] * lenght_of_diskblock)

    return map_disk

def move_to_free_space(map_disk):
    """Move to free space.

    Args:
        map_disk (str): The map disk.

    """
    new_map_disk = [*map_disk]
    for i, old_block_id in enumerate(new_map_disk):
        if old_block_id == ".":
            last_block_id = new_map_disk.pop()
            # print("new_map_disk: ", "".join(new_map_disk), 'i: ', i, 'block: ', block, len(new_map_disk))
            while last_block_id == ".":
                last_block_id = new_map_disk.pop()
            if i < len(new_map_disk):
                new_map_disk[i] = last_block_id
            else:
                new_map_disk.append(last_block_id)

    # for i in range(len(new_map_disk)-1, len(map_disk)+1):
    #     new_map_disk.append(".")

    return new_map_disk


def main(input):
    print("input: ", input)
    map_disk = find_map_disk(input)
    new_map_disk = move_to_free_space(map_disk)
    result = 0
    for i,block_id in enumerate(new_map_disk):
        result += int(block_id) * i

    print("map_disk: ", map_disk)
    print("new_map_disk: ", new_map_disk)
    return result


if __name__ == "__main__":
    # Read the strategy from the input file.
    with open('input.txt') as f:
        input = f.read()

    # Calculate and print the total score for the strategy.
    result = main(input)
    print("final result: ", result)
