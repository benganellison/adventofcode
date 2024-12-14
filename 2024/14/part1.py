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
        robots.append({
            "start_pos": (x, y),
            "vel": (vel_x, vel_y)
        })
    max_x += 1
    max_y += 1
    half_x = max_x // 2
    half_y = max_y // 2
    print(max_x, max_y, half_x, half_y)
    iterations = 100
    quadrants = [0,0,0,0]
    print(robots)
    with open("output.txt", "w") as f:
        temporary_map = [[0 for _ in range(max_x)] for _ in range(max_y)]
        for robot in robots:
            x,y = robot["start_pos"]
            vel_x, vel_y = robot["vel"]
            new_x = (x + vel_x * iterations) % max_x
            new_y = (y + vel_y * iterations) % max_y
            print(new_x, new_y)
            temporary_map[new_y][new_x] += 1
            if new_x == half_x and new_y == half_y:
                continue
            elif new_x == half_x:
                continue
            elif new_y == half_y:
                continue
            elif new_x < half_x and new_y < half_y:
                quadrants[0] += 1
            elif new_x > half_x and new_y < half_y:
                quadrants[1] += 1
            elif new_x > half_x and new_y > half_y:
                quadrants[2] += 1
            elif new_x < half_x and new_y > half_y:
                quadrants[3] += 1

        f.write("\n".join(["".join([n if n != '0' else '.' for n in map(str, row)]) for row in temporary_map]))

    print(quadrants)

    result = prod(quadrants)
    return result


if __name__ == "__main__":
    # Read the strategy from the input file.
    with open('input.txt') as f:
        input = f.read()

    # Calculate and print the total score for the strategy.
    result = main(input)
    print("final result: ", result)
