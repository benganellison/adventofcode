import pytest


@pytest.mark.parametrize(
    "picoseconds, cheats",
    [
        (50, 32),
        (52, 31),
        (54, 29),
        (56, 39),
        (58, 25),
        (60, 23),
        (62, 20),
        (64, 19),
        (66, 12),
        (68, 14),
        (70, 12),
        (72, 22),
        (74, 4),
        (76, 3),
    ],
)
def test__(picoseconds, cheats):
    # Read the strategy from the input file.
    with open("./tests/test_input.txt") as f:
        input = f.read()

    from part2 import main

    # Calculate and print the total score for the strategy.
    result, saves_exactly = main(input, picoseconds=picoseconds, no_of_cheats=20)
    print(picoseconds, saves_exactly)

    expected = cheats
    assert saves_exactly == expected, f"Expected: '{expected}', Actual: {saves_exactly}"
    print("tests passed")
