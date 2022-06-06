import random

def lootjeGenerator():
    chosenNames = []
    dictLootje = {}
    allowedToChoose = []
    ableToChoose = []
    count = 0
    repeat = True 
    while repeat:
        names = input("Choose a name, when you're done type stop:\n")
        if names in chosenNames:
            nameChecker()
            continue
        else:
            chosenNames.append(names)
        count += 1
        if names == "stop":
            count -= 1
        if count > 2 and "stop" in chosenNames:
            chosenNames.remove("stop")
        if count <= 2 and names == "stop":
            moreThanTwo()
            chosenNames.remove("stop")
            continue  
        if count > 2 and names == "stop":
            allowedToChoose = chosenNames.copy()
            ableToChoose = chosenNames.copy()
            while True:
                name1 = random.choice(allowedToChoose)
                name2 = random.choice(ableToChoose)
                if name1 != name2:
                    print(name1 + " heeft een lootje getrokken van " + name2)
                    dictLootje[name1]=name2
                    allowedToChoose.remove(name1)
                    ableToChoose.remove(name2)
                    name1 = ""
                    name2 = ""
                    if allowedToChoose == ableToChoose and len(allowedToChoose) == 1:
                        allowedToChoose = chosenNames.copy()
                        ableToChoose = chosenNames.copy()
                        continue
                    if len(allowedToChoose) == 0:
                        return dictLootje

def nameChecker():
    print("Choose a different name")

def moreThanTwo():
    print("You need to type more than two names")

print(lootjeGenerator())