#! /usr/bin/env python
import re
from math import prod

def main(input):
    """

    input = '''p=7,3 v=-1,2
    p=2,4 v=2,-3
    p=9,5 v=-3,-3'''
    """
    pattern = re.compile(r"p=(-?\d+),(-?\d+) v=(-?\d+),(-?\d+)")
    max_x, max_y = 0, 0
    robots = []
    for match in pattern.finditer(input):
        x, y, vel_x, vel_y = map(int, match.groups())
        if x > max_x:
            max_x = x
        if y > max_y:
            max_y = y
        robots.append({"start_pos": (x, y), "vel": (vel_x, vel_y)})
    max_x += 1
    max_y += 1
    half_x = (max_x+1) // 2
    half_y = (max_y+1) // 2
    print(max_x, max_y, half_x, half_y)
    iterations = 10000
    quadrants = [0, 0, 0, 0]
    # print(robots)
    text = ""
    # open file for wrting
    temporary_map = [[0 for _ in range(max_x)] for _ in range(max_y)]
    with open("output.txt", "w") as f:
        for i in range(iterations):
            for row in temporary_map:
                for j in range(len(row)):
                    row[j] = 0
            for robot in robots:
                x, y = robot["start_pos"]
                vel_x, vel_y = robot["vel"]
                new_x = (x + vel_x * i) % (max_x )
                new_y = (y + vel_y * i) % (max_y)
                temporary_map[new_y][new_x] += 1
                if temporary_map[new_y][new_x] > 1:
                    break
            else:
                text = (
                    "\n".join(
                        [
                            "".join([n if n != "0" else " " for n in map(str, row)])
                            for row in temporary_map
                        ]
                    )
                )
                name = f"iteration_{i}"
                f.write(f"\n\n\n{name}\n")
                f.write(text)
            continue

            

    # print(text)
    print("x_max: ", max_x, "y_max: ", max_y)
    print(quadrants)

    result = prod(quadrants)
    return result


if __name__ == "__main__":
    # Read the strategy from the input file.
    with open("input.txt") as f:
        input = f.read()

    # Calculate and print the total score for the strategy.
    result = main(input)
    print("final result: ", result)
