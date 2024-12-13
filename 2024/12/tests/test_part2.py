import pytest

@pytest.mark.parametrize("input, expected", [
    ("""AAAA
BBCD
BBCC
EEEC""", 80),
    ("""OOOOO
OXOXO
OOOOO
OXOXO
OOOOO""", 436),
    (""".G......
GGGG.GGG
.GGGGG..
..GG....""", 414),
    ("""XX.XX
X...X
.....
X...X
XX.XX""", 332),
    ("""AAXXX
AAXAX
AAAAX
AAXAX
AAXXX""", 300),
    ("""HHHHHHH
HOOOOOH
HOHHHOH
HOHOHOH
HHHOHHH""", 464),
    ("""OOHHH
HOHOH
HHHOH""", 146),
    ("""............
...CCC.CC...
....CCCCCC..
......CCC...
.......C....
......CCC...
............
............
............
............
............
............""", 3960),
    ("""OOO
OXO
AOO""", 78),
    ("""AAAAAA
AAABBA
AAABBA
ABBAAA
ABBAAA
AAAAAA""", 368),
    ("""AAAAAB
AAAAAA
ABBAAA
ABBAAA
AAAAAA""", 270),
    ("""RRRRIICCFF
RRRRIICCCF
VVRRRCCFFF
VVRCCCJFFF
VVVVCJJCFE
VVIVCCJJEE
VVIIICJJEE
MIIIIIJJEE
MIIISIJEEE
MMMISSJEEE""", 1206),
    ("""EEEEE
EXXXX
EEEEE
EXXXX
EEEEE""", 236)
])
def test_main(input, expected):
    from part2 import main
    result = main(input)
    assert result == expected, f"Expected: '{expected}', Actual: {result}'"
    print("test_main passed")

def test__full():
    with open("./tests/test_input.txt") as f:
        input = f.read()

    from part2 import main

    result = main(input)
    expected = 1206
    assert result == expected, f"Expected: '{expected}', Actual: {result}'"
    print("test__full passed")


def test__full(): #joels_input
    with open("./tests/input.txt") as f:
        input = f.read()

    from part2 import main

    result = main(input)
    expected = 818286
    assert result == expected, f"Expected: '{expected}', Actual: {result}'"
    print("test__full passed")



def test__explore_new_regions():
    land_map = [
        ["A", "A", "B"],
        ["A", "B", "B"],
        ["C", "C", "C"]
    ]
    from part2 import explore_new_regions

    result = explore_new_regions(land_map)
    expected = {
        "A": [(0, 0), (1, 0), (0, 1)],
        "B": [(2, 0), (1, 1), (2, 1)],
        "C": [(0, 2), (1, 2), (2, 2)]
    }
    assert result == expected, f"Expected: '{expected}', Actual: {result}'"
    print("test__explore_new_regions passed")

def test__find_max_min():
    coords = [(0, 0), (1, 1), (2, 2)]
    from part2 import find_max_min

    result = find_max_min(coords)
    expected = (2, 2, 0, 0)
    assert result == expected, f"Expected: '{expected}', Actual: {result}'"
    print("test__find_max_min passed")


def test__get_outer_bounds():
    coords = [(0, 0), (1, 0), (2, 0)]
    from part2 import get_outer_bounds

    result, _ = get_outer_bounds(coords)
    expected = 4  # This value might need adjustment based on actual perimeter calculation
    assert result == expected, f"Expected: '{expected}', Actual: {result}'"
    print("test__get_outer_bounds passed")

def test__get_outer_bounds_l():
    coords = [(0, 0), (1, 0), (1, 1)]
    from part2 import get_outer_bounds

    result, _ = get_outer_bounds(coords)
    expected = 6  # This value might need adjustment based on actual perimeter calculation
    assert result == expected, f"Expected: '{expected}', Actual: {result}'"
    print("test__get_outer_bounds passed")
