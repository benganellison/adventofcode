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
            antinode_1 = (x1 - dx, y1 - dy)
            antinode_2 = (x2 + dx, y2 + dy)

            print("testing", antinode_1, antinode_2)

            # Check if they are within bounds
            if (
                0 <= antinode_1[0] < grid_width
                and 0 <= antinode_1[1] < grid_height
            ):
                antinodes.add(antinode_1)
            if (
                0 <= antinode_2[0] < grid_width
                and 0 <= antinode_2[1] < grid_height
            ):
                antinodes.add(antinode_2)

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

    return result


if __name__ == "__main__":
    # Read the strategy from the input file.
    with open("input.txt") as f:
        input = f.read()

    # Calculate and print the total score for the strategy.
    result = main(input)
    print("final result: ", result)
