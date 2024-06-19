"""

--- *** --- Project Instructions --- *** ---
In this milestone project, you will be creating a Comple BlackJack Card Game in Python - I really wish I could stop typing "Pythin" - Sounds like "Tampin" VS "Tampon".

Here are the Requirements:
- You need to create a simple text-based BlackJack game
- The game needs to have on players versus an automated dealer.
- The player can stand or hit.
- The player must be able to pick their betting amount.
- You need to keep track of the player's total money.
- You need to alert the player of wins, losses or busts - etc.

Most Importantly:
You mnust use OOP and classes in some portion of your game.
You can not just use functions in your game.
Use Classes to help you define the Deck and the Player's Hand.
There are many right way to do this - so explore it well.

""" 

"""
My plan.
In the player class...
- Add the player's money / chips as well.

- Create a game_on Boolean which will be True initially. After a round completed, the user will be asked if he wants to play again with input. If yes, play again. Naturally then his money will be noted and saved in the class. 
If the player is done playing, his money will be his top score. - The top score will be saved in a text file - this really brings together a lot of things we have learnt.

- In the Deck class, we must figure out a way to reshuffle the deck as soon as there are no cards left to deal or draw.
- Maybe have a list which the played cards fall into - used_cards - , then if the main deck is finished, then the used_cards pack will be shuffled and added to the main deck again. Leaving dealt cards on the table, and just filling up the deck with cards that have been used.

"""

import random
ranks = (
    'Ace',
    'Two',
    'Three',
    'Four',
    'Five',
    'Six',
    'Seven',
    'Eight',
    'Nine',
    'Ten'
    )

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')

values = {
    'Ace' : 11,
    'Two' : 2,
    'Three' : 3,
    'Four' : 4,
    'Five' : 5,
    'Six' : 6,
    'Seven' : 7,
    'Eight' : 8,
    'Nine' : 9,
    'Ten' : 10,
    'Jack' : 10,
    'Queen' : 10,
    'King' : 10
}
# What about we give each card a value called "counted",  counted starts as False, then as soon as it is counted, we just make the Boolean True. Then if we need to count the values in the hand again, we check that boolean to ensure it wasn't counted yet before counting and adding it to the hand total. Otherwise it will add it to the hand total constantly, making the hand total HUGE. Then, when we throw the cards into the discard after a game, we use a loop to set their counted values back to false. Then, if a new round begins, we won't be bothered by any of this.
discard = []

class Card() :
    def __init__(self, suit, rank) :
        self.suit = suit
        self.rank = rank
        self.value = values[rank] # This value comes out of the Values dictionary.
        self.counted = False

    def __str__(self) :
        return self.rank + " of " + self.suit

class Deck() :
    def __init__(self) :
        self.all_cards = []
        for suit in suits : 
            for rank in ranks :
                created_card = Card(suit, rank)
                self.all_cards.append(created_card)
    def shuffle(self) :
        random.shuffle(self.all_cards)

    def deal_one(self) :
        return self.all_cards.pop()

# Set up player:
def get_player() :
    player_name = input("Hello, Gambler - What is your Name? ")
    return player_name

player_name = get_player()
black_jack_deck = Deck()
black_jack_deck.shuffle()

class Player() :
    def __init__(self) :
        self.player_name = player_name
        self.player_hand = []
        self.player_hand_total = 0
        self.player_chips = 50
        self.player_bet = 0
        self.ace_check = False # If this is on False, it will -10 the hand_total if there was an ace in the hand with the first 2 cards. 

    def bet_chips(self) :
        try :
            chips_to_bet = int(input(f"{self.player_name}, you have {self.player_chips} chips. How many do you want to bet? "))
            if chips_to_bet > self.player_chips :
                print(f"{self.player_name}, you don't have enough chips. Please enter a maximum of {self.player_chips}.")
                chips_to_bet
                self.player_bet += chips_to_bet
            else :
                self.player_bet = chips_to_bet
                self.player_chips -= chips_to_bet
                print(f"{self.player_name} has {self.player_bet} chips on the table. Standing to win {self.player_bet * 2}")
        except TypeError :
            print(f"{self.player_name}, seems like you did not enter a number. Please provide a betting amount with a maximum of {self.player_chips}.")

    def hit_me(self) :
        drawn_card = black_jack_deck.deal_one()
        if drawn_card.rank == 'Ace' and self.player_hand_total >= 11 : # This works for the additionally drawn cards, not the one that was there from the first pair
            drawn_card.value = 1
# Currently - This might work... but this runs BEFORE we actually know what the value of the next card will be. So it remains on 11, then draws the card and gives the result.
            if self.player_hand_total > 21 and self.ace_check == False:
                for i in self.player_hand[:2] :
                    if i.rank == 'Ace' :
                        self.player_hand_total - 10
                        self.ace_check = True

        self.player_hand.append(drawn_card)

the_player = Player()
def reset_player_hand_total() :
    the_player.player_hand_total = 0

class Dealer() :
    def __init__(self) :
        self.dealer_hand = []
        self.dealer_hand_total = 0
        self.ace_check = False

    def hit_dealer(self) :
       drawn_card = black_jack_deck.deal_one()
       if drawn_card.rank == 'Ace' and self.dealer_hand_total >= 11 :
           drawn_card.value = 1
           if self.dealer_hand_total > 21 and self.ace_check == False:
                for i in self.dealer_hand[:2] :
                    if i.rank == 'Ace' :
                        self.dealer_hand_total - 10
                        self.ace_check = True
                        
       self.dealer_hand.append(drawn_card)

    def deal(self) :
        while len(self.dealer_hand) < 2 :
            the_player.hit_me()
            # the_player.player_hand.append(black_jack_deck.deal_one())
            # self.dealer_hand.append(black_jack_deck.deal_one())
            self.hit_dealer()

    def dealer_self_deal(self) :
        value_holder = []
        print(f"self.dealer_hand[0]: {self.dealer_hand[0]}")
        for i in self.dealer_hand :
            # This first if needs to happen, otherwise he will hit if he opens on 17. So basically, a calculation of the hand total is made, then the while loop starts.
            if i.counted == False :
                self.dealer_hand_total += i.value
                i.counted = True
        while self.dealer_hand_total < 17 :
            self.hit_dealer()
            for i in self.dealer_hand :
                if i.counted == False :
                    self.dealer_hand_total += i.value
                    i.counted = True

the_dealer = Dealer()

game_on = True
player_won = False

player_chips = the_player.player_chips
player_bet = the_player.player_bet

def pay_player(player_bet, player_chips, player_won) :
    if player_won == True :
        player_chips  += (player_bet * 2)

# just shows the current cards on the table including the dealer's face up card
# I don't really like that the math for the cards is happening here... But I guess it doesn't matter.
def show_player_cards() :
    value_holder = []
    print("*****-----*****-----*****")
    print(f"{player_name}'s Hand: ")
    for i in the_player.player_hand :
        print(i)
        value_holder.append(i.value)
        the_player.player_hand_total = sum(value_holder)
        # if i.counted == False :
        #     the_player.player_hand_total += i.value
        #     i.counted = True

    print(f"{player_name}'s Hand Total is: {the_player.player_hand_total}")

def show_dealer_starting_card() :
    print("*****-----*****-----*****")
    print("The Dealer's Face Up Card: ")
    print(the_dealer.dealer_hand[0])

def show_dealer_cards() :
    value_holder = []
    print("*****-----*****-----*****")
    print("The Dealer's Face Up Card: ")

    for i in the_dealer.dealer_hand :
        print(i)
        value_holder.append(i.value)
        the_dealer.dealer_hand_total = sum(value_holder)
        # if i.counted == False :
        #     the_dealer.dealer_hand_total += i.value
        #     i.counted = True

    print(f"the_dealer.dealer_hand_total : {the_dealer.dealer_hand_total}\n")

def check_to_play(player_name) :
    global game_on

    while game_on :
        request_play = input(f"Hello, {player_name}. Would you like to play Black Jack? | 'Y' | 'N ")
        if request_play == 'Y' :
            game_on = True
            print("Game is ON!")
            the_player.bet_chips()
            break
        if request_play == 'N' :
            game_on = False
            print("Game is Off!")
            break
        if request_play != 'Y' or request_play != 'N' :
            print(f"{player_name}, please enter a valid answer. Either 'Y', or 'N': ")
            request_play

check_to_play(the_player.player_name)
if game_on :
    the_dealer.deal()

while game_on :
    show_player_cards()
    show_dealer_starting_card()
    hit_or_stay = input(f"{player_name}, would you like to hit or stand? | H | S |")
    if hit_or_stay == 'H' :
        print("Hit me...")
        the_player.hit_me()
        show_player_cards()
        show_dealer_starting_card()
        if the_player.player_hand_total > 21 :
            print(f"{player_name}, you lose. - Your {the_player.player_hand_total} BUSTED! :")
            break
    hit_or_stay
    if hit_or_stay == 'S' :
        the_dealer.dealer_self_deal()
        show_dealer_cards()

        if the_dealer.dealer_hand_total > 21 :
            print(f"{player_name}, you win. from first if under S - Dealer Busted")
            player_won = True
            pay_player(player_bet, player_chips, player_won)
            print(f"Player Chip Count: {player_chips}")
            break

        elif the_dealer.dealer_hand_total > the_player.player_hand_total :
            print(f"{player_name}, You lose.. Your {the_player.player_hand_total} vs the_dealer's {the_dealer.dealer_hand_total}")
            break

        elif the_dealer.dealer_hand_total < the_player.player_hand_total :
            print(f"{player_name}, You win! You had {the_player.player_hand_total} VS the Dealer's {the_dealer.dealer_hand_total}")
            player_won = True
            pay_player(player_bet, player_chips, player_won)
            print(f"Player Chip Count: {the_player.player_chips}")
            break

        else :
            print(f"{player_name}, this was probably a push... Your {the_player.player_hand_total} vs the_dealer's {the_dealer.dealer_hand_total}")
            break
    if hit_or_stay != 'H' or hit_or_stay != 'S' :
        print("Please provide a valid input for Hit or Stand, either 'H' or 'S'.")
        hit_or_stay

# Problem right now is that Dealer will draw if he is on 17. He should stay on 17

# I am continuing with the course in the meantime, it feels like I am losing valuable time because of this lesson, and I really don't want to look at the answer.

# Currently, the problem with changing the Ace to 1 ... I am successfully changing NEW DRAWN cards to an Ace. But the one that was there during the initial draw sequence does not change.
# print(f"Things I still need to do:\n-Change ace to act as either 11 or 1.\n-Work in the Betting amount.\n-Request if the player wants to play again or leave.\n-BONUS1: Save ending chip-count to a txt file.\nBonus2: Partition all all methods and use them within the main file.")

# Combine the below with my new way of getting the totals
# So check this... for i in hand, if i .rank == ace and total > 21, i.value = 1

#  I admit defeat...