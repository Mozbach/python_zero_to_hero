# Now, the generator Homework
# Problem 1: Create a generator that generates the squares of numbers up to some number N.
def gen_squares(n) :
    for x in range(n) :
        yield x ** 3

print("Numbers in gen_squares(10: )")
for number in gen_squares(10) :
    print(number)

# Problem 2: Create a generator that yields "n" random numbers between a low and a high number that are inputs. Just commenting it out because it stops testing on later teachings
# import random
# num1 = int(input("Please enter a starting point number: "))
# num2 = int(input("Please enter an ending point number: "))    

# def random_yield(rand1, rand2, n) :
#     for num in range(n) :
#         yield random.randrange(rand1, rand2)

# print(f"Yielded Randoms: ")
# for number in random_yield(num1, num2, 10) :
#     print(number)

# Problem 3: Use the iter() function to conver the string below into an iterator:
s = 'hello'
iter_s = iter(s)
for i in range(len(s)) :
    print(next(iter_s))


# They want me to explain something called gencomp. - Or, generator comprehension
# Apparently it is like list comprehension - here is w3schools's tutorial on that

# List comprehension offers a shorter syntac when you want to create a new list based on the balues of an existing list. 
# Example: Based on a list of fruits, you want a new list, containing only the fruits with the letter "a" in the name
# Without list comprehension, you will have to write a for statement with  a conditional test inside:
fruits = ["apple", "babana", "cherry", "kiwi", "mango"]
newList = []

for x in fruits:
    if "a" in x :
        newList.append(x)

print(newList)

# But with list comprehension, you can do that all with one line of code:
newList = [x for x in fruits if "a" in x]

print(newList)

# Now, back to Stackoverflow...
# Do you understand List Comprehensions? if So, generator expression is like a list comprehension, but instead of finding all the items you are interested in, and packing them into a list, it waits and yields each item out of the expression, one by one.
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
filtered_list = [item for item in my_list if item > 3]
print(filtered_list)
print(len(filtered_list))

# Compare this to generator Expressions
filtered_gen = (item for item in my_list if item > 3)
print(filtered_gen) # This is a generator object
# print(len(filtered_gen)) # So, it won't have a length, technically -> This gives an error

# We will have to extract each item individually
for filtered_num in filtered_list :
    print(next(filtered_gen))

# Proving that this gives the same result as list comprehension
filtered_gen = (item for item in my_list if item > 3)
gen_to_list = list(filtered_gen)
print(gen_to_list)
# Below returns true if they were to return the same thing... and it does
print(filtered_list == gen_to_list)

# Because a generator expression only has to yield one item at a time, it can lead to big savings in memory useage. Generator expressions make the most sense in scenarios where you need to take one item at a time, do some calculations on it, and then move on to the next itme. If you need more than one value, you can also use a generator expression and grab a few at a time. If you need ll the values before your program proceeds, use a list comprehension instead.

# Another user mentions:
# A generator comprehension is the lazy way of a list comprehension.
# It is just like list comprehension except that it returns an iterator instead of the list - ie an object with a next() method that will yield the next element