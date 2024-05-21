# While loop sintax:
    # while some_bool_condition :
    # do_something
    # usually_increment_something_related_to_bool_condition

x = 0
while x < 5 :
    print(f"current value of x: {x}")
    x += 1
else : 
    print(f"x, {x}, is not less than 5")


# Three keywords:
# break: Breaks out of the current closest enclosing loop
breakX = "BreakThispoint"
emptyString = ""
for letter in breakX :
    if(letter == "p") :
        break
    emptyString += letter
print(emptyString)

# continue: Goes to the top of the closest enclosing loop
continueX = "Shani"
continueList = []
for letter in continueX :
    if(letter == "a") :
        continue
    continueList.append(letter)
print(continueList)


# pass: Does nothing at all
passX = [1, 2, 3]
for item in passX :
    # pass can be used as a placeholder, because for loops can't be  empty
    pass

# easy