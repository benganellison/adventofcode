#! /usr/bin/env python
def parse_input(input):
    list_1, list_2 = [], []
    for line in input.split("\n"):
        left, right = line.split("   ")
        list_1.append(left)
        list_2.append(right)

    return list_1, list_2


def sort_list(list_1):
    return sorted(list_1)


def main(input):
    list_1, list_2 = parse_input(input)
    result = 0
    for left in list_1:
        result += int(left)*list_2.count(left)
    return result


if __name__ == "__main__":
    # Read the strategy from the input file.
    with open("input.txt") as f:
        input = f.read()

    # Calculate and print the total score for the strategy.
    result = main(input)
    print("final result: ", result)
