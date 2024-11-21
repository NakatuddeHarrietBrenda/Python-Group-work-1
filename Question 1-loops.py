#1.
# Write a Python program that prints all even numbers between 1 and 20 
# using a for loop.

for even in range(1, 21):
    # Checking if the number is even
    if even % 2 == 0:
        print(even)
#
def evenNumber():
    for even in range (2,20,2):
        print(even)
evenNumber()


 
# 2.
# Use a while loop to ask the user to input a number until they provide a 
# number greater than 10.

number = 0  # Initialize the variable to store user input

while number <= 10:  # Keep asking until the number is greater than 10

    number = int(input("\nPlease enter a number greater than 10: ")) 
     # Get user input
    if number <= 10:
        print('Number should be greater than 10. Try again!')
    else:
       print(f"\nCongraturations! You entered {number}, which is greater than 10.\t")


# 3.
# Write a program that prints the multiplication table
#  (from 1 to 10) for numbers from 1 to 5 using nested for loops.

for num in range(1, 6):  # Outer loop for numbers from 1 to 5

    print(f"\nMultiplication Table for {num}:\t")
    
    for multiplier in range(1, 11):  # Inner loop for multipliers from 1 to 10
        output = num * multiplier
        print(f"{num} * {multiplier} = {output}")

    print()  # Blank line for better readability

# 4. 
# Given a list of integers, [4, 7, 2, 9, 12, 15], write a program using a
#for loop to find the sum of all odd numbers and print the result.

# Define the list of integers
numbers = [4, 7, 2, 9, 12, 15]

# Initialize a variable to store the sum of odd numbers
sum_of_odd_numbers = 0

# Loop through the list to check each number
for num in numbers:
    if num % 2 != 0:  # Check if the number is odd
        sum_of_odd_numbers += num  # Add the odd number to the sum

print(f"Sum of all odd numbers: {sum_of_odd_numbers}")


