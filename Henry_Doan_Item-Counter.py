nameCount = 0
strFile = open("names.txt", "r")

name = strFile.readline()   # init

while name != "":     # condition
    nameCount = nameCount + 1
    name = strFile.readline()   # Update
strFile.close()

itemCounter = open("Henry_Doan_Item-Counter.txt", "w")
itemCounter.write(f"There are {nameCount} names.")
itemCounter.close()