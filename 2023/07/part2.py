from operator import itemgetter

card_values = {
    "A": 14,
    "K": 13,
    "Q": 12,
    "T": 10,
    "9": 9,
    "8": 8,
    "7": 7,
    "6": 6,
    "5": 5,
    "4": 4,
    "3": 3,
    "2": 2,
    "J": 1,
}

hand_types = {
    "Five_of_a_kind": 9,
    "Four_of_a_kind": 7,
    "Full_house": 5,
    "Three_of_a_kind": 4,
    "Two_pair": 3,
    "One_pair": 2,
    "High_card": 1,
}


def calculate_score(hand):
    cards = {}
    for card in hand:
        cards[card] = cards.get(card, 0) + 1
    factor = 10**10
    hand_type = get_hand_type(cards)
    rank_factor = hand_types.get(hand_type, 1) * factor
    for i, card in enumerate(hand):
        rank_factor += card_values[card] * 10 ** (8 - i * 2)
    return rank_factor


def get_hand_type(cards):
    jokers = cards.get("J", 0)
    if max(cards.values()) == 5:  # five of a kind
        return "Five_of_a_kind"
    elif max(cards.values()) == 4:  # four of a kind
        if jokers > 0:
            return "Five_of_a_kind"
        return "Four_of_a_kind"
    elif max(cards.values()) == 3:
        if len(cards) == 2:  # full house
            if jokers > 0:  # full house with jokers is a five of a kind
                return "Five_of_a_kind"
            return "Full_house"
        else:  # three of a kind
            if jokers > 0:  # three of a kind with atleast one joker is a four of a kind
                return "Four_of_a_kind"
            return "Three_of_a_kind"
    elif max(cards.values()) == 2:  # one pair at least
        if len(cards) == 3:  # three unique cards == two pair
            if jokers == 2:  # two pair with two jokers is a four of a kind
                return "Four_of_a_kind"
            elif jokers == 1:  # two pair + one joker is a full house
                return "Full_house"
            return "Two_pair"
        else:  # one pair
            if (
                jokers > 0
            ):  # one pair + one joker (or pair of jokers + single cards) is a three of a kind
                return "Three_of_a_kind"
            else:
                return "One_pair"
    elif jokers > 0:
        return "One_pair"
    return "High_card"


def main(input):
    result = 0
    hands = []
    for line in input.split("\n"):
        cards = line.split(" ")[0]
        hands.append(
            {
                "rank": calculate_score(cards),
                "hand": cards,
                "value": int(line.split(" ")[1]),
            }
        )

    hands = sorted(hands, key=itemgetter("rank"))
    for i, hand in enumerate(hands):
        hand["score"] = hand["value"] * (i + 1)
    result = sum([hand["score"] for hand in hands])
    return result


if __name__ == "__main__":
    # Read the strategy from the input file.
    with open("input.txt") as f:
        input = f.read()

    # Calculate and print the total score for the strategy.
    result = main(input)
    print("final result: ", result)

