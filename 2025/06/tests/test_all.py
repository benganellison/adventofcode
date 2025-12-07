import pytest


@pytest.mark.parametrize(
    "part,expected",
    [
        ("part1", 4277556),
        ("part2", 3263827),
        ("part2_alt", 3263827),
        ("part2_alt2", 3263827),
    ],
    ids=["Part 1", "Part 2", "Part 2 (alt)", "Part 2 (alt2)"],
)
def test_solution(part, expected):
    # Read the strategy from the input file.
    with open("./tests/test_input.txt") as f:
        input_data = f.read()

    # Dynamically import the correct part
    module = __import__(part)

    # Calculate and print the total score for the strategy.
    result = module.main(input_data)

    assert result == expected, f"Expected: {expected!r}, Actual: {result!r}"
    print(f"{part} test passed")
