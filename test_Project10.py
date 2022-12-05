playersStats = []
battingAvgs = []

def readFile():
    file = open("BBStats.txt", "r")    # open data.txt file
    playerInfo = file.readline()
    while playerInfo != "":
        playersStats.append(playerInfo.split())
        playerInfo = file.readline()
    #print(playersStats)
    file.close()
    return playersStats

playersStats = readFile()

def calPlayerBattingAvg(data):
    totalBattingAvg = []
    for playerIdx in range(1, len(data)):
        playerHits = int(data[playerIdx][7])
        playerAtBats = int(data[playerIdx][5])
        playerBattingAvg = playerHits / playerAtBats

        totalBattingAvg.append(playerBattingAvg)

    print("\n\n")
    print([totalBattingAvg, len(totalBattingAvg)])

    return totalBattingAvg

#calPlayerBattingAvg(playersStats)


def playerNames(data):
    nameContainer = []
    for playerIdx in range(1, len(data)):

        playerFirstName = data[playerIdx][0]
        playerLastName = data[playerIdx][1]
        playerFullName = playerFirstName + " " + playerLastName

        nameContainer.append(playerFullName)
    return nameContainer
# -- Player's Name list:
players = playerNames(playersStats)



def addNametoScores(players, scores):
    nestedData = []
    for i in range(len(players)):
        nestedData.append([players[i], scores[i]])
    
    print(nestedData)
    return nestedData





#def sortAndExport(mainData):

#    playerNames = []

#    for playerIdx in range(1, len(mainData)):

#        playerFirstName = mainData[playerIdx][0]
#        playerLastName = mainData[playerIdx][1]
#        playerFullName = playerFirstName + " " + playerLastName

#        playerNames.append(playerFullName)

#    print(playerNames, len(playerNames))

#sortAndExport(playersStats)




# def calPlayerBattingAvg(data):
#    totalBattingAvg = []
#    for playerIdx in range(1, len(data)):
#        totalPlayerBattingAvg = []

#        for scoreIdx in range(8, 11):
#            totalPlayerBattingAvg.append(int(data[playerIdx][scoreIdx]))
#        
#        playerHits = int(data[playerIdx][7]) - sum(totalPlayerBattingAvg)

#        print(totalPlayerBattingAvg)
#        calculateAvg = sum(totalPlayerBattingAvg) / int(data[playerIdx][5])
#        totalBattingAvg.append(calculateAvg)
#    print("\n\n")
#    print([totalBattingAvg, len(totalBattingAvg)])

#    return 

