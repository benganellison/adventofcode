import math


def main(input):
    grid = input.splitlines()
    # find sybols in the grid and neighbor to the symbols

    symbol_pos = find_symbols_in_grid(grid)
    return check_neighbours(grid, symbol_pos)


def find_symbols_in_grid(grid):
    symbol_pos = set()
    for row_ind, row in enumerate(grid):
        for col_ind, col in enumerate(row):
            if col == "*":
                symbol_pos.add((row_ind, col_ind))
    return symbol_pos


def check_neighbours(grid, symbol_pos):
    # check neighbours
    # if neighbour is number find the full number
    pairs = {}
    pos = set()
    for row in range(len(grid)):
        number = ""
        pos.clear()
        for i in range(len(grid[row])):
            if grid[row][i].isdigit():
                number += grid[row][i]
                for row_no in range(row - 1, row + 2):
                    for col_no in range(i - 1, i + 2):
                        if (row_no, col_no) in symbol_pos:
                            pos.add(f"{row_no},{col_no}")
            elif number != "":
                add_number_to_pairs(pairs, number, pos)
                pos.clear()
                number = ""
        add_number_to_pairs(pairs, number, pos)
    print(pairs)
    return sum([math.prod(numbers) for numbers in pairs.values() if len(numbers) == 2])


def add_number_to_pairs(pairs, number, pos):
    if number != "":
        for p in pos:
            if p not in pairs:
                pairs[p] = []
            pairs[p].append(int(number))


if __name__ == "__main__":
    # Read the strategy from the input file.
    with open("input.txt") as f:
        input = f.read()

    # Calculate and print the total score for the strategy.
    result = main(input)
    print("final result: ", result)
