def test__():
    # Read the strategy from the input file.
    with open('./tests/test_input.txt') as f:
        input = f.read()

    from part2 import find_the_top_crates
    # Calculate and print the total score for the strategy.
    result = find_the_top_crates(input)
    
    assert result == "MCD"
    print("tests passed")