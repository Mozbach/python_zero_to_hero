# Lets look at being able to build out these regex patterns with identifier syntax.
# <------------+--------------------+--------------------+----------------+>
# | Character: |  Description:      |  Example Pattern:  |  Example Match: |
# <------------+--------------------+--------------------+----------------+>
# |  \d        |  A digit           |  file_\d\d         |  file_25        |
# <------------+--------------------+--------------------+----------------+>
# |  \w        |  Alphanumeric      |  \w-\w\w\w         |  A-b_1          |
# <------------+--------------------+--------------------+----------------+>
# |  \s        |  White Space       |  a\sb\sc           |  a b c          |
# <------------+--------------------+--------------------+----------------+>
# |  \D        |  A Non-Digit       |  \D\D\D            |  ABC            |
# <------------+--------------------+--------------------+----------------+>
# |  \W        |  Non-Alphanumeric  |  \W\W\W\W\W        |  *-+=)          |
# <------------+--------------------+--------------------+----------------+>
# |  \S        |  Non-Whitespace    |  \S\S\S\S          |  Yoyo           |
# <------------+--------------------+--------------------+----------------+>
import re

text = "My phone number is 076-3310-870"
phone = re.search('076-3310-870', text) # Will actually return the correct match object
# BUT, we won't always know the number - we might just know the pattern: 000-0000-000

# So, let's replace the actual number, with the pattern identifiers:
identify_phone = re.search(r"\d\d\d-\d\d\d\d-\d\d\d", text)
print(identify_phone) # Returns: <re.Match object; span=(19, 31), match='076-3310-870'>
print(identify_phone.group()) # Returns only the matched number: 076-3310-870

# Now, lets look at quantifiers
# <-----------+------------------------+---------------------+----------------+>
# | Character | Description            | Example Pattern Code| Example Match   |
# <-----------+------------------------+---------------------+----------------+>
# | +         | Occurs once or more    | Version \w-\w+      | Version A-b1_1  | 
# <-----------+------------------------+---------------------+----------------+>
# | {3}       | Occurs exactly 3 times | \D{3}               | abc             |  
# <-----------+------------------------+---------------------+----------------+>
# | {2,4}     | Occurs 2 - 4 times     | \d{2,4}             | 123             |
# <-----------+------------------------+---------------------+----------------+>
# | {3,}      | Occurs 3 or more times | \w{3,}              | anycharacters   |
# <-----------+------------------------+---------------------+----------------+>
# | *         | Occurs 0 or more times | ABC*                | AAACC           |
# <-----------+------------------------+---------------------+----------------+>
# | ?         | Occurs Once or more    | plurals?            | plural          |
# <-----------+------------------------+---------------------+----------------+>  

# Try to convert the original search for the telephone number to use quantifiers
quantify_phone = re.search(r"\d{3}-\d{4}-\d{3}", text)
print(f"Quantify Phone: {quantify_phone}")

# We can also group individual parts of the search using the compile function
# What compile does, is it compiles together different regular expression pattern codes
# Groups are then contained within () brackets
phone_pattern = re.compile(r'(\d{3})-(\d{4})-(\d{3})')
# You can then call these groupings individually as needed
results = re.search(phone_pattern, text)
print(f"results.group : {results.group()}")
# Now, return only the first group:
print(f"first and third result out of results.group: {results.group(1, 3)}")

# Ok, so far, not too bad...