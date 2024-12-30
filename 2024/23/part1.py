#! /usr/bin/env python
from collections import defaultdict


def build_graph_from_input(input):
    graph = defaultdict(list)
    for line in input.splitlines():
        a, b = line.split("-")

        graph[b].append(a)
        graph[a].append(b)
    return graph


def main(input):
    graph = build_graph_from_input(input)
    print(graph)
    neighbour_computers = set()
    for first_computer, computers in graph.items():
        for neighbour_computer in computers:
            for distant_neighbour_computer in graph[neighbour_computer]:
                if first_computer in graph[distant_neighbour_computer]:
                    sets_of_three = sorted(
                        [
                            first_computer,
                            neighbour_computer,
                            distant_neighbour_computer,
                        ]
                    )
                    if (
                        first_computer[0] == "t"
                        or neighbour_computer[0] == "t"
                        or distant_neighbour_computer[0] == "t"
                    ):
                        neighbour_computers.add(",".join(sets_of_three))

    print(neighbour_computers)

    result = len(neighbour_computers)
    return result


if __name__ == "__main__":
    with open("input.txt") as f:
        input = f.read()

    result = main(input)
    print("final result: ", result)
