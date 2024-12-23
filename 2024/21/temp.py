movements = {
    ((0, 0), (2, 0)): "<vA>^AA<A>A",
    ((0, 1), (1, 1)): "<vA>^A<A>A",
    ((0, 2), (0, 0)): "<v<A>>^AAvA^A",
    ((1, 0), (1, 3)): "<v<A>A>^AAAvA<^A>A",
    ((1, 1), (2, 1)): "<vA>^A<A>A",
    ((1, 2), (2, 0)): "<vA>^A<v<A>^A>AAvA^A",
    ((1, 3), (1, 2)): "<v<A>>^AvA^A",
    ((1, 3), (2, 3)): "<vA>^A<A>A",
    ((2, 0), (1, 0)): "<vA<AA>>^AvAA<^A>A",
    ((2, 0), (2, 3)): "<v<A>A>^AAAvA<^A>A",
    ((2, 0), (2, 3)): "<v<A>A>^AAAvA<^A>A",
    ((2, 0), (2, 3)): "<v<A>A>^AAAvA<^A>A",
    ((2, 1), (2, 3)): "<v<A>A>^AAvA<^A>A",
    ((2, 2), (0, 0)): "<vA<AA>>^AAvA<^A>AAvA^A",
    ((2, 2), (0, 1)): "<v<A>>^A<vA<A>>^AAvAA<^A>A",
    ((2, 3), (0, 1)): "<v<A>>^AA<vA<A>>^AAvAA<^A>A",
    ((2, 3), (0, 2)): "<v<A>>^A<vA<A>>^AAvAA<^A>A",
    ((2, 3), (1, 3)): "<vA<AA>>^AvAA<^A>A",
    ((2, 3), (2, 0)): "<v<A>>^AAAvA^A",
    ((2, 3), (2, 2)): "<v<A>>^AvA^A",
}

delta_to_sequence = {
    (-1, 0): "<vA<AA>>^AvAA<^A>A",  # From (2, 0) to (1, 0)
    (-2, -1): "<v<A>>^A<vA<A>>^AAvAA<^A>A",  # From (2, 2) to (0, 1)
    (-2, -2): "<v<A>>^AA<vA<A>>^AAvAA<^A>A",  # From (2, 3) to (0, 1)
    (-2, -2): "<vA<AA>>^AAvA<^A>AAvA^A",  # From (2, 2) to (0, 0)
    (0, -1): "<v<A>>^AvA^A",  # From (1, 3) to (1, 2)
    (0, -2): "<v<A>>^AAvA^A",  # From (0, 2) to (0, 0)
    (0, -3): "<v<A>>^AAAvA^A",  # From (2, 3) to (2, 0)
    (0, 2): "<v<A>A>^AAvA<^A>A",  # From (2, 1) to (2, 3)
    (0, 3): "<v<A>A>^AAAvA<^A>A",  # From (1, 0) to (1, 3)
    (1, -2): "<vA>^A<v<A>^A>AAvA^A",  # From (1, 2) to (2, 0)
    (1, 0): "<vA>^A<A>A",  # From (0, 1) to (1, 1)
    (2, 0): "<vA>^AA<A>A",  # From (0, 0) to (2, 0)
}


def main_test(input):
    result = 0
    for key_sequence in parse_input_strings(input):
        final_sequence = []
        previous_key = "A"
        for key in key_sequence:
            x1, y1 = numeric_keypad[previous_key]
            x2, y2 = numeric_keypad[key]
            key_sequence = delta_to_sequence[(x2 - x1, y2 - y1)]
            final_sequence.append(
                movements[numeric_keypad[previous_key], numeric_keypad[key]]
            )
            previous_key = key
        print(f"{key_sequence}: {''.join(final_sequence)}")
        result += len("".join(final_sequence)) * int(key_sequence[:3])
    return result
