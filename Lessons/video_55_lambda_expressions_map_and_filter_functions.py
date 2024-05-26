# Lambda function are quick - one-time-use function to use the moment they are needed, then never again.
# Lets talk about Map

def square(num) :
    return num ** 2

nums = [1, 2 ,3 ,4 ,5]

for item in map(square, nums) :
    print(item)

print(list(map(square, nums)))

names = ['morrigan', 'kerryn', 'carsten', 'djinnimintis']

def splicer(mystring) :
    if len(mystring) % 2 == 0 :
        return "EVEN"
    else :
        return mystring[0]
    
print(list(map(splicer, names)))

# Filter Function
# returns an iterator yielding those items of the iterable for which when you pass in the item into the function, it is True - Basically means you need to filter by a function that returns either True or False
def check_even(num) :
    return num % 2 == 0

nums = [1, 2 ,3 ,4 ,5, 6, 7, 8, 9 ,10]
filtered_nums = list(filter(check_even, nums))
print("Filtered_Nums: ", filtered_nums)

# lambda - damn... this isn't much but my brain is TIRED!
# Similar to the square function we built earlier for the map... here it is in lambda
print("Lamda Squared! : " , list(map(lambda num : num ** 2, nums)))

# lambda function similar to the filter function we did earlier.
print("Lambda Check Even: ", list(filter(lambda num : num % 2 == 0, nums)))

# With lambda, grab the first character of a string
lambdaString = "This is Lambda"
lambdaList = lambdaString.split()
print("Mapped Lambda List: ", list(map(lambda word: word[0], lambdaList)))

# W3Schools Filter tutorial: 

# Filter the array, and return a new array with only the values equal to or above 18:
ages = [5, 12, 17, 18, 24, 32]
def myFilterFunction(x) :
    if x < 18 :
        return False
    else :
        return True
    
adults = filter(myFilterFunction, ages) 
for x in adults :
    if x >= 18 :
        print(x, " Makes you an adult")

# Definition and Usages:
# The filter function returns an iterator where the items are filtered throguh a function to thest if the item is accepted or not.


# W3 Schools's Map Tutorial: 
# Calculate the length of each word in a tuple
def myfunc(n) :
    return len(n)

x = map(myfunc, ('apple', 'banana', 'cherry'))
print("W3Schoosl: Calculate length of each word in a tuple: ", list(x))

# Definition and Usage:
# The map() function executes a specified function for each item in an iterable. The item is sent to the function as a parameter.

def myfunc2(a, b) :
    return a + b

x2 = map(myfunc2, ('apple', 'banana', 'cherry'), ('orange', 'lemon', 'pineapple'))
print(list(x2))

# geeksforgeeks tutorial
# map() function returns a map object, which is an iterator, of the results after applying the given function to each item of a given iterable, list, tuple etc...

# Syntax: map(function, iterator)
# Parameters:
# function: it is a function to which MAP passes each element of the given iterable
# iterable: It is the iterable which is to be mapped

# Note: You can pass one or more iterable to the map() function
# Returns a list of the results after applying the given function to each item of a given iterable - list, tuple... etc
# Note: The returned value from map() (map object) then can be passed to functions like list() to create a list, set to create a set
# Return double of n
def addition(n) :
    return n + n

# We double all numbers using map
geekNums = (1, 2, 3, 4, 5)
result = map(addition, geekNums)
print(list(result))



# geeksforgeeks filter function tutorial
# The filter() method filters the fiven sequence with the help of a function that tests each element of the sequence to be true or not.
# The filter method in Python has the following syntax
# filter(function, sequence)
# Function: Function that tests if each element of a sequence is true or not
# Sequence: Sequence which needs to be filtered, it can be sets, lists, tuples or containers of any iterators
# Returns: an iterator that is already filtered
# ython filter function examples
# IN this example, we are using the filter function along with a custom function, fun() to filter out vowels form a Python list
def fun(variable) :
    letters = ['a', 'e', 'i', 'o', 'u']
    if(variable in letters) :
        return True
    else :
        return False
    
# Sequence
sequence = ['g', 'e', 'e', 'j', 'k', 's', 'p', 'r']

filtered = filter(fun, sequence)

# Using filter function
for s in filtered:
    print(s)