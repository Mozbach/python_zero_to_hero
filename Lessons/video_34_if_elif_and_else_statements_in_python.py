import random
# Here we discuss control flow
# Often you only want certain code to execute when a particular condition has been met
# For example, if my dog is hungry (some condition), then I will feed the dog (some action)
if True :
    print("It is true!")

if 3 > 2 :
    print("It is true that 2 < 3!")

hungry = False
if hungry :
    print("Feed me !")
else : 
    print("I am stuffed!")

# I know we not by def yet - but aww well
def am_I_hungry(a) :
    if a :
        print("I am hungry!")
    else :
        print("I am stuffed!")

am_I_hungry(1)


loc = "bank"
if loc == 'Auto Shop' :
    print('Cars are cool!')
elif loc == 'bank' :
    print('Pass them a note saying "this this is a robery...')
else :
    print('No, I am by the ' + loc)


location_list = ["Home", "Store", "Bank", "Work", "Resturaunt"]

def where_am_i(theList) :
    random_number = random.randint(1, len(theList) - 1)
    list_item = theList[random_number]
    if list_item == "Home" :
        return "I am home!"
    elif list_item == "Store" :
        return "I am at the store!"
    elif list_item == "Bank" :
        return "I am just getting some money from the bank!"
    elif list_item == "Work" :
        return "I am at work - working!"
    elif list_item == "Resturaunt" :
        return "I am in the resturaunt!"
    else :
        return "I don't know where I am.. I think I am at the " + list_item 


print(where_am_i(location_list))