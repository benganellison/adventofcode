import pytest


@pytest.mark.parametrize(
    "part,expected,input_file",
    [
        ("part1", 5, "test_input.txt"),
        ("part2", 2, "test_input2.txt"),
    ],
    ids=["Part 1", "Part 2"],
)
def test_solution(part, expected, input_file):
    # Read the strategy from the input file.
    with open(f"./tests/{input_file}") as f:
        input_data = f.read()

    # Dynamically import the correct part
    module = __import__(part)

    # Calculate and print the total score for the strategy.
    result = module.main(input_data)

    assert result == expected, f"Expected: {expected!r}, Actual: {result!r}"
    print(f"{part} test passed")
