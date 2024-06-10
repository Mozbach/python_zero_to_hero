import one

one.func() # So, this will actually run the "ELSE" because it is not in main. 

if __name__ == '__main__' :
    print("Two.PY is being run directly")
    print('Top Level in two.py')
else :
    print("Two.PY has been imported!")