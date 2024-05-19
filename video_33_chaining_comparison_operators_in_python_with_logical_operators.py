# Chaining comparison operators
# We can use logical operators to combine comparisons:
#   and | or | not

print(1 < 2 < 3) # Will evaluate to True, both operators must be True, else it will evaluate to False
print(1 < 2 > 3) # This will evaluate to False, because not both are True

# and
print(1 < 2 and 2 < 3) # Will return True
print(1 < 2 and 2 > 3) # Will return False

print("h" == "h" and 2 == 2) # will return True
print("h" == "H" and 2 == 2) # will return False

# or
# Unlike "and", "or" just needs one of the conditions to be True, then it will return True. It will only return False if BOTH conditions are false
print("a" == "A" or 2 == 2) # will return True because at least one condition is True
print("a" == "A" or 2 > 4) # will return False because both conditions are False

# not
# not will return the oposite Boolean of what was given
print(not 'a' == 'A' ) # will return True
print(not 2 == 2) # will return False