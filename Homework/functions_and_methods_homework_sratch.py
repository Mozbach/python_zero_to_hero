import math
# Write a functon that computes the volume of a sphere given its radius
# Volume = 4/3 (4 over 3) * pi * r***
def myVol(rad) :
    return ((4/3) * math.pi) * math.pow(rad, 3)
print("Volume of Circle: ", myVol(2))

# Their Solution
def vol(rad) :
    return (4/3) * (3.14) * (rad ** 3)
# I like this more, because it does not need to import math. But I don't think this is as accurate as mine. Since my output slightly differs - I just think this is based on the limited length of the 3.14 pi decimal.

# Write a function that checks wheter a number is in a given range, inclusive of high and low
# In other words: (5, 2, 7) -> check whether the 5 (given number) is between and including 2 - 7
def myRan_check_boolean(num, low, high) :
    return num in range(low, high + 1)
print("Ran Check Boolean: ", myRan_check_boolean(4, 2, 7))
print("Ran Check Boolean: ", myRan_check_boolean(9, 8, 17))
print("Ran Check Boolean: ", myRan_check_boolean(91, 8, 17))

def myRan_check2(num, low, high) :
    if num in range(low, high + 1) :
        print(f"{num} is in range from {low} to and including {high}")
        return True
    else :
        print(f"{num} is not in range from {low} to {high}")

# Their Solution
def ran_check(num, low, high) :
    if num in range(low, high + 1) :
        print("{} is in the range between {} and {}".format(num, low, high))
    else :
        print("The number is outside the range.")

print(ran_check(4, 2, 7))
print(ran_check(9, 8, 17))
# Their solution is basically the same as mine - over all success!

# Write a python function that accepts a string and calculates the number of upper case letters and lower case letters.
def myUp_low(s) :
    lowerLetters = 0
    upperLetters = 0
    for i in s :
        if i.islower() :
            lowerLetters += 1
        if i.isupper() :
            upperLetters += 1
    return f"Total lower: {lowerLetters}. Total upper: {upperLetters}"
print(myUp_low("Hello Mr. Rogers, how are you this fine Tuesday?"))

# Their Solution
def up_low(s) :
    d = {"upper": 0, "lower": 0} # Creates dictionary
    for c in s : # Loops the dictionary
        if c.isupper() :
            d["upper"] += 1
        elif c.islower() :
            d["lower"] += 1
        else :
            pass
    print("Original String: ", s)
    print("No. of Upper Case Characters: ", d["upper"])
    print("No. of Lower Case Characters: ", d["lower"])

up_low("Hello Mr. Rogers, how are you this fine Tuesday?")
# I like their solution because it feels a bit less hacky than mine and more... I duno... Professional?
# I want to get into looping dictionaries for small tasks like this... I am still using one less line of code. though... Not even counting the lines they spent on output - BUT... I still think theirs is a bit cooler

# Write a Python function that takes a list and returns a new list with unique elements of the first list.
# Check back on sets... I believe
def myUnique_list(lst) :
    set_list = set(lst)
    return list(set_list)
print(myUnique_list([1,1,1,1,2,2,3,3,3,3,4,5]))

def unique_list(lst) :
    # Also possible to use list(set())
    x = []
    for a in lst :
        if a not in x :
            x.append(a)
    return x
# Ok, well here I beat their asses
# Their solution is still cool, though. Because it actively checks if the number was seen or not, and theon only appends if it is a new number not already in the list

# Write a Python function to multiply all the numbers in a list
def myMultiply(numbers) :
    current_value = 1
    for i in numbers :
        current_value *= i
    return current_value
print("Multiply a List: " , myMultiply([2,2,3,-4]))

def multiply(numbers) :
    total = 1
    for x in numbers :
        print(x)
        total *= x
    return total
print("Course Multiply a List: ", multiply([2, 2, 3, -4]))
# The example list of [1, 2, 3, -4] gives the same result. But if I change the 1 to 2, their list gives -48 and mine gives -72... Vastly different. So  I am assuming mine is incorrect. So, initially I did this: 
# current_value *= numbers[i]... Thisi s incorrect since i is alreads that specific number. It doesn't just show the location of the iterator. It is the value of what is in the location of the iteration

# Write a python function that checks wheter a word or phrase is palindrome or not.
def myPalindrome(s) :
    initial_s = s.replace(" ", "")
    the_string = list(initial_s)
    the_string = the_string[::-1]
    return "".join(the_string) == initial_s
print("Palindrome: " , myPalindrome('nursesrun'))

# Ok, here they beat my ass solid 
def palindrome(s) :
    s = s.replace(" ", "")
    return s == s[::-1]
# I like this solution - simple and to the point. Also makes plenty sense. Mine is a tad long winded

# HARD? - Who's hard -_-
# Write a Python function to check whether a string is pangram or not. Assume the string passed in does not have any punctuation.
# Pangrams are words or sentences containing every letter of the alphabet at least once.
# IE: The quick brown fox jumps over the lazy dog
# - Lowercase everything
# Set up lowerAlphabet = string.ascii_lowercase
# Use replace() to get rid of spaces - maybe string lower() to it as well - just to be sure.
# Create a SET (because it can't have duplicates)
# Loop over the parameter... check this cheat

def myIspangram(theString) :
    cleanString = theString.lower().replace(" ", "")
    theList = list(cleanString)
    theSet = set(theList)
    return len(theSet) == 26
print("Is Pangram: ", myIspangram("The quick brown fox jumps over the lazy do"))

# Lol, ok no... Ended up cheating my way to victory here - Sorry, I'm DEAD tired.
# cleanString var takes theString argument, sets it lowercase, then replaces all the spaces with blanks.
# Then, I make a list out of the string by using list... This tuns every character to be part of a list
# then I take theList and turn it into a set - removing all the duplicate characters
# Then I just check if the length of the set == 26. True will return if it is, else False will return.
# SO Sure this isn't the answer they wanted, but let me tell you - this is the answer they are getting.

# And here is what they  actually wanted and did:
import string
def ispangram(str2, alphabet=string.ascii_lowercase) :
    # Create a set of the alphabet
    alphaset = set(alphabet)

    # Remove spaces from str1
    str1 = str1.replace("", " ")

    # Lowercase all strings in the passed in string
    # Recall we assume no punctuation
    str1 = str1.lower()

    # Grab all unique letters in the string as a set
    str1 = set(str1)

    # Now check that the alphabet is same as the string
    return str1 == alphaset

# I would say the only reason their solution might be better is because they are actually comparing the two strings with each other. In my case, I just create a unique list out of the passed in value and then check if it is == 26... But I mean, this sucks because if tomorrow they were to introduce new characters to the alphabet, or I am dealing with a different alphabet other than the one we all fought and died for, then my solution kind of falls flat.
# Fuck yes! I NAILED this one! 