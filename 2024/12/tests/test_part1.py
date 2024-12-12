def test__():
    # Read the strategy from the input file.
    with open("./tests/test_input.txt") as f:
        input = f.read()

    from part1 import main

    # Calculate and print the total score for the strategy.
    result = main(input)

    expected = 1930
    assert result == expected, f"Expected: '{expected}', Actual: {result}"
    print("tests passed")

def test_main_2():
    input = """AAAA
BBCD
BBCC
EEEC"""

    from part1 import main

    result = main(input)

    expected =140
    assert result == expected, f"Expected: '{expected}', Actual: {result}"
    print("tests passed")