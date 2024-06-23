# Collections Module
# Collections Module is built into base Python
# It implements specialized container data types
# They are alternatives to Python's built-in containers which is more general purpose
# Containers are things like dictionaries, tuples or lists

from collections import Counter
myList = [1,1,1,2,2,2,3,3,3,4,4,4,5,5,5]
# Let's say we wanted to get a unique count of all numbers in the above list... Like, how many ones, how many 2's and so on...
# Counter can easily do this:
print(Counter(myList))
# above output is: Counter({1: 3, 2: 3, 3: 3, 4: 3, 5: 3})
# And this will work even if the list was a mixture of strings and ints
myMixedList = ['apples','apples',1,1,1,2,2,2,2,2,3,3,3,"pears","pears","bananas"]
print(Counter(myMixedList))
# Above will return: Counter({2: 5, 1: 3, 3: 3, 'apples': 2, 'pears': 2, 'bananas': 1})
# Now, it might look like a dictionary, but it is more of a dictionary subclass

# This will also work on a string....
myString = "This will also work on a string...."
print(Counter(myString))
# Above will return : Counter({' ': 6, '.': 4, 'i': 3, 's': 3, 'l': 3, 'o': 3, 'w': 2, 'a': 2, 'r': 2, 'n': 2, 'T': 1, 'h': 1, 'k': 1, 't': 1, 'g': 1})

# Now, let's count the words in a sentence - like this sencence
mySentence = "Now, let's count the words in a sentence - like this sencence"
print(Counter(mySentence.split()))
# Above will then return: Counter({'Now,': 1, "let's": 1, 'count': 1, 'the': 1, 'words': 1, 'in': 1, 'a': 1, 'sentence': 1, '-': 1, 'like': 1, 'this': 1, 'sencence': 1})

# Some common patterns we will encounter when using the Counter object
letters = 'aaaabbbbcccccccddddddeeeeeeeee'
c = Counter(letters)
print(c)
# Above returns : Counter({'e': 9, 'c': 7, 'd': 6, 'a': 4, 'b': 4})
# Now, on the c variable, we can call other methods - like "most_common"
print(c.most_common())
# Above will return: [('e', 9), ('c', 7), ('d', 6), ('a', 4), ('b', 4)]
# You can also specify within the most_common() parameter, just how many you want returned, for example, the 2 most common items in the c variable:
print(c.most_common(2))
# Above will return: [('e', 9), ('c', 7)]
"""
Here is a small list of the most common things you might want to do with the Counter object:
- sum(c.values()) --------------> Gives a total of all counts
- c.clear() --------------------> Resets all counts
- list(c) ----------------------> List Unique Elements
- set(c) -----------------------> Convert to a set
- dict(c) ----------------------> Convert to a regular dictionary... this might be very useful in the future....
- Counter(dict(list_of)pairs)) -> Converts from a list of (elem, cnt) pairs
- c.most_common()[:-n-1:-1] ----> n Least common elements
- c += Counter() ---------------> Remove zero and negative counts
"""
# Here is an example of how to list the unique elements
listed_c = list(c)
print(listed_c)
# Above then returns: ['a', 'b', 'c', 'd', 'e'] -> This can really be useful in the past

# Let's try the dictionary conversion
dict_c = dict(c)
print(dict_c)
# Above then returns : {'a': 4, 'b': 4, 'c': 7, 'd': 6, 'e': 9}

# From collections, here is the default dictionaryt
from collections import defaultdict
# Here is a normal dictionary
d = {'a' : 10}
# If you were to try and ask for a key that does not exist in this d dictionary, you will get an error
# But the defaultdict will create an entry and give it a default value
d2 = defaultdict(lambda: 0) # Note a lambda expression in the parameter of the defaultdict... this is the default value that will be assigned to items that are not yet in the dictionary
d2['CORRECT'] = 100
print(f"d2['CORRECT']: {d2['CORRECT']}")
# Even if you now directly call a value that is not present, it will give it the default value of 0
print(f"d2['NOT CORRECT']: {d2['NOT CORRECT']}")
# Above will return this: d2['NOT CORRECT']: 0

# This here is the named tuple!
# The namedtuple tries to expand on a normal tuple object by having named indices
mytuple = (10, 20, 30)
print(mytuple[0])
# Above simply returns : 10
# Now, the namedtuple can assign a name to each value, and then call it by name, instead of index
from collections import namedtuple
Dog = namedtuple('Dog',['age', 'breed', 'name'])
# This now works similar to a Class...
pakun = Dog("13", "Pug", "Pakun")
print(pakun)
# Above returns: Dog(age='13', breed='Pug', name='Pakun')