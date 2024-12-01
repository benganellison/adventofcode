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
    list_1, list_2 = sort_list(list_1), sort_list(list_2)
    zipped = zip(list_1, list_2)
    result = 0
    for left, right in zipped:
        distance = abs(int(left) - int(right))
        result += distance
    return result


if __name__ == "__main__":
    # Read the strategy from the input file.
    with open('input.txt') as f:
        input = f.read()

    # Calculate and print the total score for the strategy.
    result = main(input)
    print("final result: ", result)
