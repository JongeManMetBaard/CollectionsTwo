import random

kaartendeck = [] 
randomSevenCardsCounter = 1

for x in range(2):
    kaartendeck.append('joker')
def kaarten(Kaart, kaartVar):
    for x in range(2,11):
        kaartVar = f'{Kaart} {x}'
        kaartendeck.append(kaartVar)
    def persoon(Persoon):
        PersoonVar = Kaart + Persoon
        kaartendeck.append(PersoonVar)
    persoon(' boer')
    persoon(' vrouw')
    persoon(' koning')
    persoon(' aas')

kaarten('klaveren', 'klaverenNum')
kaarten('harten', 'hartenNum')
kaarten('schoppen', 'schoppenNum')
kaarten('ruiten', 'ruitenNum')

random.shuffle(kaartendeck)
for pop in range(7):
    pickedCard = kaartendeck.pop()
    randomSevenCards = f"kaart: {randomSevenCardsCounter}"
    randomSevenCardsCounter += 1
    print(randomSevenCards, pickedCard)
print("")

print(f'deck (47 kaarten): {kaartendeck}')