def test__():
    with open("./tests/test_input.txt") as f:
        input = f.read()

    from part2 import main

    global path, valid_errors, size_y
    result = main(input, 7, 12)

    expected = "6,1"
    assert result == expected, f"Expected: '{expected}', Actual: {result}"
    print("tests passed")


if __name__ == "__main__":
    test__()