# Decorators
# Decorators allow you to decorate a function... 
# Imagine you created this function
# def simple_func() :
#     something_simple = "Do some simple stuff"
#     return something_simple
# Now, let's say we wanted to add some extra code and functionality to this simple_func
# You have 2 options :
# - Add that extra code/functionality to your old function
# - Or create a brand new function that contains the old code, and then add the new code to this new function

# What if we wanted to REMOVE that extra functionality at a later stage?
# You would then need to delete it manually, or make syure to have the old function
# Is there a better way? Maybe an on/off switch to quickly add or remove this functionality?

# Python has decorators that allow you to tack on extra functionality to an already existing function
# Decorators use the @ operator and are then placed on top of the original function... Kinda like class inheritence.. kinda?

# Now, you can easily add on extra functionality with a decorator:
# @some_decorator
# def simple_func() :
#     something_simple = "Something Simple"
#     return something_simple

# This idea is pretty abstract in practice with Python syntax, so we will go through the steps of manually building out a decorator ourselves, to show what the @ operator is doing behind the scenes.

# Let's create some
def func() :
    return 1

print(f"{func()}")

def hello() :
    return "Hello!"

temp_hello = hello
print(f"Temp Hello: {temp_hello()}") # <-- Note how it basically copies the previous function?

def hello2(name = "Carsten") :
    print("The hello() function has been executed!")

    def greet():
        return "\t This is the greet() function insde the hello2 function."

    def welcome() :
        return "\n This is welcome() inside hello!"
    
    print("I am going to return a function")
    if name == "Jose" :
        return greet
    else :
        return welcome

# Note how we can access the hello2 function's...
my_new_func = hello2("Jose")
print(my_new_func())

# Note now the greet and welcome functions are only in the scope of the hello2() function. If you try to access them OUTSIDE of the hello2() function, you will get an error... a NameError, to be precise
# Another example (Thank lord)

def cool() :
    def super_cool():
        return "I am very Cool!"
    return super_cool
cool_func = cool() # This is then the super_cool function... Because cool returns the super_cool...
print(cool_func())

def hello3() :
    return "Hi, Jose!"

def other(some_def_func) :
    print('Otehr code here')
    print(some_def_func)

other(hello3)
print(other)


def new_decorator(original_func) :
    def wrap_func() :
        print("Some extra code, before the original function")

        original_func()

        print("Some extra code AFTER the original function.")

    return wrap_func

def func_needs_decorator() :

    print("i want to be decorated")

decorated_function = new_decorator(func_needs_decorator)

decorated_function()
