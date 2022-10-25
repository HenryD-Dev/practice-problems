# Author: Henry Doan
# Project 6
# program will insert text files and input out the added total of all numbers
total = 0

intFile = open("numbers.txt", "r")

number = intFile.readline()   # init

while number != "":     # condition
    number = int(number)
    total = total + number
    number = intFile.readline()   # Update
intFile.close()

sumTotal = open("Henry_Doan_Sum-Of-Numbers.txt", "w")
sumTotal.write(f"Total is: {str(total)}")
sumTotal.close()