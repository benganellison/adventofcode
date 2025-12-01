#! /usr/bin/env python
def parse_input_integers(input):
    return 


def main(input):
    combinations =  ([(x[0], int(x[1:])) for x in input.splitlines()])
    val = 50
    result = 0
    for combination in combinations:
        if combination[0] == "L":
            val -= combination[1]
            val %= 100
        elif combination[0] == "R":
            val += combination[1]
            val %= 100
        print("val: ", val)
        if val == 0:
            result += 1

    return result


if __name__ == "__main__":
    # Read the strategy from the input file.
    with open('input.txt') as f:
        input = f.read()

    # Calculate and print the total score for the strategy.
    result = main(input)
    print("final result: ", result)
