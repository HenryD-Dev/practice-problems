# Author Henry Doan
# Project 2
# Program will caculate the average test scores for each students
# and the total average test scores from each test.

# First student name and test score:
name1 = input("Please enter your name: ")
name1_score1 = int(input("Enter your first test score: "))
name1_score2 = int(input("Enter your second test score: "))
name1_score3 = int(input("Enter your third test score: "))
name1_score4 = int(input("Enter your four test score: "))

# Second student name and test score:
name2 = input("\nPlease enter your name: ")
name2_score1 = int(input("Enter your first test score: "))
name2_score2 = int(input("Enter your second test score: "))
name2_score3 = int(input("Enter your third test score: "))
name2_score4 = int(input("Enter your four test score: "))

# Third student name and test score:
name3 = input("\nPlease enter your name: ")
name3_score1 = int(input("Enter your first test score: "))
name3_score2 = int(input("Enter your second test score: "))
name3_score3 = int(input("Enter your third test score: "))
name3_score4 = int(input("Enter your four test score: "))

#Test score average for students name1, name2, name3:
name1_avg_test_score = (name1_score1 + name1_score2 + name1_score3 + name1_score4) / 4
name2_avg_test_score = (name2_score1 + name2_score2 + name2_score3 + name2_score4) / 4
name3_avg_test_score = (name3_score1 + name3_score2 + name3_score3 + name3_score4) / 4

#Test score average for test 1 to 4:
test1_avg_score = (name1_score1 + name2_score1 + name3_score1) / 3
test2_avg_score = (name1_score2 + name2_score2 + name3_score2) / 3
test3_avg_score = (name1_score3 + name2_score3 + name3_score3) / 3
test4_avg_score = (name1_score4 + name2_score4 + name3_score4) / 3



print("\n\n-----Here are the results----\n")

#Print out test score average for students name1, name2, name3 to the nearest hundredths:
print(f"Test average for {name1} is {round(name1_avg_test_score , 2)}")
print(f"Test average for {name2} is {round(name2_avg_test_score, 2)}")
print(f"Test average for {name3} is {round(name3_avg_test_score, 2)}")

#Print out test score average for test 1 to 4 to the nearest hundredths:
print(f"\nTest average for the first test score is {round(test1_avg_score, 2)}")
print(f"Test average for the second test score is {round(test2_avg_score, 2)}")
print(f"Test average for the third test score is {round(test3_avg_score, 2)}")
print(f"Test average for the fourth test score is {round(test4_avg_score, 2)}")