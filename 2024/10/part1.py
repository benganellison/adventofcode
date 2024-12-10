#! /usr/bin/env python

def construct_map(input: str) -> list[list[int]]:
    result = []
    for line in input.split("\n"):
        result.append([int(x) for x in list(line)])
    return result


def bfs_increasing_numbers(map: list[list[int]], start_coord) -> set[tuple[int, int]]:

    queue = [start_coord]
    visited = set()
    result = set()
    while queue:
        print(queue)
        x,y = queue.pop()
        print(x)
        val = map[x][y]

        if val == 9:
            result.add((x, y))
            continue

        print(x, y, val, result)
        for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            if x + dx < 0 or y + dy < 0 or x + dx >= len(map) or y + dy >= len(map[0]):
                continue
            if map[x+dx][y+dy] == val+1:
                if (x+dx, y+dy) not in visited:
                    visited.add((x+dx, y+dy))
                    queue.append((x+dx, y+dy))
    print(result)

    return result


def find_start(map: list[list[int]]) -> list[tuple[int,int]]:
    result = []
    for i in range(len(map)):
        for j in range(len(map[0])):
            if map[i][j] == 0:
                result.append((i, j))
    return result

def main(input):
    map = construct_map(input)
    start = find_start(map)
    print(start)
    print(map)
    result = 0
    for s in start:
        result += len(bfs_increasing_numbers(map, s))

    return result


if __name__ == "__main__":
    # Read the strategy from the input file.
    with open('input.txt') as f:
        input = f.read()

    # Calculate and print the total score for the strategy.
    result = main(input)
    print("final result: ", result)
