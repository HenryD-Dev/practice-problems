# Author: Henry Doan
# Project 10

# In this project we are going to calculate several values for each player. 
# One is the aforementioned batting average.
# A second calculated value is called the slugging percentage.
# This value is found as follows: (1*Singles + 2*Doubles + 3*Triples + 4*HomeRuns)/AB.
# Our data does not provide the number of singles directly but it does tell us the number of
# hits from which we can subtract the number of doubles,
# triples, and home runs to get to the number of singles.
# Additionally, you will need to calculate the overall batting average for all 25
# players combined. Note that this is different than the mean batting average of the 25 players.
# After all calculations are performed,
# create a nicely formatted report (and send it to an output file)
# that shows the top five players for each of the 6 individually calculated values.
# Additionally, include in this report the overall batting average for all 25 players combined.

# Create Players Stat Nested Lists:
def readPlayerStats():

    playersStats = []

    file = open("BBStats.txt", "r")    # open data.txt file
    playerInfo = file.readline()
    while playerInfo != "":
        playersStats.append(playerInfo.split())
        playerInfo = file.readline()
    #print(playersStats)
    file.close()
    return playersStats

# Players' informations
playerStats = readPlayerStats()


# Calculate batting Average for each players
def calPlayerBattingAvg(data):

    totalBattingAvg = []

    for playerIdx in range(1, len(data)):

        playerHits = int(data[playerIdx][7])
        playerAtBats = int(data[playerIdx][5])
        playerBattingAvg = playerHits / playerAtBats

        totalBattingAvg.append(playerBattingAvg)

    roundTotalBattingAvg = [round(num, 4) for num in totalBattingAvg]
    print(f"\n\nThis is the batting averages of each 25 players in original text file order:\n{roundTotalBattingAvg}")

    return totalBattingAvg

playerBattingAvg = calPlayerBattingAvg(playerStats)


# Calculate slugging percentage for each players
def calPlayerSluggingPercent(data):

    totalSluggingPercent = []

    for playerIdx in range(1, len(data)):

        playerHits = int(data[playerIdx][7])
        playerDoubles = int(data[playerIdx][8])
        playerTriples = int(data[playerIdx][9])
        playerHomeRuns = int(data[playerIdx][10])
        playerAtBats = int(data[playerIdx][5])
        playerSingles = playerHits - playerDoubles - playerTriples - playerHomeRuns
        
        calculatePlayerSluggingPercent = (playerSingles + playerDoubles * 2 + playerTriples * 3 + playerHomeRuns * 4) / playerAtBats

        totalSluggingPercent.append(calculatePlayerSluggingPercent)

    roundTotalSluggingPercent = [round(num, 4) for num in totalSluggingPercent]
    
    print(f"\n\nThis is the slugging percentages of each 25 players in original text file order:\n{roundTotalSluggingPercent}")


    return totalSluggingPercent

playerSluggingPercent = calPlayerSluggingPercent(playerStats)


# Calculate on-base percentage for each players
def calPlayerOnBasePercent(data):

    totalOnBasePercent = []

    for playerIdx in range(1, len(data)):

        playerHits = int(data[playerIdx][7])
        playerWalks = int(data[playerIdx][12])
        playerHitByPitch = int(data[playerIdx][16])
        playerSacrificeFly = int(data[playerIdx][17])
        playerAtBats = int(data[playerIdx][5])
        
        calculatePlayerOnBasePercent = (playerHits + playerWalks + playerHitByPitch) / (playerAtBats + playerWalks + playerHitByPitch + playerSacrificeFly)

        totalOnBasePercent.append(calculatePlayerOnBasePercent)

    roundTotalOnBasePercent = [round(num, 4) for num in totalOnBasePercent]
    
    print(f"\n\nThis is the on-base percentage of each 25 players in original text file order:\n{roundTotalOnBasePercent}")


    return totalOnBasePercent

playerOnBasePercent = calPlayerOnBasePercent(playerStats)


# Calculate on-base percentage for each players
def calPlayerOPS(data1, data2):

    totalOPS = []

    for i in range(len(data1)):
        playerSlugging = data1[i]
        playerOnBase = data2[i]
        totalOPS.append(playerSlugging + playerOnBase)

    roundTotalOPS = [round(num, 4) for num in totalOPS]

    print(f"\n\nThis is the on-base plus slugging of each 25 players in original text file order:\n{roundTotalOPS}")

    return totalOPS

playerOPS = calPlayerOPS(playerSluggingPercent, playerOnBasePercent)


# Calculate runs produced
def calPlayerRunsProduced(data):
    totalRunsProduced = []

    for playerIdx in range(1, len(data)):

        playerRuns = int(data[playerIdx][6])
        playerHomeRuns = int(data[playerIdx][10])
        playerRBI = int(data[playerIdx][11])

        calculateplayerRunsProduced = (playerRuns + playerRBI) - playerHomeRuns

        totalRunsProduced.append(calculateplayerRunsProduced)

    print(f"\n\nThis is the Runs Produced from each 25 players in original text file order:\n{totalRunsProduced}")

    return totalRunsProduced

playerRunsProduced = calPlayerRunsProduced(playerStats)


# Calculate Runs Produced per At-Bats
def calPlayerRunsProducedPerAtBat(data1, data2):
    
    totalAtBats = []
    totalRunsProducedPerAtBat = []

    for playerIdx in range(1, len(data1)):

        playerAtBat = int(data1[playerIdx][5])
    
        totalAtBats.append(playerAtBat)

    for i in range(len(totalAtBats)):

        totalRunsProducedPerAtBat.append(data2[i] / totalAtBats[i])

    roundTotalRunsProducedPerAtBat = [round(num, 4) for num in totalRunsProducedPerAtBat]

    print(f"\n\nThis is the Runs Produced per At-Bats from each 25 players in original text file order:\n{roundTotalRunsProducedPerAtBat}")

    return totalRunsProducedPerAtBat

playerRunsProducedPerAtBat = calPlayerRunsProducedPerAtBat(playerStats, playerRunsProduced)



def calAvgOfPlayerBattingAvg(data):
    
    averageOfBattingAvg = []

    sumOfBattingAverage = sum(data)

    averageOfBattingAvg.append(sumOfBattingAverage / len(data))

    roundAverageOfBattingAvg = [round(num, 4) for num in averageOfBattingAvg]

    print(f"\n\nThis is the average of batting averages from the sum each of 25 players; orginized in the original text file order:\n{roundAverageOfBattingAvg}")

    return averageOfBattingAvg

averageOfPlayerBattingAvg = calAvgOfPlayerBattingAvg(playerBattingAvg)




def sortAndExport(mainData, data1, data2, data3, data4, data5, data6, data7):

    playerNames = []
    namedBattingAvgs = []
    namedSluggingPercent = []
    namedOnBasePercent = []
    playersOPS = []
    playersRunsProduced = []
    playersRunsProducedPerAtBat = []

    for playerIdx in range(1, len(mainData)):

        playerFirstName = mainData[playerIdx][0]
        playerLastName = mainData[playerIdx][1]
        playerFullName = playerFirstName + " " + playerLastName

        playerNames.append(playerFullName)

    roundData1 = [round(num, 3) for num in data1]
    roundData2 = [round(num, 4) for num in data2]
    roundData3 = [round(num, 4) for num in data3]
    roundData4 = [round(num, 4) for num in data4]
    roundData6 = [round(num, 4) for num in data6]
    roundData7 = [round(num, 4) for num in data7]



    for i in range(len(playerNames)):
            
        totalOPS.append(playerSlugging + playerOnBase)



    data1.sort(key=lambda x:x[i], reverse = True)
    data2.sort(key=lambda x:x[i], reverse = True)
    data3.sort(key=lambda x:x[i], reverse = True)
    data4.sort(key=lambda x:x[i], reverse = True)
    data5.sort(key=lambda x:x[i], reverse = True)
    data6.sort(key=lambda x:x[i], reverse = True)


    with open("BBStats.txt", "w") as file:
        for line in data1:
            topBattingAvg = file.write(f"{line}\n")

        for line in data2:        
            topSluggingPercent = file.write(f"{line}\n")

        for line in data3:
            topOnBasePercent = file.write(f"{line}\n")

        for line in data4:
            topOPS = file.write(f"{line}\n")

        for line in data5:            
            topRunsProduced = file.write(f"{line}\n")

        for line in data6:            
            topRunsPerAtBats = file.write(f"{line}\n")

        for line in data7:           
            averageOfBattingAvg = file.write(f"{line}\n")


#sortAndExport(playerStats, playerBattingAvg, playerSluggingPercent, playerOnBasePercent, playerOPS, playerRunsProduced, playerRunsProducedPerAtBat, averageOfPlayerBattingAvg)