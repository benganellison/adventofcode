#! /usr/bin/env python
def parse_input(input):
    lines = input.split("\n")
    A = int(lines[0].split(" ")[2])
    B = int(lines[1].split(" ")[2])
    C = int(lines[2].split(" ")[2])
    instructions = list(map(int, lines[4].split(" ")[1].split(",")))
    return A, B, C, instructions

def adv(operand, A):
    return A >> operand

def bitwise_xor(X, Y):
    return X ^ Y

def main(input):
    A, B, C, instructions = parse_input(input)
    i = 0
    to_be_printed = ""
    while i < len(instructions) - 1:
        instruction = instructions[i]
        operand = instructions[i + 1]
        if 0 <= operand < 4:
            operand = operand
        elif operand == 4:
            operand = A
        elif operand == 5:
            operand = B
        elif operand == 6:
            operand = C
        else:
            raise Exception(f"Operand {operand} is not allowed")

        if instruction == 0:
            A = adv(operand, A)
        elif instruction == 1:
            B = bitwise_xor(B, instructions[i + 1])
        elif instruction == 2:
            B = operand % 8
        elif instruction == 3:
            if A != 0:
                i = instructions[i + 1]
                continue
        elif instruction == 4:
            B = bitwise_xor(B, C)
        elif instruction == 5:
            to_be_printed += (
                "," + str(operand % 8) if to_be_printed else str(operand % 8)
            )
        elif instruction == 6:
            B = adv(operand, A)
        elif instruction == 7:
            C = adv(operand, A)

        i += 2

    result = to_be_printed
    return result

if __name__ == "__main__":
    # Read the strategy from the input file.
    with open('input.txt') as f:
        input = f.read()

    # Calculate and print the total score for the strategy.
    result = main(input)
    print("final result: ", result)
