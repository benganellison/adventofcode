#! /usr/bin/env python
import re

def get_strings_from_position(matrix, x, y):
    strings = ["" for _ in range(8)]
    string = ""
    for i in range(0,4):
        if y+i < len(matrix[0]):
            strings[0] += matrix[x][y+i]
        if x+i < len(matrix) and y+i < len(matrix[x+i]):
            strings[1] += matrix[x+i][y+i]
        if x+i < len(matrix):
            strings[2] += matrix[x+i][y]
        if x+i < len(matrix) and y-i >= 0:
            strings[3] += matrix[x+i][y-i]
        if y-i >= 0:
            strings[4] += matrix[x][y-i]
        if x-i >= 0 and y-i >= 0:
            strings[5] += matrix[x-i][y-i]
        if x-i >= 0:
            strings[6] += matrix[x-i][y]
        if x-i >= 0 and y+i < len(matrix[0]):
            strings[7] += matrix[x-i][y+i]
    return strings


def main(input):
    all_strings = []
    original = input.split("\n")
    for x in range(len(original)):
        for y in range(len(original[x])):
            if original[x][y] == "X":
                all_strings += get_strings_from_position(original, x, y)

    pattern = r"(XMAS)"
    result = 0
    for string in all_strings:
        result += len(re.findall(pattern, string))

    return result


if __name__ == "__main__":
    # Read the strategy from the input file.
    with open('input.txt') as f:
        input = f.read()

    # Calculate and print the total score for the strategy.
    result = main(input)
    print("final result: ", result)
