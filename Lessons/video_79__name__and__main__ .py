# An often confusing part of Python is a mysterious line of code:
#   > if __name__=="__main__":

# Sometimes when you are importing from a module, you would like to know whether a modules function is being used as an import, or if youu are using the original.py file of that module.

from Video79Folder import one
one.func()