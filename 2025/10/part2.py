#! /usr/bin/env python
import datetime
import pulp


def parse_jolt_data(input):
    numbers = input[1:-1]
    return [int(x) for x in numbers.split(",")]


def parse_input_strings(input):
    return input.splitlines()


def parse_button_wiring_data(light):
    button_wirings = [
        eval(x) if isinstance(eval(x), tuple) else eval(x + ",")
        for x in light.split(" ")[1:-1]
    ]

    return button_wirings


def parse_target_state(light):
    target_state = [
        True if x == "#" else False
        for x in list(light.split(" ")[0])
        if x in ["#", "."]
    ]
    return target_state


def parse_machines(lights):
    machines = []
    for light in lights:
        target_state = parse_target_state(light)
        button_wirings = parse_button_wiring_data(light)
        jolts = parse_jolt_data(light.split(" ")[-1])
        machines.append(
            {
                "target_state": target_state,
                "button_wirings": button_wirings,
                "jolts": jolts,
            }
        )
    # print(machines)
    return machines


def configure_joltage_machine_pulp(machine):
    button_wirings = machine["button_wirings"]  # list of tuples
    jolts = machine["jolts"]  # list of ints

    num_buttons = len(button_wirings)
    num_counters = len(jolts)

    linear_problem = pulp.LpProblem("joltage_config", pulp.LpMinimize)

    x = [
        pulp.LpVariable(f"x_{j}", lowBound=0, cat="Integer") for j in range(num_buttons)
    ]

    linear_problem += pulp.lpSum(x), "total_presses"

    for i in range(num_counters):
        linear_problem += (
            pulp.lpSum(x[j] for j, wiring in enumerate(button_wirings) if i in wiring)
            == jolts[i],
            f"counter_{i}_joltage",
        )

    linear_problem.solve(pulp.PULP_CBC_CMD(msg=False))

    status = pulp.LpStatus[linear_problem.status]
    if status != "Optimal":
        print("Solver status for this machine:", status)
        return None

    button_presses = [int(pulp.value(var)) for var in x]
    total_presses = sum(button_presses)

    return total_presses


def main(input):
    lights = parse_input_strings(input)
    machines = parse_machines(lights)

    result = 0
    for i, machine in enumerate(machines):
        start_time = datetime.datetime.now()

        total_presses = configure_joltage_machine_pulp(machine)
        if total_presses is None:
            print("machine result:", i, "no optimal solution", "time taken: ???")
            continue

        result += total_presses
        end_time = datetime.datetime.now()

        time_delta = end_time - start_time
        hours, remainder = divmod(time_delta.total_seconds(), 3600)
        minutes, seconds = divmod(remainder, 60)
        milliseconds = time_delta.microseconds // 1000
        time_str = (
            f"{int(hours):02d}:{int(minutes):02d}:{int(seconds):02d}.{milliseconds:03d}"
        )

        print("machine result:", i, total_presses, "time taken:", time_str)


    return result


if __name__ == "__main__":
    # Read the strategy from the input file.
    with open("input.txt") as f:
        input = f.read()

    # Calculate and print the total score for the strategy.
    result = main(input)
    print("final result: ", result)
