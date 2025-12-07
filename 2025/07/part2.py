#! /usr/bin/env python
def parse_input_grid(input):
    return [[x for x in y] for y in input.splitlines()]


def main(input):
    manifold = parse_input_grid(input)

    beams = {}

    y = 0
    for x in range(len(manifold[0])):
        if manifold[y][x] == "S":
            beams[x] = 1
            break

    for y in range(len(manifold) - 1):
        x_beams = list(beams.keys())
        while x_beams:
            x = x_beams.pop()
            number_of_lives = beams[x]
            if manifold[y][x] == "^":
                if x + 1 not in beams:
                    beams[x + 1] = number_of_lives
                else:
                    beams[x + 1] += number_of_lives
                if x - 1 not in beams:
                    beams[x - 1] = number_of_lives
                else:
                    beams[x - 1] += number_of_lives
                beams[x] = 0

    result = sum(beams.values())
    return result


if __name__ == "__main__":
    # Read the strategy from the input file.
    with open("input.txt") as f:
        input = f.read()

    # Calculate and print the total score for the strategy.
    result = main(input)
    print("final result: ", result)
