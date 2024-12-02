def test__():
    # Read the strategy from the input file.
    with open("./tests/test_input.txt") as f:
        input = f.read()

    expected = 4

    from part2 import main

    # Calculate and print the total score for the strategy.
    result = main(input)
    assert result == expected, f"Expected: '{expected}', Actual: {result}"
    print("tests passed")
