def test__():
    # Read the strategy from the input file.
    with open("./tests/test_input2.txt") as f:
        input = f.read()

    from part2 import main

    # Calculate and print the total score for the strategy.
    result = main(input)

    expected = 48
    assert result == expected, f"Expected: '{expected}', Actual: {result}"
    print("tests passed")
