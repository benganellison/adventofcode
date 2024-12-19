import pytest


@pytest.mark.parametrize(
    "filename, expected",
    [
        ("./tests/test_input1.txt", 45),
        ("./tests/test_input2.txt", 64),
        # ("./tests/input.txt", 89460),
    ],
)
def test__example_2(filename, expected):
    # Read the strategy from the input file.
    with open(filename) as f:
        input = f.read()

    from part2 import main

    # Calculate and print the total score for the strategy.
    result = main(input, None)

    assert result == expected, f"Expected: '{expected}', Actual: {result}"
