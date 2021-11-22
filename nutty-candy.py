import random

colorList = ['oranje', 'blauw', 'groen', 'bruin']

def createBag(colors):
    chosencolors = []
    for x in range(colors):
        pickColor = random.randrange(0,4)
        chosencolors.append(colorList[pickColor])
    return chosencolors

ammoutcolors = int(input("Hoeveel kleuren wilt u aan de zak toevoegen? "))
showColors = createBag(ammoutcolors)
print(showColors)