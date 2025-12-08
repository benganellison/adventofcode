#! /usr/bin/env python
import math


def distance(p1, p2):
    x1, y1, z1 = p1
    x2, y2, z2 = p2
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2 + (z2 - z1) ** 2)


def get_all_distances(junction_boxes):
    distances = {}
    for i, junction in enumerate(junction_boxes):
        for j, junction_2 in enumerate(junction_boxes):
            if i == j:
                continue
            dist = distance(junction, junction_2)
            distances[dist] = [junction, junction_2, i, j]
    return distances


def main(input, iterations=10):
    junction_boxes = [
        tuple(int(x) for x in range.split(",")) for range in input.splitlines()
    ]
    circurit_roots = [i for i in range(len(junction_boxes))]

    circurits = {i: [jb] for i, jb in enumerate(junction_boxes)}
    distances = get_all_distances(junction_boxes)

    sorted_distances = sorted(distances.keys())

    connected= 0
    for dist in sorted_distances:
        connected += 1
        junction_box_a, junction_box_b, root_a, root_b = distances[dist]
        if circurit_roots[root_b] == circurit_roots[root_a]:
            continue
        if circurit_roots[root_a] in circurits:
            curr_root = circurit_roots[root_a]
            other_root = circurit_roots[root_b]
            circurits[curr_root] += circurits[other_root]

            for j, root in enumerate(circurit_roots):
                if root == other_root:
                    circurit_roots[j] = curr_root
            del circurits[other_root]
        else:
            print("error: neither circurit root found")
            print("circurit_roots: ", {i: circurit_roots[i] for i in range(len(circurit_roots))})
            print("circurit_roots: ", sorted(list(set(circurit_roots))))
            print("circurits: ", circurits)
            raise ValueError("Neither circuit root found during merge")

        if connected >= iterations:
            break


    result = math.prod(sorted([len(circurits[c]) for c in circurits])[::-1][:3])

    return result


if __name__ == "__main__":
    # Read the strategy from the input file.
    with open("input.txt") as f:
        input = f.read()

    # Calculate and print the total score for the strategy.
    result = main(input, 1000)
    print("final result: ", result)
