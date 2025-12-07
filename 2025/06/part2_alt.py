#! /usr/bin/env python
import math


def solve_problem(input):
    lines = input.splitlines()
    number_of_rows = len(lines)

    numbers = []
    solutions = []
    operator = None
    for col in range(len(lines[-1])):
        if check_if_new_problem(lines, col):
            solutions.append(calculate_solution(numbers, operator))
            operator = get_operator_from_col(lines, col)
            numbers = []
        number = 0
        for row in range(number_of_rows - 1):
            number = int(str(number) + str(lines[row][col]))
        if number > 0:
            numbers.append(number)
    else:
        solutions.append(calculate_solution(numbers, operator))

    solutions = [s for s in solutions if s is not None]
    return sum(solutions)

def get_operator_from_col(lines, col):
    return lines[-1][col]

def check_if_new_problem(lines, col):
    return lines[-1][col] in ("*", "+")

def calculate_solution(numbers, operator):
    if operator and operator == "*":
        return math.prod(numbers)
    elif operator and operator == "+":
        return sum(numbers)


def main(input):
    result = solve_problem(input)
    return result


if __name__ == "__main__":
    # Read the strategy from the input file.
    with open("input.txt") as f:
        input = f.read()

    # Calculate and print the total score for the strategy.
    result = main(input)
    print("final result: ", result)
