def test__score_strategy():
    # Read the strategy from the input file.
    with open('./tests/test_input.txt') as f:
        strategy = f.read()

    from part2 import score_strategy
    # Calculate and print the total score for the strategy.
    total_score = score_strategy(strategy)
    
    assert total_score == 12
    print("tests passed")