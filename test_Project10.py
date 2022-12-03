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

calPlayerBattingAvg(playersStats)







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