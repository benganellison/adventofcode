#! /usr/bin/env python
def parse_input_map(input):
    return [list(x) for x in input.splitlines()]

def remove_roles_of_papers(paper_rolls):
    result = 0
    for row_ind, row in enumerate(paper_rolls):
        for col_in, cell in enumerate(row):
            if cell == "@":
                neighbors = 0
                for dx,dy in [(-1,0),(1,0),(0,-1),(0,1), (-1,-1),(1,1),(-1,1),(1,-1)]:
                    row_check = row_ind + dy
                    col_check = col_in + dx
                    if 0 <= row_check < len(paper_rolls) and 0 <= col_check < len(row):
                        if paper_rolls[row_ind + dy][col_in + dx] == "@":
                            neighbors += 1
                if neighbors < 4:
                    print(
                        f"found at row {row_ind} col {col_in} with few neighbors: {neighbors}"
                    )
                    result += 1
                    paper_rolls[row_ind][col_in] = "#"
    return result


def main(input):
    paper_rolls = parse_input_map(input)
    print(paper_rolls)
    result = 0
    while True:
        removed = remove_roles_of_papers(paper_rolls)
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
