#! /usr/bin/env python
from itertools import product
from collections import deque

def evaluate_expression(numbers, operators):
    result = numbers[0]
    for i in range(len(operators)):
        if operators[i] == '+':
            result += numbers[i + 1]
        elif operators[i] == '*':
            result *= numbers[i + 1]
        elif operators[i] == '|':
            result = int(str(result) + str(numbers[i + 1]))
    return result

def bfs_find_combination(numbers, target):
    queue = deque([(numbers[0], 0, "")])
    while queue:
        current_value, index, ops = queue.popleft()
        if index == len(numbers) - 1:
            if current_value == target:
                return True
            continue
        for op in '+*|':
            next_value = current_value
            if op == '+':
                next_value += numbers[index + 1]
            elif op == '*':
                next_value *= numbers[index + 1]
            elif op == '|':
                next_value = int(str(next_value) + str(numbers[index + 1]))
            queue.append((next_value, index + 1, ops + op))
    return False

def main(input):
    total_calibration_result = 0
    lines = input.strip().split('\n')
    for line in lines:
        test_value, numbers = line.split(': ')
        test_value = int(test_value)
        numbers = list(map(int, numbers.split()))
        if bfs_find_combination(numbers, test_value):
            total_calibration_result += test_value
    return total_calibration_result

if __name__ == "__main__":
    # Read the strategy from the input file.
    with open('input.txt') as f:
        input = f.read()

    # Calculate and print the total score for the strategy.
    result = main(input)
    print("final result: ", result)
