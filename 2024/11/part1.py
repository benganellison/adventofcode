#! /usr/bin/env python
def blink_once(stones):
    new_stones = []
    for i, stone in enumerate(stones):
        if stone == '0':
            new_stones.append('1')
        elif len(stone) % 2 == 0:
            new_stones.append(stone[:len(stone) // 2])
            new_stones.append(str(int(stone[len(stone) // 2 :])))
        else:
            new_stones.append(str(int(stone) *2024))

    return new_stones

def main(input):
    stones = input.split(" ")
    for i in range(25):
        stones = blink_once(stones)

    result = len(stones)
    return result


if __name__ == "__main__":
    # Read the strategy from the input file.
    with open('input.txt') as f:
        input = f.read()

    # Calculate and print the total score for the strategy.
    result = main(input)
    print("final result: ", result)
