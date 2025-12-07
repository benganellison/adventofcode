#! /usr/bin/env python
import math
def parse_problem_input(input):
    problems = []
    lines = input.splitlines()
    for col, operation in enumerate(lines[-1]):
        if operation in ("*", "+"):
            problems.append({'index': col, 'operation': operation, 'numbers': []})

    for line in lines[:-1]:
        for ind, problem in enumerate(problems):
            start_of_number = problem['index']
            end_of_number = len(line)
            if ind + 1 < len(problems):
                end_of_number = problems[ind + 1]["index"] - 1
            #for i,number in enumerate(line[start_of_number:end_of_number][::-1]):
            for i,number in enumerate(line[start_of_number:end_of_number]):
                if i < len(problem["numbers"]):
                    problem["numbers"][i] = int(str(problem["numbers"][i]) + number)
                else:
                    problem["numbers"].append(int("0"+number))


    return problems


def solve_problem(problem):
    #print("solving problem:", problem)
    if problem["operation"] == "*":
        return math.prod(problem["numbers"])
    elif problem['operation'] == "+":
        return sum(problem['numbers'])


def main(input):
    problems = parse_problem_input(input)
    #print(problems)
    result = 0
    for problem in problems:
        problem_result = solve_problem(problem)
        #print("result:", problem_result)
        result += problem_result


    return result


if __name__ == "__main__":
    # Read the strategy from the input file.
    with open("input.txt") as f:
        input = f.read()

    # Calculate and print the total score for the strategy.
    result = main(input)
    print("final result: ", result)
