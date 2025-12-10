#! /usr/bin/env python
def parse_input_pairs_of_int(instr):
    return [tuple(int(x) for x in range.split(",")) for range in instr.splitlines()]


def get_visual_map_representation(corners):
    x_max = max(x for x, y in corners) + 1
    y_max = max(y for x, y in corners) + 1

    map = [["." for _ in range(x_max + 1)] for _ in range(y_max + 1)]

    for x, y in corners:
        map[y][x] = "#"


    for x1, y1 in corners:
        for x2, y2 in corners:
            if (x1, y1) == (x2, y2):
                continue
            if x1 == x2:
                for y in range(min(y1, y2) + 1, max(y1, y2)):
                    if map[y][x1] == ".":
                        map[y][x1] = "X"
            elif y1 == y2:
                for x in range(min(x1, x2) + 1, max(x1, x2)):
                    if map[y1][x] == ".":
                        map[y1][x] = "X"

    return map


def merge_ranges(ranges):
    if not ranges:
        return []

    ranges.sort()
    merged = [list(ranges[0])]

    for start, end in ranges[1:]:
        last_start, last_end = merged[-1]
        if start <= last_end + 1:
            if end > last_end:
                merged[-1][1] = end
        else:
            merged.append([start, end])

    return [[s, e] for s, e in merged]


def build_map(corners):

    horizontal_lines = {}
    vertical_lines = {}

    for i, (x1, y1) in enumerate(corners[:-1]):
        x2, y2 = corners[i + 1]
        if y1 == y2:
            horizontal_lines.setdefault(y1, []).append([min(x1, x2), max(x1, x2)])
        elif x1 == x2:
            vertical_lines.setdefault(x1, []).append([min(y1, y2), max(y1, y2)])
        else:
            print("non aligned corners:", (x1, y1), (x2, y2))

    x1, y1 = corners[0]
    x2, y2 = corners[-1]
    if x1 == x2:
        vertical_lines.setdefault(x1, []).append(
            [min(y1, y2), max(y1, y2)]
        )
    elif y1 == y2:
        horizontal_lines.setdefault(y1, []).append([min(x1, x2), max(x1, x2)])

    ymax = max(y for x, y in corners)

    for y in range(ymax + 1):
        intersections = []
        for x, segments in vertical_lines.items():
            for start, end in segments:
                if start <= y < end:
                    intersections.append(x)

        if intersections and len(intersections) > 1:
            intersections.sort()
            for i in range(0, len(intersections), 2):
                a = intersections[i]
                b = intersections[i + 1]

                horizontal_lines[y] = merge_ranges(horizontal_lines.get(y, []) + [[a, b]])
                if len(intersections) % 2 == 1:
                    print("ODD intersections at y =", y, ":", intersections)

    return horizontal_lines


def in_map(corner, other_corner, horizontal_lines):
    x, y = corner
    ox, oy = other_corner

    x_left = min(x, ox)
    x_right = max(x, ox)
    for y_line in range(min(y, oy), max(y, oy) + 1):
        found = False
        if y_line not in horizontal_lines:
            return False

        for start, end in horizontal_lines[y_line]:
            if end < x_left:
                continue  # too far left, keep going
            if start > x_right:
                break  # too far right, no segment will match
            if start <= x_left and x_right <= end:
                found = True
                break
        if not found:
            return False

    return True


def main(input):

    corners = parse_input_pairs_of_int(input)

    horizontal_lines = build_map(corners)

    print("final horizontal lines finalized:")

    largest_area = 0
    for i, corner in enumerate(corners):
        for j in range(i + 1, len(corners)):
            other_corner = corners[j]

            x1, y1 = corner
            x2, y2 = other_corner
            if x1 == x2 or y1 == y2:
                continue  # skip lines

            hight = abs(x1 - x2) + 1
            width = abs(y1 - y2) + 1
            area = hight * width
            if area > largest_area:

                if in_map(corner, other_corner, horizontal_lines):

                    print("found rectangle between ", corner, " and ", other_corner, " all coordinates: ", (corner, (x1, y2), other_corner, (x2, y1)))
                    largest_area = area
                    print("new largest area: ", largest_area, " between ", corner, " and ", other_corner)
                    # draw_map_overlay(corner, other_corner, map)

    result = largest_area
    return result


if __name__ == "__main__":
    # Read the strategy from the input file.
    with open("input.txt") as f:
        input = f.read()

    # Calculate and print the total score for the strategy.
    result = main(input)
    print("final result: ", result)
