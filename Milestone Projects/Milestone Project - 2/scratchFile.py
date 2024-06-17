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
"""