#! /usr/bin/env python
def main(input):

    banks = [[int(x) for x in y] for y in input.splitlines()]
    best_batteries = []
    for batteries in banks:
        bank = ""
        index_previous_battery = 0
        for last_allowed_index in range(len(batteries) - 12 + 1, len(batteries) + 1):
            highest_jolt = max(batteries[index_previous_battery:last_allowed_index])
            index_previous_battery = batteries.index(
                highest_jolt, index_previous_battery, last_allowed_index
            ) + 1
            bank += str(highest_jolt)

        best_batteries.append(int(bank))

    result = sum(best_batteries)
    return result


if __name__ == "__main__":
    # Read the strategy from the input file.
    with open("input.txt") as f:
        input = f.read()

    # Calculate and print the total score for the strategy.
    result = main(input)
    print("final result: ", result)
