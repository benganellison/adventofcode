#! /usr/bin/env python
import json
import re
import datetime
from collections import deque

def parse_jolt_data(input):
    numbers = input[1:-1]
    return [int(x) for x in numbers.split(",")]


def parse_input_strings(input):
    return input.splitlines()


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

def parse_button_wiring_data(light):
    button_wirings = [
            eval(x) if isinstance(eval(x), tuple) else eval(x + ",")
            for x in light.split(" ")[1:-1]
        ]
    
    return button_wirings

def parse_target_state(light):
    target_state = [True if x == "#" else False for x in list(light.split(" ")[0]) if x in ["#", "."]]
    return target_state

def turn_on_machine(machine):
    current_state = [False] * len(machine["target_state"])
    target_state = machine["target_state"]
    button_wirings = machine["button_wirings"]
    jolts = machine["jolts"]

    # bfs
    queue = deque()
    queue.append((current_state, 0))
    visited = set()
    result = -1
    while queue:
        state, steps = queue.popleft()
        state_tuple = tuple(state)
        if state_tuple in visited:
            continue
        visited.add(state_tuple)

        if state == target_state:
            result = steps
            # print("found solution with steps:", steps)
            # print("used wires:", used_wires)
            break

        for wiring in button_wirings:
            new_state = state.copy()
            # print("toggling wiring:", wiring, "previous wires used:", used_wires)
            # print("              from state:", state)
            toggle_light_state(new_state, wiring)
            # print("new state after toggling:", new_state)
            queue.append((new_state, steps + 1))

    return result


def toggle_light_state(light_state, wiring):
    for i in wiring:
        light_state[i] = not light_state[i]


def main(input):
    lights = parse_input_strings(input)

    machines = parse_machines(lights)

    result = 0
    for i, machine in enumerate(machines):
        start_time = datetime.datetime.now()
        machine_result = turn_on_machine(machine)
        result += machine_result
        end_time = datetime.datetime.now()
        time_delta = end_time - start_time
        hours, remainder = divmod(time_delta.total_seconds(), 3600)
        minutes, seconds = divmod(remainder, 60)
        milliseconds = time_delta.microseconds // 1000
        time_str = f"{int(hours):02d}:{int(minutes):02d}:{int(seconds):02d}.{milliseconds:03d}"
        print("machine result:", i, machine_result, "time taken:", time_str)

    return result


if __name__ == "__main__":
    # Read the strategy from the input file.
    with open("input.txt") as f:
        input = f.read()

    # Calculate and print the total score for the strategy.
    result = main(input)
    print("final result: ", result)
