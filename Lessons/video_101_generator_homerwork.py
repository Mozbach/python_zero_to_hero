# Now, the generator Homework
# Problem 1: Create a generator that generates the squares of numbers up to some number N.
def gen_squares(n) :
    for x in range(n) :
        yield x ** 3

print("Numbers in gen_squares(10: )")
for number in gen_squares(10) :
    print(number)

# Problem 2: Create a generator that yields "n" random numbers between a low and a high number that are inputs.
import random
num1 = int(input("Please enter a starting point number: "))
num2 = int(input("Please enter an ending point number: "))    

def random_yield(rand1, rand2, n) :
    for num in range(n) :
        yield random.randrange(rand1, rand2)

print(f"Yielded Randoms: ")
for number in random_yield(num1, num2, 10) :
    print(number)

# Problem 3: Use the iter() function to conver the string below into an iterator:
s = 'hello'
iter_s = iter(s)
for i in range(len(s)) :
    print(next(iter_s))