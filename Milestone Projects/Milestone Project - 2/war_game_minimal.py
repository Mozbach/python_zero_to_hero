# First, we are going to create a card class.
# The card class will have 3 main properties: Suit, Rank (2, 3, 4, 5 ...-... j, q, k), and an int Value of each card
import random
suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two' , 'Three' , 'Four' , 'Five' , 'Six' , 'Seven' , 'Eight' , 'Nine' , 'Ten' , 'Jack' , 'Queen' , 'King' , 'Ace')
values = {
    'Two' : 2,
    'Three' : 3,
    'Four' : 4,
    'Five' : 5,
    'Six' : 6,
    'Seven' : 7,
    'Eight' : 8,
    'Nine' : 9,
    'Ten' : 10,
    'Jack' : 11,
    'Queen' : 12,
    'King' : 13,
    'Ace' : 14
}

class Card :
    def __init__(self, suit, rank) :
        self.suit = suit
        self.rank = rank
        self.value = values[rank]

    def __str__(self) :
        return self.rank + " of " + self.suit

# Example of a card class
two_hearts = Card("Hearts", "Two")
print(two_hearts)

# Combine values with the card:
print(values[two_hearts.rank])

# Create Deck Class
# Three main things we want to achieve with this deck class:
#     - Instantiate a new deck
        # Create all 52 Card objects
        # Hold a list of Card objects
#     - Shuffle a Deck through a method call
        # Random library shuffle() function
#     - Deal cards from the Deck object
        # Pop method from cards list

# Deck Class
#     - We will see that theDeck class holds a list of Card objects.
#     - This means the Deck class will return Card class object instances, not just normal Python data types.
class Deck() :
    def __init__(self) :
        self.all_cards = []

        for suit in suits :
            for rank in ranks :
                # Create the card object
                created_card = Card(suit, rank)
                self.all_cards.append(created_card)

    def shuffle(self) :
        random.shuffle(self.all_cards)

    def deal_one(self) :
        return self.all_cards.pop()

new_deck = Deck()
new_deck.shuffle()
print(f"Drawn Card: {new_deck.deal_one()}")
print(f"Length of new_deck: {len(new_deck.all_cards)}")

my_card = new_deck.deal_one()

first_card_in_new_deck = new_deck.all_cards[0]
last_card_in_new_deck = new_deck.all_cards[-1]
print(f"Rank of First Card: {first_card_in_new_deck.rank}. Suit of First Card: {first_card_in_new_deck.suit}. Als called the : {first_card_in_new_deck}")
print(f"Rank of Last Card: {last_card_in_new_deck.rank}. Suit of Last Card: {last_card_in_new_deck.suit}. Als called the : {last_card_in_new_deck}")
# for card_object in new_deck.all_cards :
#     print(card_object)

# Here we will see how we are combining the values dictionary with the Card class
# Just explaining this to myself to make more sense: 
# We create a dictionary named values, then, within the init functionm of the Card class, we take the rank of the card - which is passed in to the values dictionary.
# Whatever rank is being passed into rank, will be retrieved out of the dictionary.
three_of_clubs = Card("Clubs", "Three")
print(three_of_clubs.rank)

# We then naturally compare the rank values using comparison operators...
print(f"{two_hearts.rank < three_of_clubs.rank}")

# Player Class
#   - This class will be used to hold a player's current list of cards
#   - A player should be able to add or remove cards from their "hand" (list of card objects)
#   - Last thing to think about is translating a Deck/Hand of cards with a top and bottom, to a Python list.
#   - Let's try to visualize this
#       - Player Class will have a self.all_cards list
#       - Draw a card using cards.pop(0)
#       - Add a card or cards to the bottom of the list using cards.append("Card")
#       - Say you won a "War", you will want to add multiple cards to the carsds list instead - using cards.extend()
#              -> First create a new list of all the drawn cards, then extend the cards list with the new list: cards.extend(new) 

class Player() :
    def __init__(self, name) :
        self.name = name
        self.all_cards = []

    def remove_one(self) :
        return self.all_cards.pop(0)
    
    def add_cards(self, new_cards) :
        if type(new_cards) == type([]) :
            # List of multpiple card objects
            self.all_cards.extend(new_cards)
        else :
            # For a single card object
            self.all_cards.append(new_cards)

    def __str__(self) :
        return f"Player {self.name} has {len(self.all_cards)} cards."

# Game Setup
player_one = Player("One")
player_two = Player("Two")

new_deck = Deck()
new_deck.shuffle()

for x in range(26) :
    player_one.add_cards(new_deck.deal_one())
    player_two.add_cards(new_deck.deal_one())

game_on = True 
round_num = 0
# While Loop: game_on
while game_on :

    round_num += 1
    print(f"Round {round_num}")

    if len(player_one.all_cards) == 0 :
        print("Player One is out of Cards!")
        print("--- Player One Wins! ---")
        game_on = False
        break

    if len(player_two.all_cards) == 0 :
        print("Player Two is out of Cards!")
        print("--- Player One Wins! ---")
        game_on = False
        break

    # Start a new round
    player_one_cards = [] # Cards currently held by player 1... currently on the table
    player_one_cards.append(player_one.remove_one()) # So here we basically draw a card out of the player's stack and add it to the cards currently on the table

    player_two_cards = [] # Cards currently held by player 2... currently on the table
    player_two_cards.append(player_two.remove_one()) # So here we basically draw a card out of the player's stack and add it to the cards currently on the table

    print(f"We Have Player 1's {player_one_cards[-1]} VS Player 2's {player_two_cards[-1]}")

    # while at_war

    at_war = True
    while at_war :

        if player_one_cards[-1].value > player_two_cards[-1].value :

            player_one.add_cards(player_one_cards)
            player_one.add_cards(player_two_cards)

            at_war = False

        elif player_one_cards[-1].value < player_two_cards[-1].value :

            player_two.add_cards(player_one_cards)
            player_two.add_cards(player_two_cards)

            at_war = False

        else :
            print('WAR!')
            if len(player_one.all_cards) < 5 :
                print("Player One is Unable to Declare War!")
                print("Player Two Wins!")
                game_on = False
                break

            elif len(player_two.all_cards) < 5 :
                print("Player Two is Unable to Declare War!")
                print("Player One Wins!")
                game_on = False
                break
                
            else :
                for num in range(5) : # This  range determains how many cards is added to the war stack before the next battle begins.
                    player_one_cards.append(player_one.remove_one())
                    player_two_cards.append(player_two.remove_one())
                