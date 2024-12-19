import pytest

@pytest.mark.parametrize(
    "filename, expected",
    [
        ("./tests/test_input1.txt", 7036),
        ("./tests/test_input2.txt", 11048),
        ("./tests/input.txt", 89460),
    ],
)
def test__example_1(filename, expected):
    # Read the strategy from the input file.
    with open(filename) as f:
        input = f.read()

    from part1 import main

    # Calculate and print the total score for the strategy.
    result = main(input, None)

    assert result == expected, f"Expected: '{expected}', Actual: {result}"
