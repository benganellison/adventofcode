#! /usr/bin/env python
# Dijkstra's
import heapq
import copy
import curses
import time
import argparse


def draw_maze(maze, stdscr):
    stdscr.clear()
    for i, line in enumerate(maze):
        line_to_print = "".join(line)
        stdscr.addstr(i, 0, line_to_print)


def show_path(path, stdscr):

    orientations = [">", "v", "<", "^"]
    for x, y, rotation in path:
        stdscr.addstr(y, x, orientations[rotation], curses.color_pair(1))
    stdscr.refresh()
    time.sleep(0.0001)


def hide_path(path, stdscr):

    orientations = [">", "v", "<", "^"]

    for x, y, rotation in path:
        stdscr.addstr(y, x, orientations[rotation], curses.color_pair(3))


def reconstruct_path(prev, end_node):
    path = []
    current = end_node
    while current in prev:
        path.append(current)
        current = prev[current]
    path.append(current)
    path.reverse()
    return path


def generate_graph(maze, start_state):
    graph = {}
    queue = [start_state]
    visited = set()
    graph[(start_state)] = {}
    directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    while queue:
        x, y, direction = queue.pop(0)
        if (x, y, direction) in visited:
            continue
        visited.add((x, y, direction))

        for i in [-1, 0, 1]:
            new_direction = (direction + i) % 4
            if new_direction != direction:
                graph[(x, y, direction)][(x, y, new_direction)] = 1000
                if (x, y, new_direction) not in graph:
                    graph[(x, y, new_direction)] = {}
                if (x, y, new_direction) in visited:
                    continue

            dx, dy = directions[new_direction]
            newx = x + dx
            newy = y + dy
            if newx >= 0 and newx < len(maze[0]) and newy >= 0 and newy < len(maze):
                if maze[newy][newx] != "#":
                    if (newx, newy, new_direction) not in graph:
                        graph[(newx, newy, new_direction)] = {}
                    graph[(x, y, new_direction)][(newx, newy, new_direction)] = 1
                    if (newx, newy, new_direction) in visited:
                        continue
                    queue.append((newx, newy, new_direction))

    return graph


def dijkstra(graph, start, end, maze, stdscr):
    queue = [(0, start)]
    prev = {}
    visited = {}

    while queue:
        cost, node = heapq.heappop(queue)

        if (node[0], node[1]) == end:
            return cost, reconstruct_path(prev, node)

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
            hide_path(reconstruct_path(prev, node), stdscr)

    return -1, []


def Red(skk):
    return "\033[91m{}\033[00m".format(skk)


def main(input, stdscr):

    maze = [list(row) for row in input.split("\n")]
    start, end = find_start_end(maze)
    if stdscr:
        draw_maze(maze, stdscr)
    graph = generate_graph(maze, start)
    result, path = dijkstra(graph, start, end, maze, None)
    if stdscr:
        show_path(path, stdscr)
    result, path = dijkstra(graph, start, end, maze, stdscr)
    if stdscr:
        show_path(path, stdscr)
    return result


def find_start_end(maze):
    start = (0,0)
    end = (0,0)
    for rowindex, row in enumerate(maze):
        for colindex, col in enumerate(row):
            if col == "S":
                start = (colindex, rowindex, 0)
            elif col == "E":
                end = (colindex, rowindex)
    return start,end


def wrapper(stdscr):
    curses.init_pair(1, curses.COLOR_RED, curses.COLOR_WHITE)
    curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)
    curses.init_pair(3, 134, 1)
    with open("input.txt") as f:
        input = f.read()
    result = main(input, stdscr)
    time.sleep(15)
    curses.endwin()
    print("final result: ", result)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-v", "--visualize", help="visualize graph", action="store_true")
    args = parser.parse_args()
    if args.visualize:
        curses.wrapper(wrapper)
    else:
        with open("input.txt") as f:
            input = f.read()
        result = main(input, None)
