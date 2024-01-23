def main(input):
    result = 1

    times = [s for s in input.split("\n")[0].split(": ")[1].split(" ") if s != ""]
    print(times)
    distance = [s for s in input.split("\n")[1].split(": ")[1].split(" ") if s != ""]
    print(distance)

    for race in range(len(times)):
        record = int(distance[race])
        max_time = int(times[race])
        no_of_records = 0
        for time in range(max_time):
            if ( (max_time - time) * time ) > record:
                no_of_records += 1
        result *= no_of_records
    return result


if __name__ == "__main__":
    # Read the strategy from the input file.
    with open("input.txt") as f:
        input = f.read()

    # Calculate and print the total score for the strategy.
    result = main(input)
    print("final result: ", result)
