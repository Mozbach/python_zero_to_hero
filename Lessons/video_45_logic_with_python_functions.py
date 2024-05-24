# function to check if a given number has a remainder of 0
def remain_zero(num) :
    if num %2 == 0 :
        return True
    else :
        return False

print(remain_zero(18))

# shorthand, instead of if... else
def even_check(num) :
    return num %2 == 0
print(even_check(11))

list_to_check = [1, 11, 3, 52, 7, 94]

# Return True if ANY number is Even inside a list
def even_list_check(num_list) :
    for number in num_list :
        if number %2 == 0 :
            return True
        else :
            pass
    return False

print(even_list_check(list_to_check))

def return_all_even(numList) :
    returnList = []
    for number in numList :
        if number %2 == 0 :
            returnList.append(number)
        else :
            pass
    return returnList

print(return_all_even(list_to_check))
