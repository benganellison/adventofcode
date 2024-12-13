#! /usr/bin/env python
import re


def solve_claw_machines(claw_machines):
    count_winning_machines = 0
    total_cost = 0
    for machine in claw_machines:
        a_x, a_y = machine["A"]
        b_x, b_y = machine["B"]
        prize_x, prize_y = machine["Prize"]

        min_cost = -1

        for a_presses in range(100):
            for b_presses in range(100):
                x_move = a_presses * a_x + b_presses * b_x
                y_move = a_presses * a_y + b_presses * b_y
                if x_move == prize_x and y_move == prize_y:
                    cost = a_presses * 3 + b_presses
                    if cost < min_cost or min_cost == -1:
                        min_cost = cost

        if min_cost > 0:
            count_winning_machines += 1
            total_cost += min_cost

    return total_cost


def parse_input(input_text):
    machines = []
    machine_pattern = re.compile(
        r"Button A: X\+(\d+), Y\+(\d+)\n"
        r"Button B: X\+(\d+), Y\+(\d+)\n"
        r"Prize: X=(\d+), Y=(\d+)"
    )
    for match in machine_pattern.finditer(input_text):
        a_x, a_y, b_x, b_y, prize_x, prize_y = map(int, match.groups())
        machines.append(
            {
                "A": (a_x, a_y),
                "B": (b_x, b_y),
                "Prize": (prize_x, prize_y),
            }
        )
    return machines


def main(input):
    # Solve and display results
    machines = parse_input(input)
    total_tokens = solve_claw_machines(machines)
    return total_tokens


if __name__ == "__main__":
    with open('input.txt') as f:
        input = f.read()

    result = main(input)
    print("final result: ", result)
