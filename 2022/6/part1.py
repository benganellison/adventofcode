def main(input):
    for index in range(4,len(input)):
        if len(set(input[index-4:index])) == 4:
            result = index
            break
        
    return result


if __name__ == "__main__":
    # Read the strategy from the input file.
    with open('input.txt') as f:
        input = f.read()

    # Calculate and print the total score for the strategy.
    result = main(input)
    print("final result: ", result)
