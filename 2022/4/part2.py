from typing import List, Tuple


def check_overlap(area1:List[int], area2:List[int]) -> bool:

    if len(set(area1).intersection(area2))>0:
        return True
    return False

def check_assignments(input:str)-> int:
    overlaps = 0
    for line in input.strip().split("\n"):
        areas = line.split(",")
        area1, area2 = get_areas(areas)

        if check_overlap(area1, area2):
            print(f"overlap: {area1} and {area2}")
            overlaps += 1
    return overlaps
        
def get_areas(areas:List[str]) -> Tuple[List[int], List[int]]:
    area1_lower, area1_upper = areas[0].split("-")
    area2_lower, area2_upper = areas[1].split("-")
    area1 = range(int(area1_lower), int(area1_upper)+1)
    area2 = range(int(area2_lower), int(area2_upper)+1)
    return area1, area2

if __name__ == "__main__":
    # Read the strategy from the input file.
    with open('input.txt') as f:
        input = f.read()

    # Calculate and print the total score for the strategy.
    result = check_assignments(input)
    print("final result: ", result)
