def say_hello() :
    print("hello")

# When calling a function, use () at the end to actually call the function. If the () are omitted, you will just be told that the given function is a function, and you won't actually run the function.

def say_hello(name) :
    return f"hello, {name}"

print(say_hello("Carsten"))

# use a default value, in case no argument is provided. This prevents errors
def say_hello(name="user") :
    return f"hello, {name}"

print(say_hello())
print(say_hello("Morrigan"))

# returning a mathematical equasion
def my_addition(num1=1, num2=2) :
    return num1 + num2
sumVariable = my_addition(22, 12)
print(sumVariable)

# You can also return and print - although this is uncommon
def my_print_return(num1=0, num2=0) :
    print(num1 + num2)
    return num1 + num2
myNewNum = my_print_return(44, 10)