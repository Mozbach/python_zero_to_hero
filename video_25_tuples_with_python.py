# Tuples are immutable
# tuples use round braces (1, 2, 3)

t = (1, 2 ,3)
myList = [1, 2 ,3]
# Tuples can also have different data types
t = (1, "two", [3, 4], 5, "six", 1, 5, 5)

# tuples support slicing
print(t[2:-1])

# two built-in methods for tuples
# count()
print(t.count(5))

# and index()
print(t.index([3, 4]))