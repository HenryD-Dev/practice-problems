# Author Henry Doan
# Project 4
# Program will ask the user for the number of students in a class and the number of grades for each student.
# Program will use the information to caculate an average grade for the class using the grades the student got for each assignments, and repeat the process for the
# next classes until the user stops.



#Accumulators for class average
studentGrade = 0      # accumulator for an individual student's grade
totalAverage = 0     # accumulator used to calculate overall class average


# While loop variable for user to input a new class
nextClassIsTrue = True

# caculating average grade for the class using while and for loops
while nextClassIsTrue:

# User inputs 
    studentTotal = int(input("Enter the total students in the class: \n"))
    while studentTotal <= 0:
        print("\n" +"The total amount of students cannot be 0 or lower. ")
        studentTotal = int(input("\n" + "Re-Enter the total students in the class: \n"))
    
    studentAssignment = int(input("Enter the number of assignments for each student: \n"))
    while studentAssignment <= 0:
        print("\n" + "The total amount of assignment cannot be 0 or lower. ")
        studentAssignment = int(input("\n" +"Re-Enter the number of assignments: \n"))


# caculating average grade for the class
    for studentCount in range(studentTotal):
        print("\n" + "Student ", studentCount + 1)
        student = input("Enter student name: " + "\n")
        print("\n" + "Enter grades for ", student, ": ")

        for assignment in range(studentAssignment):
            print("\n" + "Assignment ", assignment+1)
            grades = int(input("Enter grade: " + "\n"))
            while grades < 0 or grades > 100:
                print("\n" +"Please re-enter grades between 0 and 100 \n")
                grades = int(input("Please re-enter the grade: "))
            
            studentGrade += grades
    
        
        studentAverage = studentGrade/studentAssignment
    
        print("\n" + "Average grade for ", student,  " is: ", format(studentAverage, ".2f"))
    
        studentGrade = 0                                   # reset for next student
        totalAverage += studentAverage
    
    print("\n" + "Overall Class average is ", format(totalAverage/studentTotal, ".2f"))

    # Reseting Values
    totalAverage = 0
    studentTotal = 0

   # Ask if user want to calculate for another class
    nextClassIsTrue = input("\n" + "Do you want to calculate another class average? (Enter 'yes' to caculate the next class, otherwise type anything else to stop):" + "\n")

    if nextClassIsTrue == "yes" or nextClassIsTrue == "Yes" or nextClassIsTrue == "y" or nextClassIsTrue == "Y":
        nextClassIsTrue = True
    else:
        nextClassIsTrue = False
        

# The program has STOPPED
print("\n" + "The program has now stopped")