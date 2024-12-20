import pytest


@pytest.mark.parametrize(
    "picoseconds, cheats",
    [
    (2, 14),
    (4, 14),
    (6, 2),
    (8, 4),
    (10, 2),
    (12, 3),
    (20, 1),
    (36, 1),
    (38, 1),
    (40, 1),
    (64, 1),
],
)
def test__(picoseconds, cheats):
    # Read the strategy from the input file.
    with open("./tests/test_input.txt") as f:
        input = f.read()

    from part1 import main

    # Calculate and print the total score for the strategy.
    result, saves_exactly = main(input, picoseconds=picoseconds)
    print(picoseconds, saves_exactly)

    expected = cheats
    assert saves_exactly == expected, f"Expected: '{expected}', Actual: {result}"
    print("tests passed")
