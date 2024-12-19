import curses
import time


def test__():
    with open("./tests/test_input.txt") as f:
        input = f.read()

    from part1 import main

    size = 7
    result = main(input, size, 12)

    expected = 22
    assert result == expected, f"Expected: '{expected}', Actual: {result}"
    print("tests passed")


if __name__ == "__main__":
    test__()
