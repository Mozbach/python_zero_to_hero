hw = "Hello World"

# Get First Char: 
print(hw[0])

# Get second "r" in "world"
print(hw[8])

# get "l" in "world" -> I'm gonna use negative indexing, instead of 9
print(hw[-2])


# Slicing - Grabbing subsection of a string that starts at index 3, then goes all the way to the end:
abc = "abcdefghijkl"
print(abc[7:-1])
# Writing a def to do it
def returnSubstringToEnd(theString, fromHere) :
    return theString[fromHere:-1]

print(returnSubstringToEnd(abc, 4))

# One can also omit the first value in the slicing to start from the beginning of the string, and the same for the end of the string, just leave the second one blank

print("From the Start: ", abc[:-1])
print("To the End: ", abc[:]) # I mean... this is redundant since one can just go print(abc) -> but still

# The stop indexing is up to but not including.... so, abc([:3]), won't return abcd, it will return abc
print("Up to but not including position 6: ", abc[:6])

# Return only "def"
print(abc[3:6])

# Return only "bc"
print(abc[1:3])

# Step Size
# Print the entire string, but make the step size 3, returning only every 3rd letter
print(abc[::3])

# Reverse a string using step size
print(abc[::-1])


# Just on a side note - reverse a string with a for loop instead
def revStringFunction(theString) :
    revString = ""
    for c in reversed(theString) :
        revString += c
    return revString

print(revStringFunction(abc))


