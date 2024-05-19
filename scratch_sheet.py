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
f = open("myfile.txt", "r")
read_f = f.read()
print(print(f"read_f: {read_f}"))
f.seek(0)

o = open("C:\\Users\\crstn\\OneDrive\\Desktop\\Myprojects\\ZeroToHeroPython\\\holdsTextFiles\\textFile.txt")
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



