import random 

negativeNumForRed = -2
negativeNumForBlue = -2
choiceCounterRed = 0
choiceCounterBlue = 0

firstNumRed = 2
lastNumRed = 10
firstNumBlue = 1
lastNumBlue = 9

listOfNums = "all positions except -2" 
redBlue = 0

redDice = ["1", "2", "3", "4", "5", "6"]
blueDice = ["1", "2", "3", "4", "5", "6"]
whiteDice = ["1", "1", "1", "2", "2", "3"]

choicePosition = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"]

red =  [negativeNumForRed, 0, 2, 4, 5, "", 7, 10, 11, ""] 
blue = [14, 12, 11, "", 6, 5, "", 3, -1, negativeNumForBlue]
white = [1,3,2,2,1]

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
    print(f"a: {outcome_a} = {randomRed} + {randomBlue} + {randomWhite}")
    print(f"b: {outcome_b} = {randomRed} + {randomBlue} - {randomWhite}")
    print(f"c: {outcome_c} = {randomRed} + {randomBlue}")
    print(f"d: {-2} = {randomRed} - {randomWhite}" )
    print("If chosen for c or d, the white value will be registered")
    
    if randomRed > randomBlue:
        print("You must register in the red scores")
    elif randomBlue > randomRed:
        print("You must register in the blue scores")
    else:
        print("You may register in the red or the blue scores")
        redBlue = input("Red or blue (r or b)")

    # wrongChoice = True
    # while wrongChoice:
    choice = input("Please choose which result to register (a, b, c, d)\n")
    if choice == "a":
        choice = outcome_a
    elif choice == "b":
        choice = outcome_b
    elif choice == "c": 
        choice = outcome_c
    elif choice == "d":
        choice = outcome_d
        # if choice == choice in red or choice == choice in blue or choice == -2:
        #     print("Choose a different number")
        # else:
        #     wrongChoice = False


    if randomRed > randomBlue or redBlue == "r": 
        print(red) 
        position = int(input(f"This is the list of the red row, the positions you can choose are {listOfNums}\n "))
        red[position - 1] = choice
        lijst = red

    elif randomBlue > randomRed or redBlue == "b":
        print(blue)
        position = int(input(f"This is the list of the blue row, the positions you can choose are {listOfNums}\n"))
        blue[position - 1] = choice
        lijst = blue

    if choice == "c" or "d":
        white.append(randomWhite)
        print(white)

    def lst(lijst):
        if len(white) == 5 or len(red) == 10 and len(blue) == 10:
            for i,x in enumerate (lijst):
                if x == "":
                    red[i] = 0


            subtotal_1 = (-2*blue[0]) + (red[1]*blue[1]) + (red[2]*blue[2]) + (red[3]*blue[3])
            + (red[4]*blue[4]) + (red[5]*blue[5]) + (red[6]*blue[6]) + (red[7]*blue[7])
            + (red[8]*blue[8]) + (red[9]*blue[9])
            repeat = False
            break
    lst(red)
    lst(blue)


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