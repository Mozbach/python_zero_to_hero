# Define a function called myfunc that takes in a string, and returns a matching string where every even letter is uppercase, and every odd letter is a lowercase. Assume that the incomming string only contains letter, and don't worry about numbers, spaces or punctuation. The output string can start with either an uppercase letter, so long as letters alternate throug the string. 
abcString = "abcdefghijklmnop"

def myfunc(giveString) :
    newList = []
    newString = ""
    for i in range(len(giveString)) :
        if(i %2 == 0) :
            newList.append(giveString[i].lower())
        else :
            newList.append(giveString[i].upper())
        
    return newString.join(newList)

print(myfunc(abcString))

