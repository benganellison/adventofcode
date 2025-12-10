#! /usr/bin/env python
def parse_input_pairs_of_int(instr):
    return [tuple(int(x) for x in range.split(",")) for range in instr.splitlines()]

def main(input):

    corners = parse_input_pairs_of_int(input)

    largest_area = 0
    for i, corner in enumerate(corners):
        for j, other_corner in enumerate(corners):
            if i == j:
                continue
            x1, y1 = corner
            x2, y2 = other_corner

            hight = abs(x1 - x2) + 1
            width = abs(y1 - y2) + 1
            area = hight * width
            if area > largest_area:
                largest_area = area
            if corner == (2,5) and other_corner == (9,7):
                print("area between (2,5) and (9,7): ", area)
            elif corner == (7,1) and other_corner == (11,7):
                print("area between (7,1) and (11,7): ", area)
            elif corner == (2,5) and other_corner == (11,1):
                print("area between (2,5) and (11,1): ", area)



    result = largest_area
    return result


if __name__ == "__main__":
    # Read the strategy from the input file.
    with open("input.txt") as f:
        input = f.read()

    # Calculate and print the total score for the strategy.
    result = main(input)
    print("final result: ", result)
