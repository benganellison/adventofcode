#! /usr/bin/env python

import itertools

MOD = 16777216


def mix(a, b):
    return a ^ b


def prune(a):
    return a % MOD


def calculate_next_secret(secret):
    secret = mix(secret, secret * 64)
    secret = prune(secret)
    secret = mix(secret, int(secret / 32))
    secret = prune(secret)
    secret = mix(secret, secret * 2048)
    secret = prune(secret)

    return secret


def generate_prices(initial_secret):
    prices = []
    current_secret = initial_secret
    prices.append(abs(current_secret) % 10)

    secrets = [current_secret]

    price_changes = []
    last_price = abs(current_secret) % 10
    for _ in range(2000):
        current_secret = calculate_next_secret(current_secret)
        secrets.append(current_secret)
        current_price = abs(current_secret) % 10
        price_changes.append(current_price - last_price)
        prices.append(current_price)
        last_price = current_price

    return prices, price_changes


def find_sale_price_for_pattern(prices, changes, pattern):

    for i in range(len(changes) - 3):
        if (
            changes[i] == pattern[0]
            and changes[i + 1] == pattern[1]
            and changes[i + 2] == pattern[2]
            and changes[i + 3] == pattern[3]
        ):
            return (
                prices[i + 4]
            )
    return 0


def main(input_text):
    buyers_initial_secrets = [int(x) for x in input_text.splitlines()]

    buyers_data = []
    for secret in buyers_initial_secrets:
        prices, changes = generate_prices(secret)
        buyers_data.append((prices, changes))

    best_pattern, best_sum = calculate_best_price_pattern(buyers_data)

    print(f"Best 4-change pattern: {best_pattern}")
    print(f"Max bananas: {best_sum}")
    return best_sum

def calculate_best_price_pattern(buyers_data):
    best_pattern = None
    best_sum = 0

    possible_deltas = range(-9, 10)  # -9..9 inclusive

    for (c1, c2, c3, c4) in itertools.product(possible_deltas, repeat=4):
        pattern = (c1, c2, c3, c4)
        total_bananas = 0
        sale_prices = []
        for prices, changes in buyers_data:
            sale_price = find_sale_price_for_pattern(
                prices, changes, pattern
            )
            total_bananas += sale_price

        if total_bananas > best_sum:
            best_sum = total_bananas
            best_pattern = pattern
    return best_pattern,best_sum


if __name__ == "__main__":
    with open("input.txt") as f:
        puzzle_input = f.read()

    answer = main(puzzle_input)
    print("final result (part two):", answer)
