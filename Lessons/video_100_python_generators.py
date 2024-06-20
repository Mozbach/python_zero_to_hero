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

def create_cubes(n) :
    
    for x in range(n) :
        yield x ** 3 # Power of 3 is "cubed"
    
for x in create_cubes(10) :
    print(x)

# Let's create a febi sequence! Yay... My brain could literally not think of how to do this... SO FOCUS!
def gen_fibon(n) : # Will generate fibonaci up to n
    a = 1
    b = 1
    output = [] # now, appending them to a list is sort of missing the point, because a list ends up taking space in memory... while just using yield does not

    for i in range(n) :
        # yield a
        output.append(a)
        a, b = b, a + b # a will be equal to b, and then b is the sum of the previous a + b
        return output
for number in gen_fibon(10) :
    print(number)  


# Next Function
def simple_gen() :
    for x in range(10) :
        yield x

for x in simple_gen() :
    print(number)

g = simple_gen()

print(next(g))

# Iter function
s = 'hello' #through this we CAN interate
s_iter = iter(s)
print(next(s_iter))
print(next(s_iter))
print(next(s_iter))
print(next(s_iter))
print(next(s_iter))