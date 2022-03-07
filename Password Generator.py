import random

randomNumCapital = random.randint(2,6)
randomNums = random.randint(4,7)
amountOfCharacters = 24

capitalLetters = ["Q", "W", "E", "R", "T", "Y", "U", "I", "O", "P", "A", "S", "D", "F", "G", "H", "J", "K", "L", "Z", "X", "C", "V", "B", "N", "M"]
letters = ["q", "w", "e", "r", "t", "y", "u", "i", "o", "p", "a", "s", "d", "f", "g", "h", "j", "k", "l", "z", "x", "c", "v", "b", "n", "m"]
specialCharacters = ["@", "#", "$", "%", "&", "_", "?"]
nums = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']



password_lst = []  
for c in range(randomNumCapital):
    pickedCapital = random.choice(capitalLetters) 
    password_lst.append(pickedCapital)
c += 1
amountOfCharacters -= c


 
for n in range(randomNums):
    pickedNums = random.choice(nums)
    password_lst.append(pickedNums)
n += 1
amountOfCharacters -= n


for s in range(3):
    symbol = []
    pickedSpecial = random.choice(specialCharacters)
    password_lst.append(pickedSpecial)
    symbol.append(pickedSpecial)
s += 1
amountOfCharacters -= s

random.shuffle(password_lst)

lowerLetters = []
for l in range(amountOfCharacters):
    pickedLower = random.choice(letters)
    lowerLetters.append(pickedLower)
password = lowerLetters[:3] + password_lst + lowerLetters[3:]

print(password)