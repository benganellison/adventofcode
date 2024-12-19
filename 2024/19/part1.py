#! /usr/bin/env python
def can_form_design(design, towel_patterns):
    towel_set = set(towel_patterns)
    max_pattern_length = (
        max(len(pattern) for pattern in towel_patterns) if towel_patterns else 0
    )
    design_length = len(design)
    valid_designs = [False] * (design_length + 1)
    valid_designs[0] = True

    for i in range(1, design_length + 1):
        for length in range(1, min(i, max_pattern_length) + 1):
            valid_designs[i] = valid_designs[i] or (
                valid_designs[i - length] and design[i - length : i] in towel_set
            )

    return valid_designs[design_length]


def count_possible_designs(towel_patterns, desired_designs):

    count = 0
    for design in desired_designs:
        if can_form_design(design, towel_patterns):
            count += 1

    return count


def main(input):
    towel_patterns_input, desired_designs_input = input.split("\n\n")
    towel_patterns = [pattern.strip() for pattern in towel_patterns_input.split(",")]
    desired_designs = desired_designs_input.split("\n")
    result = count_possible_designs(towel_patterns, desired_designs)
    print(f"Number of possible designs: {result}")
    return result


if __name__ == "__main__":
    with open("input.txt") as f:
        input = f.read()

    result = main(input)
    print("final result: ", result)
