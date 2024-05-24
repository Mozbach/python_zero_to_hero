def myfunc(a, b) :
    # returns 5% of the sum of a and b
    return sum((a, b)) * 0.05

print(myfunc(40, 60))

# Enable functions to take an arbitrary number of arguments
def myfunc(*args) :
    # you will now deal with a tuple of arguments
    return sum(args) * 0.5

print(myfunc(10,20,30,40,50))

# Also, use **kwargs to build a dictionary of key-value pairs
def myfunc(**kwargs) :
    print(kwargs)
    if 'fruit' in kwargs:
        print('My fruit of choice is {}'.format(kwargs['fruit']))
    else :
        print("No fruit found")
    
myfunc(fruit='apple', meat='beef', veggie='broccoli')

# We can also eccept both
def myfunc(*args, **kwargs) :
    print('I would Like {} {} '.format(args[0], kwargs['food']))

myfunc(10, 20, 30, fruit='orange', food='fresh', meat='dry', drink='coffee')