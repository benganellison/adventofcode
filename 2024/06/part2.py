#! /usr/bin/env python


def get_direction_from_representation(direction_representation):
    if direction_representation == ">":
        return 0
    elif direction_representation == "v":
        return 90
    elif direction_representation == "<":
        return 180
    elif direction_representation == "^":
        return 270


def get_direction_representation(direction):
    if direction == 0:
        return ">"
    elif direction == 90:
        return "v"
    elif direction == 180:
        return "<"
    elif direction == 270:
        return "^"


def turn_right(direction):
    new_direction = (direction + 90) % 360
    return new_direction


def find_starting_point(map_of_lab):
    for x in range(len(map_of_lab)):
        for y in range(len(map_of_lab[x])):
            if map_of_lab[x][y] not in [".", "#"]:
                return y, x, get_direction_from_representation(map_of_lab[x][y])
    return 0, 0, 0


def move_on_map(col, row, map_of_lab, direction):
    map_height = len(map_of_lab)
    map_width = len(map_of_lab[0])
    direction_repr = get_direction_representation(direction)
    
    while True:
        if direction == 0:  # moving right
            next_row, next_col = row, col + 1
        elif direction == 90:  # moving down
            next_row, next_col = row + 1, col
        elif direction == 180:  # moving left
            next_row, next_col = row, col - 1
        elif direction == 270:  # moving up
            next_row, next_col = row - 1, col

        if next_row >= map_height or next_row < 0 or next_col >= map_width or next_col < 0:
            return False
        if map_of_lab[next_row][next_col] == "#":
            direction = turn_right(direction)
            direction_repr = get_direction_representation(direction)
            continue

        row, col = next_row, next_col
        map_of_lab[row][col] = direction_repr

def detect_cycle(col, row, map_of_lab, direction):
    current_pos = (col, row, direction)
    previous = []

    while True:
        current_pos = move_one_step(*current_pos, map_of_lab)
        if current_pos is None:
            return False

        if current_pos in previous:
            return True
        previous.append(current_pos)

def move_one_step(col, row, direction, map_of_lab):
    map_height = len(map_of_lab)
    map_width = len(map_of_lab[0])
    
    if direction == 0:  # moving right
        next_row, next_col = row, col + 1
    elif direction == 90:  # moving down
        next_row, next_col = row + 1, col
    elif direction == 180:  # moving left
        next_row, next_col = row, col - 1
    elif direction == 270:  # moving up
        next_row, next_col = row - 1, col

    if next_row >= map_height or next_row < 0 or next_col >= map_width or next_col < 0:
        return None
    if map_of_lab[next_row][next_col] == "#":
        direction = turn_right(direction)
        return (col, row, direction)
    
    return (next_col, next_row, direction)

def main(input):
    map_of_lab = [list(x) for x in input.split("\n")]
    col, row, direction = find_starting_point(map_of_lab)
    move_on_map(col, row, map_of_lab, direction)
    result = 0

    for x in range(len(map_of_lab)):
        for y in range(len(map_of_lab[x])):
            if map_of_lab[x][y] not in [".", "#"]:
                map_clone = [list(row) for row in map_of_lab]
                map_clone[x][y] = "#"
                if detect_cycle(col, row, map_clone, direction):
                    result += 1

    return result

if __name__ == "__main__":
    # Read the strategy from the input file.
    with open("input.txt") as f:
        input = f.read()

    # Calculate and print the total score for the strategy.
    result = main(input)
    print("final result: ", result)
