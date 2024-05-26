# Lucky me - I understand scoping quite wll already, but the lesson was good, regardless.
# Notes, instead of using the GLOBAL keyword within a function to reassign the value of a global variable from within the function, one should rather return the value then manually reassign it
# Demo:

x = 100
print(f"First, x was {x}")

def change_x(variable) :
    variable = 300
    return variable

x = change_x(x)
print(f"And now, x is {x}")

# This was the main takeaway...
