#! /usr/bin/env python
def parse_input_integers(input):
    return


def main(input):
    combinations = [(x[0], int(x[1:])) for x in input.splitlines()]
    val = 50
    result = 0

    for combination in combinations:
        previous_val = val

        # Apply movement
        if combination[0] == "L":
            val -= combination[1]
        else:  # "R"
            val += combination[1]

        if val < 0:
            if previous_val == 0:
                result += abs(val) // 100
                # print(
                #     (abs(val) // 100),
                #     f"count for val: {val=}, {previous_val=}, mod {val % 100}",
                # )
            else:
                result += (abs(val) // 100) + 1
                # print(
                #     (abs(val) // 100) + 1,
                #     f"count for val: {val=}, {previous_val=}, mod {val % 100}",
                # )

        elif val >= 100:
            result += (val // 100)
            # print(
            #     (val // 100),
            #     f"count for val: {val=}, {previous_val=}, mod {val % 100}",
            # )

        elif val == 0 and previous_val != 0:
            result += 1
            # print("1 count for val: ", val)
        # else:
        #     print("val: ", val)

        val %= 100

    return result


if __name__ == "__main__":
    # Read the strategy from the input file.
    with open("input.txt") as f:
        input = f.read()

    # Calculate and print the total score for the strategy.
    result = main(input)
    print("final result: ", result)
