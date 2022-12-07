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

playerStats = readPlayerStats()


# Calculate batting Average for each players
def calPlayerBattingAvg(data):

    totalBattingAvg = []

    for playerIdx in range(1, len(data)):

        playerHits = int(data[playerIdx][7])
        playerAtBats = int(data[playerIdx][5])
        playerBattingAvg = playerHits / playerAtBats

        totalBattingAvg.append(playerBattingAvg)

    roundTotalBattingAvg = [round(num, 3) for num in totalBattingAvg]
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


# Caculate the overall batting average of the 25 players
def calOverallPlayerBattingAvg(data):
    
    overallBattingAvg = []

    totalHits = []

    totalAtBats = []

    for playerIdx in range(1, len(data)):

        playerHits = int(data[playerIdx][7])
        playerAtBat = int(data[playerIdx][5])
    
        totalHits.append(playerHits)
        totalAtBats.append(playerAtBat)

    sumOfHits = sum(totalHits)
    sumOfAtBats = sum(totalAtBats)

    overallBattingAvg.append(sumOfHits / sumOfAtBats)

    roundAverageOfBattingAvg = [round(num, 4) for num in overallBattingAvg]
    print(f"\n{totalHits}\n")
    print(f"\n{totalAtBats}\n")
    print(f"\n{sumOfHits}\n")
    print(f"\n{sumOfAtBats}\n")

    print(f"\n\nThis is the overall batting average of the 25 players; orginized in the original text file order:\n{roundAverageOfBattingAvg}\n")

    return overallBattingAvg

overallPlayerBattingAvg = calOverallPlayerBattingAvg(playerStats)


# Player Names
def playerNames(data):
    nameContainer = []
    for playerIdx in range(1, len(data)):

        playerFirstName = data[playerIdx][0]
        playerLastName = data[playerIdx][1]
        playerFullName = playerFirstName + " " + playerLastName

        nameContainer.append(playerFullName)
    return nameContainer
# -- Player's Name list:
players = playerNames(playerStats)


# add names to Scores
def addNametoScores(players, scores):
    nestedData = {}
    for i in range(len(players)):
        nestedData[scores[i]] = players[i]
 
    return nestedData

# Lists of Names with their categories Data:
playerWithBatting = addNametoScores(players, playerBattingAvg)
playerWithSlugging = addNametoScores(players, playerSluggingPercent)
playerWithOnBase = addNametoScores(players, playerOnBasePercent)
playerWithOPS = addNametoScores(players, playerOPS)
playerWithRunPro = addNametoScores(players, playerRunsProduced)
playerWithRunPerAtBat = addNametoScores(players, playerRunsProducedPerAtBat)


# Sorting players to be highest 5 players
def sortTopFivePlayers(data, mapping, rounded):
    # Ordered from highest to lowest scores
    scores = sorted(data, reverse=True)
    topPlayers = []

    for idx in range(5):
        topPlayers.append([mapping[scores[idx]], round(scores[idx], rounded)]) 
    
    return topPlayers

# Top FIVE Players in each categories:
topFiveBattingAvg = sortTopFivePlayers(playerBattingAvg, playerWithBatting, 3)
topFiveSluggingPercent = sortTopFivePlayers(playerSluggingPercent, playerWithSlugging, 4)
topFiveOnBasePercent = sortTopFivePlayers(playerOnBasePercent, playerWithOnBase, 4)
topFiveOPS = sortTopFivePlayers(playerOPS, playerWithOPS, 4)
topFiveRunsProduced = sortTopFivePlayers(playerRunsProduced, playerWithRunPro, 4)
topFiveRunPerAtBat = sortTopFivePlayers(playerRunsProducedPerAtBat, playerWithRunPerAtBat, 4)


# Export The output Text File that contains the top 5 players in each caculations,
# as well as the average of all 25 players' Batting Average.
def exportOutput(data1, data2, data3, data4, data5, data6, data7):

    baseBallReport = "Henry_Doan_BaseBall_Report.txt"

    with open(baseBallReport, "w") as file:
        
        header1 = file.write("The Top 5 players in Batting Average:\n\n")
        
        for sublist in data1:
            writeBattingAvg = "{}: {}\n".format(sublist[0], sublist[1])
            file.write(writeBattingAvg)

        header2 = file.write("\n\nThe Top 5 players in Slugging Percentage:\n\n")

        for sublist in data2:        
            writeSluggingPercent = "{}: {}\n".format(sublist[0], sublist[1])
            file.write(writeSluggingPercent)

        header3 = file.write("\n\nThe Top 5 players in On-Base Percentage:\n\n")

        for sublist in data3:
            writeOnBasePercent = "{}: {}\n".format(sublist[0], sublist[1])
            file.write(writeOnBasePercent)

        header4 = file.write("\n\nThe Top 5 players in OPS:\n\n")

        for sublist in data4:
            writeOPS = "{}: {}\n".format(sublist[0], sublist[1])
            file.write(writeOPS)

        header5 = file.write("\n\nThe Top 5 players in Runs Produced:\n\n")

        for sublist in data5:            
            writeRunsProduced = "{}: {}\n".format(sublist[0], sublist[1])
            file.write(writeRunsProduced)

        header6 = file.write("\n\nThe Top 5 players in Runs Produced per At-Bat:\n\n")

        for sublist in data6:            
            writeRunsPerAtBats = "{}: {}\n".format(sublist[0], sublist[1])
            file.write(writeRunsPerAtBats)

        header7 = file.write("\n\nThe overall Batting averages of the 25 players:\n\n")

        for line in data7:           
            file.write(f"{round(line, 3)}")

exportOutput(topFiveBattingAvg, topFiveSluggingPercent, topFiveOnBasePercent, topFiveOPS, topFiveRunsProduced, topFiveRunPerAtBat, overallPlayerBattingAvg)