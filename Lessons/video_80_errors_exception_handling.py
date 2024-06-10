# we use three keywords for error handling:
#   - try: This is the block of code to be attempted, which may lead to an error
#   - except: Block of code will execute in case there is an error in the try block
#   - finally: A final block of code to be executed, regardless of an error.

def add(n1, n2) :
    print(n1 + n2)

add(10, 20)

number1 = 10
# number2 = input("Please provide a number: ")

try :
    #  Want to attempt this code
    #  May have an error
    result = 10 + 10
except :
    print("It looks like you are not adding correctly.")
    print("See, even if there is an error, the code following the try block actually runs and doesn't just shut down the whole program.")
else :
    print("Add was successful!")
    print(result)

# Here is an example of the finally keyword. The finally keyword will always run, regardless if there is an error or not.
try :
    f = open('testfile', 'w')
    f.write("Write a test line")
# This except will only run for a TypeError specifically.
except TypeError: 
    print("There was a TypeError")
# This except will run if you do not have permission to write to the file.
except OSError:
    print("You do not have permission to write to this file. - OSError")
# If you do not specify the type of error to expect in a given except block, leave it as except only to run for all other errors.
except :
    print("All other exceptions!")
# And then there is the finally block, which will always run, regardless if there are errors or not.
finally:
    print("I always run")

# Create function that has a try block in it
def ask_for_int() :
    while True : #Note, when using while True, be sure to break out of the loop at some point, else an infinite loop might occur
        try :
            result = int(input("Please provide a number: "))
        except :
            print("Seems like you did not provide a number.")
            continue
        else :
            print(f"You chose {result}")
            break
        finally : 
            print("End of Try/Except - I will always run, regardless if there is an error or not.")

ask_for_int()