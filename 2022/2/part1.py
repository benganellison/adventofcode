def score_strategy(strategy: str) -> int:
    """Calculates the total score for a Rock Paper Scissors strategy.

    Args:
        strategy: A string containing the strategy guide. Each line should contain
            two characters: the first character is the opponent's choice and the
            second character is the player's choice.

    Returns:
        The total score for the strategy.
    """
    score = 0
    for line in strategy.strip().split('\n'):
        # Parse the opponent's choice and the player's choice from each line.
        opponent, player = line[0], line[-1]
        player_score = 0
        round_score = 0

        # Calculate the score for the player's choice.
        if player == 'X':
            player_score = 1
        elif player == 'Y':
            player_score = 2
        elif player == 'Z':
            player_score = 3

        # Calculate the score for the round outcome.
        if (opponent, player) in [('A', 'X'), ('B', 'Y'), ('C', 'Z')]:
            round_score = 3
        elif (opponent, player) in [('A', 'Y'), ('B', 'Z'), ('C', 'X')]:
            round_score = 6
        else:
            round_score = 0
            
        print(f"opponent: {opponent}, player: {player}, player_score: {player_score}, round_score: {round_score}")

        # Add the score for this round to the total score.
        score += player_score + round_score

    return score


if __name__ == "__main__":
    # Read the strategy from the input file.
    with open('input.txt') as f:
        strategy = f.read()

    # Calculate and print the total score for the strategy.
    total_score = score_strategy(strategy)
    print("final result: ", total_score)
