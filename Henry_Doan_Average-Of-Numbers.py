# Author: Henry Doan
# Project 6
# program will insert text files and input out the list of numbers
count = 0
totalNumber = 0

intFile = open("numbers.txt", "r")

number = intFile.readline()   # init

while number != "":     # condition
    number = int(number)
    count = count + 1
    totalNumber = totalNumber + number
    number = intFile.readline()   # Update
intFile.close()

averageNum = totalNumber/count

averageNumber = open("Henry_Doan_Average-Of-Numbers.txt", "w")
averageNumber.write("The average is: " + format(averageNum, ".2f"))
averageNumber.close()