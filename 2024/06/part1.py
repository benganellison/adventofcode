#! /usr/bin/env python

DIRECTIONS = [">", "v", "<", "^"]
MOVES = [(0, 1), (1, 0), (0, -1), (-1, 0)]


def get_direction_from_representation(direction_representation):
    return DIRECTIONS.index(direction_representation)


def get_direction_representation(direction):
    return DIRECTIONS[direction]


def turn_right(direction):
    return (direction + 1) % 4


def move_on_map(col, row, map_of_lab, direction):
    print("moving on map", col, row, direction, get_direction_representation(direction))
    moved = 0
    moving = "horizontally" if direction % 2 == 0 else "vertically"
    velocity = 1 if direction < 2 else -1
    print("moving vertically", velocity)
    while True:
        if moving == "horizontally":
            next_row = row
            next_col = col + 1 * velocity
        else:
            next_row = row + 1 * velocity
            next_col = col
        if next_row >= len(map_of_lab) or next_row < 0 or next_col >= len(map_of_lab[row]) or next_col < 0:
            print("out of bounds")
            return moved
        if map_of_lab[next_row][next_col] == "#":
            print("found wall at ", next_col, next_row, "stopping at ", col, row)
            direction = turn_right(direction)
            moving = "horizontally" if direction % 2 == 0 else "vertically"
            velocity = 1 if direction < 2 else -1
            continue
        moved += 1
        row = next_row
        col = next_col
        map_of_lab[row][col] = get_direction_representation(direction)


def main(input):

    map_of_lab = [list(x) for x in input.split("\n")]

    # print(map_of_lab)
    col, row, direction = find_starting_point(map_of_lab)

    print("\n".join(["".join([str(cell) for cell in row]) for row in map_of_lab]))

    print("starting at ", col, row, direction)
    move_on_map(col, row, map_of_lab, direction)

    print("\n".join(["".join([str(cell) for cell in row]) for row in map_of_lab]))
    reduced = "".join(["".join([str(cell) for cell in row]) for row in map_of_lab])
    # print(reduced)

    return reduced.count(">") + reduced.count("v") + reduced.count("<") + reduced.count("^")

def find_starting_point(map_of_lab):
    col = 0
    row = 0
    current_direction = ""
    for x in range(len(map_of_lab)):
        for y in range(len(map_of_lab[x])):
            print(x, y, map_of_lab[x][y])
            if map_of_lab[x][y] != "." and map_of_lab[x][y] != "#":
                current_direction = map_of_lab[x][y]
                print("found starting point at ", y, x, current_direction)
                col = y
                row = x
                break
        else:
            continue
        break
    return col, row, get_direction_from_representation(current_direction)


if __name__ == "__main__":
    # Read the strategy from the input file.
    with open("input.txt") as f:
        input = f.read()

    # Calculate and print the total score for the strategy.
    result = main(input)
    print("final result: ", result)
