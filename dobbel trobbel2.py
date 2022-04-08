import random 

negativeNumForRed = -2
negativeNumForBlue = -2

listOfNums = "all positions except -2" 
redBlue = ""

red =  [negativeNumForRed, 0, 2, 4, 5, "", 7, 10, 11, ""] 
blue = [14, 12, 11, "", 6, 5, "", 3, -1, negativeNumForBlue]
white = [1,3,2,2,1]

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

    outcome_a = -2
    # randomRed + randomBlue + randomWhite
    outcome_b = randomRed + randomBlue - randomWhite
    outcome_c = randomRed + randomBlue
    outcome_d = randomRed - randomWhite 

    print("----------------------------------------------------------------------------")
    print("     Dobbel Trobbel")
    print("----------------------------------------------------------------------------")
    print("position :    |  1  |  2  |  3  |  4  |  5  |  6  |  7  |  8  |  9  |  10  |")
    print("----------------------------------------------------------------------------")
    print("Scores Red:", red)
    print("Scores Blue:", blue)
    print("----------------------------------------------------------------------------")
    print(f"Scores White: |     |     |     |    |     |")
    print("----------------------------------------------------------------------------")
    print("")
    print("Rolling dice........")
    print("")
    print( " " + str(randomRed) + "     " + str(randomBlue) + "     " + str(randomWhite))
    print("")
    print("----------------------------------------------------------------------------")
    print("Calculated results")
    print(f"a: {-2} = {randomRed} + {randomBlue} + {randomWhite}")
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
        choice = input("Please choose which result to register (a, b, c, d)\n")
        if choice == "a":
            choice = outcome_a
        elif choice == "b":
            choice = outcome_b
        elif choice == "c": 
            choice = outcome_c
        elif choice == "d":
            choice = outcome_d
        if choice in color:
            print("Choose a different number")
        else:
            wrongChoice = False


    if color == red: 
        print(red) 
        position = int(input(f"This is the list of the red row, the positions you can choose are {listOfNums}\n "))
        red[position - 1] = choice
        lijst = red

    elif color == blue:
        print(blue)
        position = int(input(f"This is the list of the blue row, the positions you can choose are {listOfNums}\n"))
        blue[position - 1] = choice
        lijst = blue

    if choice == "c" or "d":
        white.append(randomWhite)
        print(white)

    if len(white) == 5 or len(red) == 10 and len(blue) == 10:
        lst(red)
        lst(blue)
        lst(white) 

        subtotal_1 = (-2*blue[0]) + (red[1]*blue[1]) + (red[2]*blue[2]) + (red[3]*blue[3])+ (red[4]*blue[4]) + (red[5]*blue[5]) + (red[6]*blue[6]) + (red[7]*blue[7])+ (red[8]*blue[8]) + (red[9]*-2)
    	
        subtotal_2 = emptyPos * (white[0] + white[1] + white[2] + white[3] + white[4]) 
        finalScore = subtotal_1 - subtotal_2
        print(f"Your final score: {finalScore}")

        repeat = False
        break


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
                listOfNums.append(index + 1)
                index += 1
            elif int(choice) > lijst[index]:
                index += 1
            elif int(choice) < lijst[index]:
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
                listOfNums.append(index + 1)
                index -= 1
            elif int(choice) > lijst[index]:
                index -= 1
            elif int(choice) < lijst[index]:
                index -= 1

        return listOfNums

    print(checker(lijst,choice,position - 1))