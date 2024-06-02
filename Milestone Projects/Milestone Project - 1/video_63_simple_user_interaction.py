game_list = [0, 1, 2]
def display_game(game_list) :
    print("Here is the current list: ")
    print(game_list)
display_game(game_list)

def position_choice() :
    choice = "Wrong"
    while choice not in ['0', '1', '2'] :
        choice = input("Pick a position: 1, 2 or 3: ")

        if choice not in ['1', '2', '3'] :
            print(f"Sorry, {choice} is not a valid option.")

    return int(choice)

print(f"Your chose: {position_choice()}")

def replacement_choice(game_list, position) :
    user_placement = input("Type a string to place at a position: ")
    game_list[position] = user_placement

    return game_list

replacement_choice(game_list, 1)
print(game_list)

def gameon_choice() :
    choice = "Wrong"

    while choice not in ['Y', 'N'] :
        choice = input("Keep Playing?")

        if choice not in ['Y', 'N'] :
            print(f"Sorry, I do not understand the choice of : '{choice}'. Please select either 'Y' or 'N'.")

    if choice == 'Y' :
        return True
    else :
        return False
    
print(gameon_choice())

game_on = True
game_list = [0, 1, 2]

while game_on:
    display_game(game_list)
    position = position_choice()
    game_list = replacement_choice(game_list, position)
    display_game(game_list)

    game_on = gameon_choice()