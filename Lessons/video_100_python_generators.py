# We have learned how to create functions with def and the return statement.
# Generator functions allow us to write a function that can send back a value and then later resume to pick up where it left off.
# Oh my god...

# This type of function is a generator in Pythin, allowing us to generate a squence of values over time.
# The main difference in syntax will be the use of a yield statement.

# When a generator function is compiled, it becomes an obkect that supports an iteration protocol.
# That means when they are called in your code, they don't actually return a value and then exit.
# Instead, Generator Functions will automatically suspend and resume their execution and state around the last point of value generation.
# The advantage is that instead of having to compute an entire series of values up front, the genrator computes one value and then waits until the next value is called for.

# For example, the range() function doesn't produce a list in memory for all the values from start to stop.
# Instead it just keeps track of the last number and the step size, to provide a flow of numbers.

# Now, if the user did actually needa list, they have to transform the genreator to a list with list(range(0, 1))
# Let's explore how to create our own generators




# I just quickly want to run through the very short w3schools lesson on generators as well - or well... the yield keyword
# Return 3 Values from a Function
def myFunc() :
    yield "Hello"
    yield 51
    yield "Good Bye"

x = myFunc()

for z in x :
    print(z)

# ... cute

# Definition and Usage:
# The yield keyword is used to return a list of values from a function.
# Unlik the return keyword which stops further execution of the function, the yield keyword continues to the end of the function.
# When you cann a function with a yield keyword or words... the return value will be a lost of values, one for each yield.
# ... Ok, this was interesting, but seemingly had nothing to do with the use of yield in the course... Here is the course's


def create_cubes(n) : # Here we will create cubes from zero up to whatever "n" is
    result = []
    for x in range(n) :
        result.append(x ** 3)

    return result
print(f" This is from create_cubes, a list function: {create_cubes(10)}" )
# See, now this above function basically creates a list which will be stored on memory. 
# But if you don't really need it in a list or don't need it in memory, you can use yield instead
def yielded_cubes(n) :
    for x in range(n) :
        yield x ** 3
for x in yielded_cubes(10) :
    print(x)

def fibonacci_this(n) :
    a = 1
    b = 1
    for i in range(n) :
        yield a
        a,b = b, a + b
# we basically reset a to be equal to b, and b is going to be equal to the sum of that previous a + b.
# Ok, i see... The first a is equal to b, the first b is equal to the previous sum of a + b. The tuple matching works exactly how it is spaced by the commas. a, matched with the first be after the =, and the first b is matched with the sum of in the a + b, which comes second after the =.
# Just to better understand this fibonnaci_this method... THey use something called "tuple matching"... I just want to check this out quickly...
# According to Guru99: Tuple matching in Python is a method of grouping the tuples by matching the second element in the tuples. It is achieved by using a dictionary by checking the seconf element in each tuple in python programming. We can make new tuples by taking portions of existing tuples... Ok... That made fuck all sense.
# Again,. the fibo_list method below is way less memory efficient.
def fibo_list(n) :
    the_list = []
    for number in fibonacci_this(n) :
        the_list.append(number)
    return the_list

print(fibo_list(10))


# The generator object uses a similar concept to this below "next" keyword to create the generator effect.
def simple_gen() :
    for x in range(3) :
        yield(x)
g = simple_gen()
print(f"g: {g}")
print(f"Next g: {next(g)}")
print(f"Next g after that: {next(g)}")
print(f"and the Next g after that: {next(g)}")
# Next basically remembers what the previous value was, then returns the next one after that.

# Now, let's look at the iter object:
s = "Hello"
# already we know we can iterate throug this s string...
for letter in s :
    print(letter * 3)

# However, by default we can't actually directly iterate over it as we did with the generator function, but we can give it the ability to be iterated over.
s_iter = iter(s)
# Now, things like the "next" method will work to iterate through it as we need it...
print(f"Iterate over s_iter: {next(s_iter)}")
print(f"Next Iterate over s_iter: {next(s_iter)}")
print(f"And Next Iterate over s_iter: {next(s_iter)}")
print(f"And then the Next Iterate over s_iter: {next(s_iter)}")
print(f"And then the final Next Iterate over s_iter: {next(s_iter)}")