#! /usr/bin/env python
from typing import List

def is_safe(levels):

    if levels != sorted(levels) and levels != sorted(levels, reverse=True):
        return False

    for i, j in zip(levels, levels[1:]):
        diff = abs(j - i)
        if diff > 3 or diff == 0:
            return False
    return True

def safe_reports(reports: list) -> List[str]:
    safe_reports = 0
    for report in reports:
        levels = [int(i) for i in report.split(" ")]
        safe = is_safe(levels)
        if safe:
            safe_reports += 1
    return safe_reports


def extract_reports(data:str)-> List[str]:
    reports = data.split("\n")
    return reports

def main(input):
    reports = extract_reports(input)
    result = safe_reports(reports)
    return result


if __name__ == "__main__":
    # Read the strategy from the input file.
    with open('input.txt') as f:
        input = f.read()

    # Calculate and print the total score for the strategy.
    result = main(input)
    print("final result: ", result)
