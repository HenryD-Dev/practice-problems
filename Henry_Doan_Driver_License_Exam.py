# Author: Henry Doan
# Project 8 part 1
# The local driver’s license office has asked you to create an application
# that grades the written portion of the driver’s license exam.
# The exam has 20 multiple-choice questions.
# Your program should store these correct answers in a list.
# The program should read the student’s answers
# for each of the 20 questions from a text file and store the answers in another list.
# It should then display the total number of correctly answered questions,
# the total number of incorrectly answered questions,
# and a list showing the question numbers of the incorrectly answered questions.

correctAnswer = ["A", "C", "A", "A", "D", "B", "C", "A", "C", "B", "A", "D", "C", "A", "D", "C", "B", "B", "D", "A"]
incorrectAnswers = []


# import Driver_Test.txt file as student's answer
with open("Driver_Test.txt", "r") as file:  
    studentAnswer = file.read().splitlines()
studentAnswer = [answer.upper() for answer in studentAnswer]


# Grading
grading = []
for i in range(20):
    if studentAnswer[i] == correctAnswer[i]:
        grading.append(True)
    else:
        grading.append(False)


# Did the student pass or failed
if grading.count(True) >= 15:
    print("Student passed the exam.")
else:
    print("Student failed the exam.")


# The answers the student gotten correct or wrong
print(f"The total correct answers the student got are: {grading.count(True)}")
print(f"The total incorrect answers the student got are: {grading.count(False)}")


# the question(s) that the student gotten wrong
for index, value in enumerate(grading):
    if value == False:
        index = index + 1
        incorrectAnswers.append(index)
print(incorrectAnswers)