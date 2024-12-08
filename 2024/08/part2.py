#! /usr/bin/env python


def find_antinodes(frequency_map, grid_width, grid_height):
    antinodes = set()

    for frequency, coords in frequency_map.items():
        for (x1, y1), (x2, y2) in [
            (coords[i], coords[j])
            for i in range(len(coords))
            for j in range(i + 1, len(coords))
        ]:
            dx, dy = x2 - x1, y2 - y1

            x = x1
            y = y1

            while 0 <= x < grid_width and 0 <= y < grid_height:
                antinodes.add((x, y))
                x += dx
                y += dy

            x = x2
            y = y2

            while 0 <= x < grid_width and 0 <= y < grid_height:
                antinodes.add((x, y))
                x -= dx
                y -= dy

    return antinodes


def main(input):
    input_set = set(input).difference(set("\n.#"))

    frequency_map = {}
    for y, val in enumerate(input.split("\n")):
        for x, antenna in enumerate(val):
            if antenna not in input_set:
                continue
            elif antenna in frequency_map:
                frequency_map[antenna].append((x, y))
            else:
                frequency_map[antenna] = [(x, y)]

    antinodes = find_antinodes(
        frequency_map, len(input.split("\n")[0]), len(input.split("\n"))
    )

    result = len(antinodes)

    for y, val in enumerate(input.split("\n")):
        line = ""
        for x, antenna in enumerate(val):
            if antenna in frequency_map:
                line += antenna
            elif (x, y) in antinodes:
                line += "#"
            else:
                line += "."
        print(line)

    return result


if __name__ == "__main__":
    # Read the strategy from the input file.
    with open("input.txt") as f:
        input = f.read()

    # Calculate and print the total score for the strategy.
    result = main(input)
    print("final result: ", result)
