def main(input):
    grid = input.splitlines()
    # find sybols in the grid and neighbor to the symbols

    symbol_pos = find_symbols_in_grid(grid)
    neighbours = check_neighbours(grid, symbol_pos)
    print(neighbours)
    return sum(neighbours)

def find_symbols_in_grid(grid):
    symbol_pos = set()
    for row_ind, row in enumerate(grid):
        for col_ind, col in enumerate(row):
            if col.isdigit() or col == ".":
                continue
            symbol_pos.add((row_ind, col_ind))
    return symbol_pos


def check_neighbours(grid, symbol_pos):
    # check neighbours
    # if neighbour is number find the full number
    numbers = []
    for row in range(len(grid)):
        number = ""
        add_number = False
        for i in range(len(grid[row])):
            if grid[row][i].isdigit():
                number += grid[row][i]
                if any(
                    (row_no, col_no) in symbol_pos
                    for row_no in range(row - 1, row + 2)
                    for col_no in range(i - 1, i + 2)
                ):
                    add_number = True
            else:
                if number != "":
                    if add_number:
                        numbers.append(int(number))
                    number = ""
                    add_number = False
        if number != "":
            if add_number:
                numbers.append(int(number))
            number = ""

    return numbers


if __name__ == "__main__":
    # Read the strategy from the input file.
    with open("input.txt") as f:
        input = f.read()

    # Calculate and print the total score for the strategy.
    result = main(input)
    print("final result: ", result)
