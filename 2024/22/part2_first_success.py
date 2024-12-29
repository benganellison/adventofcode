#! /usr/bin/env python


from collections import defaultdict
MOD = 16777216
def parse_input_integers(input):
    return [int(x) for x in input.splitlines()]

def mix(a, b):
    return a ^ b

def prune(a):
    return a % MOD

def calculate_next_secret(secret):
    secret = mix(secret, secret * 64)
    secret = prune(secret)
    secret = mix(secret, secret // 32)
    secret = prune(secret)
    secret = mix(secret, secret * 2048)
    secret = prune(secret)

    return secret

def generate_prices(initial_secret):
    prices = []
    changes = []
    current_secret = initial_secret
    # current_price = current_secret % 10
    current_price = int(str(current_secret)[-1])
    prices.append(current_price)
    for _ in range(2000):
        previous_price = current_price
        current_secret = calculate_next_secret(current_secret)
        current_price = current_secret % 10
        changes.append(current_price - previous_price)
        prices.append(current_price)

    return prices, changes


def get_price_changes(prices):
    changes = []
    for i in range(len(prices) - 1):
        changes.append(prices[i + 1] - prices[i])
    return changes


def calculate_value_per_pattern(secrets):
    value_per_pattern = defaultdict(int)
    for secret in secrets:
        prices, changes = generate_prices(secret)
        found_for_this_buyer = set()
        for i in range(2000 - 3):
            pattern = (
                changes[i],
                changes[i + 1],
                changes[i + 2],
                changes[i + 3],
            )

            if pattern not in found_for_this_buyer:
                sale_price = prices[i + 4]
                value_per_pattern[pattern] += sale_price
                found_for_this_buyer.add(pattern)
    return value_per_pattern


def highest_value(pattern_to_sum):
    best_value = max(pattern_to_sum.values())
    pest_patterns = [pattern for pattern, value in pattern_to_sum.items() if value == best_value]
    print("best patterns:", pest_patterns)
    return best_value


def main(input):
    secrets = parse_input_integers(input)

    value_per_pattern = calculate_value_per_pattern(secrets)

    result = highest_value(value_per_pattern)
    print(f"Max bananas: {result}")
    return result


if __name__ == "__main__":
    with open("input.txt") as f:
        puzzle_input = f.read()

    answer = main(puzzle_input)
    print("final result (part two):", answer)
