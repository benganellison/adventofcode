from collections import defaultdict


def main(input):
    cards = input.splitlines()
    card_outcome = {}
    for card_id, card in enumerate(cards):
        numbers = card.split(":")[1].strip()
        numbers = numbers.split("|")
        winning_numbers = set([n for n in numbers[0].strip().split(" ") if n != ""])
        played_numbers = set([n for n in numbers[1].strip().split(" ") if n != ""])
        corrrect_numbers = len(winning_numbers.intersection(played_numbers))
        card_outcome[card_id] = corrrect_numbers

    list_of_cards = [i for i in range(len(cards))]
    my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    result = defaultdict(int)
    for card_id in range(len(cards)):
        result[card_id] += 1
        for i in range(card_outcome[card_id]):
            result[card_id + 1 + i] += result[card_id]
    return sum(result.values())


if __name__ == "__main__":
    # Read the strategy from the input file.
    with open("input.txt") as f:
        input = f.read()

    # Calculate and print the total score for the strategy.
    result = main(input)
    print("final result: ", result)
