# Author: Henry Doan
# Project 5 Part 1
# program that asks the user for a player name,
# the number of at-bats for the player,
# the number of singles, the number of doubles,
# the number of triples, and the number of home runs
# and accepts the total number of hits and the at-bats and returns the batting average.
# it will also accepts the number of singles, doubles, triples, home runs,
# and at-bats and returns the slugging percentage.

# Import a file with definitions for this file to call
import BBFUN

from BBFUN import sluggingPercent, battingAvg

def main():     # start of the function
# User Input
    playerName = input("\n" + "Enter player name here:" + "\n")

    atBat = int(input("Enter the number of at-bats from the player:" + "\n"))
    while atBat < 0:
        print("Entered number cannot be below 0")
        atBat = int(input("\nRe-Enter the number of at-bats from the player:" + "\n"))
    
    single = int(input("Enter the number of singles from the player:" + "\n"))
    while single < 0 or single > atBat:
        print("Entered number cannot be below 0")
        single = int(input("\nRe-Enter the number of at-bats from the player:" + "\n"))
    
    double = int(input("Enter the number of doubles from the player:" + "\n"))
    while double < 0 or double > atBat - single:
        print("Entered number cannot be below 0")
        double = int(input("\nRe-Enter the number of at-bats from the player:" + "\n"))

    triple = int(input("Enter the number of triples from the player:" + "\n"))
    while triple < 0 or triple > atBat - single - double:
        print("Entered number cannot be below 0")
        triple = int(input("\nRe-Enter the number of at-bats from the player:" + "\n"))

    homeRun = int(input("Enter the number of Home runs from the player:" + "\n"))
    while homeRun < 0 or homeRun > atBat - single - double - triple:
        print("Entered number cannot be below 0")
        homeRun = int(input("\nRe-Enter the number of at-bats from the player:" + "\n"))

    print(playerName , "'s batting average is: ", format(BBFUN.battingAvg(single, double ,triple, homeRun)/atBat, ".3f"))
    print(playerName , "'s slugging percentage is: ", format(BBFUN.sluggingPercent(single, double ,triple, homeRun)/atBat, ".3f"))

main()