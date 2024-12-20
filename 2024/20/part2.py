#! /usr/bin/env python
# Dijkstra's
import heapq
import copy
import curses
import time
import argparse
from collections import deque


def draw_maze(maze, stdscr):
    stdscr.erase()
    for i, line in enumerate(maze):
        line_to_print = "".join(line)
        stdscr.addstr(i, 0, line_to_print)


def show_path(path, stdscr):
    for x, y in path:
        stdscr.addstr(y, x, 'o', curses.color_pair(1))
    stdscr.refresh()
    time.sleep(0.0001)


def hide_path(path, stdscr):

    for x, y in path:
        stdscr.addstr(y, x, 'o')


def reconstruct_path(prev, end_node):
    path = []
    current = end_node
    while current in prev:
        path.append(current)
        current = prev[current]
    path.append(current)
    path.reverse()
    return path


def generate_graph(walls, start_state, max_x, max_y):
    graph = {}
    queue = [start_state]
    visited = set()
    graph[(start_state)] = {}
    directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    while queue:
        x, y = queue.pop(0)
        if (x, y) in visited:
            continue
        visited.add((x, y))

        for dx, dy in directions:
            next_x = x + dx
            next_y = y + dy
            if next_x >= 0 and next_x < max_x and next_y >= 0 and next_y < max_y:
                if (next_x, next_y) in walls:
                    continue
                if (next_x, next_y) not in graph:
                    graph[(next_x, next_y)] = {}
                graph[(x, y)][(next_x, next_y)] = 1
                if (next_x, next_y) in visited:
                    continue
                queue.append((next_x, next_y))

    return graph


def dijkstra(graph, start, end, stdscr):
    queue = [(0, start)]
    prev = {}
    visited = {}

    while queue:
        cost, node = heapq.heappop(queue)

        if (node[0], node[1]) == end:
            return reconstruct_path(prev, node)

        if node in visited and visited[node] < cost:
            continue

        visited[node] = cost

        for neighbor, weight in graph[node].items():
            new_cost = cost + weight
            if neighbor in visited and visited[node] < new_cost:
                continue
            prev[neighbor] = node
            heapq.heappush(queue, (new_cost, neighbor))
        if stdscr:
            show_path(reconstruct_path(prev, node), stdscr)
            # hide_path(reconstruct_path(prev, node), stdscr)

    return []


def Red(skk):
    return "\033[91m{}\033[00m".format(skk)


def closest_path_two_coordinates(start, end):
    """returns a path with all coordinates between start and end, including start and end"""
    path = set()
    x1, y1 = start
    x2, y2 = end

    step_x = 1 if x2 > x1 else -1
    for x in range(x1, x2 + step_x, step_x):
        if (x, y1) != end:
            path.add((x, y1))

    step_y = 1 if y2 > y1 else -1
    for y in range(y1 + step_y, y2 + step_y, step_y):
        if (x2, y) != end:
            path.add((x2, y))

    return list(path)


def main(input, picoseconds=100, no_of_cheats=20, stdscr=None):

    maze = [list(n) for n in input.split("\n")]
    max_x = len(maze[0])
    max_y = len(maze)
    walls = find_walls(maze)
    start, end = find_start_end(maze)
    result = 0
    saves_exactly = 0
    graph = generate_graph(walls, start, max_x, max_y)
    original_path = dijkstra(graph, start, end, None)
    if stdscr:
        stdscr.clear()
        draw_maze(maze, stdscr)
        show_path(original_path, stdscr)
    for i in range(len(original_path)):
        for j in range(i+1, len(original_path)):
            distance = abs(original_path[i][0] - original_path[j][0]) + abs(original_path[i][1] - original_path[j][1])

            if distance <= no_of_cheats:
                start, end = original_path[i], original_path[j]
                shortcut = closest_path_two_coordinates(start, end)

                new_path = original_path[:i] + shortcut + original_path[j:]
                savings = len(original_path) - len(new_path)

                # print("new_path", new_path)
                if savings == picoseconds:
                    saves_exactly += 1
                if savings >= picoseconds:
                    result += 1
                    if stdscr:
                        show_path(new_path, stdscr)
                        time.sleep(0.001)
                        draw_maze(maze, stdscr)

    print("result", result, "saves_exactly", saves_exactly)

    return result, saves_exactly

def find_walls(maze):
    walls = set()
    for rowindex, row in enumerate(maze):
        for colindex, col in enumerate(row):
            if col == "#":
                walls.add((colindex, rowindex))
    return walls


def find_start_end(maze):
    start = (0, 0)
    end = (0, 0)
    for rowindex, row in enumerate(maze):
        for colindex, col in enumerate(row):
            if col == "S":
                start = (colindex, rowindex)
            elif col == "E":
                end = (colindex, rowindex)
    return start, end


def wrapper(stdscr):
    curses.init_pair(1, curses.COLOR_RED, curses.COLOR_WHITE)
    curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)
    curses.init_pair(3, 134, 1)
    with open("input.txt") as f:
        input = f.read()
    result, _ = main(input, picoseconds=100, no_of_cheats=20, stdscr=stdscr)
    time.sleep(15)
    curses.endwin()
    print("final result: ", result)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-v", "--visualize", help="visualize graph", action="store_true"
    )
    args = parser.parse_args()
    if args.visualize:
        curses.wrapper(wrapper)
    else:
        with open("input.txt") as f:
            input = f.read()
        result = main(input, picoseconds=100, no_of_cheats=20, stdscr=None)
        print(result)
