#! /usr/bin/env python


def main(input):

    connected_to = {}
    for line in input.splitlines():
        devices = line.split(" ")
        connected_to[devices[0][:-1]] = devices[1:]

    # start with device 'svr' end with device 'out' find paths
    memo = {}

    def dfs(device, visited, seen_fft, seen_dac):
        # Check memo - key is (device, seen_fft, seen_dac)
        state = (device, seen_fft, seen_dac)
        if state in memo:
            return memo[state]

        # Add current device to visited for cycle detection
        visited.add(device)

        # Track if we see required nodes
        if device == "fft":
            seen_fft = True
        if device == "dac":
            seen_dac = True

        if device == "out":
            # Check if we've seen both required nodes on this path
            result = 1 if (seen_fft and seen_dac) else 0
            visited.remove(device)
            memo[state] = result
            return result

        total_paths = 0

        for neighbor in connected_to.get(device, []):
            if neighbor not in visited:
                total_paths += dfs(neighbor, visited, seen_fft, seen_dac)

        visited.remove(device)
        memo[state] = total_paths
        return total_paths

    total_paths = dfs("svr", set(), False, False)

    print(connected_to)

    result = total_paths
    return result


if __name__ == "__main__":
    # Read the strategy from the input file.
    with open("input.txt") as f:
        input = f.read()

    # Calculate and print the total score for the strategy.
    result = main(input)
    print("final result: ", result)
