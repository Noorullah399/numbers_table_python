# Ask the user to enter a number for the table
number = int(input('Enter A Number: '))

# Define the range of the table (e.g., from 1 to 10)
number_range = range(1, 11)

# Loop through the range and print the table
for i in number_range:
    result = number * i
    print(f"{number} x {i} = {result}")
