def test__():
    # Read the strategy from the input file.
    with open("./tests/test_input.txt") as f:
        input = f.read()

    from part2 import main

    # Calculate and print the total score for the strategy.
    result = main(input)

    expected = 126384
    assert result == expected, f"Expected: '{expected}', Actual: {result}"
    print("tests passed")


def test__joel():
    # Read the strategy from the input file.
    with open("./tests/input.txt") as f:
        input = f.read()

    from part2 import main

    # Calculate and print the total score for the strategy.
    result = main(input)

    expected = 105458
    expected = 129551515895690
    assert result == expected, f"Expected: '{expected}', Actual: {result}"
    print("tests passed")
