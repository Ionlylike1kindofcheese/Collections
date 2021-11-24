import random

colorList = ['oranje', 'blauw', 'groen', 'bruin']

dictionarylist = {

        'oranje' : 0,
        'blauw' : 0,
        'groen' : 0,
        'bruin' : 0
        }

def createBaglist(colors):
    chosencolorslist = []
    for x in range(colors):
        pickColor = random.randrange(0,4)
        chosencolorslist.append(colorList[pickColor])
    return chosencolorslist


def createBagdictionary(colors):
    for y in range(colors):
        pickColor = random.choice(colorList)
        dictionarylist[pickColor] = dictionarylist[pickColor] +1
    return dictionarylist

ammoutcolors = int(input("Hoeveel kleuren wilt u aan de zak toevoegen? "))
# showColors = createBaglist(ammoutcolors)
showColorsdictionary = createBagdictionary(ammoutcolors)
print(showColorsdictionary)