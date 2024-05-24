from random import shuffle

# function to shuffle a list
def shuffle_list(list_to_shuffle) :
    shuffle(list_to_shuffle)
    return list_to_shuffle

# Function to take a player's Guess
def player_guess() :
    guess = ''
    while guess not in ['0', '1', '2'] :
        guess = input("Pick a number: 0, 1 or 2: 5")
    return int(guess)

# Function to check the guess and compare it to the shuffled list
def check_guess(cup_list, guess) :
    if cup_list[guess] == 'O' :
        print("Correct!")
        print(cup_list)
    else :
        print("Wrong Guess, play again!")
        print(cup_list)

# Initial List
cup_list = [' ', 'O', ' ']

# Shuffle the List
mixed_list = shuffle_list(cup_list)

# User guess 
guess = player_guess()

# Check guess
check_guess(mixed_list, guess)