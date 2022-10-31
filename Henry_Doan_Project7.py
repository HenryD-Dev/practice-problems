# Author: Henry Doan
# Project 7
# project will use string manipulation to create and validate
# a school survey on the school overall experience from the user.

# main function

def main():
    
    # Question 1: The User's rating on cleanliness of their school

    question1 = input("\nFrom 0 to 10 how would you rate the cleanliness of your school:\n")
    
    isDigit = question1.isdigit()   # True or False build-in function to see of string contains only digits    
    
    while isDigit == False: # Input validation
        question1 = input("\nRe-Enter your answer using numbers no less than 0 or more than 10 (unless you really like it that much):\n")
        isDigit = question1.isdigit()

    # Question 2: The User is asked if they would recommend others to join or attend their school.

    question2 = input("\nWould you recommend others to join or attend your school? (Enter Yes or No.)\n")
    
    question2 = question2.lower()   # Lowercase the string to help with input validation
    
    question2 = question2.rstrip(".!?")     # Remove any punctuations from the user's input answer.

    endWith = question2.endswith("yes") or question2.endswith("no")     # Checks if answer is yes or no
    
    # replace answers to prefered Uppercases and Lowercases
    if question2 == "yes":
        question2 = question2.replace("yes", "Yes")
    elif question2 == "no":
        question2 = question2.replace("no", "No")

    # Input Validation
    while endWith == False: # input validation
        question2 = input("\nRe-Enter your answer with yes or no:\n")
        question2 = question2.lower() 
        question2 = question2.rstrip(".!?")
        endWith = question2.endswith("yes") or question2.endswith("no")
        if question2 == "yes":
            question2 = question2.replace("yes", "Yes")
        elif question2 == "no":
            question2 = question2.replace("no", "No")

    # Question 3: User's School name.
    
    question3 = input("\nEnter your School Name: (No Spaces)\n")

    isAlpha = question3.isalpha()   # Checks if answer only contains words and no numbers

    # Input Validation
    while isAlpha == False:
        question3 = input("\nRe-Enter your School Name using only words and no numbers: (No Spaces)\n")
        isAlpha = question3.isalpha()

    print(f"\nThank you for your feedback.\n\nYour Answers are:\nRated cleanliness: {question1}\nRecommend school: {question2}\nSchool Name: {question3}")
main()