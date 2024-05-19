# Lists are ORDERED sequences that can hold a variety of object types.
# They use [] brackets and commas to separate objects in the list aList = [1, 2, 3, 4], for example
# Lists support indexing and slicing
# Lists can be nested and also have many useful methods that can be called off them

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
my_second_list = [11, 12, 13, 14, 15]

# lists can hold any combination of data types
mixed_list = [1, "string", 1.2]

# check the length of a list
lenOf_my_list = len(my_list)

# Slice a list
slicedList = my_list[2:-4]

# List indexing: 
indexOfList = my_list[7]

# Concatinate lists:
my_third_list = my_list + my_second_list
print(my_third_list)

# We can also, unlike strings, mutate lists. So, strings are mutable!
my_third_list[5] = 100
print(my_third_list) # So here, item at index 5 will become 100.

# Add an element to the end of a list
my_third_list.append(678)

# Remove, or "pop" off an item at the end of a list, it also returns the popped of value.
poppedList = my_third_list.pop()

# Remove an item at a specific index
def popAnItem(theList, theIndex) :
    poppedItem = theList.pop(theIndex)
    return poppedItem

# Sort a List
unsorted_list = ["c", "u", "a", "b", "z", "l",]
unsorted_num_list = [3, 7, 12, 1, 66, 11, 2, 8]
unsorted_list.sort()
sorted_list = unsorted_list

unsorted_num_list.sort()
sorted_num_list = unsorted_num_list
print(sorted_num_list)

# Reverse items in the list
sorted_num_list.reverse()
print(sorted_num_list)