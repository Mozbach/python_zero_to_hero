# Sets are unordered collections of unique elements.
# Meaning there can only be one representative of the same object
myset = set()
myset.add(19)
print(myset)

# It is useful to have a list with duplicate values, then cast it to a set, which will then create a set of unique values, removing all of the duplicate values in the list
myList = [1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4, 5, 5, 5]
myset = set(myList)
print(myset)
