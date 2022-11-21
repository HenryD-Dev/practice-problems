testList = []

testOpen = open("test.txt", "r")

testAnswer = testOpen.readlines()

while testAnswer !='':
    testList.append(testAnswer)
    testAnswer = testOpen.readline()
    print(testList)
testOpen.close()