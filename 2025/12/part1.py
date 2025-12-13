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

    shapes = []
    shape = []
    for i, line in enumerate(input.splitlines()):
        if 'x' in line:
            break
        if ':' in line:
            shape = []
        elif line == "":
            shapes.append({"area":sum(1 for r in shape for f in r if f == "#"), "shape": shape})
        else:
            shape.append(line)
    result = 0
    for region in input.splitlines()[i:]:
        if region == "":
            continue
        # parse 12x5: 1 0 1 0 2 2 as x,y, number_of_shapes
        parts = region.split(":")
        dims = parts[0].split("x")
        shape_w = int(dims[0])
        shape_h = int(dims[1])
        counts = [int(x) for x in parts[1].strip().split(" ")]

        total_area = shape_w * shape_h
        print("region ", region, " total area ", total_area)
        area_needed = 0
        for j, count in enumerate(counts):
            if count > 0:
                area_needed += shapes[j]["area"] * count
        print(" area needed ", area_needed)
        if area_needed * 1.2 > total_area:
            print(" area needed ", area_needed, " exceeds total area ", total_area)
        else:
            print(" area needed ", area_needed, " fits in total area ", total_area)
            result += 1
    print("shapes: ", shapes)
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
