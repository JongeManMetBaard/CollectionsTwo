import random 

negativeNumForRed = -2
negativeNumForBlue = -2

choiceCounterRed = 0
choiceCounterBlue = 0

redDice = ["1", "2", "3", "4", "5", "6"]
blueDice = ["1", "2", "3", "4", "5", "6"]
whiteDice = ["1", "1", "1", "2", "2", "3"]

choicePosition = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"]

red =  [{negativeNumForRed}, "", "", "", "", "", "", "", "", ""] 
blue = ["", "", "", "", "", "", "", "", "", {negativeNumForBlue}]

for x in range(4):

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
    print(red)
    print(blue)
    print("----------------------------------------------------------------------------")
    print("Scores White: |     |     |     |     |     |")
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
    
    if randomRed > randomBlue:
        print("You must register in the red scores")
    elif randomBlue > randomRed:
        print("You must register in the blue scores")
    else:
        print("You may register in the red or the blue scores")
        redBlue = input("Red or blue (r or b)")

    choice = input("Please choose which result to register (a, b, c, d)\n")
    if choice == "a":
        choice = outcome_a
    elif choice == "b":
        choice = outcome_b
    elif choice == "c": 
        choice = outcome_c
    elif choice == "d":
        choice = outcome_d

    if randomRed > randomBlue:
        
        print(red)        
        position = int(input("This is the list of the red row, choose a position fr\n"))
        red[position] = choice
        if choice < choiceCounterRed:
            print("error")
    elif randomBlue > randomRed:
        print(blue)
        position = int(input("This is the list of the blue row, choose a position\n"))
        blue[position] = choice
        if choice < choiceCounterBlue:
            print("error")
    elif randomRed == randomBlue:
        if redBlue == "r":
            print(red)
            position = int(input("This is the list of the red row, choose a position\n"))
            red[position] = choice
        elif redBlue == "b":
            print(blue)
            position = int(input("This is the list of the blue row, choose a position\n"))
            blue[position] = randomBlue
    choiceCounterRed = choice
    choiceCounterBlue = choice


    # def checkingPosition(red,blue):
    #     repeat = True
    #     while repeat:
    #         repeat = False
    #         if red[position] == "" or blue[position] == "":
    #             print("Choose a different position")
    #             repeat = True

    # checkingPosition(red,blue)