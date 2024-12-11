#! /usr/bin/env python
from collections import defaultdict

def blink(stones, n):
    for i in range(n):
        new_stones = defaultdict(int)
        for stone, count in stones.items():
            if stone == "0":
                new_stones["1"] += count
            elif len(stone) % 2 == 0:
                mid = len(stone) // 2
                new_stones[stone[: mid]] += count
                new_stones[stone[mid:].lstrip("0") or "0"] += count
            else:
                new_stones[str(int(stone) * 2024)] += count
        stones = new_stones

    return stones


def main(input):
    stones = defaultdict(int)
    for stone in input.split(" "):
        stones[stone] += 1

    stones = blink(stones, 75)
    result = sum(stones.values())
    return result


if __name__ == "__main__":
    # Read the strategy from the input file.
    with open("input.txt") as f:
        input = f.read()

    # Calculate and print the total score for the strategy.
    result = main(input)
    print("final result: ", result)
