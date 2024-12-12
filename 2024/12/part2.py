#! /usr/bin/env python
from collections import deque, defaultdict


def explore_new_regions(land_map: list[list[str]]):
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
        # if land_type != "C":
        #     continue
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


def find_islands(coords: list[list[str]]):
    # print("coords: ", coords)
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    que = deque()
    connected_areas = []
    # create a full matrix with size max value in coords [(x,y)] and fill with . for coords not in coords
    max_x, max_y, min_x, min_y = find_max_min(coords)

    empty_area = get_empty_areas(coords, (min_x, min_y, max_x, max_y))
    print("empty_area: ", empty_area, "max_x, max_y, min_x, min_y: ", max_x, max_y, min_x, min_y)

    checked = set()
    for coord in empty_area:

        if any(coord in area for area in connected_areas):
            continue
        # elif len(connected_areas) > 0:
        #     print(f"coord not in connected_areas: {coord}, {connected_areas}")
        #     return connected_areas
        que.append(coord)
        # print(f"Initial queue: {que}")
        # print(f"Initial queue: {que}")
        island = []
        while que:
            x, y = que.popleft()
            # print(f"Popped from queue: {(x, y)}")
            if (x, y) in island or (x, y) in checked:
                # print(f"Already in island: {(x, y)}")
                # print(f"Queue: {que}")
                continue
            if any(coord in area for area in connected_areas):
                # print(f"Coordinate {coord} already in connected areas")
                # print(f"Queue: {que}")
                continue
            island.append((x, y))
            checked.add((x, y))

            # print(f"Added to island: {(x, y)}")

            for dx, dy in directions:
                new_x, new_y = x + dx, y + dy
                # print(f"Checking new coordinates: {(new_x, new_y)}")
                if (new_x, new_y) in empty_area:
                    # print(f"New coordinates are in empty area: {(new_x, new_y)}")
                    if (new_x, new_y) not in checked:
                        # print(f"Adding to queue: {(new_x, new_y)}")
                        que.append((new_x, new_y))
            # print(f"Queue: {que}")
        connected_areas.append(island)
        # print(f"island: {island}")
    # print(f"empty_area: {empty_area}")
    return connected_areas

def get_empty_areas(coords, bounderies):
    empty_area = []
    min_x, min_y, max_x, max_y = bounderies
    for x in range(min_x, max_x):
        for y in range(min_y, max_y):
            if (x, y) not in coords:
                empty_area.append((x, y))
    return empty_area

def find_max_min(coords):
    max_x, max_y = 0, 0
    min_x, min_y = -1, -1
    for x, y in coords:
        if x > max_x:
            max_x = x
        if x < min_x or min_x == -1:
            min_x = x
        if y > max_y:
            max_y = y
        if y < min_y or min_y == -1:
            min_y = y
    return max_x, max_y, min_x, min_y


def calculate_perimeter_cost(regions: dict[str, list[tuple]]):

    total_cost = 0
    for coords in regions:
        perimeter, visited = get_outer_bounds(coords)
        print("perimeter", perimeter, "len(coords)", len(coords))

        connected_areas = find_islands(coords)
        print("More areas to explore: ", connected_areas)
        print("visited: ", visited)

        connected_areas = [
            area for area in connected_areas if not any((x,y) in area for x,y,d in visited)
        ]
        print("More areas to explore: ", connected_areas)
        for area in connected_areas:
            # print("connected_areas: ", area)
            new_perimeter, _ = get_outer_bounds(area)
            perimeter += new_perimeter

        total_cost += perimeter * len(coords)
        print(len(coords), perimeter, perimeter * len(coords), total_cost)

    return total_cost

def get_outer_bounds(coords):

    directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    diagonals = [(1, 1), (-1, 1), (-1, -1), (1, -1)]

    start_coord = (coords[0][0], coords[0][1]-1)
    print("start coord: ", start_coord)
    print("coords: ", coords)
    direction = 0
    perimeter = 0
    visited = set()
    left_turns = 0
    current_coord = start_coord
    safty = 0
    while (*current_coord, direction) not in visited:
        next_coord = tuple(map(sum, zip(current_coord, directions[direction])))
        diagonally_right = tuple(
                map(sum, zip(current_coord, diagonals[direction]))
            )
        # print(f"{current_coord=}, {next_coord=}, {diagonally_right=}")
        if next_coord in coords:
            # turn left
            if left_turns == 4:
                visited.add((*current_coord, direction))
                break
            direction = (direction - 1) % 4
            perimeter += 1
            left_turns += 1
            # print("turning left from ", current_coord, next_coord)
        elif diagonally_right in coords:
            left_turns = 0
            visited.add((*current_coord, direction))
            # print(
            #     f"moving forward from {current_coord} to: {next_coord}", perimeter, "diagonally_right: ", diagonally_right, diagonally_right in coords
            # )
            current_coord = next_coord
            continue
        else:
            # turn right
            visited.add((*current_coord, direction))
            direction = (direction + 1) % 4
            perimeter += 1
            # print(
            #     f"turning around corner from {current_coord} to: {diagonally_right}",
            #     perimeter,
            # )
            current_coord = diagonally_right
            left_turns = 0
            # print("corner found current pos: ",current_coord , perimeter)
        safty += 1
        if safty > 1000:
            print(f"safty break: {current_coord=}, {next_coord=}, {diagonally_right=}")
            print(f"coords: {coords}")
            print(f"visited: {visited}")
            print(f"(*current_coord, direction) {(*current_coord, direction)}")
            print(f"in visited: {(*current_coord, direction) in visited}")
            break

    # print(f"perimeter: {perimeter}")
    # print(f"in visited: {(*current_coord, direction)} in {visited}")
    return perimeter,visited


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
    with open("input.txt") as f:
        input = f.read()

    # Calculate and print the total score for the strategy.
    result = main(input)
    print("final result: ", result)
