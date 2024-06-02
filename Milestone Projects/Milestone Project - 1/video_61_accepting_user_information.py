def display(row1, row2, row3) :
    print(row1)
    print(row2)
    print(row3)
    
row1 = [' ', ' ', ' ']
row2 = [' ', ' ', ' ']
row3 = [' ', ' ', ' ']

print(display(row1, row2, row3))

# Remember that input always returns strings. So be sure to convert into whatever you need it to be
result = input("Please enter a value: ")

# Bettery way is to convert it to what you need it the moment you get it...
index_position = int(input("Choose Index Position: "))

print("Type of Original Input: ", index_position)