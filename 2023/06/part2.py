def main(input):
    times = int(input.split("\n")[0].split(": ")[1].strip().replace(" ", ""))
    print(times)
    distance = int(input.split("\n")[1].split(": ")[1].strip().replace(" ", ""))
    print(distance)

    record = distance
    max_time = times
    no_of_records = 0
    for time in range(max_time):
        if ((max_time - time) * time) > record:
            no_of_records += 1

    return no_of_records


if __name__ == "__main__":
    # Read the strategy from the input file.
    with open("input.txt") as f:
        input = f.read()

    # Calculate and print the total score for the strategy.
    result = main(input)
    print("final result: ", result)
