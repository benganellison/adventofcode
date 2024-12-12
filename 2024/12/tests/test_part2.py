def test__full():
    # Read the strategy from the input file.
    with open("./tests/test_input.txt") as f:
        input = f.read()

    from part2 import main

    # Calculate and print the total score for the strategy.
    result = main(input)

    expected = 1206
    assert result == expected, f"Expected: '{expected}', Actual: {result}"
    print("tests passed")


def test__1():
    # Read the strategy from the input file.
    input = """AAAA
BBCD
BBCC
EEEC"""

    from part2 import main

    # Calculate and print the total score for the strategy.
    result = main(input)

    expected = 80
    assert result == expected, f"Expected: '{expected}', Actual: {result}"
    print("tests passed")


def test__2():
    # Read the strategy from the input file.
    input = """AAAAAA
AAABBA
AAABBA
ABBAAA
ABBAAA
AAAAAA"""

    from part2 import main

    # Calculate and print the total score for the strategy.
    result = main(input)

    expected = 368
    assert result == expected, f"Expected: '{expected}', Actual: {result}"
    print("tests passed")

def test__find_islands():
    coords = [
        (0, 0),
        (0, 1),
        (0, 2),
        (0, 3),
        (0, 4),
        (0, 5),
        (1, 0),
        (1, 1),
        (1, 2),
        (1, 5),
        (2, 0),
        (2, 1),
        (2, 2),
        (2, 5),
        (3, 0),
        (3, 3),
        (3, 4),
        (3, 5),
        (4, 0),
        (4, 3),
        (4, 4),
        (4, 5),
        (5, 0),
        (5, 1),
        (5, 2),
        (5, 3),
        (5, 4),
        (5, 5),
    ]

    expected = [[(1, 3), (1, 4), (2, 3), (2, 4)], [(3, 1), (3, 2), (4, 1), (4, 2)]]

    from part2 import find_islands

    result = find_islands(coords)

    print(result)
    assert result == expected, f"Expected: '{expected}', Actual: {result}"


def test__e():
    # Read the strategy from the input file.
    input = """EEEEE
EXXXX
EEEEE
EXXXX
EEEEE"""

    from part2 import main

    # Calculate and print the total score for the strategy.
    result = main(input)

    expected = 236
    assert result == expected, f"Expected: '{expected}', Actual: {result}"
    print("tests passed")
