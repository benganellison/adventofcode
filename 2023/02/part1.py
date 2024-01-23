def main(input):
    max_cubes = {"red": 12, "green": 13, "blue": 14}
    result = 0
    for line in input.split("\n"):
        game, cubes = line.split(":")
        game = game.strip()[5:]
        cubes = cubes.strip()
        valid = True
        for set_of_cubes in cubes.split(";"):
            set_of_cubes = set_of_cubes.strip()
            for cubes in set_of_cubes.split(","):
                cubes = cubes.strip()
                no, color = cubes.split(" ")
                no = int(no)
                color = color.strip()
                if no > max_cubes[color]:
                    valid = False
                    break
        if valid:
            result += int(game)

    return result


if __name__ == "__main__":
    # Read the strategy from the input file.
    with open("input.txt") as f:
        input = f.read()

    # Calculate and print the total score for the strategy.
    result = main(input)
    print("final result: ", result)
