# OOP Allows programmers to create their own objects that have methods and attributes.
# Recall htat after defining a string, list, dictionaroy or other objects, you were able to call methods off them with the .method_name() syntax.

# These methods act as function that use information about the object, as well as the object itself to return results, or change the current object.
# For example this  include appending to a list, or counting the occurences of an element in a tuple.

# OOP allows users to create their own objects.
# The general format is often cofusing when first encountered, and its usefulness may not be c ompletely clear at first.
# IN general, OOP allows us to create code that is repeatable and organized.

# For much larger scripts of Python code, functions by themselves are not enough for organization and repeatability.
# Commonly repeated tasks and objects can be defined with OOP to create code that is more usable.
# The Syntax of OOP!

class NameOfClass() : # ClassKeyword uses camel casing
    def __init__(self, param1, param2) : #The method - looks like a function, but is called a method when it is inside a class-call
        self.param1 = param1 
        self.param2 = param2 # Pass in a parameter, in this case param2, and then connect it to this class - NameOfClass. Then we refer to this parameter with self.param2

    def some_method(self) : #Then we can add various other method calls, and they, built insided the class, and they look much like functions... Again we use "self" in the arguments to connect it to the NameOfClass class
        # Perform some action
        print(self.param1)