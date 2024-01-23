from datetime import datetime
from tqdm import tqdm

def main(input):
    sections = input.split("\n\n")
    result = 0

    map_order = [
        "seed-to-soil",
        "soil-to-fertilizer",
        "fertilizer-to-water",
        "water-to-light",
        "light-to-temperature",
        "temperature-to-humidity",
        "humidity-to-location",
    ]

    seeds = [
        int(seed) for seed in sections.pop(0).split(":")[1].split(" ") if seed != ""
    ]
    seeds = [(seeds[i], seeds[i + 1]) for i in range(0, len(seeds), 2)]
    seed_map = {}

    print("starting parsing sections")
    for section in sections:
        lines = section.split("\n")
        section_name = lines.pop(0).split(" ")[0]
        seed_map[section_name] = []
        for line in lines:
            destination, source, length = (int(i) for i in line.split(" "))
            seed_map[section_name].append(
                {
                    "start": source,
                    "end": source + length,
                    "offset": destination - source,
                }
            )

    print("starting seed loop")
    lowest_location_value = 0
    for seed, count in tqdm(seeds):
        for i in range(count):
            next_index = seed + i
            for step in map_order:
                # print(
                #     "step: ", step, "next_index: ", next_index, "seed_map: ", seed_map[step]
                # )
                for map in seed_map[step]:
                    if next_index >= map["start"] and next_index < map["end"]:
                        next_index += map["offset"]
                        break
            # print("location: ", next_index)
            if int(next_index) < lowest_location_value or lowest_location_value == 0:
                lowest_location_value = int(next_index)
    result = lowest_location_value
    print("result: ", result)
    return result


if __name__ == "__main__":
    # Read the strategy from the input file.
    with open("input.txt") as f:
        input = f.read()

    # Calculate and print the total score for the strategy.
    print(f"starting main at {datetime.now()}")
    result = main(input)
    print("final result: ", result)
    print(f"ending main at {datetime.now()}")
