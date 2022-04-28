import random 

redBlue = ""

countRed = 1
countBlue = 1
countWhite = 0

red =  [-2, 1, 2, 3, 4, "", 6, 7, 8, 9] 
blue = [14, 12, 11, 7, 6, 5, 4, 3, -1, -2]
white = [1,2,3,4,5]


def checker(lijst,choice,pos):
    index = pos
    rightValid = True
    global listOfNums
    listOfNums = []

    while rightValid:
        if index == 10:
            rightValid = False
            break
        if lijst[index] == int(choice):
            index += 1 
        elif lijst[index] == "":
            index += 1
        elif int(choice) < lijst[index] and lijst == red:
            index += 1
        elif int(choice) > lijst[index] and lijst == red:
            print("Choose a different position")
            redPos()
        elif int(choice) < lijst[index] and lijst == blue:
            print("Choose a different position")
            bluePos()
        elif int(choice) > lijst[index] and lijst == blue:
            index += 1

    index = pos
    leftValid = True

    while leftValid:
        if index == -1:
            leftValid = False
            break
        if lijst[index] == int(choice):
            index -= 1
        elif lijst[index] == "":
            index -= 1
        elif int(choice) > lijst[index] and lijst == red:
            index -= 1
        elif int(choice) < lijst[index] and lijst == red:
            print("Choose a different position")
            redPos()
        elif int(choice) > lijst[index] and lijst == blue:
            print("Choose a different position")
            bluePos()
        elif int(choice) < lijst[index] and lijst == blue:
            index -= 1


def redPos():   
    position = int(input(f"Choose a position in the red row\n "))
    if int(choice) > red[index] or int(choice) < red[index]:
        repeat = False
        endScore()
    else:
        lijst = red
        checker(lijst,choice,position - 1)
        red[position - 1] = choice
        countRed += 1

def bluePos():
    position = int(input(f"Choose a position in the blue row\n"))
    lijst = blue
    checker(lijst,choice,position - 1)
    blue[position - 1] = choice
    global countBlue
    countBlue += 1

def endScore():
    countRed = 10
    countBlue = 10
    if countRed == 10 and countBlue == 10 or countWhite == 5:
        lst(red) 
        lst(blue)
        lst(white) 

        subtotal_1 = 0 
        for i in range(len(red)):
            subtotal_1 += red[i] * blue[i]
        
        subtotal_2 = emptyPos * sum(white)
        finalScore = subtotal_1 - subtotal_2
        print(f"Your final score: {finalScore}")


emptyPos = 0
def lst(lijst):
    for i,x in enumerate (lijst):
        if x == "":
            lijst[i] = 0
            global emptyPos
            emptyPos += 1
     
repeat = True
while repeat:

    randomRed = random.randint(1,6)
    randomBlue = random.randint(1,6)
    randomWhite = random.randint(1,3)

    outcome_a = randomRed + randomBlue + randomWhite
    outcome_b = randomRed + randomBlue - randomWhite
    outcome_c = randomRed + randomBlue
    outcome_d = randomRed - randomWhite 

    print("----------------------------------------------------------------------------")
    print("     Dobbel Trobbel")
    print("----------------------------------------------------------------------------")
    print("position :    |  1  |  2  |  3  |  4  |  5  |  6  |  7  |  8  |  9  |  10  |")
    print("----------------------------------------------------------------------------")
    print(f"Scores Red:   | {red[0]}  |  {red[1]}  |  {red[2]}  |  {red[3]}  |  {red[4]}  |  {red[5]}   |  {red[6]}  |  {red[7]} |  {red[8]} |{red[9]}      |")
    print(f"Scores Blue:  | {blue[0]}  |  {blue[1]} | {blue[2]}  |  {blue[3]}   |  {blue[4]}  |  {blue[5]}  |  {blue[6]}   |  {blue[7]}  | {blue[8]}  |  {blue[9]}  |")
    print("----------------------------------------------------------------------------")
    print(f"Scores White: | {white[0]}    |  {white[1]}  |  {white[2]}    | {white[3]}   |  {white[4]}   |")
    print("----------------------------------------------------------------------------")
    print("")
    print("Rolling dice........")
    print("")
    print( " " + str(randomRed) + "     " + str(randomBlue) + "     " + str(randomWhite))
    print("")
    print("----------------------------------------------------------------------------")
    print("Calculated results")
    print(f"a: {outcome_a} = {randomRed} + {randomBlue} + {randomWhite}")
    print(f"b: {outcome_b} = {randomRed} + {randomBlue} - {randomWhite}")
    print(f"c: {outcome_c} = {randomRed} + {randomBlue}")
    print(f"d: {outcome_d} = {randomRed} - {randomWhite}" )
    print("If chosen for c or d, the white value will be registered")
    
    color = ""
    if randomRed > randomBlue:
        print("You must register in the red scores")
        color = red
    elif randomBlue > randomRed:
        print("You must register in the blue scores")
        color = blue
    else:
        print("You may register in the red or the blue scores")
        redBlue = input("Red or blue (r or b)")
        if redBlue == "r":
            color = red
        else:
            color = blue


    wrongChoice = True
    while wrongChoice:
        listOutcomes = [outcome_a, outcome_b, outcome_c,outcome_d]
        letters = ["a", "b", "c", "d"]

        choice = input("Please choose which result to register (a, b, c, d)\n")
        letterChoice = choice
        for index in range(0,4): 
            if choice == letters[index]:
                choice = listOutcomes[index]

        if choice in color:
            print("Choose a different number")
        else:
            wrongChoice = False

    if color == red:
        redPos()
    elif color == blue:
        bluePos()        

    if letterChoice == "c" or letterChoice == "d":
        white.append(randomWhite)
        countWhite += 1