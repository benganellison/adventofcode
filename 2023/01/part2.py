import re

value_dict = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9,
    "1": 1,
    "2": 2,
    "3": 3,
    "4": 4,
    "5": 5,
    "6": 6,
    "7": 7,
    "8": 8,
    "9": 9,
}


def find_occurences(wordList, bigString, startIndex=0):
    words_string = "|".join(wordList)
    return re.findall(r"(?=(" + words_string + r"))", bigString[startIndex:])


def main(input):
    result = 0
    for line in input.splitlines():
        occurances = find_occurences(value_dict.keys(), line)
        line_value = value_dict[occurances[0]] * 10 + value_dict[occurances[-1]]
        result += line_value
    return result


if __name__ == "__main__":
    # Read the strategy from the input file.
    with open("input.txt") as f:
        input = f.read()

    # Calculate and print the total score for the strategy.
    result = main(input)
    print("final result: ", result)
