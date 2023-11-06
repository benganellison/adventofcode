import pytest

@pytest.mark.parametrize("input, expected", [
    ("mjqjpqmgbljsphdztnvjfqwrcgsmlb", 19),
    ("bvwbjplbgvbhsrlpgdmjqwftvncz", 23),
    ("nppdvjthqldpwncqszvftbrmjlhg", 23),
    ("nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg", 29),
    ("zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw", 26),
])
def test__find_message_start(input, expected):
    # Read the strategy from the input file.

    from part2 import find_message_start 
    # Calculate and print the total score for the strategy.
    result = find_message_start(input, 14)
    
    assert result == expected, f"Expected: {expected}, Actual: {result}"
    print("tests passed")