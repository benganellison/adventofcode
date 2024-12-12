#! /usr/bin/env python
from collections import deque, defaultdict

def explore_new_regions(land_map:list[list[str]]):
    landtypes = defaultdict(list[tuple])
    for y, ys in enumerate(land_map):
        for x, land_type in enumerate(ys):
            landtypes[land_type].append((x, y))

    return landtypes


def find_regions_not_connected(landtypes: list[list[str]]):
    # Check if the coordinate is already in the previous regions.

    # Check if the coordinate is connected to the previous regions.
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    que = deque()
    regions = []
    # For each land type, check if the regions are connected.
    for land_type, coords in landtypes.items():
        previous_regions = []
        for coord in coords:
            region = []
            if coord in previous_regions:
                continue
            que.append(coord)
            while que:
                x, y = que.popleft()
                if (x, y) in previous_regions:
                    continue
                for dx, dy in directions:
                    new_x, new_y = x + dx, y + dy
                    if (new_x, new_y) in landtypes[land_type] and (
                        new_x,
                        new_y,
                    ) not in previous_regions:
                        que.append((new_x, new_y))
                region.append((x, y))
                previous_regions.append((x, y))
            regions.append(region)
    return regions


def calculate_perimeter_cost(regions: dict[str, list[tuple]]):

    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    total_cost = 0
    for coords in regions:
        perimeter = 0
        for coord in coords:
            for dx,dy in directions:
                new_coord = (coord[0] + dx, coord[1] + dy)
                if new_coord in coords:
                    continue
                perimeter += 1
        total_cost += perimeter * len(coords)
        print(perimeter, len(coords), coords, total_cost)

    return total_cost


def main(input):
    land_map = input.split("\n")
    land_map = [list(row) for row in land_map]
    landtypes = explore_new_regions(land_map)
    regions = find_regions_not_connected(landtypes)
    print(landtypes)
    result = calculate_perimeter_cost(regions)
    return result


if __name__ == "__main__":
    # Read the strategy from the input file.
    with open('input.txt') as f:
        input = f.read()

    # Calculate and print the total score for the strategy.
    result = main(input)
    print("final result: ", result)
