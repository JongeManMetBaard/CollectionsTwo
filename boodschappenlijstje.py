def generateGroceryList():
    groceryList = {}
    while True:
        groceryItems = input("Which product do you want to add to the shopping list?")
        if groceryItems == "stop":
            break
        elif groceryItems in groceryList:
            groceryList[groceryItems] += 1
        else:
            groceryList[groceryItems] = 1
    return groceryList

print(generateGroceryList())