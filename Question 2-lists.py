# 1.
#  Create a list of 5 fruits and print each fruit on a new line using a for loop.

# Create a list of fruits
fruits = ["Apple", "Berry", "Cherry", "Mango", "Orange"]

# Loop through the list and print each fruit
for fruit in fruits:
    print(fruit)



# 2.
#Write a function that takes a list of numbers and returns a new list with 
# each number squared. Example: [1, 2, 3] should become [1, 4, 9].

def square_numbers(numbers):
    # Create a new list with each number squared
    squared_numbers = [num ** 2 for num in numbers]
    return squared_numbers

# Example usage:
numbers = [1, 2, 3]
squared_list = square_numbers(numbers)

# Print the result
print(squared_list)


#3.
# Write a Python program that takes two lists, list1 = [1, 2, 3] and list2 = 
# [4, 5, 6], and combines them into a single list, combined = [1, 4, 2, 5, 3, 6].
# Define the two lists
list1 = [1, 2, 3]
list2 = [4, 5, 6]

# Combine the two lists in an alternating pattern
combined = []
for a, b in zip(list1, list2):
    combined.append(a)
    combined.append(b)

# Print the resulting combined list
print("Combined list:", combined)


# 4.
# Given a list of numbers, [3, 1, 4, 1, 5, 9, 2], write a program 
# to find and print the two largest numbers in the list without using the max() function.
# Define the list of numbers
numbers = [3, 1, 4, 1, 5, 9, 2]

# Initialize two variables to hold the two largest numbers
largest = float()  # Smallest possible value
second_largest = float()  # Smallest possible value

# Iterate through the list to find the two largest numbers
for num in numbers:
    if num > largest:
        second_largest = largest  # Update the second largest
        largest = num  # Update the largest
    elif num > second_largest:
        second_largest = num  # Update only the second largest

# Print the results
print("The largest number is:", largest)
print("The second largest number is:", second_largest)

