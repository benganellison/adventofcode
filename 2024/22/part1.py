#! /usr/bin/env python
def parse_input_integers(input):
    return [int(x) for x in input.splitlines()]

def parse_input_strings(input):
    return input.splitlines()

def parse_input_map(input):
    return [list(x) for x in input.splitlines()]

def parse_input_grid_of_int(input):
    return [[int(x) for x in y] for y in input.splitlines()]

def parse_input_tuples(input):
    return [tuple(map(int, x.split(',')) for x in input.splitlines())]

def mix(a, b):
    """ biwise xor operation of a and b"""

    return a ^ b

def prune(a):
    return a % 16777216

def calculate_next_secret(secret):
    secret = mix(secret, secret * 64)
    secret = prune(secret)
    secret = mix(secret, int(secret / 32))
    secret = prune(secret)
    secret = mix(secret, secret * 2048)
    secret = prune(secret)

    return secret

def main(input):

    secrets = parse_input_integers(input)
    secrets_results = {}
    for secret in secrets:
        new_secret = secret
        for i in range(2000):
            new_secret = calculate_next_secret(new_secret)
        secrets_results[secret] = new_secret

    print("secrets_results:", secrets_results)
    result = sum(secrets_results.values())
    return result


if __name__ == "__main__":
    # Read the strategy from the input file.
    with open('input.txt') as f:
        input = f.read()

    # Calculate and print the total score for the strategy.
    result = main(input)
    print("final result: ", result)
