import random 


redBlue = ""

countRed = 1
countBlue = 1
countWhite = 0

red =  [-2, "", "", "", "", "", "", "", "", ""] 
blue = ["", "", "", "", "", "", "", "", "", -2]
white = [1,2,3,4,5]


# Valid plek checker
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
        elif outcome_a < blue[index] and outcome_b < blue[index] and outcome_c < blue[index] and outcome_d < blue[index]:
            endScore()
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
        elif outcome_a > blue[index] and outcome_b > blue[index] and outcome_c > blue[index] and outcome_d > blue[index]:
            endScore()
            repeat = False
            break
        elif int(choice) < lijst[index] and lijst == red:
            print("Choose a different position")
            redPos()
        elif int(choice) > lijst[index] and lijst == blue:
            print("Choose a different position")
            bluePos()
        elif int(choice) < lijst[index] and lijst == blue:
            index -= 1


# rode lijst positie
def redPos():   
    position = int(input(f"Choose a position in the red row\n "))
# checker of de getallen kwijt kan
    if outcome_a > red[index] or outcome_a < red[index] and outcome_b > red[index] or outcome_b < red[index] and outcome_c > red[index] or outcome_c < red[index] and outcome_d > red[index] or outcome_d < red[index]:
        global repeat
        repeat = False
        endScore()
    else:
        lijst = red
        checker(lijst,choice,position - 1)
        red[position - 1] = choice
        countRed += 1

# blauwe lijst positie
def bluePos():
    position = int(input(f"Choose a position in the blue row\n"))
    
    lijst = blue
    checker(lijst,choice,position - 1)
    blue[position - 1] = choice
    global countBlue
    countBlue += 1

# eindscore
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


# van lege plekken een 0 maken
emptyPos = 0
def lst(lijst):
    for i,x in enumerate (lijst):
        if x == "":
            lijst[i] = 0
            global emptyPos
            emptyPos += 1
     
# rode en blauwe lijst generator
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

        # keuze koppelen aan berekend uitkomst
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