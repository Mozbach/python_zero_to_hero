# In this file is where we actually use the unittest
# When writing test functions, it is best to go from simple to complex
# As each function will be run in order, you want to usually first test the simple things, then later on,  test the more complicated things.
# Firsts we import unittest, it is a built-in python library.
import unittest
# Then, import the files you want to test
import  cap

# Start by creating a class
# Then, inherrit the testCase class that comes with unittest
class TestCap(unittest.TestCase) :
    def test_one_word(self) :
        # This test checks to see that if you were to for example pass in "python", that it returns the capitalized version - "Python"
        text = 'python'
        result = cap.cap_text(text)
        self.assertEqual(result, 'Python')

    def test_multiple_words(self) :
        text = 'monty python'
        result = cap.cap_text(text)
        self.assertEqual(result, 'Monty Python')

if __name__ =='__main__' :
    unittest.main()

    #  I am definitely going to read more about this in the documentation. I think it is important and even though I do understand it, more examples and practice won't hurt.