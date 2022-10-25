# Author: Henry Doan
# Project 6
# program will insert text files and input out the list of numbers
total = 0

intFile = open("numbers.txt", "r")

number = intFile.readline()   # init
fileDisplay = open("Henry_Doan_File-Display.txt", "w")

while number != "":     # condition
    number = int(number)
    fileDisplay.write(f"Num is: {str(number)}\n")
    number = intFile.readline()   # Update
intFile.close()
fileDisplay.close()