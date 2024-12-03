#! /usr/bin/env python
import re

def find_values(input):
    pattern = re.compile(r"mul\((\d{1,3}),(\d{1,3})\)")
    matches = re.findall(pattern, input)
    return sum([int(a) * int(b) for a, b in matches])

def main(input):
    dos = input.split("do()")
    result = 0
    for do in dos:
        donts = do.split("don't()")
        result += find_values(donts[0])
    return result

if __name__ == "__main__":
    # Read the strategy from the input file.
    with open("input.txt") as f:
        input = f.read()

    # Calculate and print the total score for the strategy.
    result = main(input)
    print("final result: ", result)
