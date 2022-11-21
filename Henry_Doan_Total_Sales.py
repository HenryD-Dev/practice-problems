# Author: Henry Doan
# Project 8 part 1
# Design a program that asks the user to enter a store’s sales for each day of the week.
# The amounts should be stored in a list.
# Use a loop to calculate the total sales for the week and display the result.

# Each individual days store into a list
weekTotal = []

# Input validation for input less than zero
def lessZero(x):
    while x < 0:
        x = float(input("\nRe-Enter a number greater than 0:\n"))
        weekTotal.append(x)

# The store sales for each day in the week
def weekSale():
    for saleDays in range(7):
        saleDays = float(input("\nEnter the store sales for the day:\n"))
        if saleDays > 0:
            weekTotal.append(saleDays)
        else: lessZero(saleDays)
weekSale()

print(f"The total sales for the week is: {sum(weekTotal)}$")