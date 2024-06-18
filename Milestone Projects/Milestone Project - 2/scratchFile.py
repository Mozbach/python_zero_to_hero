# Give a list and get the total value of the cards within:
the_list = [1, 2, 11, 3]
# def get_total_of_list(listHere) :
#     new_val = 0
#     for i in listHere :
#         if i == 11 :
#             request_change = input("Would you like to change the 11 to 1? | Y || N |")
#             if(request_change == 'Y') :
#                 i = 1
#             else :
#                 i = i
#         new_val += i
#     return new_val

# print(get_total_of_list(the_list))

# can I sum a list? -> Yes
# print(sum(the_list))

def black_jack(*args) :
    total = sum(args)
    score = "BUST"
    if 11 in args and total <= 31 :
        score = total - 10
    if total <= 21 :
        score = total
    return score
"""
when the card is being dealt and it is an ace, 
if the hand total > 21
turn that card's value to 1

or if the hand totat + the ace's 11 > 21, turn the ace's value to 21

Ok. so the above worked. But the problem is that it does not fix the Ace that was in the hand initially.
Currently my counting system works on a boolean system. Changing a card to counted = True after it was counted in the hand. So, that does not work. Because if the card is counted as it's 11 value, it won't be recounted on a 1 value.

-10 might still work.
if drawn card == Ace and drawn card.counted == False, handTotal - 10
Nah... this will still reduce the value too much when another ace and another ace is being drawn... But this idea might work in some way... Maybe if we can get it so that that -10 can only happen once per round. Problem might be if you draw Ace, Ace then Ace Again. 

We can do this by having a boolean that starts on false, then if this happened once already, it changes to true
"""

print(f"Square of 8: {8 ** 2}")