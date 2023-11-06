def find_message_start(input, unique_length=14):
    for index in range(unique_length,len(input)):
        current_set = set(input[index-unique_length:index])
        if len(current_set) == unique_length:
            result = index
            break        
    return result


if __name__ == "__main__":
    # Read the strategy from the input file.
    with open('input.txt') as f:
        input = f.read()

    # Calculate and print the total score for the strategy.
    result = find_message_start(input, 14)
    print("final result: ", result)
