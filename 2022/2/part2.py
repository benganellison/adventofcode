def score_strategy(strategy: str) -> int:
    """Calculates the total score for a Rock Paper Scissors strategy.

    Args:
        strategy: A string containing the strategy guide. Each line should contain
            two characters: the first character is the opponent's choice and the
            second character is the player's choice.

    Returns:
        The total score for the strategy.
    """

    winning = {"A": "B", "B": "C", "C": "A"}
    draw = {"A": "A", "B": "B", "C": "C"}
    losing = {"A": "C", "B": "A", "C": "B"}
    score = 0
    for line in strategy.strip().split('\n'):
        # Parse the opponent's choice and the player's choice from each line.
        opponent, round_strategy = line[0], line[-1]
        player_score = 0
        round_score = 0

        player = ""
        if round_strategy == 'X':
            player = losing[opponent]
        elif round_strategy == 'Y':
            player = draw[opponent]
        elif round_strategy == 'Z':
            player = winning[opponent]

        # Calculate the score for the player's choice.
        if player == 'A':
            player_score = 1
        elif player == 'B':
            player_score = 2
        elif player == 'C':
            player_score = 3

        # Calculate the score for the round outcome.
        # A for Rock, B for Paper, and C for Scissors
        if (opponent, player) in [('A', 'A'), ('B', 'B'), ('C', 'C')]:
            round_score = 3
        elif (opponent, player) in [('A', 'B'), ('B', 'C'), ('C', 'A')]:
            round_score = 6
        else:
            round_score = 0

        print(f"opponent: {opponent}, player: {player}, player_score: {player_score}, round_score: {round_score}")

        # Add the score for this round to the total score.
        score += player_score + round_score

    return score


if __name__ == "__main__":
    # Read the strategy from the input file.
    with open('./input.txt') as f:
        strategy = f.read()

    # Calculate and print the total score for the strategy.
    total_score = score_strategy(strategy)
    print("final result: ", total_score)
