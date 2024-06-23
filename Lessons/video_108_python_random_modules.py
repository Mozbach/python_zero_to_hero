# Here we will look at the Math module and the Random module
import math
# To see much info on the math function:
# help(math)

# Round given numbers
value = 4.35
print(f"Floor of {value} = {math.floor(value)}") 
print(f"Ceil of {value} = {math.ceil(value)}")
print(f"Round of {value} = {round(value)} >--> Note, this is not part of the Math module. Just part of Base Python")
print(f"rounded 4.5 = {round(4.5)} VS rounded 5.5 = {round(5.5)} -> Rounding always happens to go for what makes the roudned value EVEN -- if the decimal value is just split down the middle, like .5")

# Lets grab some mathematical constants
my_pi = math.pi
print(f"math.pi: {my_pi}")
my_e = math.e
print(f"math.e: {my_e}")
# I never knew what e was... so basically, e is "exponential constant" -> Is an important mathematical constant and is gtiven the symbol "e".
# Its value is approximately 2.718.
# It has been found that this value occures so frequently when mathematics is used to model physical and exonomic phenomena, so it is conveniently written as "e".
my_inf = math.inf
print(f"my_inf: {my_inf}")
my_nan = math.nan
print(f"my_nan: {my_nan}")

# Some Randomness...
import random
# random.randint(a, b) -> Returns a random number in range of a and b
randomInt = random.randint(10, 20)
print(f"Randomness between 10 - 20, included: {randomInt}")

# We can also set a seed on thhe randint method.
# Meaning, for testing purposes, you can test the same random numbers
# random.seed(101)

# print(random.randint(0, 100)) # Always produces, 74 because seed is set. 
# print(random.randint(0, 100)) # Always produces, 24 because seed is set. 
# print(random.randint(0, 100)) # Always produces, 69 because seed is set. 
# print(random.randint(0, 100)) # Always produces, 45 because seed is set. 


# This here is how to take a random item from a list...
myList = list(range(0, 20)) #Creates a list containing numbers frpm 0 - 20
# Now lets grab a random number our of myList
myListRandom = random.choice(myList)
print(f"My Random Item from a List: {myListRandom}")
# Seed also affects this, so I just commented seed.
# Now, lets grab 5 random numbers from the list:

# Sample with replacement
# Population is the list we are actually picking from, in this case, myList.
# k is then how many random items you want from this
randommedList = random.choices(population = myList, k = 10)
print(randommedList)

# Sample without replacement: Means once a number was picked, it won't be picked again.
sampledRandomedList = random.sample(population = myList, k = 10)
print(sampledRandomedList)

# Shuffle a list
# This shuffles an existing list in place, so don't reassign it - it won't matter.
random.shuffle(myList)
print(f"my shuffled list: {myList} ")
# The random.shuffle(list) method, permenantly affects the list.

# There is also a uniform distribution method, which randomly picks a value between a and be -> Unsure how this is different from random.randrange(a, b) -> Turns out it will also returns floating point numbers.
# Also the reason this is "uniform", is that every number between 0 and 100, or a and b, has the same likelyhood of being chosen... strange. I wonder how randrange gives any sort of advantage to certain numbers.
uniformRandom = random.uniform(a=0, b=100)
print(f"Random Uniform: {uniformRandom}")
 