winning_dict = {
    "winning_positions_1_2_3" : [1, 2, 3],
    "winning_positions_4_5_6" : [4, 5, 6],
    "winning_positions_7_8_9" : [7, 8, 9],

    "winning_positions_3_5_7" : [3, 5, 7],
    "winning_positions_1_5_9" : [1, 5, 9],

    "winning_positions_1_4_7" : [1, 4, 7],
    "winning_positions_2_5_8" : [2, 5, 8],
    "winning_positions_3_6_9" : [3, 6, 9]
}

player1 = [5, 2, 8]
def checkWinning(player_code, winning_dict) :
    sorted_player = sorted(player_code)
    for i in winning_dict :
        print(winning_dict[i])
        if sorted_player == winning_dict[i] :
            return True
    return False

print(checkWinning(player1, winning_dict))

def play_again() :
    again = False
    answer = ""
    while answer != 'Y' and answer != 'N' :
        answer = input("Would you like to play again? ")
    if answer == 'Y' :
        again = True
        print("PLAY AGAIN")
    if answer == 'N' :
        print("Thanks for playing.")
play_again()