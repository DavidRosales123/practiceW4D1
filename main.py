# Problem Set: Working with Numbers & Strings in Python

#################### PROBLEM 1: Types of Numbers & Basic Arithmetic ####################
# Task 1: Declare an integer named 'age' with a value of 25.
age = int(25)
# Print out its type to ensure it's an integer.
print(type(age))
# Task 2: Declare a float named 'height' with a value of 5.9 (which represents someone's height in feet).
height = float(5.9)
# Print out its type to ensure it's a float.
print(type(height))

# Task 3: What is the data type of the result when 'age' is divided by 'height'? 
print(type(age / height))
# Write the code to find out.

#################### PROBLEM 2: Data Type Conversions ####################
# Task 4: Convert the 'age' to float and 'height' to integer.
# Print out both converted values.
print(type(age))
print(type(height))
# Task 5: Add the original 'age' and 'height' values.
# Convert the result into an integer and then print it.
total = int(age + height)
print(total)
#################### PROBLEM 3: Formatting Strings ####################
# Task 6: You are given the following variables:
team_name = "Los Angeles Lakers"
championships_won = 17
# Use string formatting to print: "The Los Angeles Lakers have won 17 championships!"
print(f"The {team_name} have wone {championships_won} championships!")
# Task 7: Create two new variables:
points_game1 = 89
points_game2 = 102
# Use string formatting to print: "The team scored 89 points in game 1 and 102 points in game 2."
print(f"The team scored {points_game1} in game 1 and {points_game2} in game 2.")
# Task 8: Calculate the average points across both games and print:
total = int(points_game1 + points_game2)
average = total/2
# "The average points over two games is: [average_points]!"
print(f"The average points over two games is {average}")
# Ensure average_points is a float with one decimal.
print(type(average))
#################### END OF PROBLEM SET ####################


