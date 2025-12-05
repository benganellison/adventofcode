#! /usr/bin/env python


def parse_input_integers(input):
    return [int(x) for x in input.splitlines()]


def parse_input_pairs(instr):
    return [tuple(int(x) for x in range.split('-')) for range in instr.splitlines()]


def main(input):

    fresh_id_ranges = parse_input_pairs(input.split("\n\n")[0])
    available_ingredients = parse_input_integers(input.split("\n\n")[1])

    result = 0
    for ingredient in available_ingredients:
        for fresh_id_range in fresh_id_ranges:
            if ingredient >= fresh_id_range[0] and ingredient <= fresh_id_range[1]:
                result += 1
                break

    return result


if __name__ == "__main__":
    # Read the strategy from the input file.
    with open('input.txt') as f:
        input = f.read()

    # Calculate and print the total score for the strategy.
    result = main(input)
    print("final result: ", result)
