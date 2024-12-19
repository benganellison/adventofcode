#! /usr/bin/env python
from itertools import product
from collections import deque


def bfs(graph, start, end):
    queue = deque([(start, 0)])
    visited = set([start])

    while queue:
        current, path_length = queue.popleft()
        if current == end:
            return path_length

        for neighbor in graph[current]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append((neighbor, path_length + 1))

    return -1


def create_graph(errors, size, fallenbytes):
    graph = {}
    relevant_errors = errors[:fallenbytes]
    directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]

    for i, j in product(range(size), range(size)):
        if (i, j) not in relevant_errors:
            graph[(i, j)] = set()
            for dx, dy in directions:
                x = i + dx
                y = j + dy
                if 0 <= x < size and 0 <= y < size:
                    coord = (x, y)
                    if coord not in relevant_errors:
                        graph[(i, j)].add(coord)
    return graph


def main(input, size, fallenbytes):
    errors = []
    for line in input.split("\n"):
        if line:
            coordinate = tuple(map(int, line.split(",")))
            errors.append(coordinate)

    graph = create_graph(errors, size, fallenbytes)
    result = bfs(graph, (0, 0), (size - 1, size - 1))

    return result


if __name__ == "__main__":
    with open("input.txt") as f:
        input = f.read()

    result = main(input, 71, 1024)
    print("final result: ", result)
