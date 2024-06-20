# Well... I can't find this notebook brother is on about, so, I went to datacamp to check out their explanation on decorators. - I just don't quite get it yet.
# To kick us off, we create a function that will add one to a number whenever it is called. We'll then assign the function to a variable and use this variable to call the function.
def plus_one(number) :
    return number + 1

add_one = plus_one
print(add_one(5))

# Defining Function inside other functions
# Next, we'll illustrate how you can define a function inside another function in Python.
def plus_one(number) :
    def add_one(number) :
        return number + 1
    
    result = add_one(number)
    return result

print(plus_one(4))

# Passing functions as Arguments to other Functions
# Functions can also be passed as parameters to other functions. Let's illustrate that below.
def plus_one(number) :
    return number + 1
def function_call(function) :
    number_to_add = 5
    return function(number_to_add)

print(f"Honestly, though - still not really getting it... {function_call(plus_one)}. Like... I get it. I guess the question more is 'why?'")

# Functions returning other functions
# A function can also generate another Function. We'll show that below...
def hello_function() :
    def say_hi():
        return "Hi"
    return say_hi
hello = hello_function()
print(f"Hello Function: {hello()}")

# Nested functions have access to the Enclosing Fucntion's variable scope - cool
# Python (stop typing pythIn... gawd damn!) - Python allows to access the outer scope of the enclosing function. This is a critical concept in decorators - This pattern is known as a Closure.
def print_message(message) :
    "Enclosing Function"
    def message_sender() :
        "Nested Function"
        print(message)

    message_sender()

print("Random message from print_message, enclosing message_sender, which is returned by print message:")
print_message("This is a random message!")

# Creating Decorators
# With these prerequisites out of the way, let's go ahead and create a simple decorator that will convert a sentence to uppercase, we do this by defining a wrapper inside an enclosed function. As you can see it is very similar to the function inside another function that we created earlier
def uppercase_decorator(function) :
    def wrapper() :
        func = function()
        make_uppercase = func.upper()
        return make_uppercase
    return wrapper

# Above, our decorator function takesa function as an argument, and we shall, therefore, define a function and pass it to our decorator. we learned earlier that we could assign a function to a variable. We'll use that trick to call our decorator function.

def say_hi() :
    return 'Hello There'

decorate = uppercase_decorator(say_hi)
print("uppercase_decorator using the say_hi function we made...")
print(decorate())

# However, Python provides a much easier way for us to apply decorators. We simply use the @ symbol before the function we'd like to decorate.
@uppercase_decorator #so, here we reference the decorator... and right below it, we use it on the function that we would like to decorate... Kinda like a cherry on top?
def say_hi() :
    return "hello, fiends"

print(say_hi())

# Applying Multiple Decorators to a Single Function
# We can also use multiple decorators to a single function. The decoratos will be applied in the order that we have called them. Below, we define another decorator that splits the sentence into a list. We'll then apply the uppercase_Decorator and split_string decorator to a single function
import functools
def split_string(function):
    @functools.wraps(function)
    def wrapper():
        func = function()
        splitted_string = func.split()
        return splitted_string

    return wrapper 

@split_string
@uppercase_decorator
def say_hi3() :
    return 'i need to stop greeting...'

print("This is using multiple wrappers at once...")
print(say_hi3())

# ... Ok, the part on decorators from https://www.datacamp.com/tutorial/decorators-python continues... But they basically covered what was covered in the Zero to Hero course. I am moving on the the homework for now.