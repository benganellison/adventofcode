#! /usr/bin/env python

def parse_input_pairs(input):
    pairs = [tuple(x.split("-")) for x in input.splitlines()]
    return [(int(x), int(z)) for x, z in pairs]


def merge_ranges(ranges):
    if not ranges:
        return []

    ranges.sort()
    merged = [list(ranges[0])]

    for start, end in ranges[1:]:
        last_start, last_end = merged[-1]
        if start <= last_end + 1:
            if end > last_end:
                merged[-1][1] = end
        else:
            merged.append([start, end])

    return [(s, e) for s, e in merged]


def main(input):

    fresh_id_ranges = parse_input_pairs(input.split("\n\n")[0])

    unique_fresh_id_ranges = merge_ranges(fresh_id_ranges)

    result = 0
    for fresh_id_range in unique_fresh_id_ranges:
        result += fresh_id_range[1] - fresh_id_range[0] + 1

    return result


if __name__ == "__main__":
    # Read the strategy from the input file.
    with open("input.txt") as f:
        input = f.read()

    # Calculate and print the total score for the strategy.
    result = main(input)
    print("final result: ", result)
