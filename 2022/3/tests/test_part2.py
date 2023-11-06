def test__get_total_priorities():
    # Read the strategy from the input file.
    with open('./tests/test_input.txt') as f:
        input = f.read()

    from part2 import get_total_priorities
    # Calculate and print the total score for the strategy.
    result = get_total_priorities(input)
    
    assert result == 70
    print("tests passed")