item_priority = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"


def get_total_priorities(input):
    priorities = 0
    lines = input.strip().split("\n")
    #batches of 3 lines
    for i in range(0, len(lines), 3):
        print(lines[i:i+3])
        common = set(lines[i]).intersection(*lines[i+1:i+3])
        print(common)
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