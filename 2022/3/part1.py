item_priority = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"


def get_total_priorities(input):
    priorities = 0
    for line in input.strip().split("\n"):
        first_compartment = line[0 : len(line) // 2]
        second_compartment = line[
            len(line) // 2 if len(line) % 2 == 0 else ((len(line) // 2) + 1) :
        ]
        common = set(first_compartment).intersection(set(second_compartment))
        for item in common:
            priorities += item_priority.index(item)

        priorities += 1
    return priorities


if __name__ == "__main__":
    # Read the strategy from the input file.
    with open("input.txt") as f:
        input = f.read()

    # Calculate and print the total score for the strategy.
    result = get_total_priorities(input)
    print("final result: ", result)
