import random

# Some useful operators

# range()
# range() takes 3 parameters: start, stop and step
# start and stop is optional

myList = [1, 2, 3, 4, 5]
emptyList = []
for num in range(0, 12, 2) :
    emptyList.append(num)

print(emptyList)
# Note, range is not saving items to memory, it is just generating numebers

# enumerate
indexCount = 0
word = 'a,b,c,d,e'
for index, letter in enumerate(word) :
    print(index)
    print(letter)
    print('\n')

#  zip
myList1 = [1, 2, 3, 4, 5]
myList2 = ["a", "b", "c", "d", "e"]
blankDict = {}
for count, item in zip(myList1, myList2) :
    blankDict[count] = item

print(blankDict)

# in operator
# check if an object is in a list:
print(3 in myList1)
# Works for strings as well
print("apples" in "my granny loves oranges")
print("apples" in "but I love apples")
# you can also check keys dictionaries:
print(3 in blankDict)
# check items in dictionaries
print("d" in blankDict.values())

# min and max operators
minMaxList = []
def quickDice(rs, re) :
    randomInt = random.randint(rs, re)
    return randomInt

def minMaxDef(takesList) :
    i = 0
    while i <= 10 :
        minMaxList.append(quickDice(0, 100))
        i += 1

minMaxDef(minMaxList)
print(minMaxList)

print("Minumum number in minMaxList: ", min(minMaxList))
print("Maximum number in minMaxList: ", max(minMaxList))


# random
from random import shuffle
shuffleList = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
shuffle(shuffleList)
print(shuffleList)

# deck shuffler
deck = []
hand = []
grave = []
def deckShuffle(deckSize, deck) :
    i = 0
    while i <= deckSize :
        i += 1
        deck.append(i)
    shuffle(deck)
    print(deck)

deckShuffle(60, deck)

# Hand Draw
def drawHand(deckList, drawSize) :
    i = 0
    while i <= drawSize :
        if drawSize > 7 :
            print("You can only draw 7")
        drawnCard = deckList.pop(-1)
        hand.append(drawnCard)
        i += 1

def drawCard(deckToDraw) :
    drawnCard = deck.pop(-1)
    hand.append(drawnCard)

def discardCard(deckToDiscard) :
    discardedCard = hand.pop()
    grave.append(discardedCard)

def discardHand(handToDiscard) :
    i = 0
    handLen = len(hand)
    while i < handLen :
        currentlyDiscarding = handToDiscard.pop()
        grave.append(currentlyDiscarding)
        i += 1

drawHand(deck, 7)
print("Hand: ", hand)
print("Deck", deck)
drawCard(deck)
print("Current Hand: ", hand)
discardHand(hand)
print("Current Hand: ", hand)


# My deck generator can use some more work... but now is not the time

# input
# myInput = input("What is your name?")
# Just note, input always makes input into a string, so if you give it a number and want a number, just convert it to an int or float
# myNumInput = int(input("What is your favorite number?"))

# print(type(myNumInput))