def test__():
    # Read the strategy from the input file.
    with open('./tests/test_input.txt') as f:
        input = f.read()

    from part2 import check_assignments
    # Calculate and print the total score for the strategy.
    result = check_assignments(input)
    
    assert result == 4
    print("tests passed")