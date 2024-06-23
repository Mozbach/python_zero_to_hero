# As you learn more Python, you will discover multiple solutions for as ingle task, and you may find yourself trying to figure out the most efficient approach.
# An easy way to do this is to time your code's performance.
# Here we will focus on 3 wats to do this:
    # Simply tracking the time elapsed
    # Using the timeit module
    # ... and then some Jupyter notebook things

def function_one(n) :
    return [str(num) for num in range(n)]

print(function_one(10))

def function_two(n) :
    return(list(map(str, range(n))))

print(function_two(10))
# These two functions returns the exact same thing, but let's try to see which one is more efficient
import time
# Current time before we run the code
# start_time = time.time()
# Run Code
# result = function_one(1000000)
# elapsed_time for function_one: 0.10900664329528809

# result = function_two(1000000)
# elapsed_time for function_two: 0.11499500274658203

# This takes: 
# Current time after we run the code
# end_time = time.time()
# Elapsed Time
# elapsed_time = end_time - start_time
# print(f"elapsed_time for function_two: {elapsed_time}")

# Now, lets look at the timeit module
import timeit

stmt = """
function_one(100)
"""

setup = """
def function_one(n) :
    return [str(num) for num in range(n)]
"""

print(f"timeit.timeit(stmt, setup, number=1000000): {timeit.timeit(stmt, setup, number=1000000)}")
# Above returns: timeit.timeit(stmt, setup, number=1000000): 6.298079700092785

# Now, lets try it with function_two
stmt2 = """
function_two(100)
"""

setup2 = """
def function_two(n) :
    return list(map(str, range(n)))
"""

print(f"timeit.timeit(stmt2, setup2, number=1000000): {timeit.timeit(stmt2, setup2, number=1000000)}")
# Above returns: timeit.timeit(stmt2, setup2, number=1000000): 7.159273499972187

# So, with both timing methods, the second function returns slower than the first. Conclusion here would be that the first wway is the better way?
