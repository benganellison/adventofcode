#! /usr/bin/env python
from collections import deque, defaultdict

def explore_new_regions(land_map: list[list[str]]):
    landtypes = defaultdict(list)
    for y, ys in enumerate(land_map):
        for x, land_type in enumerate(ys):
            landtypes[land_type].append((x, y))
    return landtypes

def find_regions_not_connected(landtypes: dict[str, list[tuple]]):
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    que = deque()
    regions = []
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
                    if (new_x, new_y) in landtypes[land_type] and (new_x, new_y) not in previous_regions:
                        que.append((new_x, new_y))
                region.append((x, y))
                previous_regions.append((x, y))
            regions.append(region)
    return regions

def find_islands(coords: list[tuple]):
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    que = deque()
    connected_areas = []
    max_x, max_y, min_x, min_y = find_max_min(coords)
    empty_area = get_empty_areas(coords, (min_x, min_y, max_x, max_y))
    checked = set()
    for coord in empty_area:
        if any(coord in area for area in connected_areas):
            continue
        que.append(coord)
        island = []
        while que:
            x, y = que.popleft()
            if (x, y) in island or (x, y) in checked:
                continue
            if any(coord in area for area in connected_areas):
                continue
            island.append((x, y))
            checked.add((x, y))
            for dx, dy in directions:
                new_x, new_y = x + dx, y + dy
                if (new_x, new_y) in empty_area:
                    if (new_x, new_y) not in checked:
                        que.append((new_x, new_y))
        connected_areas.append(island)
    return connected_areas

def get_empty_areas(coords, boundaries):
    empty_area = []
    min_x, min_y, max_x, max_y = boundaries
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

def calculate_perimeter_cost(regions: list[list[tuple]]):
    total_cost = 0
    for coords in regions:
        perimeter, visited = get_outer_bounds(coords)
        connected_areas = find_islands(coords)
        connected_areas = [area for area in connected_areas if not any((x, y) in area for x, y, _ in visited)]
        for area in connected_areas:
            new_perimeter, _ = get_outer_bounds(area)
            perimeter += new_perimeter
        total_cost += perimeter * len(coords)
    return total_cost

def get_outer_bounds(coords):
    directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    diagonals = [(1, 1), (-1, 1), (-1, -1), (1, -1)]
    start_coord = (coords[0][0], coords[0][1] - 1)
    direction = 0
    perimeter = 0
    visited = set()
    left_turns = 0
    current_coord = start_coord
    safty = 0
    while (*current_coord, direction) not in visited:
        next_coord = tuple(map(sum, zip(current_coord, directions[direction])))
        diagonally_right = tuple(map(sum, zip(current_coord, diagonals[direction])))
        if next_coord in coords:
            visited.add((*current_coord, direction))
            if left_turns == 4:
                break
            direction = (direction - 1) % 4
            perimeter += 1
            left_turns += 1
        elif diagonally_right in coords:
            left_turns = 0
            visited.add((*current_coord, direction))
            current_coord = next_coord
            continue
        else:
            visited.add((*current_coord, direction))
            direction = (direction + 1) % 4
            perimeter += 1
            current_coord = diagonally_right
            left_turns = 0
        safty += 1
        if safty > 1000:
            break
    return perimeter, visited

def main(input):
    land_map = input.split("\n")
    land_map = [list(row) for row in land_map]
    landtypes = explore_new_regions(land_map)
    regions = find_regions_not_connected(landtypes)
    result = calculate_perimeter_cost(regions)
    return result

if __name__ == "__main__":
    with open("input.txt") as f:
        input = f.read()
    result = main(input)
    print("final result:", result)
