# From the video, nothing I didn't know already, but here is a note:
# Python uses Dynamic Typing, meaning you can reassign variables to different data types.
# For example, str1 = str("This is a string") can be turned into an int str1 = int(33)

str1 = str("This is a string")
print(str1)

str1 = int(33) # Only this value will appear, not the previous str1 str value
print(str1) 

# You can even turn str1 into something like a list
str1 = ["First, this was a string", "Then it became an integer", "Now it is a List"]
print(str1)

# Pros and Cons of Dynamic Typing:
"""
Pros:
- Very easy to work with
- Faster Development time

Cons:
- May result in bugs for unexpected data types
- You also need to be aware of type() to check the current type of a variable
""" 

# Basic tax calculator
def taxCalculator(salary, taxRate) :
    payableTax = salary * taxRate
    myMoney = salary - payableTax
    return f"Your payable tax is: {payableTax}. Making your money: {myMoney}."

print(taxCalculator(19200, 0.15)) # Something like this