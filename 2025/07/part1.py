#! /usr/bin/env python
def parse_input_grid(input):
    return [[x for x in y] for y in input.splitlines()]


def main(input):
    manifold = parse_input_grid(input)

    beams = set()

    y = 0
    for x in range(len(manifold[0])):
        if manifold[y][x] == "S":
            beams.add((x, y))
            break
    result = 0
    for y in range(len(manifold) - 1):
        new_beams = set()
        while beams:
            x, _ = beams.pop()
            if manifold[y][x] == "^":
                new_beams.add((x - 1, y))
                new_beams.add((x + 1, y))
                result += 1
            else:
                new_beams.add((x, y + 1))
            
        beams = new_beams

    return result


if __name__ == "__main__":
    # Read the strategy from the input file.
    with open("input.txt") as f:
        input = f.read()

    # Calculate and print the total score for the strategy.
    result = main(input)
    print("final result: ", result)
