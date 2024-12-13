def test__():
    # Read the strategy from the input file.
    with open("./tests/test_input.txt") as f:
        input = f.read()

    from part2 import main

    # Calculate and print the total score for the strategy.
    total_tokens, num_prizes = main(input)

    expected = 2
    assert num_prizes == expected, f"Expected: '{expected}', Actual: {num_prizes}"
    print("tests passed")
