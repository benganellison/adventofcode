#! /usr/bin/env python
from collections import deque, defaultdict

def explore_new_regions(land_map: list[list[str]]):
    landtypes = defaultdict(list)
    for y, ys in enumerate(land_map):
        for x, land_type in enumerate(ys):
            landtypes[land_type].append((x, y))
    return landtypes

def bfs(start, valid_neighbors):
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    que = deque([start])
    visited = set()
    region = []
    while que:
        x, y = que.popleft()
        if (x, y) in visited:
            continue
        visited.add((x, y))
        region.append((x, y))
        for dx, dy in directions:
            new_x, new_y = x + dx, y + dy
            if valid_neighbors(new_x, new_y):
                que.append((new_x, new_y))
    return region

def find_cost_of_fences(landtypes: dict[str, list[tuple]]):
    regions = []
    result = 0
    for land_type, coords in landtypes.items():
        previous_regions = set()
        for coord in coords:
            if coord in previous_regions:
                continue
            region = bfs(coord, lambda x, y: (x, y) in landtypes[land_type] and (x, y) not in previous_regions)
            previous_regions.update(region)
            regions.append(region)
            result += calculate_perimeter_cost(region)
    return result

def find_islands(coords: list[tuple]):
    empty_area = get_empty_areas(coords)
    connected_areas = []
    for coord in empty_area:
        if any(coord in area for area in connected_areas):
            continue
        island = bfs(
            coord, lambda x, y: (x, y) in empty_area and (x, y) not in connected_areas
        )
        connected_areas.append(island)
    return connected_areas


def get_empty_areas(coords):
    max_x, max_y, min_x, min_y = find_max_min(coords)
    return [(x, y) for x in range(min_x-1, max_x+1) for y in range(min_y-1, max_y+1) if (x, y) not in coords]


def find_max_min(coords):
    xs, ys = zip(*coords)
    return max(xs), max(ys), min(xs), min(ys)

def calculate_perimeter_cost(coords: list[tuple]):
    total_cost = 0
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
    current_coord = start_coord
    while (*current_coord, direction) not in visited:
        next_coord = tuple(map(sum, zip(current_coord, directions[direction])))
        diagonally_right = tuple(map(sum, zip(current_coord, diagonals[direction])))
        if not diagonally_right in coords:
            visited.add((*current_coord, direction))
            direction = (direction + 1) % 4
            perimeter += 1
            current_coord = diagonally_right
        elif next_coord in coords:
            direction = (direction - 1) % 4
            perimeter += 1
        elif diagonally_right in coords:
            visited.add((*current_coord, direction))
            current_coord = next_coord


    return perimeter, visited

def main(input):
    land_map = [list(row) for row in input.split("\n")]
    landtypes = explore_new_regions(land_map)
    result = find_cost_of_fences(landtypes)
    return result

if __name__ == "__main__":
    with open("input.txt") as f:
        input = f.read()
    result = main(input)
    print("final result:", result)
