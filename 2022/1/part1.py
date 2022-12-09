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

  # Keep track of the Elf with the most calories
  max_calories = 0
  max_elf = None

  # Iterate through the data
  for elf, calories in enumerate(data):
    # Calculate the total number of calories for this Elf
    total_calories = sum(calories)

    # Update the max_calories and max_elf variables if necessary
    if total_calories > max_calories:
      max_calories = total_calories
      max_elf = elf

  # Print the results
  print('Elf', max_elf, 'is carrying the most calories:', max_calories)
