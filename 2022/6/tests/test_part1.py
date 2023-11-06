import pytest

@pytest.mark.parametrize("input, expected", [
    ("mjqjpqmgbljsphdztnvjfqwrcgsmlb", 7),
    ("bvwbjplbgvbhsrlpgdmjqwftvncz", 5),
    ("nppdvjthqldpwncqszvftbrmjlhg", 6),
    ("nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg", 10),
    ("zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw", 11),
])
def test__main(input, expected):
    # Read the strategy from the input file.

    from part1 import main
    # Calculate and print the total score for the strategy.
    result = main(input)
    
    assert result == expected, f"Expected: '', Actual: {result}"
    print("tests passed")