#! /usr/bin/env python
import re

def solve_linear_problem(machine):
    """
    Solves the linear problem for the given machine configuration.

    Args:
        machine (tuple): A tuple containing six integers (ax, ay, bx, by, px, py).

    Returns:
        tuple: A tuple (A, B) representing the number of presses for buttons A and B, or None if no solution exists.

    Examples:
        >>> solve_linear_problem((1, 2, 3, 4, 5, 6))
        
        >>> solve_linear_problem((1, 0, 0, 1, 1, 1))
        (1, 1)
    """
    ax, ay, bx, by, px, py = machine

    D = ax * by - ay * bx
    if D == 0:
        return None

    A = (px * by - py * bx)
    B = (ax * py - ay * px)

    if A % D != 0 or B % D != 0:
        return None

    A //= D
    B //= D

    if A < 0 or B < 0:
        return None

    return A, B


def solve_claw_machines(claw_machines):
    """
    Solves the claw machine problems and calculates the total cost.

    Args:
        claw_machines (list): A list of machine configurations.

    Returns:
        tuple: A tuple (num_prizes, total_cost) representing the number of prizes won and the total tokens spent.

    Examples:
        >>> solve_claw_machines([(1, 0, 0, 1, 1, 1)])
        (1, 4)
        >>> solve_claw_machines([(1, 2, 3, 4, 5, 6)])
        (0, 0)
    """
    results = []
    for machine in claw_machines:
        result = solve_linear_problem(machine)
        if result is not None:
            a_presses, b_presses = result
            cost = a_presses * 3 + b_presses
            results.append(cost)

    total_cost = sum(results)
    return len(results), total_cost


def get_claw_machines(input_text):
    """
    Parses the input text to extract claw machine configurations.

    Args:
        input_text (str): The input text containing machine configurations.

    Returns:
        list: A list of machine configurations.

    Examples:
        >>> input_text = "Button A: X+1, Y+2\\nButton B: X+3, Y+4\\nPrize: X=5, Y=6"
        >>> get_claw_machines(input_text)
        [(1, 2, 3, 4, 10000000000005, 10000000000006)]
    """
    machines = []
    machine_pattern = re.compile(
        r"Button A: X\+(\d+), Y\+(\d+)\n"
        r"Button B: X\+(\d+), Y\+(\d+)\n"
        r"Prize: X=(\d+), Y=(\d+)"
    )
    for match in machine_pattern.finditer(input_text):
        a_x, a_y, b_x, b_y, prize_x, prize_y = map(int, match.groups())
        machines.append(
            (a_x, a_y, b_x, b_y, prize_x + 10000000000000, prize_y + 10000000000000)
        )
    return machines


def main(input):
    """
    Main function to process the input and solve the claw machine problems.

    Args:
        input (str): The input text containing machine configurations.

    Returns:
        tuple: A tuple (total_tokens, num_prizes) representing the total tokens spent and the number of prizes won.

    Examples:
        >>> input_text = "Button A: X+26, Y+66\\nButton B: X+67, Y+21\\nPrize: X=12748, Y=12176"
        >>> main(input_text) 
        Prizes won: 1
        Total tokens spent: 459236326669
        (459236326669, 1)
    """
    claw_machines = get_claw_machines(input)
    num_prizes, total_tokens = solve_claw_machines(claw_machines)
    print(f"Prizes won: {num_prizes}")
    print(f"Total tokens spent: {total_tokens}")
    return total_tokens, num_prizes


if __name__ == "__main__":
    with open("input.txt") as f:
        input = f.read()

    total_tokens, num_prizes = main(input)
    print("final result: ", total_tokens, "number of prizes", num_prizes)
