# Well - not much I don't know but going through it anyway.
# String indexing:
characters = str("characters")

def returnCharacters(a) :
    for i in a :
        print(i)

print(returnCharacters(characters))
print("Letter at index 3: ", characters[3])

# Slicing
print(characters[4:-1])
print(characters[2:6:2])

# Escape Characters
print("Hello\nWorld")

# len function
print(len("characters"))