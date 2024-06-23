# When trying to figure out what errors there are in your code, you have probably used print() to track down the error.
# Fortunately, Python comes with a built-in debugger tool that allows you to interactively explore variables within mid-operation of your Python code -> Did we not cover this already? 
# Example of an error

# import pdb, the python debugger
import pdb

x = [1, 2, 3]
y = 2
z = 3

result1 = y + z

pdb.set_trace()
result2 = x + y # This here should cause an error. Because we are trying to add a list to an intiger....

# Ok, pretty cool. It opens a small interface where you can call variables at any point in the code to see what they are at any given stage. Then that way, figure out for example we can't add an int 2 to a list.
