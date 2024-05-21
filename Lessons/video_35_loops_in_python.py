mylist = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for num in mylist :
    print(" *-_^* " * num)

# print only even numbers in the list
for num in mylist :
    if num % 2 == 0 :
        print(num)


# create number tally to see how many times the loop happens
tally_num = 0
for num in mylist :
    tally_num = tally_num + 1
    print("Current loop: ", tally_num)

list_sum = 0
for num in mylist :
    list_sum = list_sum + num
    print(list_sum)

# loop over a string
mystring = "Morrigan"
emptylist = []
for letter in mystring :
    emptylist.append(letter)
    print(emptylist)

# loop a tup
looptup = (1, 2, 3, 4, 5, 6)
for tupItem in looptup :
    print("From a tuple!" * tupItem)

complexlist = [(1, 2), (3, 4), (5, 6), (7, 8)]
for complexitem in complexlist :
    print(complexitem)

# This I found cool... Tuple unpacking
for a, b in complexlist :
    print(a)
    print(b)

# iterate through a dictionary
dict1 = {"name": "carsten", "age": 35, "sex": "m"}
for item in dict1.items() :
    print(item)
