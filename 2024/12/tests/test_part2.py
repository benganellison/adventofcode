def test__full():
    with open("./tests/test_input.txt") as f:
        input = f.read()

    from part2 import main

    result = main(input)
    expected = 1206
    assert result == expected, f"Expected: '{expected}', Actual: {result}'"
    print("test__full passed")

def test__1():
    input = """AAAA
BBCD
BBCC
EEEC"""

    from part2 import main

    result = main(input)
    expected = 80
    assert result == expected, f"Expected: '{expected}', Actual: {result}'"
    print("test__1 passed")

def test__2():
    input = """AAAAAA
AAABBA
AAABBA
ABBAAA
ABBAAA
AAAAAA"""

    from part2 import main

    result = main(input)
    expected = 368
    assert result == expected, f"Expected: '{expected}', Actual: {result}'"
    print("test__2 passed")

def test__find_islands():
    coords = [
        (0, 0), (0, 1), (0, 2), (0, 3), (0, 4), (0, 5),
        (1, 0), (1, 1), (1, 2),                 (1, 5),
        (2, 0), (2, 1), (2, 2),                 (2, 5),
        (3, 0), (3, 3), (3, 4),                 (3, 5),
        (4, 0), (4, 3), (4, 4),                 (4, 5),
        (5, 0), (5, 1), (5, 2), (5, 3), (5, 4), (5, 5),
    ]

    expected = [
        [
            (-1, -1),
            (-1, 0),
            (0, -1),
            (-1, 1),
            (1, -1),
            (-1, 2),
            (2, -1),
            (-1, 3),
            (3, -1),
            (-1, 4),
            (4, -1),
            (-1, 5),
            (5, -1),
        ],
        [(1, 3), (1, 4), (2, 3), (2, 4)],
        [(3, 1), (3, 2), (4, 1), (4, 2)],
    ]

    from part2 import find_islands

    result = find_islands(coords)
    print("Islands:", result)  # Debug print
    assert result == expected, f"Expected: '{expected}', Actual: {result}'"

def test__e():
    input = """EEEEE
EXXXX
EEEEE
EXXXX
EEEEE"""

    from part2 import main

    result = main(input)
    expected = 236
    assert result == expected, f"Expected: '{expected}', Actual: {result}'"
    print("test__e passed")

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

def test__find_cost_of_fences():
    landtypes = {
        "A": [(0, 0), (1, 0), (0, 1)],
        "B": [(2, 0), (1, 1), (2, 1)],
        "C": [(0, 2), (1, 2), (2, 2)]
    }
    from part2 import find_cost_of_fences

    result = find_cost_of_fences(landtypes)
    expected = 48
    assert result == expected, f"Expected: '{expected}', Actual: {result}'"
    print("test__find_regions_not_connected passed")

def test__get_empty_areas():
    coords = [(0, 0), (0, 1), (1, 1), (1,2), (2, 2)]
    from part2 import get_empty_areas

    result = get_empty_areas(coords)
    expected = [
        (-1, -1),
        (-1, 0),
        (-1, 1),
        (-1, 2),
        (0, -1),
        (0, 2),
        (1, -1),
        (1, 0),
        (2, -1),
        (2, 0),
        (2, 1),
    ]
    assert result == expected, f"Expected: '{expected}', Actual: {result}'"
    print("test__get_empty_areas passed")

def test__find_max_min():
    coords = [(0, 0), (1, 1), (2, 2)]
    from part2 import find_max_min

    result = find_max_min(coords)
    expected = (2, 2, 0, 0)
    assert result == expected, f"Expected: '{expected}', Actual: {result}'"
    print("test__find_max_min passed")

def test__calculate_perimeter_cost():
    regions = [(0, 0), (1, 0), (0, 1)]
    from part2 import calculate_perimeter_cost

    result = calculate_perimeter_cost(regions)
    expected = 18  # This value might need adjustment based on actual perimeter calculation
    assert result == expected, f"Expected: '{expected}', Actual: {result}'"
    print("test__calculate_perimeter_cost passed")

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
