# Further valudate user input by using a While loop to continuosly ask the user for the input, until the correct input is given.

# set choice var
# set acceptable range
# set within range bool
# While choice is not a digit or we are out of range, ask the user for a choice
# Check the digit
# Check the range
# return the choice
def user_choice() :
    choice = "Wrong"
    acceptable_range = range(1, 10 + 1)
    within_range = False

    while choice.isdigit() == False or within_range == False :
        choice = input("Please insert a number between 1 - 10: ")

        if choice.isdigit() == False :
            print(f"The provided choice: '{choice}' is not a number.")

        if choice.isdigit() == True :
            if int(choice) in acceptable_range :
                within_range = True
            else :
                print(f"The provided number: '{choice}' is not within the valid range")
                within_range = False
    return f"You chose: {choice}"

print(user_choice())