#! /usr/bin/env python
from itertools import product

def evaluate_expression(numbers, operators):
    result = numbers[0]
    for i in range(len(operators)):
        if operators[i] == '+':
            result += numbers[i + 1]
        elif operators[i] == '*':
            result *= numbers[i + 1]
    return result

def main(input):
    total_calibration_result = 0
    lines = input.strip().split('\n')
    for line in lines:
        test_value, numbers = line.split(': ')
        test_value = int(test_value)
        numbers = list(map(int, numbers.split()))
        operator_combinations = product('+-*', repeat=len(numbers) - 1)
        for operators in operator_combinations:
            if evaluate_expression(numbers, operators) == test_value:
                total_calibration_result += test_value
                break
    return total_calibration_result

if __name__ == "__main__":
    # Read the strategy from the input file.
    with open('input.txt') as f:
        input = f.read()

    # Calculate and print the total score for the strategy.
    result = main(input)
    print("final result: ", result)
