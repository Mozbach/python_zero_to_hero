import random

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ( 'Ace', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten' )
values = { 'Ace' : 11, 'Two' : 2, 'Three' : 3, 'Four' : 4, 'Five' : 5, 'Six' : 6, 'Seven' : 7, 'Eight' : 8, 'Nine' : 9, 'Ten' : 10, 'Jack' : 10, 'Queen' : 10, 'King' : 10 }

# Boolean to check if the game is still ongoing
playing = True

# Class Definitions
class Card() :
    def __init__(self, suit, rank) :
        self.suit = suit
        self.rank = rank

    def __str__(self) :
        return self.rank + " of " + self.suit
    
class Deck() :
    def __init__(self) :
        self.deck = [] # start with an empty list
        for suit in suits :
            for rank in ranks :
                self.deck.append(Card(suit, rank))

    def __str__(self) :
        deck_comp = ''
        for card in self.deck :
            deck_comp += '\n' + card.__str__()
        return "The deck has: " + deck_comp

    def shuffle(self) :
        random.shuffle(self.deck)

    def deal(self) :
        single_card = self.deck.pop()
        return single_card

test_deck = Deck()
test_deck.shuffle()
# print(test_deck)

class Hand() :
    def __init__(self) :
        self.cards = [] # Start with an empty list as we did in the deck class
        self.value = 0 # Start with Zero value
        self.aces = 0 # Add an attribute to keep track of aces

    def add_card(self, card) :
        # Card passed in is from Deck's deal()
        self.cards.append(card)
        self.value += values[card.rank]

        # Track the aces -> God damnits
        if card.rank == 'Ace' :
            self.aces += 1

    def adjust_for_ace(self) :
        # if total value > 21 and I still have an ace
        # Then change my ace to be a 1 instead of an 11
        while self.value > 21 and self.aces :
            self.value -= 10
            self.aces -= 1

class Chips() :
    def __init__(self, total = 100) :
        self.total = total
        self.bet = 0

    def win_bet(self) :
        self.total += self.bet

    def lose_bet(self) :
        self.total -= self.bet

def take_bet(chips) :
    while True :
        try :
            chips.bet = int(input("How many chips would you like to bet? "))
        except: 
            print("Sorry, please provide a numerical amount of chips. ")
        else :
            if chips.bet > chips.total :
                print(f"Sorry, you do not have enough chips. You have {chips.total} chips.")
            else :
                break

def hit(deck, hand) :
    single_card = deck.deal()
    hand.add_card(single_card)
    hand.adjust_for_ace()

def hit_or_stand(deck, hand) :
    global playing

    while True :
        x = input("Hit or Stand? - Enter 'H' or 'S'." )

        if x[0].lower() == 'h' :
            hit(deck, hand)

        elif x[0].lower() == 's' :
            print("Player Stands. - Dealer's Turn!")
            playing = False
        
        else :
            print("Sorry, I did not understand the input. Please enter 'H' or 'S' only.")
            continue
        break

# Functions to display Cards
# When the game starts, and after each time Player takes a card, the dealer's card is hidden and all of Player's cards are visible. At the end of the hand all cards are shown, and you may want t show each hand't total value.
def show_some(player, dealer) :
    # Show only one of the dealer's cards
    print("\nDealer's Hand: ")
    print("First card hidden!")
    print(dealer.cards[1])

    # Show all of the player's hand/cards
    print("\nPlayer's Hand")
    for card in player.cards :
        print(card)

def show_all(player, dealer) :
    #  Show all the dealer's Cards
    print("\nDealer's Hand")
    # Calculate and display the value
    for card in dealer.cards :
        print(card)
    print(f"Dealer's Hand Total: {dealer.value}")

    # This little handsome devil can be done instead of printing each item in a list using a for loop. -> I need to explore this more in order to really see the capabilities... Like can it call functions in the loop - so forth.
    # print(f"\nDealer's Hand:", * dealer.cards, sep="\n")

    # Show all the player's Cards
    print("\nPlayer's Hand")
    for card in player.cards :
        print(card)
    print(f"Player's Hand Total: {player.value}")

    # Write functions to hanle end-game scenarios
    # Here we will need to pass the player's hand, dealer's hand and chips needed.
def player_busts(player, dealer, chips) :
    print("PLAYER BUSTS!")
    chips.lose_bet()

def player_wins(player, dealer, chips) :
    print("PLAYER WINS!")
    chips.win_bet()

def dealer_busts(player, dealer, chips) :
    print("PLAYER WINS! - DEALER BUSTED")
    chips.win_bet()

def dealer_wins(player, dealer, chips) :
    print("DEALER WINS! - PLAYER BUSTED!")
    chips.lose_bet()

def push() :
    print("PUSH!")

# Here we handle the game logic - I failed at this because during some random - literally random instances, player will lose eventhough his count is higher than the dealer's. - This was the final straw to my spirit.
while True :
    print("Welcome to BlackJack!")

    deck = Deck()
    deck.shuffle()

    player_hand = Hand()
    player_hand.add_card(deck.deal())
    player_hand.add_card(deck.deal())

    dealer_hand = Hand()
    dealer_hand.add_card(deck.deal())
    dealer_hand.add_card(deck.deal())

    player_chips = Chips()

    take_bet(player_chips)

    show_some(player_hand, dealer_hand)

    while playing : # Recall this variable from our hit_or_stand function
        # prompt the player to hit or stand
        hit_or_stand(deck, player_hand)

        #Show cards (but keep one dealer card hidden)
        show_some(player_hand, dealer_hand)

        # If player's hand exceeds 21, run player_busts() and break out of the loop
        if player_hand.value > 21 :
            player_busts(player_hand, dealer_hand, player_chips)
            break

    # If the player hasn't busted, play Dealer's hand until the dealer reaches 17
    if player_hand.value <= 21 :
        while dealer_hand.value < 17 :
            hit(deck, dealer_hand)

        # Show all cards
        show_all(player_hand, dealer_hand)

        # Run different winning scenarios
        if dealer_hand.value > 21 :
            dealer_busts(player_hand, dealer_hand, player_chips)

        elif dealer_hand.value > player_hand.value :
            dealer_wins(player_hand, dealer_hand, player_chips)

        elif dealer_hand.value < player_hand.value :
            player_wins(player_hand, dealer_hand, player_chips)

        else :
            push(player_hand, dealer_hand)

    # inform player of their chips total
    print(f"\nPlayer total chips are at: {player_chips.total}.")
    #  Ask to play again:
    new_game = input("Would you like to play again? y/n?")
    if new_game[0].lower() == 'y' :
        playing = True
        continue
    else :
        print("Thanks for playing.")
        break