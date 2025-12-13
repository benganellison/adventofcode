#! /usr/bin/env python
from aocd import get_data, submit

import os


def parse_input_pairs_of_int(instr):
    return [tuple(int(x) for x in range.split("-")) for range in instr.splitlines()]


def parse_input_integers(input):
    return [int(x) for x in input.splitlines()]


def parse_input_strings(input):
    return input.splitlines()


def parse_input_map(input):
    return [list(x) for x in input.splitlines()]


def parse_input_grid_of_int(input):
    return [[int(x) for x in y] for y in input.splitlines()]


def parse_input_tuples(input):
    return [tuple(map(int, x.split(",")) for x in input.splitlines())]


def main(input):
    result = 0
    return result


def get_year_day_part(__file__):
    file_path = os.path.realpath(__file__)

    directory = os.path.dirname(file_path)
    parent = os.path.basename(directory)
    parent_dir = os.path.dirname(directory)
    grandparent = os.path.basename(parent_dir)
    day = int(parent)
    year = int(grandparent)
    part = "b"
    if file_path.endswith("part1.py"):
        part = "a"
    return day, year, part


if __name__ == "__main__":
    # Read the strategy from the input file.

    day, year, part = get_year_day_part(__file__)

    input = get_data(day=day, year=year)
    with open("input.txt", "w") as f:
        f.write(input)

    # Calculate and print the total score for the strategy.
    result = main(input)
    print("final result: ", result)

    submit(result, part=part, day=day, year=year)
