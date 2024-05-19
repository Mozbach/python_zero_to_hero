# Dictionaries are unordered mappings for storing objects (but as we have seen, since python3.7, the are ordered)
# Dictionaries use key-value pairing as opposed to numerical reference
# Key-Value allows users to grab objects without needing to know an index location

# Create a dictionary similar to objects in JS.
# Then items are stored in key-value pairs
name_of_dict = {
    "item1" : "Value of item1",
    "item2" : ["value", "of", "item", 2],
    "item3" : {
        "item3.1" : 1,
        "item3.2" : ["value", "of", "item", 3.1]
    }
}

# When do we choose a list? and When do we choose a dictionary?
# Dictionaries: Objects retrieved by key name, and before 3.7, are unorted and can't be sorted
# Lists: Objects retrieved by location. Ordered Sequence can be indexed or sliced

# To get values out of the dictionary, use the key-name in square brackets next to the name of the dictionary
print(name_of_dict["item1"])

# Access arrays within the dictionary
print(name_of_dict["item2"][3])

# Access dictionaries within dictionaries
print(name_of_dict["item3"]["item3.2"][3])

# Each item needs to be explicitly accessed
print(name_of_dict["item3"]["item3.2"][0] + " " + name_of_dict["item3"]["item3.2"][1] + " " + name_of_dict["item3"]["item3.2"][2])

prices_lookup = {
    "apple" : 4.00,
    "oranges" : 3.00,
    "milk" : 20.00
}

# Hey, what is the price of milk these days?
print(prices_lookup["milk"])

# Disctionaries are mutable
d = {'key1' : ['a', 'b', 'c']}
d["key1"][2] = "z"
print(d["key1"][2].upper())

# Add items to a Dictionary
new_dict = {
    "k1" : 100,
    "k2" : 200
}
new_dict["k3"] = 300
print(new_dict)

# Overwrite a value in a dictionary
new_dict["k2"] = 200.2
print(new_dict)

# see all the keys in a dictionary:
print(new_dict.keys())

# see all the values in a dictionary:
print(new_dict.values())

# see all the key-value pairings
print(new_dict.items())