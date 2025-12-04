#! /usr/bin/env python
def parse_input_map(input):
    return [list(x) for x in input.splitlines()]

def main(input):
    paper_rolls = parse_input_map(input)
    result = 0
    max_row_ind = len(paper_rolls)
    max_col_ind = len(paper_rolls[0])
    while True:
        removed = 0
        for row_ind, row in enumerate(paper_rolls):
            for col_in, cell in enumerate(row):
                if cell == "@":
                    neighbors = 0
                    for dx,dy in [(-1,0),(1,0),(0,-1),(0,1), (-1,-1),(1,1),(-1,1),(1,-1)]:
                        row_check = row_ind + dy
                        col_check = col_in + dx
                        if 0 <= row_check < max_row_ind and 0 <= col_check < max_col_ind:
                            if paper_rolls[row_ind + dy][col_in + dx] == "@":
                                neighbors += 1
                    if neighbors < 4:
                        removed += 1
                        paper_rolls[row_ind][col_in] = "#"
        if removed == 0:
            break
        result += removed

    return result


if __name__ == "__main__":
    # Read the strategy from the input file.
    with open("input.txt") as f:
        input = f.read()

    # Calculate and print the total score for the strategy.
    result = main(input)
    print("final result: ", result)
