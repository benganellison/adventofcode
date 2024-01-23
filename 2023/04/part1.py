def main(input):
    cards = input.splitlines()
    result = 0
    for card in cards:
        numbers = card.split(":")[1].strip()
        numbers = numbers.split("|")
        winning_numbers = set([n for n in numbers[0].strip().split(" ") if n != ""])
        played_numbers = set([n for n in numbers[1].strip().split(" ") if n != ""])
        corrrect_numbers = len(winning_numbers.intersection(played_numbers))
        if corrrect_numbers > 0:
            result += pow(2, corrrect_numbers - 1)
    return result


if __name__ == "__main__":
    # Read the strategy from the input file.
    with open("input.txt") as f:
        input = f.read()

    # Calculate and print the total score for the strategy.
    result = main(input)
    print("final result: ", result)
