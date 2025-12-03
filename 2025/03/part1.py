#! /usr/bin/env python
def parse_input_grid_of_int(input):
    return [[int(x) for x in y] for y in input.splitlines()]


def main(input):

    banks = parse_input_grid_of_int(input)

    best_batteries = []
    for batteries in banks:
        highest = max(batteries)
        index_highest = batteries.index(highest)
        batteries[index_highest] = 0
        if index_highest != len(batteries) - 1:
            # find next highest
            next_highest = max(batteries[index_highest + 1:])
            best_batteries.append(int(str(highest) + str(next_highest)))
        else:
            next_highest = max(batteries[:index_highest])
            best_batteries.append(int(str(next_highest) + str(highest)))

    result = sum(best_batteries)
    return result


if __name__ == "__main__":
    # Read the strategy from the input file.
    with open('input.txt') as f:
        input = f.read()

    # Calculate and print the total score for the strategy.
    result = main(input)
    print("final result: ", result)
