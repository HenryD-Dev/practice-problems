# Author: Henry Doan
# Project 8 part 1
# Design a program that asks the user to enter a series of 20 numbers.
# The program should store the numbers in a list then display the following data:
#   --The lowest number in the list--
#   --The highest number in the list--
#   --The total of the numbers in the list--
#   --The average of the numbers in the list--

# A list of the 20 numbers.
list20 = []

# User adds the 20 numbers to the list.
def numAppend():
    for number20 in range(20):
        number20 = float(input("\nEnter a number:\n"))
        list20.append(number20)
numAppend()


# total and average
listTotal = sum(list20)
listAverage = sum(list20) / len(list20)

# Answers
print(f"The lowest number in the list is: {min(list20)}")
print(f"The highest number in the list is: {max(list20)}")
print(f"The total of the list is: {round(listTotal, 2)}")
print(f"The average of the list is: {round(listAverage, 2)}")