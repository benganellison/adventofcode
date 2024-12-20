#! /usr/bin/env python
def parse_input_integers(input):
    return [int(x) for x in input.splitlines()]

def parse_input_strings(input):
    return input.splitlines()

def parse_input_map(input):
    return [list(x) for x in input.splitlines()]

def parse_input_grid_of_int(input):
    return [[int(x) for x in y] for y in input.splitlines()]

def parse_input_tuples(input):
    return [tuple(map(int, x.split(',')) for x in input.splitlines())]
            
def main(input):
    result = ""
    return result


if __name__ == "__main__":
    # Read the strategy from the input file.
    with open('input.txt') as f:
        input = f.read()

    # Calculate and print the total score for the strategy.
    result = main(input)
    print("final result: ", result)
