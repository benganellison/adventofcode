#! /usr/bin/env python

def parse_input_strings(input):
    return input.splitlines()


def movement_robot1(x1, y1, x2, y2):
    """
    +---+---+---+      +---+---+---+
    | 7 | 8 | 9 |      |0,0|1,0|2,0|
    +---+---+---+      +---+---+---+
    | 4 | 5 | 6 |      |0,1|1,1|2,1|
    +---+---+---+      +---+---+---+
    | 1 | 2 | 3 |      |0,2|1,2|2,2|
    +---+---+---+      +---+---+---+
        | 0 | A |          |1,3|2,3|
        +---+---+          +---+---+
    """
    steps = []
    if y1 == 3 and x2 == 0:
        while y1 > y2:
            steps.append("^")
            y1 -= 1
    if x1 == 0 and y2 == 3:
        while x1 < x2:
            steps.append(">")
            x1 += 1
    while x1 > x2:
        steps.append("<")
        x1 -= 1
    while y1 > y2:
        steps.append("^")
        y1 -= 1
    while y1 < y2:
        steps.append("v")
        y1 += 1
    while x1 < x2:
        steps.append(">")
        x1 += 1
    return steps


def movement_robot_directional(x1, y1, x2, y2):
    """
        +---+---+          +---+---+
        | ^ | A |       0,0|1,0|2,0|
    +---+---+---+      +---+---+---+
    | < | v | > |      |0,1|1,1|2,1|
    +---+---+---+      +---+---+---+
    """
    steps = []
    if y1 == 0 and x2 == 0:

        steps.append("v")
        y1 += 1
        while x1 > x2:
            steps.append("<")
            x1 -= 1
    if x1 == 0 and y2 == 0:
        while x1 < x2:
            steps.append(">")
            x1 += 1
        steps.append("^")
        y1 -= 1

    while x1 > x2:
        steps.append("<")
        x1 -= 1
    while y1 > y2:
        steps.append("^")
        y1 -= 1
    while x1 < x2:
        steps.append(">")
        x1 += 1
    while y1 < y2:
        steps.append("v")
        y1 += 1
    return steps


def move_numeric_keypad(current, next):
    x1, y1 = numeric_keypad[current]
    x2, y2 = numeric_keypad[next]

    steps = movement_robot1(x1, y1, x2, y2)

    return steps+["A"]

best_moves = {}

def move_directional_keypad(current, next):
    x1, y1 = directional_keypad[current]
    x2, y2 = directional_keypad[next]

    if (current, next) in best_moves:
        return best_moves[(current, next)] + ["A"]
    steps = movement_robot_directional(x1, y1, x2, y2)
    best_moves[(current, next)] = steps

    return steps + ["A"]


numeric_keypad = {
    '7': (0, 0), '8': (1, 0), '9': (2, 0),
    '4': (0, 1), '5': (1, 1), '6': (2, 1),
    '1': (0, 2), '2': (1, 2), '3': (2, 2),
    '0': (1, 3), 'A': (2, 3)
}

directional_keypad = {"^": (1, 0), "A": (2, 0), "<": (0, 1), "v": (1, 1), ">": (2, 1)}


def main(input):
    result = 0
    last_key_robot_1 = "A"
    last_key_robot_2 = 'A'
    last_key_robot_3 = "A"
    for key_sequence in parse_input_strings(input):
        factor = int(key_sequence[:3])
        for_robot_1 = []
        for_robot_2 = []
        for_robot_3 = []
        for key in list(key_sequence):
            next_mov_r1 = move_numeric_keypad(last_key_robot_1, key)
            for_robot_1 += next_mov_r1
            robo3_last_sequence = []
            for key_r2 in next_mov_r1:
                next_mov_r2 = move_directional_keypad(last_key_robot_2, key_r2)
                for_robot_2 += next_mov_r2
                for key_r3 in next_mov_r2:
                    next_mov_r3 = move_directional_keypad(last_key_robot_3, key_r3)
                    # if "379A" == key_sequence or True:
                    #     print(
                    #         "robot1 moving from: ",
                    #         last_key_robot_1,
                    #         "robot1 moving to: ",
                    #         key,
                    #         "robot2 moving from: ",
                    #         last_key_robot_2,
                    #         "robot2 moving to: ",
                    #         key_r2,
                    #         "robot3 moving from: ",
                    #         last_key_robot_3,
                    #         "robot3 moving to: ",
                    #         key_r3,
                    #         "steps needed: ",
                    #         next_mov_r3,
                    #     )
                    robo3_last_sequence += next_mov_r3
                    for_robot_3 += next_mov_r3
                    last_key_robot_3 = key_r3
                # print("for_robot_3done ")
                last_key_robot_2 = key_r2
            # print(f"({last_key_robot_1},{key}) = '{''.join(robo3_last_sequence)}'")
            # print(
            #     f"({numeric_keypad[last_key_robot_1]},{numeric_keypad[key]}) = '{''.join(robo3_last_sequence)}'"
            # )
            # print("".join(for_robot_3))
            last_key_robot_1 = key

        # print(f"{key_sequence}:","".join(for_robot_1))
        # print(f"{key_sequence}:","".join(for_robot_2))
        # print(f"{key_sequence}:","".join(for_robot_3))
        result += len(for_robot_3) * factor
        print("length:", len(for_robot_3), "x factor:", factor, "=", len(for_robot_3) * factor, ", result:", result)

    return result


if __name__ == "__main__":
    # Read the strategy from the input file.
    with open('input.txt') as f:
        input = f.read()

    # Calculate and print the total score for the strategy.
    result = main(input)
    print("final result: ", result)


