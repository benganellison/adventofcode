#! /usr/bin/env python

global connected_to
connected_to = {}

def dfs(device, visited, connected_to):
    if device == "out":
        return 1
    visited.add(device)
    total_paths = 0
    for neighbor in connected_to.get(device, []):
        if neighbor not in visited:
            total_paths += dfs(neighbor, visited, connected_to)
    visited.remove(device)
    return total_paths


def main(input):

    connected_to = parse_device_connections(input)

    total_paths = dfs("you", set(), connected_to)

    result = total_paths
    return result

def parse_device_connections(input):
    connected_to = {}
    for line in input.splitlines():
        devices = line.split(" ")
        connected_to[devices[0][:-1]] = devices[1:]
    return connected_to


if __name__ == "__main__":
    # Read the strategy from the input file.
    with open("input.txt") as f:
        input = f.read()

    # Calculate and print the total score for the strategy.
    result = main(input)
    print("final result: ", result)
