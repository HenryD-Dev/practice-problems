# Author: Henry Doan
# Project 8 part 2
# program can read the contents of a file, 
# where each record in the file has 5 fields,
# and store all of the records in a single data structure.
# The program should then present a menu of options to the user.
# The user should be able to select one of the following three actions to take:
#1) Display the average number of hours earned.
#2) Display the average GPA.
#3) Display the major of a student with a specified Last name.

personList = []     # Main list where the file get's read and append to.
calculateAvgHours = []  # stores all hours into a list to caculate average.
calculateAvgGPA = []    # stores all GPA into a list to caculate average.


# Read and append data.txt into a list: order is [First, Last, GPA, Major, Hours]
file = open("data.txt", "r")    # open data.txt file
personInfo = file.readline()
while personInfo != "":
    personList.append(personInfo.split())
    personInfo = file.readline()
print(personList)
file.close()


# Function to Read user input and fufill's request.
def inputAnswer(list):
    # User Input: 1, 2, or 3
    userInput = int(input(f"\nEnter 1 if you want to know the average number of hours earned.\nEnter 2 if you want to know the average GPA.\nEnter 3 to find the major of your inputed last name of the person.\n\n"))
    while userInput <= 0 or userInput > 3:
        userInput = int(input(f"\nPlease Re-Enter your answer to only 1, 2, or 3\n"))
    
    # Input 1: Finding average hour earned.
    if userInput == 1:
        for student in list:
            for idx in range(len(student)):
                if idx == 4:
                    calculateAvgHours.append(int(student[idx]))
        avgHours = sum(calculateAvgHours) / len(calculateAvgHours)
        print(f"\nThe average hour earned is: {round(avgHours)}\n") 


    # Input 2: Finding average GPA
    elif userInput == 2:
        for student in list:
            for idx in range(len(student)):
                if idx == 2:
                    calculateAvgGPA.append(float(student[idx]))
        avgGPA = sum(calculateAvgGPA) / len(calculateAvgGPA)
        print(f"\nThe average GPA is: {round(avgGPA, 2)}\n") 

    # Input 3: Finding a person's major using the inputed last name
    elif userInput == 3:
        lastName = input("\nEnter the last name of the person you're looking for:\n\n")
        for student in list:
            if student[1] == lastName:
                print(f"\n{student[3]}\n")

inputAnswer(personList)

