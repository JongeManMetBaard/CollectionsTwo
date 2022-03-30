import random 

negativeNumForRed = -2
negativeNumForBlue = -2

choiceCounterRed = 0
choiceCounterBlue = 0

firstNumRed = 2
lastNumRed = 10

firstNumBlue = 1
lastNumBlue = 9


redBlue = 0

repeat = True

# def checker(lijst, choice, position):

#     if lijst == red:
#         if lijst[position] == "":
#             index = position 
#             if index == 9:
#                 return True
#             while index < len(lijst - 1):
#                 index += 1
#                 if lijst[index] != "":
#                     if lijst[index] > choice:
#                         return True
#     else:
#         if lijst[position] == "":
#             index = position 
#             while index < len(lijst - 1):
#                 index -= 1
#                 if lijst[index] != "":
#                     if lijst[index] > choice:
#                         return True


redDice = ["1", "2", "3", "4", "5", "6"]
blueDice = ["1", "2", "3", "4", "5", "6"]
whiteDice = ["1", "1", "1", "2", "2", "3"]

choicePosition = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"]

red =  [negativeNumForRed, "", "", 4, 5, "", "", 9, 10, ""] 
blue = ["", 8, "", 6, "", 4, 3, 0, "", negativeNumForBlue]
white = []


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
    print(red)
    print(blue)
    print("----------------------------------------------------------------------------")
    print("Scores White: |   {b[0]}  |     |     |     |     |")
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

    if randomRed > randomBlue or redBlue == "r": 
        print(red)
        position = int(input(f"This is the list of the red row, choose a position from {firstNumRed} upto {lastNumRed}\n"))
        red[position - 1] = choice
        lijst = red

    elif randomBlue > randomRed or redBlue == "b":
        print(blue)
        position = int(input(f"This is the list of the blue row, choose a position from {firstNumBlue} upto {lastNumBlue}\n"))
        blue[position - 1] = choice
        lijst = blue

    if choice == "c" or "d":
        white.append(randomWhite)
        print(white)

    # if len(white) == 5 or len(red) == 10 and len(blue) == 10:
    #     repeat = False

    def checker(lijst,choice,pos):

        if lijst[0] != -2:
            lijst.reverse()
            pos = len(lijst) - 1 - pos   


        listOfNums = []
        index = pos
        index -= 1

        leftValid = True
        while leftValid:
            if index == -1:
                leftValid = False
            elif lijst[index] == "":
                listOfNums.append(index + 1)
                index -= 1
            elif lijst[index] != "":
                if lijst[index] < int(choice): 
                    index -= 1

        index = 0
        rightValid = True
        if pos != 9:
            index = pos

        while rightValid:
            if pos == 9:
                rightValid == False 
                break
            if index == 10:
                rightValid = False
            elif lijst[index] == "":
                listOfNums.append(index)
                index += 1
            elif lijst[index] != "":
                if lijst[index] == int(choice):
                    index += 1
                elif lijst[index] > int(choice): 
                    index += 1
        if lijst == blue:
            lijst.reverse()
            for x in range(len(listOfNums)):
                listOfNums[x] = len(lijst) - 1 - listOfNums[x]
        return listOfNums
        
        

    print(checker(lijst,choice,position - 1))

























    # def checker(lijst,choice):
    #     listOfNums = []
    #     index = 0
    #     step = 1
        
    #     leftValid = True
    #     while leftValid:
    #         for x in lijst:
    #             if index > 9:
    #                 leftValid = False
    #                 break
    #             if lijst[index] != "":
    #                 index += 1
    #             else:
    #                 if lijst[index] == "":
    #                     index += 1
    #                 if lijst[index - step] != "" or lijst[index - step] == "":
    #                     index = 1
    #                     if lijst[index - step] < int(choice):
    #                         step += 1
    #                         listOfNums.append(index) 
    #                         leftValid = False
    #                         if lijst[index] == "":
    #                             step += 1
                    
            
    #     rightValid = True
    #     step = 1
    #     index = 0
    #     while rightValid:
    #         for x in lijst:
    #             if lijst[index] != "":
    #                 index += 1

    #             else:
    #                 if lijst[index] == "":
    #                     index += 1 
    #                 if lijst[index] != "":
    #                     if int(choice) > lijst[index]:
    #                         step += 1
    #                         listOfNums.append(index)
    #                         rightValid = False
    #                 if index == 9:
    #                     rightValid = False
    #                     break 
    #     return listOfNums
    # print(checker(lijst,choice))                                           
                    


    # def checkingPosition(red,blue):
    #     repeat = True
    #     while repeat:
    #         repeat = False
    #         if red[position] == "" or blue[position] == "":
    #             print("Choose a different position")
    #             repeat = True

    # checkingPosition(red,blue)