import random

def main():
    hits = int(input('Enter the number of hits'))
    atBats = int(input('Enter the number of atBats'))
    battingAve = hits/atBats
    print('BA is ', format(battingAve, '.3f'))
    input()

    for plateAp in range(10):
        prob = random.randint(1, 1000)/1000

        if battingAve > prob:
            print('It\'s a hit')
            hits = hits + 1
            atBats = atBats + 1
            battingAve = hits/atBats
            print('BA is ', format(battingAve, '.3f'))
            input()

        else:
            print('out')
            atBats = atBats + 1
            battingAve = hits/atBats
            print('BA is ', format(battingAve, '.3f'))
            input()

main()
