#! /usr/bin/env python
import re

def main(input):
    pattern = re.compile(r"mul\((\d{1,3}),(\d{1,3})\)")
    matches = re.findall(pattern,input)
    return sum([int(a) * int(b) for a, b in matches])


if __name__ == "__main__":
    # Read the strategy from the input file.
    with open('input.txt') as f:
        input = f.read()

    # Calculate and print the total score for the strategy.
    result = main(input)
    print("final result: ", result)
