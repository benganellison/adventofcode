#! /usr/bin/env python
from timeit import timeit, repeat
from functools import cmp_to_key

rules = {}
def sort_manuals(a, b):
    global rules
    if b in rules.get(a, []):
        return -1
    elif a in rules.get(b, []):
        return 1
    else:
        return 0

manuals_cmp_key = cmp_to_key(sort_manuals)


def new_main():
    # Read the strategy from the input file.
    with open("input.txt") as f:
        input = f.read()
    result = 0

    global rules
    rules = {}
    for rule in input.split("\n\n")[0].split("\n"):
        first, second = rule.split("|")
        if first not in rules:
            rules[first] = [second]
        else:
            rules[first].append(second)

    manuals = [manual.split(",") for manual in input.split("\n\n")[1].split("\n")]

    for manual in manuals:
        sorted_manuals = sorted(manual, key=manuals_cmp_key)
        if sorted_manuals != manual:
            result += int(sorted_manuals[int(len(sorted_manuals) / 2)])

    # print("final result: ", result)
    assert result == 4713


if __name__ == "__main__":

    # Calculate and print the total score for the strategy.

    result_new = repeat(new_main, number=1, repeat=100)
    def print_statistics(results, label):
        min_result = min(results)
        max_result = max(results)
        avg_result = sum(results) / len(results)
        std_dev = (sum((x - avg_result) ** 2 for x in results) / len(results)) ** 0.5
        print(f"{label} Min: {min_result:.5f}, Max: {max_result:.5f}, Avg: {avg_result:.5f}, Std Dev: {std_dev:.5f}")

    print_statistics(result_new, "New")
