# I was unsatisfied with my lackluster performance in the functions exercices / assessment. So here I will master every question and their solution and spend this sheet to understand every crevece of every solution. Why was I unsatisfied with my lackluster performance? Well, I had to look at the answers of at least 4 questions in it, and the ones I did get correct was not really effective enough.
# For the sake of becoming a better coder, I will master the most efficient version of all the solutions.

# First Section |---\_Function Practice Exercises_/---|

# 1: Lesser of Two evens: Write a function that returns the lesser of 2 given numbers if both are even, but returns the greater if one or both of them are odd:
# Step 1: Create function with 2 arguments
# Step 2: Check if both are even
# Step 3: If both are even, return minimum between the two
# Step 4: Else if both or one is odd, return maximum between the two
def lesser_of_two_evens(n1, n2) :
    if n1 % 2 == 0 and n2 % 2 == 0 :
        return f"Both are even, so here is the lesser between {n1} and {n2}:", min(n1, n2)
    else :
        return f"One or both of {n1} and {n2} was odd, so here is the max between the two: ", max(n1, n2)
print("Lesser of Two Evens: ", lesser_of_two_evens(22, 42))

#2: Animal Crackers: Write a function that takes a two-word string and returns True if both words begin with the same letter.
# Step 1: Create a function with a string-based argument
# Step 2: Make a list out of the argument, lower-case everythin as it enters the list.
# Step 3: Check if the first letter in the first word matches with the first letter in the second word - one line is all that you need.
def animal_cracker(stringHere) :
    stringList = stringHere.lower().split()
    return stringList[0][0] == stringList[1][0]

# 3: Makes Twenty: Given two integers, return True if the sum of the integers is 20 or if one of the integers is 20. If not, return False.
# Step 1: Make a function that takes in two arguments
# Step 2: I would normally use an if/else statement to do this, but remember, only one line is needed if you are checking if some boolean statement is returning a boolean.
def makes_twenty(*args) :
    return sum(args) == 20 or 20 in args

print("Makes Twenty? ", makes_twenty(10, 5))
print("Makes Twenty? ", makes_twenty(10, 15))
print("Makes Twenty? ", makes_twenty(10, 10))
print("Makes Twenty? ", makes_twenty(20, 10))

# Second Section |---\_ Function Practice Level 1 _/---|
# 1: Old Macdonald: Write a function that capitalizes the first and fourth letter of a name
# Step 1: Create function named old_macdonald, taking one string argument.
# Step 2: Going for the function that requires the highest level indexing and the least amount of code
# Step 3: Create two variables,  one getting characters from 1-3, and the other getting characters from 4 onward
# Step 4: return the first variable, capitalizing the first letter within, and then within the same line, return the second variable, capitalizing the first letter within
def old_macdonald(name) : 
    first_half = name[:3] # Index gets the first 3 letters of the name
    second_half = name[3:] # Index gets the from 4th letter onward
    return first_half.capitalize() + second_half.capitalize()
print("Old Macdonald: ", old_macdonald("morrigan"))

# 2: Master Yoda: Given a sentence, return the sentence with the words reversed - Reverse the sentence
# Again, use the version that uses the highest level understanding of string indexing, for learning purposes
# Step 1: Create a function named master_yoda, taking in one string parameter
# Step 2: Create a list of the sentence, effectively making a list entry of each word
# Step 3: Reverse the word list using indexing (easy)
# Step 4: Return a string version of the list
def master_yoda(sentence) :
    word_list = sentence.split()
    word_list = word_list[::-1] # overwriting a reversed version of the list
    return " ".join(word_list).capitalize()
print("Master Yoda's Message: ", master_yoda("You will master this, and this vacancy will be granted to you."))

# 3: Almost There: given an integer, return True if it is within 10 of either 100 or 200
# Step 1: Write a function named almost_there, taking a numerical argument - n
# Step 2: Return True using absolute numbers, comparison operators and logical operators
# Trying to explain this to myself: 100 - number is less than or equal to 10, OR if 200 - number less than or equal to ten > Really simple, actually. It will then naturally return True if true and False if not. Really, really not hard. Sad this took me so long
def almost_there(n) :
    return ((abs(100 - n) <= 10) or (abs(200 - n) <= 10))

# Third Section |---\_Function Practice Level 2_/---|
# This is the whoore 

# 1: Find 33: given a list of ints, return True if the array contains a 3 next to a 3 somewhere
# I am again going for the version using the highest level of array indexing for practice purposes
# Step 1: Create a function named find_33, taking a list of integers
# Step 2: Create a for loop, checking the i in the range of the length of the list
# Step 3: Within the loop, if i and the i next to it is 3 and 3, return true
# In hindsight - this is actually pretty simple
def find_33(numList) :
    for i in range(0, len(numList) - 1) :
        if numList[i : i + 2] == [3, 3] :
            return True
    return False

print(find_33([1, 3, 3]))
print(find_33([1, 3, 1, 3]))
print(find_33([3, 1, 3]))


# 2: Paper Doll: Given a String, return a string where for every character in the original , there are three characters
# Step 1: Create a function named paper_doll, taking a String argument
# Step 2: create an empty string
# Step 3: Using a for loop, loop the string parameter, making 2 copies (to total three) of each character, and adding them to the empty string
# Step 4: return the created string
def paper_dolls(stringHere) :
    newString = ""
    for x in stringHere :
        newString += x * 3
    return newString

# 3: BlackJack: Given three integers between 1 and 11, if their sum is less than or equal to 21, return their sum. If their sum exceeds 21 and there is an eleven, return their sum - 10, Finally, if the sum, even after adjustments, exceeds 21, return 'BUST'
# Got this solution from Lourenzo... So I am going with this one
# 1: Create a function named black_jack, taking in 3 args -> or *args
# 2: Set up 2 variables, one for the total of the args, and a score variable holding "BUST" by default
# 3: create an if statement that checks if 11 is in args AND the total is less than or equal to 31
# 4: If so, change the score variable's total to total -10
# 5: If the total is less than or equal to 21, make the score the total
# 6: Return the score...
# Overall not a difficult solution, but it sure is an obscure approach. This is where experience communicates
def black_jack(*args) :
    total = sum(args)
    score = "BUST"
    if 11 in args and total <= 31 :
        score = total - 10
    if total <= 21 :
        score = total
    return score


# 4: Summer of 69: Return the sum of the numbsers in the array, except, ignore the sections of numbers starting with a 6 and extending to the next 9. Every 6 will be followed by at least one 9. Return 0 for no numbers.
# Step 1: Create a function named summer_69 taking a list as an argument
# Step 2: Create two variables, one holding a value of 0, and the other holding the boolean True
# Step 3: Create a for loop, looping the list argument
# Step 4: While the boolean is True, check if current iteration is not 6, if not 6, the current iteration's number should be added to the variable holding 0 - then, break out of the loop
# Step 5: Else make the boolean False
# Step 6: Then, create another while, checking if the boolean is False, then if the current iteration is not 9, break out of the loop
# Step 7: Else -> Make the boolean True, then break out of the loop
# Step 8: Finally, return the variable origionally set up to hod 0, but now holds the total we are looking for
def summer_69(num_list) :
    total = 0
    the_bool = True
    for num in num_list :
        while the_bool :
            if num != 6 :
                total += num
                break
            else :
                the_bool = False
        while not the_bool :
            if num != 9 :
                break
            else :
                the_bool = True
                break
    return total
print("My Summer 69: ", summer_69([2, 1, 6, 9, 11]))
print("My Summer 69: ", summer_69([4, 5, 6, 7, 8, 9]))
print("My Summer 69: ", summer_69([1, 3, 5]))

# Third Section |---\_Challenge Problems_/---|

# 1: Spy Game: Write a function that takes in a list of integers and returns True if it contains 007 in order
# Step 1: Create a function named spy_game, taking a list as an argument
# Step 2: Create a code list, containing the 007 that we will be looking for - also, add a string to be the break
# Step 3: Create a for loop, looping over the argument list, then check if the current iteration of the list is the first number in the code list, if so, pop the first item in the code list
# Step 4: Return True once the length of the code list is 1. It should automatically return false
def spy_game(num_list) :
    code_list = [0, 0, 7, 'x']
    for num in num_list :
        if num == code_list[0] :
            code_list.pop(0)
    return len(code_list) == 1
print("My Spy Game: ", spy_game([1,2,4,0,0,7,5])) 
print("My Spy Game: ", spy_game([1,0,2,4,0,5,7])) 
print("My Spy Game: ", spy_game([1,7,2,0,4,5,0])) 

# 2: Count Primes: Write a function that returns the number of prime numbers that exist up to and including a given number. By convention, 0 and 1 are not prime
# Step 1: Create a function named count_primes, taking a single int as argument
# Step 2: Check if the number is 0 or 1, if so, return 0
# Step 3: create a list with the number 2 in it, this is the list that will store the prime numbers
# Step 4: Create a variable x with the value of 3, we will then continue adding onto this variable until we hit the argument number
# Step 5: Create a while loop, checking if variable x is less than or equal to the argument number > 
# Step 6: Create a for loop within the while loop, tracking y within the range from 3 to the current number of x - taking step size of two (Because prime numbers are never even)
# Step 7: Within the for loop, check if remainder of x divided by y is 0, if so, we know we don't have a prime, then within this for loop, add 2 to x, then break out of the loop
# Step 8: If we can complete the for loop without breaking out of it, we know we have a prime number somewhere and we want to add it to the list
# Step 9: Use a for-else statement, the else will then run if we never broke out of the loop
# Step 10: Within the else, take x and add it to the list, because it is then prime, then add 2 to x
# Step 11: Print the list of primes
# Step 12: Return the length of the primes list
def count_primes(num) :
    if num == 1 or num == 0 :
        return 0
    primes = [2]
    x = 3
    while x <= num :
        for y in range(3, x , 2) : # from 3 to x, skipping 2 at a time 
            if x % y == 0 :
                x += 2
                break
        else :
            primes.append(x)
            x += 2
    print(primes)
    return len(primes)