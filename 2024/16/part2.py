#! /usr/bin/env python
# Dijkstra's
import heapq
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


def generate_graph(maze, start_state):
    graph = {}
    directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    queue = [start_state]
    visited = set()
    graph[start_state] = {}

    while queue:
        x, y, direction = queue.pop(0)
        if (x, y, direction) in visited:
            continue
        visited.add((x, y, direction))

        for i in [-1, 0, 1]:
            new_direction = (direction + i) % 4
            if (x, y, new_direction) not in graph:
                graph[(x, y, new_direction)] = {}
            if new_direction != direction:
                graph[(x, y, direction)][(x, y, new_direction)] = 1000

            dx, dy = directions[new_direction]
            newx = x + dx
            newy = y + dy
            if 0 <= newx < len(maze[0]) and 0 <= newy < len(maze):
                if maze[newy][newx] != "#":
                    if (newx, newy, new_direction) not in graph:
                        graph[(newx, newy, new_direction)] = {}
                    graph[(x, y, new_direction)][(newx, newy, new_direction)] = 1
                    if (newx, newy, new_direction) not in visited:
                        queue.append((newx, newy, new_direction))

    return graph


def dijkstra(graph, start, end, maze):
    dist = {}
    dist[start] = 0
    queue = [(0, start)]

    while queue:
        cost, node = heapq.heappop(queue)
        if cost > dist[node]:
            continue

        for neighbor, weight in graph[node].items():
            new_cost = cost + weight
            if neighbor not in dist or new_cost < dist[neighbor]:
                dist[neighbor] = new_cost
                heapq.heappush(queue, (new_cost, neighbor))

    return dist


def back_propagate_shortest_paths(graph, dist, end, best_distance):
    end_states = [
        node
        for node, c in dist.items()
        if (node[0], node[1]) == end and c == best_distance
    ]

    shortest_path_states = set(end_states)

    reverse_graph = {}
    for u in graph:
        for v, w in graph[u].items():
            if v not in reverse_graph:
                reverse_graph[v] = []
            reverse_graph[v].append((u, w))

    stack = end_states[:]
    while stack:
        v = stack.pop()
        v_cost = dist[v]
        if v in reverse_graph:
            for u, w in reverse_graph[v]:
                if u in dist and dist[u] + w == v_cost:
                    if u not in shortest_path_states:
                        shortest_path_states.add(u)
                        stack.append(u)

    return shortest_path_states


def main(input, stdscr):
    maze = [list(row) for row in input.split("\n")]
    start, end = find_start_end(maze)
    if stdscr:
        draw_maze(maze, stdscr)

    graph = generate_graph(maze, start)
    dist = dijkstra(graph, start, end, maze)

    best_distance = min(dist[node] for node in dist if (node[0], node[1]) == end)

    shortest_path_states = back_propagate_shortest_paths(
        graph, dist, end, best_distance
    )

    best_seats = {(x, y) for (x, y, d) in shortest_path_states if maze[y][x] != "#"}

    result = len(best_seats)
    if stdscr:
        show_path(
            [
                (x, y, d)
                for (x, y, d) in back_propagate_shortest_paths(
                    graph,
                    dist,
                    end,
                    min(dist[node] for node in dist if (node[0], node[1]) == end),
                )
            ],
            stdscr,
        )
    return result


def find_start_end(maze):
    start = (0, 0, 0)
    end = (0, 0)
    for rowindex, row in enumerate(maze):
        for colindex, col in enumerate(row):
            if col == "S":
                start = (colindex, rowindex, 0)
            elif col == "E":
                end = (colindex, rowindex)
    return start, end


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
    parser.add_argument(
        "-v", "--visualize", help="visualize graph", action="store_true"
    )
    args = parser.parse_args()
    if args.visualize:
        curses.wrapper(wrapper)
    else:
        with open("input.txt") as f:
            input = f.read()
        main(input, None)
