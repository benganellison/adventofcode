import re

def find_the_top_crates(input):
    result = ""

    crates, instructions = input.split("\n\n")

    stacks = get_stacks(crates)
    stacks = reorder_crates(stacks, instructions.strip().split("\n"))
    result = get_top_crates(stacks)
    return result

def reorder_crates(stacks, instructions):
    for instruction in instructions:
        print(f'instruction: {instruction}')
        move, from_stack, to_stack = re.findall(r"move (\d+) from (\d+) to (\d+)", instruction)[0]
        print(f'move: {move}, from_stack: {from_stack} ({stacks[from_stack]}), to_stack: {to_stack} ({stacks[to_stack]})')
        for i in range(int(move)):
            if len(stacks[from_stack]) > 0:
                crate = stacks[from_stack].pop()

                stacks[to_stack].append(crate)
            else:
                print(f'stack {from_stack} is empty, stacks: {stacks}, stacks[from_stack]: {stacks[from_stack]} ')
                return stacks
    return stacks

def get_top_crates(stacks):
    result = ""
    for stack in stacks:
        if len(stacks[stack]) > 0:
            result += stacks[stack][-1]
    return result

def get_stacks(crates):
    stacks = {}
    
    crates = crates.split("\n")
    stack_ids = []
    bottom_stack = len(crates) - 1
    for index, col in enumerate(crates[bottom_stack]):
        if col != " ":
            stack_ids.append(index)
    
    for row in range(len(crates) - 2, -1, -1):
        for col in range(len(crates[row])):

            if col in stack_ids:
                if crates[row][col] != " ":
                    if crates[bottom_stack][col] in stacks:
                        stacks[crates[bottom_stack][col]].append(crates[row][col])
                    else:
                        stacks[crates[bottom_stack][col]] = [crates[row][col]]
    return stacks


if __name__ == "__main__":
    # Read the strategy from the input file.
    with open('input.txt') as f:
        input = f.read()

    # Calculate and print the total score for the strategy.
    result = find_the_top_crates(input)
    print("final result: ", result)
