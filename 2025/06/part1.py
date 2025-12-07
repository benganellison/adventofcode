#! /usr/bin/env python
import math

def parse_problem_input(input):
    problems = {}
    lines = input.splitlines()
    number_of_rows = len(lines)
    for row, line in enumerate(lines):
        for problem, number in enumerate(line.split()):
            if problem not in problems:
                problems[problem] = []
            if row < number_of_rows - 1:
                problems[problem].append(int(number))
            else:
                problems[problem].append(number)
    return problems


def solve_problem(problem):
    print("solving problem:", problem)
    if problem[-1] == "*":
        return math.prod(problem[:-1])
    elif problem[-1] == "+":
        return sum(problem[:-1])


def main(input):
    problems = parse_problem_input(input)
    print(problems)
    result = 0
    for problem in problems.values():
        problem_result = solve_problem(problem)
        print( "result:", problem_result)
        result += problem_result

    return result


if __name__ == "__main__":
    # Read the strategy from the input file.
    with open("input.txt") as f:
        input = f.read()

    # Calculate and print the total score for the strategy.
    result = main(input)
    print("final result: ", result)
