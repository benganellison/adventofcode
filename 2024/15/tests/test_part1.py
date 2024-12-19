def test__():
    with open("./tests/test_input.txt") as f:
        input = f.read()

    from part1 import main
    result = main(input)

    expected = 2028
    assert result == expected, f"Expected: '{expected}', Actual: {result}"


def test__2():
    with open("./tests/test_input2.txt") as f:
        input = f.read()

    from part1 import main
    expected = 10092
    result = main(input)

    assert result == expected, f"Expected: '{expected}', Actual: {result}"
