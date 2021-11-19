listOne = [1,2,3,4,5,6,7,8,9,10]
listtwo = [2,4,6,8,10,12,14,16,18,20]

def addAndDisplayLists():
    print("---------------")
    print("Add Lists")
    for x in range(0,10):
        global listOne
        global listtwo
        anwser = listOne[x] + listtwo[x]
        print(str(listOne[x]), "+", str(listtwo[x]), "=", str(anwser))


def subtractAndDisplayLists():
    print("---------------")
    print("Subtract Lists")
    for x in range(0,10):
        global listOne
        global listtwo
        anwser = listOne[x] - listtwo[x]
        print(str(listOne[x]), "-", str(listtwo[x]), "=", str(anwser))


def multiplyAndDisplayList():
    print("---------------")
    print("Multiply Lists")
    for x in range(0,10):
        global listOne
        global listtwo
        anwser = listOne[x] * listtwo[x]
        print(str(listOne[x]), "x", str(listtwo[x]), "=", str(anwser))


def divideAndDisplayLists():
    print("---------------")
    print("Divide Lists")
    for x in range(0,10):
        global listOne
        global listtwo
        anwser = listOne[x] / listtwo[x]
        print(str(listOne[x]), ":", str(listtwo[x]), "=", str(anwser))


addAndDisplayLists()
subtractAndDisplayLists()
multiplyAndDisplayList()
divideAndDisplayLists()