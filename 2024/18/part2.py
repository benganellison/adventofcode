#! /usr/bin/env python
from itertools import product
from collections import deque


def bfs(graph, start, end):
    queue = deque([(start, 0, [start])])
    visited = set([start])

    while queue:
        current, path_length, path = queue.popleft()
        if current == end:
            return path_length, path

        for neighbor in graph[current]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append((neighbor, path_length + 1, path + [neighbor]))

    return -1, []


def create_graph(errors, size):
    graph = {}
    directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]

    for i, j in product(range(size), range(size)):
        if (i, j) not in errors:
            graph[(i, j)] = set()
            for dx, dy in directions:
                x = i + dx
                y = j + dy
                if 0 <= x < size and 0 <= y < size:
                    coord = (x, y)
                    if coord not in errors:
                        graph[(i, j)].add(coord)
    return graph


def main(input, size, fallenbytes):
    errors = []
    for line in input.split("\n"):
        if line:
            coordinate = tuple(map(int, line.split(",")))
            errors.append(coordinate)

    graph = create_graph(errors[:fallenbytes], size)
    shortest_path, latest_path = bfs(graph, (0, 0), (size - 1, size - 1))
    result = ""
    for i in range(fallenbytes, len(errors)):
        if errors[i-1] in latest_path:
            graph = create_graph(errors[:i], size)
            shortest_path, latest_path = bfs(graph, (0, 0), (size - 1, size - 1))
            if shortest_path == -1:
                result = errors[i - 1]
                break

    return f"{result[0]},{result[1]}"


if __name__ == "__main__":
    with open("input.txt") as f:
        input = f.read()

    result = main(input, 71, 1024)
    print("final result: ", result)
