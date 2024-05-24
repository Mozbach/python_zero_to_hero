#  List comprehensions are a unique way of quickly creating a list with Python
# If you find yourself using a for loop along with .append() to create, List Comprehensions are a good alternative

myString = "hello"
myList = [item for item in myString]
# for letter in myString :
#     myList.append(letter)
print(myList)
# This basically reads "for element in element, itterable"
numList = [num for num in range(1,10)]
print(numList)

celcius = [0, 1, 10, 15, 20, 25, 30, 32]
# to do comutions on the numbers, do so in the first element
farenheit = [((9/5) * temp + 32) for temp in celcius]
print(farenheit)

# list of celcius given
def listOfCelciusToFarenheit(celcList) :
    return [((9/5) * temp + 32) for temp in celcList]
print("Next Week's Temps: ", listOfCelciusToFarenheit([2, 10, 15, 18, 22, 32]))

# Single celcius given
def celciusToFarenheit(celc) :
    return ((9/5) * celc + 32)
print("Single celcius to farenheit:", celciusToFarenheit(23))

# use if statements in list comrehension
ifStateMyList = [x for x in "this string takes time" if x == "t" or x == "s" ]
print(ifStateMyList)


# I just realised, using the or operator in Python, we don't need to write the whole statement again. You just need to write the comparison again... in Javascript, the above would have been something like: if x == "t" || if x == "s", Python does not require the second "if"

def evensOnly(listOfNums) :
    return [num for num in listOfNums if num % 2 == 0]
print(evensOnly([1,10,2,60,34,32,33,15,7]))

# if else in list comprehension
# Above all else, readability and reproduceability should be the most important thing, not slick one-liners, but here it is...
results = [num if num%2 == 0 else 'ODD' for num in range(1, 21)]
print(results)

stringResults = [x if x == "a" or x == "e" or x == "i" or x == "o" or x == "u" else "consonant" for x in "thisstringoverhere"]
print(stringResults)

# Nested loops in list comprehension
# loop method:
newList = []
for x in [2, 3, 5, 8] :
    for y in [2, 4, 6, 8] :
        newList.append(x * y)
print("New List: ", newList)
# comprehension method
newList2 = [x * y for x in [2, 4, 6, 8] for y in [2, 4, 6, 8]]
print("New List2: ", newList2)
