# Often you want to inject a variable into a string for printing or output. This is known as string interpolation
my_name = "Carsten"
print("Hello, my name is", my_name)

# exploring two ways of doing this
# .format()
# f-strings (formatted string literals) which are basicially ${} in javascript or jsx (template literals)
# f-strings will probably be my choice

# First, .format
firstPart = "This is the first part of the string."
insertedPart = "This is the insterted part of the string."
formattedParts = firstPart + " {} ".format(insertedPart)
print("This is a hard-written string, {} ".format(insertedPart))

# you can combine many and index them in {2} braces.
randomPart1 = "Random Part 1"
randomPart2 = "Random Part 2"
randomPart3 = "Random Part 3"

combinedAllThree = "{1} {0} {2}".format(randomPart1, randomPart2, randomPart3)
print(combinedAllThree)

# Keywords can also be assigned
combinedWithKeys = "This is {b} and this {c} and then there is {a}".format(a=randomPart3, b=randomPart1, c=randomPart2)
print(combinedWithKeys)

# Float number formatting - it even has a ring to it
crazyFloatNum = 200/1992
# Float formatting gollows: "{value:width.precision f}"
# The "width" adds 1 white for every 9 it seems... to the output, so putting 9 there will include 1 space before the output
# The precision takes in how deep into the decimal you want to go
crazyFloatNumFormatted = "The result is{theNum:9.6f}".format(theNum = crazyFloatNum)
print(crazyFloatNumFormatted)

# Finally f-strings! I prefer this
totalGreeting = f"Hello, my name is {my_name}"
# This can word with multiple variables as well:
fStringRandomness = f"{totalGreeting}. This is {randomPart1} and this is {randomPart2} then there is {randomPart3}"
print(fStringRandomness)