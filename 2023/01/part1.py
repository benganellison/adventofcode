import re


def main(input):
    result = 0
    first_digit = re.compile(r"^[^\d]*(\d)")
    last_digit = re.compile(r"(\d)[^\d]*$")
    for line in input.splitlines():
        print("line: ", line)
        first = int(first_digit.search(line).group(1))
        last = int(last_digit.search(line).group(1))
        print("first: ", first, "last: ", last)
        line_value = first * 10 + last
        print("line_value: ", line_value)
        result += line_value
        print("result: ", result)
    return result


if __name__ == "__main__":
    # Read the strategy from the input file.
    with open("input.txt") as f:
        input = f.read()

    # Calculate and print the total score for the strategy.
    result = main(input)
    print("final result: ", result)
