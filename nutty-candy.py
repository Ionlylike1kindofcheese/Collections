import random

colorList = ['oranje', 'blauw', 'groen', 'bruin']

dictionarylist = {'oranje' : 0, 'blauw' : 0, 'groen' : 0, 'bruin' : 0}

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


def sortBags(readyforsort, ammoutmnm):
    ammoutorange = 0
    ammoutblue = 0
    ammoutgreen = 0
    ammoutbrown = 0
    currentposition = 0
    sorting = False
    while sorting == False:
        while currentposition < ammoutmnm:
            colorcheck = False
            while colorcheck == False:
                if readyforsort[currentposition] == "oranje":
                    ammoutorange += 1
                    colorcheck = True
                elif readyforsort[currentposition] == "blauw":
                    ammoutblue += 1
                    colorcheck = True
                elif readyforsort[currentposition] == "groen":
                    ammoutgreen += 1
                    colorcheck = True
                elif readyforsort[currentposition] == "bruin":
                    ammoutbrown += 1
                    colorcheck = True
                else:
                    None
            currentposition += 1
        sorting = True
    listcreation = False
    sortedcolorsammout = [ammoutorange, ammoutblue, ammoutgreen, ammoutbrown]
    sortedcolors = []
    currentsortedcolorposition = 0
    while listcreation == False:
        for b in range(sortedcolorsammout[currentsortedcolorposition]):
            sortedcolors.append(colorList[currentsortedcolorposition])
        currentsortedcolorposition += 1
        if currentsortedcolorposition >= 4:
            listcreation = True
    dictionarylist = {'oranje' : ammoutorange, 'blauw' : ammoutblue, 'groen' : ammoutgreen, 'bruin' : ammoutbrown}
    print(dictionarylist)
    return sortedcolors
        
                            

ammoutcolors = int(input("Hoeveel M&Ms wilt u aan de zak toevoegen? "))
mnmcount = ammoutcolors
chosencolorsoutside = createBaglist(ammoutcolors) 
showColorslist = sortBags(chosencolorsoutside, mnmcount)
print(showColorslist)