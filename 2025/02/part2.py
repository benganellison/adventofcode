#! /usr/bin/env python
def parse_product_range(input):
    return input.split(",")

def find_invalid_products_in_range(start, end):
    result = 0
    for i in range(int(start), int(end) + 1):
        id = str(i)
        length = len(id)
        for j in range(length // 2):
            #print(f"Checking if Product ID {id} is invalid with segment length {j+1}, {id[:j+1]=} * {(length//(j+1))=} = {id[:j+1]*(length//(j+1))}")
            if (length//(j+1)*(j+1)) == length and id[:j+1]*(length//(j+1)) == id:
                result += i
                #print(f"Product ID {id} is invalid.")
                break
    return result


def main(input):
    product_ranges = parse_product_range(input)
    result = 0
    for product_range in product_ranges:
        range_parts = product_range.split("-")
        result += find_invalid_products_in_range(range_parts[0], range_parts[1])

    return result


if __name__ == "__main__":
    # Read the strategy from the input file.
    with open("input.txt") as f:
        input = f.read()

    # Calculate and print the total score for the strategy.
    result = main(input)
    print("final result: ", result)
