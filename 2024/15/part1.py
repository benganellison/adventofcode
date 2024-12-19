#!/usr/bin/env python3

def main(input_data):
    warehouse_map, movements_raw = input_data.split("\n\n")
    warehouse_map = [list(row) for row in warehouse_map.split("\n")]
    movements_str = "".join(movements_raw.split())
    movements = get_path(movements_str)
    boxes, start_pos, walls = explore_map(warehouse_map)
    current_pos = start_pos

    for dx, dy in movements:
        new_x = current_pos[0] + dx
        new_y = current_pos[1] + dy

        if (new_x, new_y) in walls:
            continue

        if (new_x, new_y) in boxes:
            if can_push(boxes, walls, new_x, new_y, dx, dy):
                push_boxes(boxes, new_x, new_y, dx, dy)
                current_pos = (new_x, new_y)
            else:
                continue
        else:
            current_pos = (new_x, new_y)

    gps_sum = sum(100 * y + x for (x, y) in boxes)
    return gps_sum

def explore_map(warehouse_map):
    boxes = set()
    start_pos = (0, 0)
    walls = set()

    for y, row in enumerate(warehouse_map):
        for x, char in enumerate(row):
            if char == "O":
                boxes.add((x, y))
            elif char == "@":
                start_pos = (x, y)
            elif char == "#":
                walls.add((x, y))

    return boxes, start_pos, walls

def get_path(movements):
    path = []
    for movement in movements:
        if movement == ">":
            path.append((1, 0))
        elif movement == "<":
            path.append((-1, 0))
        elif movement == "^":
            path.append((0, -1))
        elif movement == "v":
            path.append((0, 1))
    return path

def can_push(boxes, walls, x, y, dx, dy):
    cur_x, cur_y = x, y
    while (cur_x, cur_y) in boxes:
        cur_x += dx
        cur_y += dy
        if (cur_x, cur_y) in walls:
            return False
        if (cur_x, cur_y) in boxes:
            continue
    return True

def push_boxes(boxes, x, y, dx, dy):
    chain = []
    cur_x, cur_y = x, y

    while (cur_x, cur_y) in boxes:
        chain.append((cur_x, cur_y))
        cur_x += dx
        cur_y += dy

    next_x, next_y = cur_x, cur_y
    for bx, by in reversed(chain):
        boxes.remove((bx, by))
        boxes.add((next_x, next_y))
        next_x -= dx
        next_y -= dy

if __name__ == "__main__":
    with open("input.txt") as f:
        input_data = f.read()
    result = main(input_data)
    print("final result:", result)
