import math

def main(input):
    result = 0
    for line in input.split("\n"):
        max_cubes = {"red": 0, "green": 0, "blue": 0}
        game, cubes = line.split(":")
        game = game.strip()[5:]
        cubes = cubes.strip()
        for set_of_cubes in cubes.split(";"):
            set_of_cubes = set_of_cubes.strip()
            for cubes in set_of_cubes.split(","):
                cubes = cubes.strip()
                no, color = cubes.split(" ")
                no = int(no)
                color = color.strip()
                if no > max_cubes[color]:
                    max_cubes[color] = no
        result += math.prod(max_cubes.values())

    return result


if __name__ == "__main__":
    # Read the strategy from the input file.
    with open("input.txt") as f:
        input = f.read()

    # Calculate and print the total score for the strategy.
    result = main(input)
    print("final result: ", result)
