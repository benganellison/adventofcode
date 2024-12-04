#! /usr/bin/env python
import re


def get_strings_from_position(matrix, x, y):
    list_of_words = ["" for _ in range(2)]

    for i in range(0, 3):
        if x + i - 1 >= 0 and x + i - 1 < len(matrix):
            if y + i - 1 >= 0 and y + i - 1 < len(matrix[x + i - 1]):
                list_of_words[0] += matrix[x + i - 1][y + i - 1]
            else:
                list_of_words[0] += " "
            if y - i + 1 >= 0 and y - i + 1 < len(matrix[x + i - 1]):
                list_of_words[1] += matrix[x + i - 1][y - i + 1]

    list_of_words += [word[::-1] for word in list_of_words]
    return list_of_words

def test_wordlist(strings):
    result = strings.count("MAS")
    return result > 1


def main(input):
    result = 0
    original = input.split("\n")
    for x in range(len(original)):
        for y in range(len(original[x])):
            if original[x][y] == "A":
                list_of_words = get_strings_from_position(original, x, y)
                result += 1 if test_wordlist(list_of_words) else 0

    return result


if __name__ == "__main__":
    # Read the strategy from the input file.
    with open("input.txt") as f:
        input = f.read()

    # Calculate and print the total score for the strategy.
    result = main(input)
    print("final result: ", result)
