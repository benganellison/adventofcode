def test__():
    with open("./tests/test_input.txt") as f:
        input = f.read()

    from part1 import main

    result = main(input)

    expected = 6
    assert result == expected, f"Expected: '{expected}', Actual: {result}"
