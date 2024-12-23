# import pytest
# @pytest.mark.parametrize(
#     "input, result",
#     [
# "029A", "<vA<AA>>^AvAA<^A>A<v<A>>^AvA^A<vA>^A<v<A>^A>AAvA^A<v<A>A>^AAAvA<^A>A",
# "980A", "<v<A>>^AAAvA^A<vA<AA>>^AvAA<^A>A<v<A>A>^AAAvA<^A>A<vA>^A<A>A",
# "179A", "<v<A>>^A<vA<A>>^AAvAA<^A>A<v<A>>^AAvA^A<vA>^AA<A>A<v<A>A>^AAAvA<^A>A",
# "456A", "<v<A>>^AA<vA<A>>^AAvAA<^A>A<vA>^A<A>A<vA>^A<A>A<v<A>A>^AAvA<^A>A",
# "379A", "<v<A>>^AvA^A<vA<AA>>^AAvA<^A>AAvA^A<vA>^AA<A>A<v<A>A>^AAAvA<^A>A",
# ],
# )


def test__():
    # Read the strategy from the input file.
    with open("./tests/test_input.txt") as f:
        input = f.read()

    from part1 import main

    # Calculate and print the total score for the strategy.
    result = main(input)
    expected = 126384

    assert result == expected, f"Expected: '{expected}', Actual: {result}"
    print("tests passed")


def test__joel():
    # Read the strategy from the input file.
    with open("./tests/input.txt") as f:
        input = f.read()

    from part1 import main

    # Calculate and print the total score for the strategy.
    result = main(input)
    expected = 105458

    assert result == expected, f"Expected: '{expected}', Actual: {result}"
    print("tests passed")
