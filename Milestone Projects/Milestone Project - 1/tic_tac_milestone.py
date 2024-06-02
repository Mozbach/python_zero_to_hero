# GLOBALS
the_board = ['#' , '1' , '2' , '3' , '4' , '5' , '6' , '7' , '8' , '9']
player1 = "" #This actually == the X or O
player2 = "" #This actually == the X or O
current_player = "player1"

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

def checkWinning(player_code, winning_dict) : #Here, check the boolean before the end of a player's turn
    sorted_player = sorted(player_code)
    for i in winning_dict :
        if sorted_player == winning_dict[i] :
            return True
    return False

def display_board(board) :
    the_board_row_top = [board[7] + " | " + board[8] + " | " + board[9]]
    the_board_row_mid = [board[4] + " | " + board[5] + " | " + board[6]]
    the_board_row_bot = [board[1] + " | " + board[2] + " | " + board[3]]
    def print_board() :
        return f"{the_board_row_top}\n{the_board_row_mid}\n{the_board_row_bot}"
    return print_board()

def player_placement(player1, player2, board) :
    global current_player
    current_player = "Player 1"
    taken_slot = []
    player_1_slots = []
    player_2_slots = []
    winner = False

    while winner == False :
        if current_player == "Player 1" :
            print(f"Player1, please choose where to place the {player1}")    
            player_choice = input("Please select a slot from 1 - 9: ")
            the_choice = int(player_choice)
            taken_slot.append(f"Player 1 Took : {the_choice} .")
            player_1_slots.append(the_choice)
            the_board[the_choice] = player1
            current_player = "Player 2"
            print("Taken Slots: ", taken_slot)
            print(f"Current Player Turn: {current_player}")
            print(display_board(board))
            if checkWinning(player_1_slots, winning_dict) == True :
                winner = True
                print("Player 1 Wins!")
                break
            
        else :
            print(f"Player 2, please choose where to place the {player2}")
            player_choice = input("Please select a slot from 1 - 9: ")
            the_choice = int(player_choice)
            taken_slot.append(f"Player 2 Took : {the_choice} .")
            player_2_slots.append(the_choice)
            the_board[the_choice] = player2
            current_player = "Player 1"
            print("Taken Slots: ", taken_slot)
            print(f"Current Player Turn: {current_player}")
            print(display_board(board))
            if checkWinning(player_2_slots, winning_dict) == True :
                winner = True
                print("Player 2 Wins!")
                break
    play_again()
# Include a play-again...
def player_input() :
    marker = ""
    # Keep asking player 1 to choose X or O
    while marker != 'X' and marker != 'O' :
        marker = input("PLayer 1, choose X or O...")
    # Assign Player 2 the oposite marker
    global player1
    global player2
    player1 = marker

    if player1 == 'X' :
        player2 = 'O'
    else :
        player2 = 'X'

    return (player1, player2)

def play_again() :
    answer = ""
    while answer != 'Y' and answer != 'N' :
        answer = input("Would you like to play again? ")
        global the_board
    if answer == 'Y' :
        the_board = ['#' , '1' , '2' , '3' , '4' , '5' , '6' , '7' , '8' , '9']
        player_input()
        player_placement(player1, player2, the_board)
        
    if answer == 'N' :
        print("Thanks for playing.")

print(player_input())

print(f"Player 1: {player1}")
print(f"Player 2: {player2}")

player_placement(player1, player2, the_board)

print(f"Current Board: \n{display_board(the_board)}" )