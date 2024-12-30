def test__():
    with open("./tests/test_input.txt") as f:
        input = f.read()

    from part2 import main

    result = main(input)

    expected = "co,de,ka,ta"
    assert result == expected, f"Expected: '{expected}', Actual: {result}"
    print("tests passed")
