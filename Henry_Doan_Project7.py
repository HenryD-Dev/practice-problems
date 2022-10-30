# Author: Henry Doan
# Project 7
# project will use string manipulation to create and validate
# a school survey on the school overall experience from the user.

# main function


def main():
    # User Inputs
    question1 = input("From 0 to 10 how would you rate the cleanliness of your school:\n")
    isDigit = question1.isdigit()
    print(question1)
    print(isDigit)
    while isDigit == False:
        question1 = input("Re-Enter your answer using numbers:\n")
        isDigit = question1.isdigit()
    print(question1)
    print(isDigit)
    
main()