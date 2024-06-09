# Special Methods allow us to use built in methods in python, such as len or print with our own user created objects
mylist = [1, 2, 3]
print(len(mylist))

class Sample() :
    pass

mySample = Sample()

# len(mySample) This creates a TypeError: 'Sample has no len'

class Book() :
    def __init__(self, author, title, pages) :
        self.author = author
        self.title = title
        self.pages = pages

    def __str__(self) :
        return f"{self.title} by {self.author} has {self.pages} total pages."

    def __len__(self) :
        return self.pages
    
    # Specify extra things to occure when using del
    def __del__(self) :
        print("A book object was deleted") 

book1 = Book("Python Rocks!", 'Jose', 200)
print(book1)

# This I already covered in W3Schools - But it is handy to do so again....
# Delete property in an object using del:
del(book1.author) # Deletes the author property
del(book1) # Deletes the entire object

# del can delete all sorts of variables, it is not just restricted to classes.... I wonder if it can delete dictionary entries:
myDict = {
    "name" : "Carsten",
    "Surname" : "Niemand",
    "Age" : 35
}

del(myDict["name"])
print(myDict)


# Yes, you can delete entries in a dictionary...
