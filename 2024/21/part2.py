#! /usr/bin/env python
from collections import defaultdict
import json
import os

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
    steps = ""
    if y1 == 3 and x2 == 0:
        while y1 > y2:
            steps += "^"
            y1 -= 1
    if x1 == 0 and y2 == 3:
        while x1 < x2:
            steps += ">"
            x1 += 1
    while x1 > x2:
        steps += "<"
        x1 -= 1
    while y1 > y2:
        steps += "^"
        y1 -= 1
    while y1 < y2:
        steps += "v"
        y1 += 1
    while x1 < x2:
        steps += ">"
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
    steps = ""
    if y1 == 0 and x2 == 0:

        steps += "v"
        y1 += 1
        while x1 > x2:
            steps += "<"
            x1 -= 1
    if x1 == 0 and y2 == 0:
        while x1 < x2:
            steps += ">"
            x1 += 1
        steps += "^"
        y1 -= 1

    while x1 > x2:
        steps += "<"
        x1 -= 1
    while y1 > y2:
        steps += "^"
        y1 -= 1
    while x1 < x2:
        steps += ">"
        x1 += 1
    while y1 < y2:
        steps += "v"
        y1 += 1
    return steps

best_keysequence = {}
best_moves = {}
best_numerical_moves = {}
if os.path.exists("best_keysequence.txt"):
    with open("best_keysequence.txt", "r") as f:
        best_keysequence = json.load(f)

if os.path.exists("best_moves.txt"):
    with open("best_moves.txt", "r") as f:
        best_moves = json.load(f)

if os.path.exists("best_numerical_moves.txt"):
    with open("best_numerical_moves.txt", "r") as f:
        best_numerical_moves = json.load(f)


def move_numeric_keypad(current, next):
    x1, y1 = numeric_keypad[current]
    x2, y2 = numeric_keypad[next]

    key = f"{current}_{next}"
    if key in best_numerical_moves:
        return best_numerical_moves[key]
    steps = movement_robot1(x1, y1, x2, y2) + "A"
    best_numerical_moves[key] = steps

    return steps


def move_directional_keypad(current, next):
    x1, y1 = directional_keypad[current]
    x2, y2 = directional_keypad[next]

    key = f"{current}_{next}"
    if key in best_moves:
        return best_moves[key]
    steps = movement_robot_directional(x1, y1, x2, y2) + "A"
    # print("steps:", steps)
    best_moves[key] = steps

    return steps


numeric_keypad = {
    "7": (0, 0),
    "8": (1, 0),
    "9": (2, 0),
    "4": (0, 1),
    "5": (1, 1),
    "6": (2, 1),
    "1": (0, 2),
    "2": (1, 2),
    "3": (2, 2),
    "0": (1, 3),
    "A": (2, 3),
}

directional_keypad = {"^": (1, 0), "A": (2, 0), "<": (0, 1), "v": (1, 1), ">": (2, 1)}

def get_key_sequence(key_sequence_to_press):

    new_key_sequence = []
    last_key = "A"
    if key_sequence_to_press in best_keysequence:
        return best_keysequence[key_sequence_to_press]
    
    for key in key_sequence_to_press:
        next_move = move_directional_keypad(last_key, key)
        # print("next_move:", next_move)
        new_key_sequence.append(next_move)
        last_key = key
    
    best_keysequence[key_sequence_to_press] = new_key_sequence
    # print("new_key_sequence:", new_key_sequence)

    return new_key_sequence


def main(input):
    result = 0
    last_key = "A"
    for key_sequence in parse_input_strings(input):
        key_sequences = defaultdict(int)
        factor = int(key_sequence[:3])
        for key in list(key_sequence):
            new_key_sequence = move_numeric_keypad(last_key, key)
            key_sequences[new_key_sequence] += 1
            last_key = key
        print("key_sequences after numpad :", dict(key_sequences))
        for i in range(25):
            new_key_sequences = defaultdict(int)
            for key_sequence_to_press in key_sequences.keys():
                next_robot_key_sequences = get_key_sequence(key_sequence_to_press)
                for new_key_sequence in next_robot_key_sequences:
                    new_key_sequences[new_key_sequence] += key_sequences[key_sequence_to_press]
            key_sequences = new_key_sequences

            # print("key_sequences:", key_sequences, "after robot:", i+1)

        total_length = sum([len(key_sequence) * occurrences for key_sequence, occurrences in key_sequences.items()])

        result += total_length * factor
        print(
            "length:",
            total_length,
            "x factor:",
            factor,
            "=",
            total_length * factor,
            ", result:",
            result,
        )

    return result


if __name__ == "__main__":
    # Read the strategy from the input file.
    with open("input.txt") as f:
        input = f.read()

    # Calculate and print the total score for the strategy.
    result = main(input)
    print("final result: ", result)

    with open("best_keysequence.txt", "w") as f:
        json.dump(best_keysequence, f, indent=4)
    with open("best_moves.txt", "w") as f:
        json.dump(best_moves, f, indent=4)
    with open("best_numerical_moves.txt", "w") as f:
        json.dump(best_numerical_moves, f, indent=4)
