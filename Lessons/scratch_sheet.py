# Dictionaries from w3Schools!
# Dictionaries are basically structured like object in js
thisDict = {
    "entry1" : "Info from entry 1",
    "entry2" : 99,
    "entry3" : [1, 2, "string", "and the thing", 55.4 ],
    "entry4" : {
        "entry4.1" : "Info from entry 4.1",
        "entry4.2" : 33,
        "entry4.3" : [1, 2, "string", "and the thing", 88.7]
    }
}

# Dictionaries are used to store data in key-value pairs, key and value are seperated by a colon:
# Dictionaries can hold any type of data type... even dictionaries, I'm sure
# Access items in a dictionary using square brackets containing the name of the entry
print(thisDict["entry3"][2] + " " + thisDict["entry3"][3])
print(thisDict["entry4"]["entry4.3"][2] + " " + thisDict["entry4"]["entry4.3"][3])

# In python 3.7, dictionaries are ordered, anything before that, dictionaries were unordered
# When we say ordered, we mean that the items have a defined order, and that order will not change. Order is defined upon creation of the dictionary
# Unordered means that the items do not have a defined order, you cannot refer to an item by using an index

# Dictionaries are mutable
thisDict["entry4"]["entry4.3"][2] = "KING"
print(thisDict["entry4"]["entry4.3"][2] + " " + thisDict["entry4"]["entry4.3"][3])


# TUPPLES! from W3Schools
# Tuples are used to store multiple items in a single variable - interesting
# Tuples is one of 4 built-in data types in Python used to store collections of data, the otehr 3 are List, Set and Dictionary
# A tuple is a collection which is ordered and unchangeable (immutable)
# Tupples are written with round brackets
my_tupple = ("apple", "banana", "cherry", "berry", "guava")
print(my_tupple[3])

# tuples are ordered, immutable and allow duplicate values
#  Tuple items are indexed - similar to lists

# Check length of a tuple
print(len(my_tupple))

# Create a tuple with one item by adding a comma after the item, otherwise Python won't recognize it as a tuple
single_item_tuple = ("peas",)
print(single_item_tuple[0])

# Tuples can have any data type and can also contain different data types
different_type_tuple = (
    "string",
    True,
    [0, 2, 4, 5],
    {
        "tupDictItem1": 1,
        "tupDictItem2": [2],
        "tupDictItem3": "three"
    }
)

# The tuple constructor:::
declaredTuple = tuple((1, 2, "berry", "peas", [1, 2, 3]))
print(declaredTuple)

# Access tuples the same as you would a list
print(different_type_tuple[3]["tupDictItem2"][0])

# Negative indexing is also valid
print(different_type_tuple[-2][3])

# You can specify the range of idexes by specifying where to start and wehre to end the range
# When specifying a range, the return value will be an ew tuple with the specified items
fruitTuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
smallFruitTuple = fruitTuple[2:6]
print(smallFruitTuple)

# indexing rules are similar to slicing rules


# check if an item exists within a tuple
def checkTuple(tupleName, itemName) :
    if itemName in tupleName :
        return f"Yes, {itemName} is in this tuple"
    else :
        return f"No, {itemName} is not in this tuple"
    
print(checkTuple(fruitTuple, "watermelon"))

# Update Tuples

# Tuples are immutable, so they can't be changed, but there are some workarounds
# You can change a tuple into a list, change the list, then change it back into a tuple
initialTuple = ("a", "b", "c")
listedTuple = list(initialTuple)
listedTuple.append("e")
print(listedTuple)
initialTuple = tuple(listedTuple)
print(initialTuple)

listedTuple[2] = "CHANGED"
initialTuple = tuple(listedTuple)
print(initialTuple)

# Add a tuple to a tuple
thirdTuple = ("h", "i", "j")
thirdTuple += initialTuple
print(thirdTuple)

# Tuple Items can't be removed, but the list trick with a pop(2), can work
listedTuple.pop(2)
initialTuple = tuple(listedTuple)
print(initialTuple)

# Delete a tuple completely
del thirdTuple
# print(thirdTuple) # 'thirdTuple' is not defined error

# Unpack Tuples
# When we create a tuple, we normally assign values to it, this is called "packing" a tuple
# We can also extract the values vack into variables, this is called "unpacking"
packedTuple = ("avos", "bananas", "lemons", "trees", "witches", "squeez", "weez", "breez")
# (soft, mush, sour, stern) = packedTuple
# print(soft, mush, sour, stern)

# If the number of variables is less than the number of values, you can add an asterisk * to the variable name and the values will be assigned to the variable as a list
# So a list containing everything from THAT point to the end of the tuple will be created
(bigPip, seed, *lemonTree) = packedTuple
print(lemonTree)

# If the asterisk is added to another variable name than the last, Python will assign values to the variable until the number of values left matches the number of variables left - what??? -> To me it looks like it just takes the last one and makes it "notFruit", things before that will fall in the "smallLeaves" list
(greenLeaves, bigLeaves, *smallLeaves, notFruit) = packedTuple
print(smallLeaves)
# Yea, still does not really make sense.... But ok.

# Looping tuples using a for loop
for item in packedTuple :
    print("Current Item: " + item)

# Loop throug the index numbers
# Use range() and len() functions to create a suitable iterable
for item in range(len(packedTuple)) :
    print("The Current Item: " + packedTuple[item])

# Using a While Loop
# Use the len function to determine the length of the tuple, then start at 0 and loop your way through the tuple times by referring to their indexes.
i = 0
while i < len(packedTuple) :
    print(f"Number {i} From While: {packedTuple[i]}")
    i = i + 1

# Join Tuples
# To join 2 tuples, you can use the + operator.
tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)
tuple3 = tuple1 + tuple2
print(tuple3)

# Multiply Tuples
# If you want to multiple the content of a tuple a given number of times, use the * operator:
multiTuple = ("shani", "lenè", "daniella")
multipliedTuple = multiTuple * 4
print(multipliedTuple)

# Tuple methods
# count(): returns the number of times a specific value occurs in a tuple
print(multipliedTuple.count("shani"))
# and index()
# Searchjes the tuple for a specified value and returns the position of where it was found
print(packedTuple.index("bananas"))



# SETS
# Sets are used to store multiple items in a single variabe
# Set is one of 4 built-in data types in python used to stroe collections of data, the other 3 are: List, Tuple and Dictionary
# A Set is a collection which is unordered, immutable and unindexed
# Note that set items are immutable, but you can still add or remove new items
# sets are written with curly brackets
thisset = {"setItem1", "setItem2", "setItem3","setItem4", "setItem5", "setItem6"}
print(thisset)

# Set items are unordered and immutable, they will not allow duplicate values

# unordered means that the items in a set do not have a defined order, so you probably can't index them like a list: thisset[2]

# In sets, "True" and 1 are treated as duplicates, to sets they mean the same thing... same with "False" and 0? -> Yes.
for i in thisset :
    print("current item in thisset: " + i)
# This comes back completely random, not the "unorderedness of it"

if "setItem7" in thisset :
    print("yes, setItem7 is in thisset")
else :
    print("nope, it aint there")

# check if an item is NOT in a set
if "banana" not in thisset : 
    print("no bananas found")
else : 
    print("banana at the red door")

# Add set items
# To add one item to a set, use the add() method
thisset.add("setItem7")
print(thisset)

# You can add a set to another set using the update method
thisset2 = {"setItem8", "setItem9", "setItem10"}
thisset.update(thisset2)
print(thisset)

# Add any iterable
# The object in the update() method does not have to bae a set, it can be any iterable object like tuples, lists, dictionaries - etc
listForSet = [1, 2, 3, 4]
thisset.update(listForSet)
print(thisset)

dictForSet = {
    "name" : "carsten",
    "surname" : "niemand",
    "age" : 35
}

thisset.update(dictForSet)
print(thisset)

# remove set items
# remove items in a set using the remove() or the discard() method
thisset.remove("name")
print(thisset)
# If the item does not exist, remove() will throw an error

# remove "setItem10" by using the discard method
thisset.discard("setItem10")
print(thisset)
# If the item does not exist, discard WILL NOT raise an error
# pop() will remove the last item in the set, but since sets are unordered, you won't know what is getting popped

poppedSetItem = thisset.pop()
print(poppedSetItem)

# Use the clear() method to empty a set
# thisset.clear()
print(thisset)

# Then, to delete a set completely, use the del() method
# del thisset


# Loop sets 
for anItem in thisset :
    print(f"This is the current item in thisset: {anItem}")

# Join Multiple sets
set1 = {1, 2, 3}
set2 = {4, 5, 6}
set3 = {7, 8, 9}
set4 = {10, 11, 12}
joinedSet = set1.union(set2, set3, set4)
print(joinedSet)

# one can also use the | operator to join sets
joinedSet2 = set4 | set3 | set2 | set1
print(joinedSet2)

# Join a set and a tuple
x = {"a", "b", "c"}
y = (1, 2, 3)
z = x.union(y)
print(z)

# The update method inserts all items from one set into another
# The update method changes the original set, and does not return the new set
x.update(set4)
print(x)

# Intersection
# the intersection() method will return a new set, that only contains the items that are present in both sets
set5 = {13, 14, 15, 16, 17}
set6 = {11, 12, 13, 14, 14}
set7 = set5.intersection(set6)
print(set7)

# you can use the & operator instead of the intersection() method to get the same result
set8 = set5 & set6
print(set8)

# True and 1 are considered one and the same, similar to 0 and False

# the difference() method will return all the items in the first set that are not present in the second set
set9 = set6.difference(set5)
print(set9)

# you can use the - operator instead of the difference() method to get the same result
set10 = set9 - set8
print(set10)

# The difference_update() method will also keep the items from the first set that are not in the other set, but will change the original set instead of returning a new set

set5.difference_update(set7)
print(f"set5: {set5}")

# FILE HANDLING
# The key function for worling with files in Python is the open() function
# The open() function takes two parameters, filename and ModuleNotFoundError
# There are 4 different methods (modes) for opening a file:
# - r: Default value. Opens a file for reading, error id the file does not exist
# - a: Append. Opens a file for appending, creates the file it does not exist
# - w: Write. Opens a file for writing, creates the file if it does not exist
# - x: Creates the specified file, returns an error if the file exists

# In addition, you can specify if the file should be handled as binary or text mode
# - t: Text. The default value. Text Mode
# - b: Binary. Binary mode (e.g. images)

# Syntax
# To open a file for reading it is enough to specify the name of the file
# f = open("myfile.txt")
# The code above is the same as 
# f = open("demofile.txt", 'rt')

# Open a file on the server
f = open("C:\\Users\\crstn\\OneDrive\\Desktop\\Myprojects\\ZeroToHeroPython\\Lessons\\holdsTextFiles\\myfile.txt", "r")
read_f = f.read()
print(print(f"read_f: {read_f}"))
f.seek(0)

o = open("C:\\Users\\crstn\\OneDrive\\Desktop\\Myprojects\\ZeroToHeroPython\\Lessons\\holdsTextFiles\\textFile.txt")
read_o = o.read(6)
print(f"read_o: {read_o}")

# Reads only part of the file:
# By default, the read() method returns the whole text, but you can also specify how many characters you want to return
# Return the first 5 characters in the text file
print(o.read(5)) # not getting anything to actually return... it returns a blank line

# you can return one line by using readline()
print("below is readline: ")
print(f.readline())
f.readlines()
f.seek(0)

st = "Print only the words that start with s in this sentence"
splitList = st.split()
for x in splitList :
    if x[0] == "s" and len(x) > 1 :
        print(x)

# use range to print even nums from 0-10
for x in range(0, 10) :
    if x %2 == 0 :
        print(x)

myFiftyList = [x for x in range(0, 51) if x % 3 == 0]
print("myFiftyList", myFiftyList)

# Write a function that returns the lesser of 2 given numbers if BOTH numbers are even, but returns the greater one if both numbers are odd

def lesser_of_two_evens(a, b) :
    if a % 2 == 0 and b % 2 == 0 :
        if a < b :
            return a
        else :
            return b
    elif a %2 != 0 and b % 2 != 0:
        if a > b :
            return a
        else :
            return b
    else :
        pass

print(lesser_of_two_evens(117, 127))


# Write a function that takes a two-word string and returns True if both words begin with the same letter.
def animal_crackers(text) :
    textList = text.split()
    if(textList[0][0] == textList[1][0]) :
        return True
    else : pass
    return False
print("Animal Crackers: ", animal_crackers("Animal Cranus"))


# Makes Twenty: Given two integers, return true if the sum f the integers is 20 or if one of the integers is 20. If not, return false
def makes_twenty(n1, n2) :
    if n1 + n2 == 20 or n1 == 20 or n2 == 20 :
        return True
    else :
        pass
    return False
print("Makes Twenty: ", makes_twenty(20, 11))

# Level 1 : Problems:
# OLD MACDONALD: Write a function that capilaizes the firs and fourth letter of a name
# old_macdonald('macdonald') --> MacDonald
# Note: macdonald.capitalize() returns Macdonald
def old_macdonald(name) :
    name.capitalize()
    capList = list(name)
    capList[3] = capList[3].upper()
    return "".join(capList)

print("Old Macdonald: ",old_macdonald("carsten"))

# Master Yoda Give an sentence, return a sentence with the words reversed
# def master_yoda(text) :
#     textSplit = text.split()
#     currentWord = ""
#     newList = []
#     for x in range(len(textSplit)) :
#         currentWord = textSplit.pop()
#         newList.append(currentWord)
    
#     return " ".join(newList)
# print("Master Yoda: ", master_yoda("My name is Master Yoda"))

# This below soltion is a bit better, I rate - not so long winded
def master_yoda(text) :
    textSplit = text.split()
    textSplit.reverse()
    return " ".join(textSplit)

print("Master Yoda: ", master_yoda("My name is Master Yoda"))

# Given an integer n, return true if n is within 10 of either 100 or 200
#  I looked at the answer - my moron brain just could not
def almost_there(n) :
    return((abs(100 - n) <= 10) or (abs(200 - n) <= 10))
# Why do they insist on using abs, though - why does it matter? - Just in case a negative number is assigned? Still stupid because why will the given negative number be considered in range of 100 or 200, since it most definitely is no... Seems like google's search results where they would take your search request, mess with it behind the scenes to basically be like "I think what you meant to search was this...."
print(almost_there(198))
# FAILED the above!

# Level 2, Problems:
# Find 33:
# Given a list of ints, return True if the array contains a 3 next to a 3 somewhere
# first idea: if [i] == 3 and [i + 1] == 3 (this won't directly work... but something like this)
# def find33(givenList) :
#     i = 0
#     while i < len(givenList) :
#         if givenList[i] == 3 :
#             prevNum = i - 1
#             nextNum = i + 1
#             if givenList[prevNum] == 3 or givenList[nextNum] == 3 :
#                 return True
#         else :
#             pass
#         i += 1
#         return "No 3's next to a 3"
    
# print("Find33: " , find33([1, 2, 3, 3, 4, 5, 6]))
# Bitching out on this one - here is the answer
def has_33(nums) :
    for i in range(0, len(nums)-1) :
        # I prefer this version, the "real" solution is too unreadable
        if nums[i] == 3 and nums[i+1] == 3 : # This is essentially what I tried... just a dumber version of this - I didn't know one can do math within square brackets... This isn't working..though
            return True
        
        # This is the version I don't really like - but I will try and break it down for myself.
        # if nums[i:i+2] == [3,3] : return True
        # Again, math within the square brackets. Come now Carsten, don't be so hard on yourself
        
    return False
has_33_list = [1,2,3,3,4,5,10,3,5,2,3,3,12]
print("Has 33!" , has_33(has_33_list))
# Totally cheated on this one... my brain is just not nailing the logic.



# Paper doll... I already see no way out.
# Given a string, return a string where for every character in the original, there are three characters.: "Apples" = "AAApppllleeesss"
def paper_doll(text) :
    result = ''
    for x in text :
        result += x * 3
    return result # And I know you can multiply chars, it is just like my mind does not WANT to come up with solutions anymore

# Blackjack - Im looking forward to this one
# Given three integers between 1 and 11 >
# if their sum is less than or equal to 21, return their sum.
# If their sum exceeds 21 and there is an eleven, reduce the total sum by 10.  
# Finally, if the sum, even after adjustment, exceesds 21, return 'BUST'

def blackjack(a,b,c):    
    if sum((a, b, c)) <= 21 :
        return sum((a, b, c))
    elif sum((a, b, c)) > 21 and 11 in (a, b, c) :
        return sum((a, b, c)) - 10
    elif sum((a, b, c)) > 21 and 11 not in (a, b, c) :
        return "BUST!"
    else :
        pass
print(blackjack(2, 11, 5))

# Ok, my blackjack works - now lets see the ways of the master:
# Ok I see he already used an in operator to make things a bit clearer... But he used <=31, which isn't wrong but not how my brain works...

def blackjack2(a, b, c) :
    if sum((a, b, c)) <= 21 :
        return sum((a, b, c))
    elif sum((a, b, c)) <= 31 and 11 in (a, b, c) :
        return sum((a, b, c)) - 10
    else :
        return 'BUST'
    

# Summer of 69: Return the sum of the numbers in the array, except ignore section of the numbers starting with a 6 and extending to the next 9. Every 6 will be followed by at least 1 9. Return 0 for no numbers
#  I immediately went to the solution of this one. Just, working with lists is a bit new for this.
def summer_69(arr) :
    total = 0
    add = True
    for num in arr:
        while add:
            if num != 6:
                total += num
                break
            else :
                add = False
        while not add:
            if num != 9:
                break
        else :
            add = True
            break
    return total

# SPy Game: Write a function that takes in a list of integers and returns True if it contains 007 in order

def spy_game(nums) :
    for i in range(0, len(nums) -1) :
        if nums[i] == 0 and nums[i + 1] == 0 and nums[i + 2] == 7 :
            return True
        else :
            pass
    return False
print("Spy Game: ", spy_game([1,2,7,0,0,7,5]))
# Nailed this one - Nope... Turns out we will get an "Out of Range" error if the final int is a 0... Makes sense because it will try check for the next step and see it can't. So, cute and almost there, but their solution covers all bases. Still so confused about the 'x' in the code list. Because I pass all checks without it.

# Here is their solution:
def spy_game2(nums) :
    code = [0, 0, 7, 'x']
    for num in nums :
        if num == code[0]:
            code.pop(0)
    return len(code) == 1
# Lets break theirs down.
# they create a code list which will be used to match the sequence
# they then in a for loop, num in nums, checks if num == code[0]... then pops code(0).
# I dont understand the 'x' and I don't understand the return. I will have to zoom in on it during explanations - I am registering my code, though. In this case, sure it is not as cool, but I understand it fully
# Still so confused about the 'x' in the code list. Because I pass all checks without it.

# Count Primes. Write a function that returns the number of prime numbers that exist upt and including a given number... 
# My non-Mathematical brain had to first try and register what a prime number is.
# A prime number is a number which you can't equate to by multiplying anything by anything else except 1. Like, for example, 1x5, 1x11, 7x1... Now I just need to find a way to translate that into a function.
# Alternatively, it is a number that can't be divided by any whole number except for itself. 
# I also see you can put it as "prime numbers only has 2 factors, itself and 1", others have like 3... So it must be something that can be times by itself to get a number... x * x = XX... but y * y will never = YY

# First try to make list of a range - done

def count_primes(num) :
    primes = [2]
    x = 3
    if num < 2: # for case of num = 0 or 1
        return 0
    while x <= num :
        for y in range(3, x, 2): #test all odd factors up to x-1
            if x % y == 0:
                x += 2
                break
        else :
            primes.append(x)
            x += 2
    print(primes)
    return len(primes)
print("Primes:", count_primes(50))
    # Whole function basically goes over my head - so I need to focus on the review

# Then there is the Big Letter one, which in all honesty was not really explained all to  well - because the solution is not even how I understood the question
def print_big(letter) :
    patterns = {1: "  *  ", 2: " * * ", 3: "*   *", 4: "*****", 5: "**** " ,6: "   * ", 7:" *   ", 8: "*   *", 9: "*    " }
    alphabet = {'A':[1,2,4,3,3],'B':[5,3,5,3,5],'C':[4,9,9,9,4],'D':[5,3,3,3,5],'E':[4,9,4,9,4]}
    for pattern in alphabet[letter.upper()]:
        print(patterns[pattern])

print(print_big("B"))
