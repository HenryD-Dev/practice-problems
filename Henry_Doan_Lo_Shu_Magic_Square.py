# Author: Henry Doan
# Project 8 part 1
# In a program you can simulate a magic square using a two-dimensional list.
# Write a function that accepts a two-dimensional list as an argument
# and determines whether the list is a Lo Shu Magic Square.
# Test the function in a program.

# the main Magic Square
loShuMagicSquare = [
    [4,9,2],
    [3,5,7],
    [8,1,6]]

# making it look like a 3x3 square
for row in loShuMagicSquare:
    print(row)
# Validating if it's a Lo Shu Magic Square or not function
def magicSquare(list2D):
    if isinstance(list2D, list) and len(list2D)==3:
        list1D = sum(list2D,[]) # ID list
        print(list1D)
        if max(list1D) >= 10 or min(list1D) <= 0:   # Input Validation: less than 0 or Greater than 9
            print("Check if your list values are greater than 9 or less than 0")
            return False
        if len(list1D) != len(set(list1D)):   # Duplicate Valadation
            print("Check if your list contains duplicate values")
            return False
        # Index gets organized into rows, columns, and diagonal:
        row1Sum = list2D[0][0] + list2D[0][1] + list2D[0][2]
        row2Sum = list2D[1][0] + list2D[1][1] + list2D[1][2]
        row3Sum = list2D[2][0] + list2D[2][1] + list2D[2][2]
        col1Sum = list1D[0] + list1D[3] + list1D[6]
        col2Sum = list1D[1] + list1D[4] + list1D[7]
        col3Sum = list1D[2] + list1D[5] + list1D[8]
        rightDiagonalSum = list1D[2] + list1D[4] + list1D[6]
        leftDiagonalSum = list1D[0] + list1D[4] + list1D[8]
        # if it's a Lo Shu Magic Square, it's True. Else False
        if row1Sum == row2Sum == row3Sum == col1Sum == col2Sum == col3Sum == rightDiagonalSum == leftDiagonalSum:
            print("Your 2D list is a Lo Shu Magic Square.")
            return True
        else:
            print("Your 2D list is not a Lo Shu Magic Square.")
            return False

print(magicSquare(loShuMagicSquare))