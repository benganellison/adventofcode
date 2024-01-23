from operator import itemgetter
import json

card_values = {
    "A": 14,
    "K": 13,
    "Q": 12,
    "J": 11,
    "T": 10,
    "9": 9,
    "8": 8,
    "7": 7,
    "6": 6,
    "5": 5,
    "4": 4,
    "3": 3,
    "2": 2,
}


def calculate_score(hand):
    result = 0
    cards = {}
    for card in hand:
        cards[card] = cards.get(card, 0) + 1
    factor = 10**10
    if max(cards.values()) == 5:  # five of a kind
        result += 9 * factor
    elif max(cards.values()) == 4:  # four of a kind
        result += 8 * factor
    elif max(cards.values()) == 3:
        if len(cards) == 2:  # full house
            result += 7 * factor
        else:  # three of a kind
            result += 4 * factor
    elif max(cards.values()) == 2:  # one pair
        if len(cards) == 3:  # two pair
            result += 3 * factor
        else:  # one pair
            result += 1 * factor
    for i, card in enumerate(hand):
        result += card_values[card] * 10 ** (8 - i * 2)
    return result


def main(input):
    result = 0
    hands = []
    for line in input.split("\n"):
        cards = line.split(" ")[0]
        hands.append(
            {
                "rank": calculate_score(cards),
                "value": int(line.split(" ")[1]),
                "hand": cards,
            }
        )

    hands = sorted(hands, key=itemgetter("rank"))
    for i, hand in enumerate(hands):
        result += hand["value"] * (i + 1)
    return result


if __name__ == "__main__":
    # Read the strategy from the input file.
    with open("input.txt") as f:
        input = f.read()

    # Calculate and print the total score for the strategy.
    result = main(input)
    print("final result: ", result)
