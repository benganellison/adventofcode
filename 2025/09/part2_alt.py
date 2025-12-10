#! /usr/bin/env python

from bisect import bisect_right


def parse_input_pairs_of_int(instr):
    return [
        tuple(int(x) for x in line.split(","))
        for line in instr.splitlines()
        if line.strip()
    ]


def merge_ranges(ranges):
    if not ranges:
        return []

    ranges.sort()
    merged = [list(ranges[0])]

    for start, end in ranges[1:]:
        last_start, last_end = merged[-1]
        # merge if overlapping or touching
        if start <= last_end + 1:
            if end > last_end:
                merged[-1][1] = end
        else:
            merged.append([start, end])

    return [[s, e] for s, e in merged]


def build_map(corners):
    """
    From polygon corners, build horizontal_lines that represent filled interior segments.

    horizontal_lines[y] = list of [x_start, x_end] segments (inclusive).
    """
    horizontal_lines = {}
    vertical_lines = {}

    # Edges between consecutive corners
    for i, (x1, y1) in enumerate(corners[:-1]):
        x2, y2 = corners[i + 1]
        if y1 == y2:  # horizontal edge
            horizontal_lines.setdefault(y1, []).append([min(x1, x2), max(x1, x2)])
        elif x1 == x2:  # vertical edge
            vertical_lines.setdefault(x1, []).append([min(y1, y2), max(y1, y2)])
        else:
            print("non aligned corners:", (x1, y1), (x2, y2))

    # Close polygon between last and first
    x1, y1 = corners[0]
    x2, y2 = corners[-1]
    if y1 == y2:
        horizontal_lines.setdefault(y1, []).append([min(x1, x2), max(x1, x2)])
    elif x1 == x2:
        vertical_lines.setdefault(x1, []).append([min(y1, y2), max(y1, y2)])
    else:
        print("non aligned corners:", (x1, y1), (x2, y2))

    ymax = max(y for x, y in corners)

    # Scanline fill using vertical edges
    for y in range(ymax + 1):
        intersections = []
        for x, segments in vertical_lines.items():
            for start, end in segments:
                if start <= y < end:
                    intersections.append(x)

        if intersections and len(intersections) > 1:
            intersections.sort()
            for i in range(0, len(intersections), 2):
                if i + 1 >= len(intersections):
                    # odd number of intersections -> shape problem
                    print("ODD intersections at y =", y, ":", intersections)
                    break

                a = intersections[i]
                b = intersections[i + 1]
                horizontal_lines[y] = merge_ranges(
                    horizontal_lines.get(y, []) + [[a, b]]
                )

    # Finally, make sure all rows are merged & sorted
    for y in list(horizontal_lines.keys()):
        horizontal_lines[y] = merge_ranges(horizontal_lines[y])

    return horizontal_lines


def build_horizontal_index(horizontal_lines):
    """
    Precompute an index for fast queries:
        index[y] = (segments, starts)
    where:
        segments = [[start, end], ...] (sorted, non-overlapping)
        starts   = [start0, start1, ...] (just the starts, for bisect)
    """
    index = {}
    for y, segments in horizontal_lines.items():
        segs = merge_ranges(segments)  # safety, ensures sorted & merged
        starts = [s for s, e in segs]
        index[y] = (segs, starts)
    return index


def row_covers_segment(segments, starts, x_left, x_right):
    """
    Check if ANY segment in this row fully covers [x_left, x_right] (inclusive),
    using binary search on segment starts.
    """
    # Find rightmost segment whose start <= x_left
    # bisect_right(starts, x_left) returns index of first start > x_left
    i = bisect_right(starts, x_left) - 1
    if i < 0:
        return False

    start, end = segments[i]
    # we need: start <= x_left and x_right <= end
    return (start <= x_left) and (x_right <= end)


def in_map(corner, other_corner, horizontal_index):
    """
    Check if every row between corner and other_corner (inclusive in y)
    has a horizontal segment fully covering [x_left, x_right].

    This matches your original in_map() semantics, but uses binary search
    instead of scanning all segments.
    """
    x, y = corner
    ox, oy = other_corner

    x_left = min(x, ox)
    x_right = max(x, ox)

    y_start = min(y, oy)
    y_end = max(y, oy)

    for y_line in range(y_start, y_end + 1):
        if y_line not in horizontal_index:
            return False
        segments, starts = horizontal_index[y_line]
        if not row_covers_segment(segments, starts, x_left, x_right):
            return False

    return True


def main(input_text):
    corners = parse_input_pairs_of_int(input_text)

    horizontal_lines = build_map(corners)
    horizontal_index = build_horizontal_index(horizontal_lines)

    print("final horizontal lines finalized:")

    largest_area = 0
    best_pair = None

    n = len(corners)

    for i in range(n):
        x1, y1 = corners[i]
        for j in range(i + 1, n):  # only j > i: avoid duplicate pairs
            x2, y2 = corners[j]

            # Skip degenerate rectangles (zero width or height)
            if x1 == x2 or y1 == y2:
                continue

            # Compute area in the same way you did:
            # hight = abs(x1 - x2) + 1
            # width = abs(y1 - y2) + 1
            # area  = hight * width
            #
            # Let's actually do that step-by-step to be explicit:
            dx = abs(x1 - x2)
            dy = abs(y1 - y2)
            hight = dx + 1  # number of x-cells
            width = dy + 1  # number of y-cells
            area = hight * width  # total cells in the rectangle

            # If the area can't beat current best, don't bother checking
            if area <= largest_area:
                continue

            if in_map((x1, y1), (x2, y2), horizontal_index):
                print(
                    "found rectangle between",
                    (x1, y1),
                    "and",
                    (x2, y2),
                    "all coordinates:",
                    ((x1, y1), (x1, y2), (x2, y2), (x2, y1)),
                )
                largest_area = area
                best_pair = ((x1, y1), (x2, y2))
                print("new largest area:", largest_area, "between", best_pair)

    print("best rectangle corners:", best_pair)
    result = largest_area
    return result


if __name__ == "__main__":
    with open("input.txt") as f:
        input_data = f.read()

    result = main(input_data)
    print("final result:", result)
