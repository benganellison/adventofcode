''' Advent of Code 2022 - Day 1 - Part 2
written by https://chat.openai.com/chat'''


# Open the input file
with open('input.txt') as input_file:
  # Create an empty list to hold the data
  data = []

  # Create a list to hold the current Elf's calories
  current_elf = []

  # Read in the data line by line
  for line in input_file:
    # If the line is empty, we've reached the end of the current Elf's inventory
    if line.strip() == '':
      # Add the current Elf's calories to the data list
      data.append(current_elf)

      # Clear the current Elf's list to start a new one
      current_elf = []
    else:
      # Parse the line as an integer and add it to the current Elf's list
      current_elf.append(int(line))

  # Add the last Elf's calories to the data list
  data.append(current_elf)

  # Create a list to hold the top three Elves and their Calories
  top_elves = []

  # Iterate through the data
  for elf, calories in enumerate(data):
    # Calculate the total number of calories for this Elf
    total_calories = sum(calories)

    # If the top_elves list is not full, add the current Elf to it
    if len(top_elves) < 3:
      top_elves.append((elf, total_calories))
    # Otherwise, check if the current Elf's Calories is higher than the lowest-ranked Elf in the list
    else:
      # Sort the top_elves list by Calories in descending order
      top_elves = sorted(top_elves, key=lambda x: x[1], reverse=True)

      # If the current Elf's Calories is higher than the lowest-ranked Elf, replace that Elf in the list
      if total_calories > top_elves[-1][1]:
        top_elves[-1] = (elf, total_calories)

  # Sort the top_elves list by Calories in descending order
  top_elves = sorted(top_elves, key=lambda x: x[1], reverse=True)

  # Calculate the total Calories carried by the top three Elves
  total_calories = sum([x[1] for x in top_elves])


  # Print the results
  print('The top three Elves are:')
  for elf, calories in top_elves:
    print('Elf', elf, 'with', calories, 'calories')
  print('Total calories:', sum([x[1] for x in top_elves]))
