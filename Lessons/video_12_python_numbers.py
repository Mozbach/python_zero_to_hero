#  Python Numbers
# Two Main Number types:
# -> Integers:
intNum = int(22)
smallInt1 = int(2)
smallInt2 = int(4)
smallInt3 = int(7)


# -> Floating Point Numbers:
floatNum = float(22.2)
floatNum2 = float(22) # This will auto-convert the int to a float
floatNum3 = float(intNum - 5) # Can obviously be done with int variables as well


# Basic Math with Python
# Addition:
def defAddThis(a, b) :
    return a + b
print(defAddThis(intNum, floatNum))

# Subtraction
def defSubtractThis(a, b) :
    return a - b
print(defSubtractThis(floatNum, floatNum3))

# Multipliction
def defMultiplyThis(a, b) :
    return a * b
print(defMultiplyThis(floatNum2, smallInt3))

# Division
def defDivideThis(a, b) :
    return a / b
print(defDivideThis(floatNum2, smallInt2))

# Modulo operator
def defModuloThis(a, b) :
    return a % b
print(defModuloThis(smallInt1, smallInt2))

# Powers
powerThis = smallInt2 ** smallInt2
def defPowerThis(a, b) :
    return a ** b
print(defPowerThis(smallInt2, smallInt3))

# Use Parentheses to group numbers and then perform math
def defGroupedMath(a, b, c, d) :
    return (a * b) + (c + d)
print(defGroupedMath(smallInt1, smallInt3, smallInt2, smallInt3))