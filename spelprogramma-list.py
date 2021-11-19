import random

spelList = ['Monopoly', 'Yathzee', 'Bridge', 'Poker', 'Pesten', 'Mens erger je niet', 'Cluedo']

def spelProgramma(spelList, minimum, maximum):
    hoeveelspellen = random.randrange(3,11)
    for x in range(hoeveelspellen):
        welkspel = random.randrange(0,7)
        print(spelList[welkspel])
    print("Minimum =", minimum)
    print("Maximum =", maximum)


spelProgramma(spelList, 3, 10)