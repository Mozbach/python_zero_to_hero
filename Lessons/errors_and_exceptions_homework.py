# Problem 1:
# Handle the exception thrown by the code below using the try and except blocks.
try :
    for i in ['a', 'b', 'c'] :
        print(i ** 2) 
except TypeError :
    print("There was a TypeError here.")
    for i in ['a', 'b', 'c'] :
        print(f"You won't be able to find the root of '{i}' because it is not a number...")


# Problem 2:
# Handle the exception thrown by the code below using a try and except blocks. Then, use a finally block to print 'All Done':
try :
    x = 5
    y = 0
    z = x / y
except ZeroDivisionError:
    print("You can't divide by zero as you are attempting. Hence, the ZeroDivisionError.")
finally :
    print("All Done ! :)")

# Problem 3:
# Write a function that asks for an integer and prints the square of it. Use a while loop with a tyy, except, else block to acclount for incorrect inputs.
def ask() :
    while True :
        try :
            requestNum = int(input("Please provide a number to get the square of: "))
        except :
            print( "Seems like you did not provide a valid number... Please provide a number to get the square of.")
        else :
            print("Hope you got squared!")
            break
    print(f"Square of {requestNum} is : {requestNum ** 2}")
ask()