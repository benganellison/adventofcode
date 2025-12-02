#! /usr/bin/env python
def parse_product_range(input):
    return input.split(',')


def main(input):
    product_ranges = parse_product_range(input)
    result = 0
    for product_range in product_ranges:
        range_parts = product_range.split('-')
        count = 0
        for i in range(int(range_parts[0]), int(range_parts[1]) + 1):
            id = str(i)
            length = len(id)
            if id[:length // 2] == id[length // 2:]:
                count += 1
                result += i


    return result


if __name__ == "__main__":
    # Read the strategy from the input file.
    with open('input.txt') as f:
        input = f.read()

    # Calculate and print the total score for the strategy.
    result = main(input)
    print("final result: ", result)
