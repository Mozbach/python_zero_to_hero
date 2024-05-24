# Define a function called myfun that takes in an arbiutrary number of argumenets, and returns a list containing only those arguments that are even

def myfunc(*args) :
    even_list = []
    for x in args :
        if x %2 == 0 :
            even_list.append(x)
        else :
            pass
    return even_list

print(myfunc(11,12,14,15,16,17,18,19,20))