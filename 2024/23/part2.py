#! /usr/bin/env python
from collections import defaultdict


def build_graph_from_input(input):
    graph = defaultdict(list)
    for line in input.splitlines():
        a, b = line.split("-")

        graph[b].append(a)
        graph[a].append(b)
    return graph


def find_lan(graph):
    def bron_kerbosch(r, p, x):
        if not p and not x:
            cliques.append(r)
        for v in list(p):
            bron_kerbosch(
                r.union({v}), p.intersection(graph[v]), x.intersection(graph[v])
            )
            p.remove(v)
            x.add(v)

    cliques = []
    bron_kerbosch(set(), set(graph.keys()), set())
    return max(cliques, key=len)


def main(input):
    graph = build_graph_from_input(input)
    lan_group = list(find_lan(graph))
    lan_group.sort()
    result = ",".join(lan_group)
    return result


if __name__ == "__main__":
    with open("input.txt") as f:
        input = f.read()

    result = main(input)
    print("final result: ", result)
