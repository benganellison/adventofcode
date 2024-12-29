#! /usr/bin/env python


from collections import defaultdict
MOD = 16777216
def parse_input_integers(input):
    return [int(x) for x in input.splitlines()]

MAX_PATTERNS = 19**4  # 130321


def main(input_text):
    secrets = parse_input_integers(input_text)

    # Instead of defaultdict(int), we use a list for sums
    # Initialize all sums to 0
    pattern_sums = [0] * MAX_PATTERNS

    # For each buyer, we need to track if we've used a pattern.
    # We can re-init a boolean list each time, or do something more clever below.
    visited_byers = [0] * MAX_PATTERNS

    for byer_id, secret in enumerate(secrets):
        # create a local boolean list

        # Single-pass approach
        prev_price = secret % 10
        d1 = d2 = d3 = None  # to store last 3 deltas

        for i in range(2000):
            secret = secret ^ (secret * 64)
            secret %= MOD
            secret = secret ^ (secret // 32)
            secret %= MOD
            secret = secret ^ (secret * 2048)
            secret %= MOD

            current_price = secret % 10
            d4 = current_price - prev_price

            # shift the deltas
            if i > 2:
                # We have 4 deltas: d1, d2, d3, d4
                pattern_code = (
                    (d1 + 9) + 19 * (d2 + 9) + 19**2 * (d3 + 9) + 19**3 * (d4 + 9)
                )
                if visited_byers[pattern_code] != byer_id:
                    pattern_sums[pattern_code] += current_price
                    visited_byers[pattern_code] = byer_id

                # shift
            d1, d2, d3 = d2, d3, d4

            prev_price = current_price

    # At the end, find the max
    best_value = max(pattern_sums)
    # If you need to find all patterns that tie for best_value:
    # best_patterns = [i for i, val in enumerate(pattern_sums) if val == best_value]

    print(f"Max bananas: {best_value}")
    return best_value


if __name__ == "__main__":
    with open("input.txt") as f:
        puzzle_input = f.read()

    answer = main(puzzle_input)
    print("final result (part two):", answer)
